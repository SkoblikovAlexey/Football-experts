from flask import Blueprint, render_template

prediction = Blueprint("prediction", __name__, template_folder="templates")


@prediction.get("")
def list():
    tours_list = [1, 2, 3]
    return render_template("prediction/list.j2", tours=tours_list)


@prediction.get("/<int:tour_id>")
def item(tour_id):
    return render_template("prediction/item.j2", tour_id=tour_id)
