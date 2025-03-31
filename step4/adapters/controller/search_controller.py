from flask import Blueprint, request, jsonify
from use_cases.search_operators import SearchOperators
from utils.logger import setup_logger

def create_search_controller(search_use_case: SearchOperators):
    bp = Blueprint('search', __name__)
    logger = setup_logger("SearchController")

    @bp.route('/search', methods=['GET'])
    def search():
        logger.info("Nova requisição de busca recebida")

        query = request.args.get('q', '').strip()
        page = request.args.get('page', '1')
        per_page = request.args.get('per_page', '10')
        sort_by = request.args.get('sort_by', None)
        order = request.args.get('order', 'asc')

        logger.debug(f"Parâmetros recebidos - q: {query}, page: {page}, per_page: {per_page}, sort_by: {sort_by}, order: {order}")

        try:
            page = int(page)
            per_page = int(per_page)
        except ValueError:
            logger.warning(f"Parâmetros inválidos - page: {page}, per_page: {per_page}")
            return jsonify({
                "error": "Parâmetros 'page' e 'per_page' devem ser números inteiros"
            }), 400

        if query:
            logger.info(f"Executando busca por: '{query}' com ordenação '{sort_by}' ({order})")
            operators = search_use_case.execute(query, sort_by, order)
        else:
            logger.info("Nenhum termo de busca informado. Retornando todos os registros.")
            operators = search_use_case.get_all(sort_by, order)

        total = len(operators)
        start = (page - 1) * per_page
        end = start + per_page
        paginated_operators = operators[start:end]

        total_pages = (total // per_page) + (1 if total % per_page > 0 else 0)

        logger.info(f"Retornando {len(paginated_operators)} resultados (página {page} de {total_pages})")

        return jsonify({
        "data": [op.to_dict() for op in paginated_operators],
        "meta": {
            "total": len(operators),
            "page": page,
            "per_page": per_page,
            "total_pages": (len(operators) // per_page) + 1
        }
        }), 200

    return bp