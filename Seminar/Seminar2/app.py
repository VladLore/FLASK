from flask import Flask, render_template, request, redirect, url_for, flash, abort
from pathlib import PurePath, Path
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'secret'


@app.route("/")
@app.route("/hi/")
def main():
    return render_template("index.html")


@app.route("/hello")
def hello():
    return f"Привет"


@app.route("/upload/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files.get("file")
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), "uploads", file_name))
        return f"Файл {file_name} загружен на страницу"
    return render_template("upload.html")


@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")
        if login == 'Вася' and password=='123':
            return f'Добро пожаловать'
        return f'ошибка'
    return render_template("login.html")

@app.route('/len/', methods=['GET', 'POST'])
def length():
    if request.method == 'POST':
        text = request.form.get('text')
        return f'Длина текста{len(text)}'
    return render_template('text.html')

# Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом

@app.route('/sum/', methods = ['GET', 'POST'] )
def sum():
    if request.method == 'POST':
        num1 = int(request.form.get('num1'))
        num2 = int(request.form.get('num2'))
        operation = request.form.get('Operation')
        if operation == 'SUM':
            sum = num1 + num2
            return f'Сумма равна {sum}'
        elif operation == 'SUB':
            sub = num1 - num2
            return f'Разность равна {sub}'
        elif operation == 'MULT':
            mult = num1 * num2
            return f'Произведение равно {mult}'
        elif operation == 'DIV':
            div = num1 / num2
            return f'Частное равно {div}'
    return render_template('sum.html')


# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.

@app.route('/number/', methods = ['GET','POST'])
def number():
    if request.method == 'POST':
        num1 = int(request.form.get('num1'))
        return redirect(url_for('quadrat', number=num1**2))
    return render_template('number.html')

@app.get('/quadrat/<int:number>')
def quadrat(number):
    return f'{number}'


# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".


@app.route('/flash/', methods = ['GET', 'POST'])
def flash_msg():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Привет, {name}', 'success')
        redirect(url_for("flash_msg"))
    return render_template('flash.html')


# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.


@app.errorhandler(403)
def error(e):
    return f'Доступ запрещён', 403


@app.route('/age/', methods = ['GET', 'POST'])
def age():
    if request.method == 'POST':
        ages = int(request.form.get('age'))
        if ages < 18:
            abort(403)
        return 'Добро пожаловать!'
    return render_template ('ages.html')





if __name__ == "__main__":
    app.run(debug=True)
