from flask import current_app, url_for
from flask_resize.exc import ImageNotFoundError

from app.extensions import resize


def url_for_icon(icon_name: str) -> str:
    """Формирование пути к иконке из спрайта."""
    filename = f"img/sprite.svg#{icon_name}"
    return url_for("static", filename=filename).replace("%23", "#")


def url_for_resize(
    filename: str,
    width: int = 200,
    height: int = 150,
    ext: str = "jpg",
    fill: bool = False,
):
    filename = f"images/{filename}"
    try:
        return resize(url_for("static", filename=filename), f"{width}x{height}", format=ext, fill=fill)
    except ImageNotFoundError as err:
        current_app.logger.error(f"Изображение '{filename}' не найдено {err}")
    return url_for("static", filename="images/no-image.jpg")


def calc_points(result: str, predict: str|None):
    if result == predict:
        return 4
    diff_result = int(result.split(":")[0]) - int(result.split(":")[1])
    if predict:
        diff_predict = int(predict.split(":")[0]) - int(predict.split(":")[1])
    else:
        return 0
    if diff_result == diff_predict:
        return 3
    if (diff_result > 0 and diff_predict > 0) or ( diff_result < 0 and diff_predict < 0):
        return 2
    return 0
