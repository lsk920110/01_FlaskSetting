from flask import Blueprint, render_template, request

bp = Blueprint('user',__name__,url_prefix='/user')


@bp.route('/login')
def login():
    return render_template('user/login.html')


@bp.route('/join', methods=('GET','POST'))
def join():
    if request.method == 'GET':
        return render_template('user/join.html')
    elif request.method == 'POST':
        print('post')
        #print(request.form('id'))
        request.form('user_id')
        return 'post'


