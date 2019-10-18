from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class AddUserForm(FlaskForm):
    firstname = StringField('Firstname', validators=[
                            DataRequired(), Length(min=3, max=20)])
    lastname = StringField('Lastname', validators=[
        DataRequired(), Length(min=3, max=20)])
