from flask import Blueprint, jsonify

health_bp = Blueprint('health_bp', __name__)

@health_bp.route('/health', methods=['GET'])
def health_check():
    ## Endpoint para checar a saúde da aplicação ##
    return jsonify({"status": "ok"}), 200

