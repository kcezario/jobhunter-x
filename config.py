# -*- coding: utf-8 -*-

"""
Este arquivo contém as configurações globais do projeto jobhunter-x.
"""

# --- Configurações de busca ---

# termos de busca

SEARCH_ROLES_BR = [
    "mobile",
    "Full-stack",
    "Back-end",
    "Front-end",
    "DevOps",
    "UX+Design",
    "Dados"
]
SEARCH_ROLES_US = [
    "mobile+developer",
    "Full-stack+developer",
    "Back-end+developer",
    "Front-end+developer",
    "DevOps",
    "UX+Design",
    "Data"
]

FIELDS_TO_EXTRACT = [
            {'field': 'job_url', 'selector': 'a', 'class_name': 'jcs-JobTitle', 'attribute': 'href'},
            {'field': 'title', 'selector': 'h2', 'class_name': 'jobTitle', 'attribute': 'text'},
            {'field': 'company', 'selector': 'span', 'class_name': 'companyName', 'attribute': 'text'},
            {'field': 'location', 'selector': 'div', 'class_name': 'companyLocation', 'attribute': 'text'},
            {'field': 'salary_raw', 'selector': 'span', 'class_name': 'salary-snippet', 'attribute': 'text'},
            {'field': 'description', 'selector': 'div', 'class_name': 'job-snippet', 'attribute': 'text'}
        ]