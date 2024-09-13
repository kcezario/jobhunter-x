import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, search_url, search_website):
        self.search_url = search_url
        self.search_website = search_website

    def fetch_page(self):
        """Faz a requisição HTTP para a URL e retorna o HTML."""
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(self.search_url, headers=headers)
        response.raise_for_status()
        return response.content

    def extract_jobs(self):
        """Extrai as informações de cada vaga da página de resultados (abstrato)."""
        raise NotImplementedError("Subclasses devem implementar este método")

    def extract_job_data(self, job_element):
        """Extrai os dados de uma única vaga (abstrato)."""
        raise NotImplementedError("Subclasses devem implementar este método")

