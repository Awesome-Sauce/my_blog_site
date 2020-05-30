from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class BlogPostForm(FlaskForm):
    title = StringField('Blog Title: ', validators=[DataRequired()])
    text = TextAreaField('Blog Text: ', validators=[DataRequired()])
    submit = SubmitField("Post Blog")