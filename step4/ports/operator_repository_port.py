from abc import ABC, abstractmethod
from domain.operator import Operator

class OperatorRepositoryPort(ABC):
    @abstractmethod
    def search(self, query: str, sort_by: str, order: str) -> list[Operator]:
        pass
    
    @abstractmethod
    def get_all(self, sort_by: str, order: str) -> list[Operator]:
        pass