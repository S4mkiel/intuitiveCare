import pandas as pd
from domain.operator import Operator
from ports.operator_repository_port import OperatorRepositoryPort
from utils.logger import setup_logger

class OperatorRepository(OperatorRepositoryPort):
    def __init__(self, csv_path: str, separator: str = ';', encoding: str = 'utf-8'):
        self.logger = setup_logger("OperatorRepository")
        self.logger.info(f"Inicializando repositório com arquivo CSV: {csv_path}")
        self.logger.debug(f"Configurações - Separador: '{separator}', Encoding: {encoding}")
        
        try:
            self.df = pd.read_csv(csv_path, sep=separator, encoding=encoding)
            self.df = self.df.fillna('')
            self.logger.info(f"CSV carregado com sucesso. Total de registros: {len(self.df)}")
        except Exception as e:
            self.logger.error(f"Erro ao carregar CSV: {str(e)}")
            raise
        
    def search(self, query: str, sort_by: str = None, order: str = 'asc') -> list:
        self.logger.debug(f"Iniciando busca por: '{query}' com ordenação '{sort_by}' ({order})")
        
        if not query:
            self.logger.warning("Busca vazia recebida, retornando lista vazia")
            return []
            
        query = query.lower()
        
        try:
            mask = self.df.apply(
                lambda row: any(query in str(cell).lower() for cell in row),
                axis=1
            )
            results_df = self.df[mask]

            if sort_by and sort_by in results_df.columns:
                ascending = order.lower() == 'asc'
                results_df[sort_by] = results_df[sort_by].astype(str) 
                results_df = results_df.sort_values(by=sort_by, ascending=ascending)

            results = results_df.to_dict('records')
            self.logger.info(f"Busca por '{query}' encontrou {len(results)} resultados")

            return [self._row_to_operator(row) for row in results]
        except Exception as e:
            self.logger.error(f"Erro durante a busca: {str(e)}")
            raise
        
    def get_all(self, sort_by: str = None, order: str = 'asc') -> list[Operator]:
        self.logger.debug("Obtendo todos os operadores cadastrados")
        
        try:
            results_df = self.df.copy()

            if sort_by and sort_by in results_df.columns:
                ascending = order.lower() == 'asc'
                results_df[sort_by] = results_df[sort_by].astype(str) 
                results_df = results_df.sort_values(by=sort_by, ascending=ascending)

            results = results_df.to_dict('records')
            self.logger.info(f"Total de operadores cadastrados: {len(results)}")

            return [self._row_to_operator(row) for row in results]
        except Exception as e:
            self.logger.error(f"Erro ao obter todos os operadores: {str(e)}")
            raise
    
    def _row_to_operator(self, row: dict) -> Operator:
        try:
            return Operator(**{
                'registro_ans': row['Registro_ANS'],
                'cnpj': row['CNPJ'],
                'razao_social': row['Razao_Social'],
                'nome_fantasia':row['Nome_Fantasia'],
                'modalidade':row['Modalidade'],
                'logradouro':row['Logradouro'],
                'numero':row['Numero'],
                'complemento':row['Complemento'],
                'bairro':row['Bairro'],
                'cidade':row['Cidade'],
                'uf':row['UF'],
                'cep':row['CEP'],
                'ddd':row['DDD'],
                'telefone':row['Telefone'],
                'fax':row['Fax'],
                'endereco_eletronico':row['Endereco_eletronico'],
                'representante':row['Representante'],
                'cargo_representante':row['Cargo_Representante'],
                'data_registro_ans':row['Data_Registro_ANS']
            })
        except Exception as e:
            self.logger.error(f"Erro ao converter linha para Operator: {str(e)}")
            raise