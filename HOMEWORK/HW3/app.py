from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from model import db, User
from forms import RegisterForm
import random
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash


app = Flask("__name__")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SECRET_KEY"] = "secret"
db.init_app(app)
csrf = CSRFProtect(app)


@app.route("/")
def hello():
    return "Welcome!"


@app.route("/register/", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "POST" and form.validate():
        name = form.name.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        print(email, password)
        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return f'Пользователь {name} добавлен'
    return render_template("forms.html", form=form)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    # add_test_data()
    app.run(debug=True)
