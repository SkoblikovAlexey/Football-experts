from flask import Blueprint,g, render_template

prediction = Blueprint("prediction", __name__, template_folder="templates")


@prediction.get("")
def list():
    g.breadcrumbs = [{"title": "Прогнозы по турам"}]
    tours_list = [1, 2, 3]
    return render_template("prediction/list.j2", tours=tours_list)


@prediction.get("/<int:tour_id>")
def item(tour_id):
    g.breadcrumbs = [{"controller": ".list", "title": "Прогнозы по турам"}, {"title": f"Прогноз на {tour_id} тур"}]
    return render_template("prediction/item.j2", tour_id=tour_id)
