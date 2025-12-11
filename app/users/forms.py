from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField("Логін", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired(), Length(min=4, max=10)])
    remember = BooleanField("Запам'ятати мене")
    submit = SubmitField("Увійти")



class RegisterForm(FlaskForm):
    username = StringField("Логін", validators=[DataRequired(), Length(min=3)])
    password = PasswordField("Пароль", validators=[DataRequired(), Length(min=4)])
    submit = SubmitField("Зареєструватися")
