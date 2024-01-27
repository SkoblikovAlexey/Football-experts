from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TelField


class EditProfileForm(FlaskForm):
    """Форма редактирования пользователя."""

    username = StringField("Логин")
    firstname = StringField("Имя")
    lastname = StringField("Фамилия")
    phone = TelField("Телефон")
    submit = SubmitField("Сохранить")
