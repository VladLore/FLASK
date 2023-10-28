from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField,PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
