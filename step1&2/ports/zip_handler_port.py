from abc import ABC, abstractmethod

class ZipHandlerPort(ABC):
    @abstractmethod
    def zip_pdfs(self):
        pass