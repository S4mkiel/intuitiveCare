from adapters.pdf_downloader import PDFDownloader
from adapters.zip_handler import ZipHandler
from rich.console import Console

console = Console()

def pdf_execute():
    pdf_downloader = PDFDownloader()
    zip_handler = ZipHandler()
    
    pdf_links = pdf_downloader.get_pdf_links()
    if not pdf_links:
        console.print("[bold red]Nenhum PDF encontrado para download.[/bold red]")
        return
    
    pdf_downloader.download_pdfs(pdf_links)
    zip_handler.zip_pdfs()
