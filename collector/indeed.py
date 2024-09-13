import re
from bs4 import BeautifulSoup
from config import *
from .scraper import Scraper
from .job_data import JobData

class IndeedScraper(Scraper):
    def __init__(self, search_url, search_website):
        super().__init__(search_url, search_website)

    def extract_jobs(self):
        """Extrai as informações de cada vaga da página de resultados do Indeed."""
        html_content = self.fetch_page()
        soup = BeautifulSoup(html_content, 'html.parser')
        jobs_elements = soup.find_all('div', class_='job_seen_beacon')
        return jobs_elements

    def extract_job_data(self, job_element):
        """Extrai os dados brutos de uma única vaga do Indeed e retorna um objeto JobData."""
        job_data = JobData()

        for field_data in FIELDS_TO_EXTRACT:
            element = job_element.find(field_data['selector'], class_=field_data['class_name'])
            if element:
                if field_data['attribute'] == 'text':
                    setattr(job_data, field_data['field'], element.text.strip())
                else:
                    setattr(job_data, field_data['field'], element[field_data['attribute']])

        job_data.job_id = job_element['data-jk']
        job_data.search_website = self.search_website
        job_data.search_url = self.search_url

        self.process_job_data(job_data)  # Processa os dados da vaga

        return job_data

    def process_job_data(self, job_data):
        """Processa os dados da vaga, preenchendo campos faltantes e limpando dados."""

        # Área (baseado no termo de busca)
        if self.search_website == "Indeed BR":
            job_data.area = next((role for role in SEARCH_ROLES_BR if role in self.search_url), None)
        elif self.search_website == "Indeed US":
            job_data.area = next((role for role in SEARCH_ROLES_US if role in self.search_url), None)

        # Senioridade
        if any(keyword in job_data.title.lower() for keyword in ["junior", "iniciante", "trainee", "estag", "entry", "beginner", "intern"]):
            job_data.seniority = "junior"
        elif any(keyword in job_data.title.lower() for keyword in ["sênior", "senior", "lead", "especialista", "expert"]):
            job_data.seniority = "senior"
        else:
            job_data.seniority = "pleno"

        # Modalidade de trabalho (fixo por enquanto)
        job_data.work_modality = "remote"

        # Moeda e Período de Remuneração (baseado na localização e salário)
        if self.search_website == "Indeed BR":
            job_data.currency = "BRL" if "R$" in job_data.salary_raw else "USD"
            job_data.remuneration_period = "mensal" if not re.search(r"anual|annual", job_data.salary_raw, re.IGNORECASE) else "anual"
        elif self.search_website == "Indeed US":
            job_data.currency = "USD"
            job_data.remuneration_period = "anual" if not re.search(r"monthly", job_data.salary_raw, re.IGNORECASE) else "mensal"

