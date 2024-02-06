from flask import Blueprint, render_template

result = Blueprint("result", __name__, template_folder="templates")


@result.get("")
def list():
    result_list = [1, 2, 3]
    return render_template("result/list.j2", tours=result_list)


@result.get("/<int:tour_id>")
def item(tour_id):
    return render_template("result/item.j2", tour_id=tour_id)
