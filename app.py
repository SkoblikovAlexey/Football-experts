from os import getenv

from dotenv import load_dotenv
from extensions import db, security
from flask import Flask, flash, g, jsonify, redirect, render_template, request, url_for
from flask_security import hash_password, login_required
from models import User, user_datastore
import pymysql


load_dotenv()

app = Flask(__name__)

DB_USERNAME = "football"
DB_PASSWORD = "12345678"
DB_HOST = "localhost"
DB_NAME = "footballexperts"

app.config.from_mapping(
    MAIL_BACKEND="console",
    SECRET_KEY=getenv("SECRET_KEY"),
    SECURITY_PASSWORD_SALT="bcrypt",
    SECURITY_REGISTERABLE=True,
    SECURITY_USERNAME_ENABLE=True,
    SECURITY_USERNAME_REQUIRED=True,
    SECURITY_CONFIRMABLE=True,
    SECURITY_TRACKABLE=True,
    SECURITY_PASSWORD_LENGTH_MIN=5,
    SECURITY_LOGIN_URL="/войти",
    SECURITY_LOGOUT_URL="/выйти",
    SECURITY_REGISTER_URL="/регистрация",
    SECURITY_CONFIRM_URL="/подтверждение-регистрации",
    SECURITY_LOGIN_USER_TEMPLATE="security/login.j2",
    SECURITY_REGISTER_USER_TEMPLATE="security/register.j2",
    SECURITY_SEND_CONFIRMATION_TEMPLATE="security/confirm.j2",
    SQLALCHEMY_DATABASE_URI=f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}",
    SQLALCHEMY_ENGINE_OPTIONS={"pool_pre_ping": True},
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)


db.init_app(app)
security.init_app(app, user_datastore)


with app.app_context():
    db.create_all()
    if not user_datastore.find_user(email="Alex@mail.ru"):
        user_datastore.create_user(email="Alex@mail.ru", password=hash_password("123456"), username="Алексей")
    db.session.commit()

@app.before_request
def before_request():
    g.main_menu = [{
        "title": "Главная",
        "url": "index",
    }, {
        "title": "Сделать прогноз",
        "url": "predictions",
    }, {
        "title": "Рекорды",
        "url": "records",
    }, {
        "title": "Результаты матчей",
        "url": "results",
    }]

@app.get("/")
def index():
    return render_template("index.j2")

@app.get("/predictions")
def predictions():
    return render_template("predictions.j2")

@app.get("/records")
def records():
    return render_template("records.j2")

@app.get("/results")
def results():
    return render_template("results.j2")
