from flask import Flask, render_template

app = Flask(__name__)
html = """
<h1>Привет, меня зовут Владислав</h1>
<p>Я только начала писать сайты на Flask. </br>Посмотрите на мой сайт</p>
"""


@app.route('/index1/')
def index_1():
    context = {
        'title': 'Личный блог',
        'name': 'Харитон',
    }
    return render_template('index1.html', **context)


@app.route('/index/')
def html_index():
    return render_template('index.html')




@app.route('/')
@app.route('/<name>/')
def hello(name = 'незнакомец'):
    return f'Привет, {name.capitalize()}!'


@app.route('/file/<path:file>')
def set_path(file):
    print(type(file))
    return f'Путь до файла "{file}"'


@app.route('/number/<float:num>')
def set_number(num):
    print(type(num))
    return f'Передано число {num}'


@app.route('/text/')
def text():
    return html


@app.route('/poems/')
def poems():
    poem = ['Вот не думал, не гадал',
            'Программистом взял и стал.',
            'Хитрый знает он язык',
            'Он у другому не привык.'
            ]
    txt = '<h1>Стихотворение</h1>\n<p>' + '<br/>'.join(poem) + '</p>'
    return txt



@app.route('/Николай/')
def nike():
    return 'Привет, Николай!'


@app.route('/Иван/')
def ivan():
    return 'Привет, Иван!'


@app.route('/Фёдор/')
@app.route('/Fedor/')
@app.route('/Федя/')
def fedot():
    return 'Привет, Федор!'


if __name__ == '__main__':
    app.run()