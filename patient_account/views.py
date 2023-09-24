from flask import Blueprint


bp = Blueprint(name='patient',
               url_prefix='/patient',
               import_name=__name__)


@bp.route('/return_secret_number')
def secret_number_handler():
    return str(42)
