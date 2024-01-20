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
