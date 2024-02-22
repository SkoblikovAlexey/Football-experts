from flask import Blueprint, render_template

from app.utils import calc_points

result = Blueprint("result", __name__, template_folder="templates")


@result.get("")
def list():
    result_list = [1, 2, 3]
    return render_template("result/list.j2", tours=result_list)


@result.get("/<int:tour_id>")
def item(tour_id):
    results = [{
        "title": "Спартак — Зенит",
        "result": "2:1",
        "predict": None,
    }, {
        "title": "Краснодар — ЦСКА",
        "result": "2:0",
        "predict": "2:1",
    }, {
        "title": "Ростов — Динамо",
        "result": "3:1",
        "predict": "3:1",
    }, {
        "title": "Крылья Советов — Урал",
        "result": "0:0",
        "predict": "1:1",
    }, {
        "title": "Рубин — Ахмат",
        "result": "2:0",
        "predict": "0:1",
    }]

    final_score = 0
    for match in results:
        match["score"] = calc_points(match["result"], match["predict"])
        final_score += match["score"]

    tour_results = {
        "title": "Матчи первого тура (2024)",
        "final_score": final_score,
        "results": results
    }
    return render_template("result/item.j2", tour_id=tour_id, tour_results=tour_results)
