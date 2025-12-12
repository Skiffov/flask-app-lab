from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField, SubmitField, DateTimeLocalField
from wtforms.validators import DataRequired
from datetime import datetime


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    category = SelectField("Category", choices=[
        ("news", "News"),
        ("tech", "Tech"),
        ("life", "Life")
    ])
    posted = DateTimeLocalField("Дата публікації", format="%Y-%m-%dT%H:%M", default=datetime.utcnow)
    enabled = BooleanField("enabled", default=True)
    submit = SubmitField("Submit")
