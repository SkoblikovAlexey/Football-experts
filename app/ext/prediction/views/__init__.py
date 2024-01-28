from flask import Blueprint, render_template

prediction = Blueprint("prediction", __name__, template_folder="templates")


@prediction.get("")
def list():
    prediction_list = [1, 2, 3]
    return render_template("prediction/list.j2", predictions=prediction_list)


@prediction.get("/<int:prediction_id>")
def item(prediction_id):
    return render_template("prediction/item.j2", prediction_id=prediction_id)
