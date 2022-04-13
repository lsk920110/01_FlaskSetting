from flask import Blueprint

bp = Blueprint('board',__name__,url_prefix='/board')

@bp.route('/list')
def list():
    return 'this is board_list'

@bp.route('/write')
def write():
    return 'this is write form'