from flask import Flask, flash, g, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)


@app.before_request
def before_request():
    g.main_menu = [{
        "title": "Главная",
        "url": "index",
    }, {
        "title": "Сделать прогноз",
        "url": "predictions",
    }, {
        "title": "Контакты",
        "url": "contacts",
    }, {
        "title": "Предложения по улучшению сайта",
        "url": "suggestions_improvement",
    }, {
        "title": "Таблица РПЛ",
        "url": "show_table",
    }]
