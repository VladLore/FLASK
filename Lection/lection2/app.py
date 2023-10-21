from flask import Flask, url_for, request, render_template, make_response
from markupsafe import escape
from werkzeug.utils import secure_filename
from pathlib import PurePath, Path

app = Flask(__name__)


@app.route("/")
def index():
    # устанавливаем coockie
    response = make_response('Cookie установлен')
    response.set_cookie('usesrname', 'admin')
    return response


@app.route('/getcookie/')
def get_cookies():
    name = request.cookies.get('username')
    return f'Значение cookie: {name}'



@app.route("/test_url_for/<int:num>")
def test_url(num):
    text = f"В num лежит {num}<br>"
    text += f'Функция {url_for("test_url", num=42)=} <br>'
    text += f'Функция {url_for("test_url", num=42, data = "new_data")=} <br>'
    text += f'Функция {url_for("test_url", num=42, data = "new_data", pi = 3.14515)=} <br>'
    return text


@app.route("/<path:file>/")
def get_file(file):
    print(file)
    # return f'Ваш файл находится в: {file}!'
    return f"Ваш файл находится в: {escape(file)}!"


@app.route('/get/')
def get():
    if level := request.args.get('level'):
        text = f'Похоже ты опытный игрок, раз имеешь уровень {level}<br>'
    else:
        text = 'Привет, новичок. <br>'
    return f'{text} {request.args}'


@app.route('/submit', methods =['GET', 'POST'])
def submit():
    if request.method =='POST':
        name = request.form.get('name')
        return f'Hello {name}!'
    return render_template('index.html')


@app.route('/upload', methods =['GET','POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f'Файл {file_name} загружен на сервер'
    return render_template('uplload.html')







if __name__ == "__main__":
    app.run(debug=True)
