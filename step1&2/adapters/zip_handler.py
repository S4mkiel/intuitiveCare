import zipfile
import os
from ports.zip_handler_port import ZipHandlerPort
from rich.console import Console
from rich.progress import track

class ZipHandler(ZipHandlerPort):
    DOWNLOAD_DIR = os.path.join("output", "step_1") 
    ZIP_FILE = os.path.join(DOWNLOAD_DIR, "anexos.zip") 
    
    def zip_pdfs(self):
        console = Console()
        console.print("[bold blue]Iniciando a compactação dos PDFs...[/bold blue]")
        
        # Garante que a pasta de saída exista
        os.makedirs(self.DOWNLOAD_DIR, exist_ok=True)
        
        with zipfile.ZipFile(self.ZIP_FILE, 'w') as zipf:
            files = [
                os.path.join(root, file)
                for root, _, files in os.walk(self.DOWNLOAD_DIR)
                for file in files
                if file.endswith(".pdf")  # Compacta apenas arquivos PDF
            ]
            for file in track(files, description="Compactando arquivos..."):
                zipf.write(file, arcname=os.path.basename(file))
        
        console.print(f"[green]Arquivo ZIP criado com sucesso: {self.ZIP_FILE}[/green]")