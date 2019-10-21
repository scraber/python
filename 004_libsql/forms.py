from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length


class AddUserForm(FlaskForm):
    firstname = StringField("Firstname", validators=[DataRequired(), Length(min=3, max=20)])
    lastname = StringField("Lastname", validators=[DataRequired(), Length(min=3, max=20)])
    submit = SubmitField("Add")


class AddAuthorForm(FlaskForm):
    firstname = StringField("Firstname", validators=[DataRequired(), Length(min=3, max=20)])
    lastname = StringField("Lastname", validators=[DataRequired(), Length(min=3, max=20)])
    submit = SubmitField("Add")


class AddCategoryForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=20)])
    submit = SubmitField("Add")


class AddBookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=3, max=50)])
    category = SelectField("Category", coerce=int, choices=[])
    isbn = IntegerField("ISBN", validators=[DataRequired()])
    author = SelectField("Author", coerce=int, choices=[])
    submit = SubmitField("Add")


class RemoveUserForm(FlaskForm):
    fullname = SelectField("Fullname", coerce=int, choices=[])
    submit = SubmitField("Remove")


class RemoveAuthorForm(FlaskForm):
    fullname = SelectField("Fullname", coerce=int, choices=[])
    submit = SubmitField("Remove")


class RemoveCategoryForm(FlaskForm):
    name = SelectField("Name", coerce=int, choices=[])
    submit = SubmitField("Remove")


class RemoveBookForm(FlaskForm):
    book = SelectField("Book", coerce=int, choices=[])
    submit = SubmitField("Remove")
