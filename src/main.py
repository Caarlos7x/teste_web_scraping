from web_scraper import baixar_pdfs
from extract_data import processar_dados, salvar_csv, compactar_csv

def executar_processo():
    """Executa todas as etapas do processo"""
    print("📥 Baixando PDFs...")
    baixar_pdfs()

    print("📊 Extraindo e processando dados do Anexo I...")
    df_final = processar_dados()

    if df_final is not None:
        print("💾 Salvando como CSV...")
        csv_file = salvar_csv(df_final, "Teste_Carlos_Augusto.csv")

        print("📦 Compactando CSV...")
        compactar_csv("Teste_Carlos_Augusto.csv")

        print("✅ Processo concluído!")
    else:
        print("⚠️ Ocorreu um erro na extração dos dados.")

if __name__ == "__main__":
    executar_processo()