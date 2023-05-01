from scr.models.ExchangeModel import ExchangeModel
from flask import Blueprint, jsonify

main = Blueprint('exchange_blueprint', __name__)

@main.route('/')
def list_exchange():
    try:
        exchange = ExchangeModel.list_exchange()
        return jsonify(exchange)
    except Exception as ex:
        return jsonify({'mensaje': str(ex)}), 500
