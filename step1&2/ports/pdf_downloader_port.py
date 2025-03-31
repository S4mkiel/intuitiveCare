from abc import ABC, abstractmethod

class PDFDownloaderPort(ABC):
    @abstractmethod
    def get_pdf_links(self):
        pass

    @abstractmethod
    def download_pdfs(self, pdf_links):
        pass