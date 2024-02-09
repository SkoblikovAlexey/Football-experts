from flask_security import RegisterForm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TelField
from wtforms.validators import DataRequired


class EditProfileForm(FlaskForm):
    """Форма редактирования пользователя."""

    username = StringField("Логин")
    firstname = StringField("Имя")
    lastname = StringField("Фамилия")
    phone = TelField("Телефон")
    submit = SubmitField("Сохранить")


class ExtendedRegisterForm(RegisterForm):
    """Расширенная форма регистрации."""

    firstname = StringField("Имя", [DataRequired()])
    lastname = StringField("Фамилия", [DataRequired()])
