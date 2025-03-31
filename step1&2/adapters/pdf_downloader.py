import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from ports.pdf_downloader_port import PDFDownloaderPort
from rich.console import Console
from rich.progress import track

class PDFDownloader(PDFDownloaderPort):
    BASE_URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    DOWNLOAD_DIR = os.path.join("output", "step_1") 
    
    def __init__(self):
        os.makedirs(self.DOWNLOAD_DIR, exist_ok=True)

    def get_pdf_links(self):
        response = requests.get(self.BASE_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        pdf_links = []
        
        for link in soup.find_all('a', string=True):
            text = link.get_text().strip()
            href = link.get("href", "")
            if ("Anexo I" in text or "Anexo II" in text) and href and href.endswith(".pdf"):
                pdf_links.append(urljoin(self.BASE_URL, href))
        return pdf_links

    def download_pdfs(self, pdf_links):
        console = Console()
        console.print("[bold blue]Iniciando o download dos PDFs...[/bold blue]")
        
        for url in track(pdf_links, description="Baixando PDFs..."):
            if "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf" in url:
                filename = os.path.join(self.DOWNLOAD_DIR, "Anexo I.pdf")
            elif "Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf" in url:
                filename = os.path.join(self.DOWNLOAD_DIR, "Anexo II.pdf")
            else:
                filename = os.path.join(self.DOWNLOAD_DIR, url.split('/')[-1])

            response = requests.get(url)
            response.raise_for_status()
            with open(filename, 'wb') as file:
                file.write(response.content)
            console.print(f"[green]Baixado: {filename}[/green]")