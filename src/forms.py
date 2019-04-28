from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    feild = StringField('feild', validators=[DataRequired()])
    submit = SubmitField('submit')

    def validation(self, string):
        error = ''
        if error:
            raise ValidationError('error msg')
