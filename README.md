# jobhunter-x
JobHunter X é um projeto de ciência de dados focado na análise do mercado de trabalho remoto em áreas como tecnologia e design. Utilizando web scraping, análise de dados e machine learning, buscamos identificar tendências e gerar insights sobre oportunidades e demandas no mercado global.

### Ajustes no Plano e Especialidades

1. **Engenharia de Dados**:
   - Foco principal em _web scraping_, coleta, armazenamento e limpeza dos dados.
   - Ferramentas sugeridas: `Scrapy` (ou `BeautifulSoup` + `Selenium`), `Python`, `Pandas`, `AWS S3` ou `Google Cloud Storage`, `Airflow` para orquestração de pipelines de dados.
   - Organizar e transformar os dados de maneira eficiente para consumos futuros (Análises e Machine Learning).

2. **Ciência de Dados**:
   - Transformar dados brutos em insights significativos: análise de salários, número de vagas, mercados com maior/menor demanda, etc.
   - Ferramentas: `Python`, `Jupyter`, `Pandas`, `Numpy`, `Matplotlib`, `Seaborn`, `Scikit-learn` para análise e modelagem inicial.
   - Exploratory Data Analysis (EDA) para identificar tendências e insights com base nos cargos, localização e níveis de senioridade.

3. **Análise de Dados**:
   - Criar dashboards interativos e visuais periódicos para postagens no LinkedIn.
   - Ferramentas: `Power BI` ou `Tableau`, `Google Data Studio` para visualização de dados.
   - Foco na visualização de tendências em diferentes áreas, como crescimento de vagas, comparação entre países, senioridades e o impacto da língua inglesa.

4. **Machine Learning**:
   - Desenvolver modelos preditivos que antecipem mudanças nas demandas de mercado (número de vagas, requisitos, etc).
   - Ferramentas: `Scikit-learn`, `XGBoost`, `PyCaret`, `TensorFlow` ou `PyTorch` para modelos mais avançados.
   - Usar algoritmos supervisionados para previsões de demanda de vagas, segmentação de cargos e classificações.

---

### Passo a Passo:

1. **Fase de Planejamento**:
   - Definir claramente as perguntas que você quer responder com os dados, como:
     - Vale a pena aprender inglês para trabalhar remotamente?
     - Quais áreas têm maior demanda nos EUA e no Brasil?
     - Quais níveis (junior, pleno, senior) têm mais oportunidades?
     - Como varia a concorrência entre quem fala ou não inglês?

2. **Coleta de Dados (Engenharia de Dados)**:
   - Escolha das fontes (Indeed, LinkedIn Jobs, Glassdoor, etc.).
   - Implementar _web scraping_ usando `Scrapy` ou `BeautifulSoup` para coletar dados estruturados das vagas.
   - Armazenar os dados em um banco de dados como `PostgreSQL`, ou em um _data lake_ como `AWS S3`.

3. **Limpeza e Tratamento dos Dados**:
   - Usar `Pandas` para limpar dados faltantes, duplicados ou incoerentes.
   - Normalizar os dados (ex: unificação de formato de salários entre países).

4. **Análise Exploratória de Dados (Ciência de Dados)**:
   - Realizar análises exploratórias para entender as distribuições de vagas por área, nível de senioridade, localidade e habilidades exigidas.
   - Identificar padrões como crescimento ou queda na oferta de vagas e correlação entre inglês e oportunidades.

5. **Criação de Dashboards (Análise de Dados)**:
   - Configurar dashboards com `Power BI`, `Tableau`, ou `Google Data Studio`.
   - Publicar insights periodicamente em seu LinkedIn, mostrando tendências e dados em gráficos interativos.

6. **Desenvolvimento de Modelos Preditivos (Machine Learning)**:
   - Construir um pipeline para treinar e validar modelos de previsão de mercado de trabalho.
   - Testar modelos como `Random Forest`, `XGBoost` e redes neurais (se aplicável) para prever a demanda futura de vagas, analisando diferentes fatores (tecnologia, nível, localização).

7. **Monitoramento e Feedback**:
   - Automatizar o pipeline de coleta e análise de dados com `Airflow` ou `Prefect`.
   - Revisar periodicamente os modelos e insights conforme novos dados forem coletados.

8. **Publicação e Divulgação**:
   - Divulgar seus achados periodicamente em redes sociais (LinkedIn).
   - Criar um portfólio com esses projetos, destacando as tecnologias utilizadas e os resultados obtidos.

### Tecnologias Sugeridas:
- **Coleta e Armazenamento**: Scrapy, BeautifulSoup, Selenium, PostgreSQL, AWS S3.
- **Tratamento de Dados**: Python, Pandas, Numpy.
- **Visualização**: Power BI, Tableau, Google Data Studio.
- **Machine Learning**: Scikit-learn, XGBoost, TensorFlow, PyCaret.
- **Orquestração**: Airflow, Prefect.
- **Dashboards/Relatórios**: Google Data Studio, Tableau.


