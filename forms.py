from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    """
        contact form
    """
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email",  validators=[DataRequired()])
    subject = StringField("Subject", validators=[DataRequired()])
    message = StringField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")
