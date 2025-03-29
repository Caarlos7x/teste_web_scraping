import os
import requests
import zipfile
from bs4 import BeautifulSoup

URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def baixar_pdfs():
    """Faz o scraping da página e baixa os PDFs dos anexos"""
    response = requests.get(URL)
    if response.status_code != 200:
        raise Exception("Erro ao acessar a URL")

    soup = BeautifulSoup(response.text, "html.parser")
    pdf_links = [a['href'] for a in soup.find_all('a', href=True) if "Anexo" in a['href'] and a['href'].endswith(".pdf")]

    pdf_files = []
    for link in pdf_links:
        full_url = link if link.startswith("http") else f"https://www.gov.br{link}"
        file_name = os.path.join(DOWNLOAD_DIR, os.path.basename(full_url))
        pdf_files.append(file_name)

        response = requests.get(full_url)
        with open(file_name, "wb") as f:
            f.write(response.content)
        print(f"✅ Download concluído: {file_name}")

    # Compactar os PDFs baixados
    zip_file_name = os.path.join(DOWNLOAD_DIR, "anexos.zip")
    with zipfile.ZipFile(zip_file_name, 'w') as zipf:
        for pdf in pdf_files:
            zipf.write(pdf, os.path.basename(pdf))

    print(f"📦 Arquivos compactados em {zip_file_name}")

if __name__ == "__main__":
    baixar_pdfs()