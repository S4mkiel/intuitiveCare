from ports.operator_repository_port import OperatorRepositoryPort
from utils.logger import setup_logger

class SearchOperators:
    def __init__(self, repository: OperatorRepositoryPort):
        self.repository = repository
        self.logger = setup_logger("SearchOperators")
        self.logger.info("Caso de uso SearchOperators inicializado")

    def execute(self, query: str, sort_by: str = None, order: str = 'asc') -> list:
        self.logger.debug(f"Executando busca por: '{query}' com ordenação '{sort_by}' ({order})")
        try:
            results = self.repository.search(query, sort_by, order)
            self.logger.info(f"Busca concluída com {len(results)} resultados")
            return results
        except Exception as e:
            self.logger.error(f"Erro durante a execução da busca: {str(e)}")
            raise
        
    def get_all(self, sort_by: str = None, order: str = 'asc') -> list:
        self.logger.debug("Retornando todos os operadores cadastrados")
        try:
            results = self.repository.get_all(sort_by, order)
            self.logger.info(f"Total de operadores cadastrados: {len(results)}")
            return results
        except Exception as e:
            self.logger.error(f"Erro ao obter todos os operadores: {str(e)}")
            raise