from flask import Flask, render_template

app = Flask(__name__)

html = """
<h1>Моя первая HTML страница</h1>
<p>Привет, мир!</p>
 """

@app.get('/')
@app.get('/Hello/')
def show_info():
    return 'Hello world!!!'


@app.get('/About/')
def about():
    return 'About'

@app.get('/contact/')
def contact():
    return 'Contact'


@app.get('/calc/<int:number_1>/<int:number_2>')
def set_number(number_1, number_2):
    return f'Передано число {number_1 + number_2}'


@app.get('/str/<string:word>')
def len_str(word):
    return f'Количество символов {len(word)}'

@app.get('/text/')
def text():
    return html


students = [
    {'name': 'Иван', 'surname':'Иванов', 'age': 20, 'raiting': 3},
    {'name': 'Антон', 'surname':'Жулимов', 'age': 24, 'raiting': 2},
    {'name': 'Кирилл', 'surname':'лобов', 'age': 18, 'raiting': 5}
]

@app.route('/students/')
def get_students():
    return render_template('students.html', students = students)


news = [{'Heading':'Заголовок', 'Description': 'описание', 'date_of_publication':'12.12.12'},
        {'Heading':'Заголовок1', 'Description': 'описание1', 'date_of_publication':'13.12.12'},
        {'Heading':'Заголовок2', 'Description': 'описание2', 'date_of_publication':'14.12.12'}
        ]

@app.route('/news/')
def get_news():
    return render_template('news.html', news=news)



if __name__ == '__main__':
    app.run(debug=True)