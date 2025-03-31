import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from adapters.repository.operator_repository import OperatorRepository
from use_cases.search_operators import SearchOperators
from adapters.controller.search_controller import create_search_controller
from utils.logger import setup_logger

load_dotenv()

logger = setup_logger("Main")

app = Flask(__name__)

if os.getenv('CORS_ENABLED', 'True').lower() == 'true':
    CORS(app)
    logger.info("CORS habilitado")
else:
    logger.info("CORS desabilitado")

try:
    logger.info("Iniciando aplicação...")
    
    csv_path = os.getenv('CSV_FILE_PATH', 'Relatorio_cadop.csv')
    csv_separator = os.getenv('CSV_SEPARATOR', ';')
    csv_encoding = os.getenv('CSV_ENCODING', 'utf-8')
    
    logger.info(f"Configurações carregadas - CSV: {csv_path}, Separador: {csv_separator}, Encoding: {csv_encoding}")
    
    repository = OperatorRepository(csv_path, csv_separator, csv_encoding)
    search_use_case = SearchOperators(repository)
    search_bp = create_search_controller(search_use_case)

    app.register_blueprint(search_bp, url_prefix='/api')
    
    logger.info("Aplicação configurada com sucesso")
    
except Exception as e:
    logger.critical(f"Falha na inicialização da aplicação: {str(e)}")
    raise

if __name__ == '__main__':
    port = int(os.getenv('APP_PORT', 3000))
    host = os.getenv('APP_HOST', '0.0.0.0')
    debug = os.getenv('APP_DEBUG', 'True').lower() == 'true'
    
    logger.info(f"Servidor iniciando em {host}:{port} (debug={'ativo' if debug else 'inativo'})")
    app.run(debug=debug, host=host, port=port)