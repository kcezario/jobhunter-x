# jobhunter-x
JobHunter X é um projeto de ciência de dados focado na análise do mercado de trabalho remoto em áreas como tecnologia e design. Utilizando web scraping, análise de dados e machine learning, buscamos identificar tendências e gerar insights sobre oportunidades e demandas no mercado global.

#### Objetivo:
Criar um projeto colaborativo focado em coletar, analisar e prever tendências no mercado de trabalho das áreas de tecnologia e dados, sempre com foco em vagas remotas nos Estados Unidos e no Brasil. O projeto inclui webscraping de sites de emprego, análise de dados e visualizações, além de modelos de Machine Learning para previsão de tendências de mercado. O resultado final será uma série de relatórios e dashboards dinâmicos, que podem ser compartilhados periodicamente no LinkedIn.

---

### 1. **Coleta e Armazenamento de Dados**
- **Responsável:** Engenharia de Dados
- **Ferramentas:** 
  - **Webscraping:** Python com **Selenium** e **BeautifulSoup**.
  - **Automatização:** **Apache Airflow** para coleta automatizada.
  - **Armazenamento:** Banco de dados relacional **PostgreSQL** ou **NoSQL (MongoDB)**, complementado com backups em **Amazon S3**.
  - **Formato de dados:** Usar formatos eficientes como **Parquet** e **JSON**.

- **Passo a passo:**
  1. Configurar webscraping de sites de emprego (Indeed, LinkedIn) para buscar vagas remotas no Brasil e EUA nas áreas: **Mobile, Full-stack, Back-end, Front-end, DevOps, UX+Design e Dados**.
  2. **Padronização dos Dados:** Definir os campos a serem extraídos de cada vaga e seus respectivos tipos, garantindo a qualidade e a utilidade para análise.
    - **Justificativa da Escolha dos Campos:**
        - É crucial coletar dados relevantes para responder às perguntas de negócio do projeto **jobhunter-x**, como: quais as áreas mais promissoras? Quais habilidades estão em alta? Qual a influência do inglês nas vagas internacionais? 
        - Os campos escolhidos permitem análises comparativas entre Brasil e EUA, segmentação por área, senioridade e análise de tendências salariais. 
        - A coleta da URL da vaga possibilita futuras consultas e análise detalhada de cada oportunidade.
        - A inclusão do ID da vaga, site de pesquisa e URL de busca tornam o processo mais escalável, permitindo futuras adições de sites e garantindo que não haverá duplicidade de dados.

    - **Campos e Tipos:**
        - **ID (Inteiro):** Identificador único para cada vaga. **(Gerado durante a inserção no banco)**
        - **ID da Vaga no Site (Texto):** ID único da vaga no site de emprego.
        - **Site de Pesquisa (Texto):** Nome do site de onde a vaga foi extraída (Ex: Indeed, LinkedIn).
        - **URL de Busca (Texto):** URL utilizada para encontrar a vaga, incluindo filtros.
        - **URL da Vaga (Texto):** Link da vaga no site de emprego.
        - **Área (Texto):** Área de atuação dentro de tecnologia (Ex: Dados, DevOps, Mobile).
        - **Título (Texto):** Título da vaga.
        - **Descrição (Texto):** Descrição da vaga, responsabilidades e requisitos.
        - **Empresa (Texto):** Nome da empresa que oferece a vaga.
        - **Senioridade (Texto):** Nível de experiência (Ex: Júnior, Pleno, Sênior).
        - **Tipo de Contratação (Texto):** Tipo de contrato (Ex: PJ, CLT, Estágio).
        - **Modalidade (Texto):** Detalhes sobre a forma de trabalho (Ex: Remoto, Híbrido, Presencial).
        - **Data da Extração (Data):** Data em que a vaga foi coletada.
        - **Localização (Texto):** Localização da vaga (cidade, estado, país).
        - **Salário Raw (Texto):** Informação de salário bruta extraída do site.
        - **Moeda (Texto):** Moeda original do salário informado na vaga.
        - **Período de Remuneração (Texto):** Informa se o salário é mensal, anual, etc.
        - **Salário Mensal em Reais (Número Decimal):** Salário padronizado em R$/mês para facilitar comparações.
  3. Implementar automação com **Airflow** para atualização contínua e coleta diária ou semanal.

---

