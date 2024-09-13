class JobData:
    def __init__(self):
        self.job_id = None
        self.search_website = None
        self.search_url = None
        self.job_url = None
        self.area = None
        self.title = None
        self.description = None
        self.company = None
        self.seniority = None
        self.contract_type = None
        self.work_modality = None
        self.extraction_date = None
        self.location = None
        self.salary_raw = None
        self.currency = None
        self.remuneration_period = None
        self.monthly_salary_brl = None

    def __repr__(self):
        return f"JobData(title='{self.title}', company='{self.company}')"