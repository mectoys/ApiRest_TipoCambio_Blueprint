from flask import Blueprint, jsonify, request

from scr.models.EmailModel import EmailModel
from scr.models.entities.Email import Email

main = Blueprint('email_blueprint', __name__)


# Listar Email
@main.route('/')
def listar_email():
    try:
        email = EmailModel.listar_email()
        return jsonify(email)
    except Exception as ex:
        return jsonify({'mensaje': str(ex)}), 500


# Add Email

@main.route('/addemail', methods=['POST'])
def add_email():
    try:
        email = request.json['email']
        fecharegister = request.json['fecharegister']
        email = Email(email, fecharegister)
        affected_rows = EmailModel.add_email(email)
        if affected_rows == 1:
            return jsonify(email.fecharegister)
        else:
            return jsonify({'mensaje': "Error on Insert"}), 500
    except Exception as ex:
        return jsonify({'mensaje': str(ex)}), 500

#del EMAIL

@main.route('/delemail/<email>', methods=['DELETE'])
def delete_email(email):
    try:
        email = Email(email)
        affected_rows = EmailModel.del_email(email)
        if affected_rows == 1:
            return jsonify(email.email)
        else:
            return jsonify({'mensaje': "Error on delete"}), 500
    except Exception as ex:
        return jsonify({'mensaje': str(ex)}), 500