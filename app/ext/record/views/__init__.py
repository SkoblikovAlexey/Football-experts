from flask import Blueprint, render_template

record = Blueprint("record", __name__, template_folder="templates")


@record.get("")
def records():
    return render_template("record/records.j2")


