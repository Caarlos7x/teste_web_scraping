### TESTES DE NIVELAMENTO  

## 1. TESTE DE WEB SCRAPING
Este teste deve ser realizado nas linguagens Python ou Java. E o código deverá executar o/a:

- 1.1. Acesso ao site: https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-
sociedade/atualizacao-do-rol-de-procedimentos
- 1.2. Download dos Anexos I e II em formato PDF
- 1.3. Compactação de todos os anexos em um único arquivo (formatos ZIP, RAR, etc.).

## 2. TESTE DE TRANSFORMAÇÃO DE DADOS
Crie um código em Python ou Java que execute as seguintes tarefas:
- 2.1. Extraia os dados da tabela **Rol de Procedimentos e Eventos em Saúde** do **PDF do Anexo I** (todas as páginas)
- 2.2. Salve os dados em uma tabela estruturada, em formato **CSV**.
- 2.3. Compacte o CSV em um arquivo denominado `"Teste_{seu_nome}.zip"`.
- 2.4. Substitua as abreviações das colunas **OD** e **AMB** pelas descrições completas:
  - **OD** → *Seg. Odontológica*
  - **AMB** → *Seg. Ambulatorial*

---

## **📌 Como Rodar o Projeto**
### **⚙️ Pré-requisitos**
Antes de rodar o projeto, verifique se você tem instalado:
- **Python 3.9+** → [Baixar Python](https://www.python.org/downloads/)
- **Git** (caso queira clonar do repositório) → [Baixar Git](https://git-scm.com/downloads)
- **Bibliotecas do Python** (serão instaladas com `pip`)

### **📥 Clonando o Repositório**
Se ainda não clonou o projeto, execute no terminal:
```bash
git clone git@github.com:Caarlos7x/teste_web_scraping.git
cd teste_web_scraping
```

## **📦 Instalando as Dependências**
Dentro do projeto, instale todas as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```
- As bibliotecas instaladas incluem:
- requests → Para fazer requisições HTTP
- beautifulsoup4 → Para web scraping
- pdfplumber → Para extrair dados de PDFs
- pandas → Para manipulação de dados
- zipfile → Para compactar os arquivos

## **🚀 Executando o Projeto**
Para rodar o script principal e iniciar o processo de web scraping + transformação de dados, execute:
```bash
python src/main.py
```

## **📂 Saída Esperada**
1. O script **baixa os PDFs do site oficial** e os salva em `downloads/`.

2. Os PDFs são **compactados em um único arquivo ZIP**.

3. O **Anexo I** é processado e os dados extraídos são:

    - Convertidos para CSV.

    - Substituídas as siglas OD e AMB.

4. O **CSV final é compactado em** `Teste_Carlos_Augusto.zip` dentro da pasta `output/`.

## **📌 Estrutura do Projeto**
```bash
teste_web_scraping/
│── downloads/                # PDFs baixados
│── output/                   # CSVs e arquivos compactados
│── src/                      # Código-fonte do projeto
│   ├── main.py               # Arquivo principal que executa todo o processo
│   ├── web_scraper.py        # Script responsável por baixar os PDFs
│   ├── extract_data.py       # Script que processa os dados do PDF e gera CSV
│── requirements.txt          # Dependências do projeto
│── README.md                 # Documentação do projeto
```

## **📌 Autor**
👤 Carlos Augusto
📧 Contato: caarlos.frei@gmail.com