from flask import Blueprint, render_template

suggestion = Blueprint("suggestion", __name__, template_folder="templates")


@suggestion.get("")
def list():
    suggestion_list = [1, 2, 3]
    return render_template("suggestion/list.j2", suggestions=suggestion_list)


@suggestion.get("/<int:suggestion_id>")
def item(suggestion_id):
    return render_template("suggestion/item.j2", suggestion_id=suggestion_id)
