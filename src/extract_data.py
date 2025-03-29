import os
import pandas as pd
import pdfplumber
import zipfile

DOWNLOAD_DIR = "downloads"
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def encontrar_anexos():
    """Encontra automaticamente os arquivos Anexo I e II dentro da pasta downloads"""
    pdf_anexo_I, pdf_anexo_II = None, None

    for file in os.listdir(DOWNLOAD_DIR):
        if "Anexo_I" in file and file.endswith(".pdf"):
            pdf_anexo_I = os.path.join(DOWNLOAD_DIR, file)
        elif "Anexo_II" in file and file.endswith(".pdf"):
            pdf_anexo_II = os.path.join(DOWNLOAD_DIR, file)

    return pdf_anexo_I, pdf_anexo_II

def extrair_tabela_pdf(pdf_path):
    """Extrai TODAS as tabelas do PDF Anexo I e retorna um DataFrame"""
    print(f"Processando PDF: {pdf_path}")

    dados_tabela = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tabela = page.extract_table()
            if tabela:
                for row in tabela:
                    dados_tabela.append(row)

    if not dados_tabela:
        print("Nenhuma tabela encontrada no PDF.")
        return None

    df = pd.DataFrame(dados_tabela)

    df.dropna(how="all", inplace=True)

    df.columns = df.iloc[0]
    df = df[1:]

    print(f"PDF extraído com {df.shape[1]} colunas.")

    colunas_para_substituir = ["OD", "AMB"]
    
    for coluna in colunas_para_substituir:
        if coluna in df.columns:
            df[coluna] = df[coluna].replace({"OD": "Seg. Odontológica", "AMB": "Seg. Ambulatorial"})

    return df

def processar_dados():
    """Executa o processo de extração e estruturação dos dados"""
    pdf_anexo_I, _ = encontrar_anexos()

    if not pdf_anexo_I:
        print("O PDF do Anexo I não foi encontrado.")
        return None

    df_final = extrair_tabela_pdf(pdf_anexo_I)

    if df_final is None:
        print("Erro na extração de dados do PDF.")
        return None

    return df_final

def salvar_csv(df, nome_arquivo):
    """Salva o DataFrame final como CSV"""
    csv_file_path = os.path.join(OUTPUT_DIR, nome_arquivo)
    df.to_csv(csv_file_path, index=False, encoding='utf-8')
    print(f"CSV salvo em: {csv_file_path}")
    return csv_file_path

def compactar_csv(nome_arquivo):
    """Compacta o arquivo CSV em um ZIP"""
    csv_file_path = os.path.join(OUTPUT_DIR, nome_arquivo)
    zip_file_name = os.path.join(OUTPUT_DIR, f"Teste_Carlos_Augusto.zip")

    with zipfile.ZipFile(zip_file_name, 'w') as zipf:
        zipf.write(csv_file_path, os.path.basename(csv_file_path))

    print(f"CSV compactado em: {zip_file_name}")

if __name__ == "__main__":
    df_final = processar_dados()
    if df_final is not None:
        csv_file = salvar_csv(df_final, "Teste_Carlos_Augusto.csv")
        compactar_csv("Teste_Carlos_Augusto.csv")
    else:
        print("Ocorreu um erro na estruturação dos dados.")