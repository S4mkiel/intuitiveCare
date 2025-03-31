from abc import ABC, abstractmethod

class PDFParserPort(ABC):
    @abstractmethod
    def extract_table(self, pdf_path):
        pass