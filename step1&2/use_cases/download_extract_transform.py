import os
import zipfile
import fitz
import pandas as pd
from rich.console import Console
from rich.progress import track

from adapters.pdf_downloader import PDFDownloader
from adapters.pdf_parser import PDFParser

console = Console()

def rename_columns(df: pd.DataFrame):
    return df.rename(columns={
        "OD": "Seg. Odontológica",
        "AMB": "Seg. Ambulatorial"
    }) 
    
def save_zip(df: pd.DataFrame, nome):
    output_dir = os.path.join("output", "step_2")
    os.makedirs(output_dir, exist_ok=True)
    
    csv_path = os.path.join(output_dir, "Rol_de_Procedimentos.csv")
    zip_path = os.path.join(output_dir, f"Teste_{nome}.zip")

    df.to_csv(csv_path, index=False)

    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(csv_path, arcname="Rol_de_Procedimentos.csv")

    return zip_path

def csv_execute():
    console.print("[bold blue]Iniciando o processamento do Anexo I...[/bold blue]")
    
    pdf_downloader = PDFDownloader()
    pdf_parser = PDFParser()
    
    anexo_i_path = os.path.join(pdf_downloader.DOWNLOAD_DIR, "Anexo I.pdf")
    
    console.print("[bold blue]Extraindo tabela do PDF...[/bold blue]")
    df = pdf_parser.extract_table(anexo_i_path)
    
    if "OD" not in df.columns or "AMB" not in df.columns:
        console.print("[bold red]Erro: Estrutura do DataFrame não corresponde ao esperado![/bold red]")
        raise ValueError("Estrutura do DataFrame não corresponde ao esperado!")
    
    console.print("[bold blue]Renomeando colunas...[/bold blue]")
    df = rename_columns(df)
    
    console.print("[bold blue]Salvando o arquivo CSV e compactando em ZIP...[/bold blue]")
    zip_path = save_zip(df, "Roberto_Barreto_Ferraz_Filho")
    
    console.print(f"[green]Processo concluído com sucesso! Arquivo ZIP criado: {zip_path}[/green]")