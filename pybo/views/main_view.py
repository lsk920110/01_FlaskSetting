from flask import Blueprint, render_template


bp = Blueprint('main',__name__,url_prefix='/')
#해당 py를 controller 역할을 하도록선언

@bp.route('/')
def index():
    return render_template('main.html')



