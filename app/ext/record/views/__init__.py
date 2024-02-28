from flask import Blueprint, g, render_template

record = Blueprint("record", __name__, template_folder="templates")


@record.get("")
def records():
    g.breadcrumbs = [{"title": "Рекорды"}]
    return render_template("record/records.j2")


