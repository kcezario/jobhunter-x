import sqlite3

class Database:
    def __init__(self, db_path="jobs.db"):
        self.db_path = db_path

    def connect(self):
        """Conecta ao banco de dados (cria se não existir)."""
        self.conn = sqlite3.connect(self.db_path)
        return self.conn

    def create_table(self):
        """Cria a tabela 'jobs' se ela não existir."""
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id TEXT NOT NULL,
                search_website TEXT NOT NULL,
                search_url TEXT NOT NULL,
                job_url TEXT NOT NULL,
                area TEXT,
                title TEXT NOT NULL,
                description TEXT,
                company TEXT NOT NULL,
                seniority TEXT,
                contract_type TEXT,
                work_modality TEXT,
                extraction_date DATE DEFAULT CURRENT_DATE,
                location TEXT,
                salary_raw TEXT,
                currency TEXT,
                remuneration_period TEXT,
                monthly_salary_brl REAL
            )
        """)
        self.conn.commit()

    def insert_job(self, job_data):
        """Insere dados de uma vaga na tabela 'jobs'."""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO jobs (job_id, search_website, search_url, job_url, area, title, description, company, 
                             seniority, contract_type, work_modality, location, salary_raw, currency, 
                             remuneration_period, monthly_salary_brl)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (job_data['job_id'], job_data['search_website'], job_data['search_url'], job_data['job_url'],
              job_data['area'], job_data['title'], job_data['description'], job_data['company'],
              job_data['seniority'], job_data['contract_type'], job_data['work_modality'],
              job_data['location'], job_data['salary_raw'], job_data['currency'],
              job_data['remuneration_period'], job_data['monthly_salary_brl']))
        self.conn.commit()

    def close_connection(self):
        """Fecha a conexão com o banco de dados."""
        if self.conn:
            self.conn.close()