### 2. **Análise de Dados**
- **Responsável:** Ciência de Dados
- **Ferramentas:** 
  - **Exploração de dados:** **Pandas**, **Seaborn**, e **Matplotlib**.
  - **Testes estatísticos:** **SciPy** para validar os insights.
  - **Análise comparativa:** Realizar comparações entre Brasil e EUA, focando em vagas por área, nível (Júnior, Pleno, Sênior) e exigência de inglês.

- **Perguntas principais a responder:**
  1. **Inglês é essencial?** Qual o impacto do inglês na quantidade de vagas disponíveis nos EUA?
  2. **Concorrência:** Qual o nível de concorrência por área e por nível de experiência?
  3. **Distribuição de vagas:** Quais áreas de dados e tecnologia oferecem mais oportunidades e onde estão concentradas?

- **Análises sugeridas:**
  - Distribuição de vagas por área e país.
  - Comparação do impacto do inglês na acessibilidade das vagas internacionais.
  - Análise da concorrência por nível de experiência.

---

### 3. **Visualização de Dados**
- **Responsável:** Análise de Dados
- **Ferramentas:** 
  - **Dashboards dinâmicos:** Criar visualizações em **Tableau** ou **Power BI** com integração direta aos bancos de dados, permitindo atualizações automáticas.
  - **Relatórios dinâmicos:** Configurar a geração de relatórios semanais ou quinzenais, que podem ser publicados diretamente no LinkedIn.

- **Passo a passo:**
  1. Desenvolver dashboards que mostrem:
     - Tendências de vagas por área e país.
     - Concorrência por nível de experiência.
     - Previsões baseadas em modelos de Machine Learning.
  2. Configurar um sistema de relatórios periódicos que se alimentam automaticamente dos dados mais recentes para análise e publicação.

---

### 4. **Previsão de Tendências**
- **Responsável:** Engenharia de Machine Learning
- **Ferramentas:** 
  - **Modelos de previsão:** **Random Forest**, **XGBoost**, e **Facebook Prophet** para prever o número de vagas e a concorrência por área e nível.
  - **Séries temporais:** Previsão de tendências de vagas ao longo do tempo usando **ARIMA** e **Facebook Prophet**.

- **Modelos preditivos:**
  1. **Previsão de demanda:** Prever o número de vagas futuras em áreas como Data Science, Engenharia de Dados, DevOps e Full-stack.
  2. **Concorrência:** Prever a relação entre vagas e número de candidatos por área e país.
  3. **Séries temporais:** Criar modelos de séries temporais para monitorar a evolução do mercado ao longo dos meses.

---

### 5. **Estrutura Tecnológica e Integração**
- **Responsável:** Gerente de Projeto
- **Ferramentas e Tecnologias:**
  - **Coleta de dados:** Python com **Selenium**, **BeautifulSoup**, e **Apache Airflow** para orquestração.
  - **Armazenamento:** **PostgreSQL**, **Parquet**, **Amazon S3** para backups.
  - **Análise de dados:** **Pandas**, **Seaborn**, **SciPy**.
  - **Machine Learning:** **scikit-learn**, **TensorFlow**, **Facebook Prophet** para previsões.
  - **Visualização:** **Tableau** e **Power BI** para dashboards interativos.

- **Passo a passo integrado:**
  1. **Fase 1: Coleta de dados automatizada** – Configurar o webscraping e armazenamento contínuo.
  2. **Fase 2: Limpeza e padronização dos dados** – Padronizar títulos, salários e localização.
  3. **Fase 3: Análise exploratória** – Realizar a análise inicial para identificar padrões.
  4. **Fase 4: Desenvolvimento dos modelos preditivos** – Criar algoritmos para prever o movimento de vagas e concorrência.
  5. **Fase 5: Criação de dashboards dinâmicos** – Implementar visualizações em Tableau ou Power BI.
  6. **Fase 6: Publicação de relatórios periódicos** – Automatizar a criação de relatórios semanais para LinkedIn.

---

### Conclusão:
Este projeto oferece uma visão completa e automatizada do mercado de trabalho em áreas de tecnologia e dados, focando nas oportunidades remotas no Brasil e nos Estados Unidos. Com a coleta contínua de dados, análise detalhada e previsões baseadas em Machine Learning, será possível identificar tendências e ajudar profissionais a tomar decisões informadas sobre suas carreiras.

O próximo passo é implementar as ferramentas e tecnologias sugeridas para começar a coleta de dados, seguir o fluxo estabelecido e publicar os primeiros relatórios no LinkedIn.


