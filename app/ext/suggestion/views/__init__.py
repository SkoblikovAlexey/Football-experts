from flask import Blueprint, g, render_template
from flask_security import current_user, login_required, roles_accepted

suggestion = Blueprint("suggestion", __name__, template_folder="templates")


@suggestion.get("")
def list():
    g.breadcrumbs = [{"title": "Предложения по улучшению сайта"}]
    suggestion_list = [1, 2, 3]
    # suggestion_links = [
    #     {"controller": "suggestions.list", "title": f"Предложение {suggestion_list[0]}"} for role in current_user.roles if role.name == "admin"
    # ]
    # if current_user.roles.name == "admin":
    return render_template("suggestion/list.j2", suggestions=suggestion_list)



@suggestion.get("/<int:suggestion_id>")
# @roles_accepted("admin")
def item(suggestion_id):
    return render_template("suggestion/item.j2", suggestion_id=suggestion_id)
