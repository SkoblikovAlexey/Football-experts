import requests
from app.ext.result.models import Match
# tournament = requests.post('https://premierliga.ru/ajax/match/', data=[('ajaxAction','getHeaderCalendar'), ('tournament', 1)])
# for i in range(len(tournament.json()['contents'])):
#     match = Match(tournament.json()['contents'][i])
#     # db.session.add(match)
# # db.session.commit()
# print(match)
tournament = requests.post('https://premierliga.ru/ajax/match/', data=[('ajaxAction','getHeaderCalendar'), ('tournament', 1)])
def get_results(tournament):
    "Получение результатов матчей с помощью запроса на оф. сайт РПЛ"
    # tournament = requests.post('https://premierliga.ru/ajax/match/', data=[('ajaxAction','getHeaderCalendar'), ('tournament', 1)])
    # print(tournament.json()['contents'])
    for i in range(len(tournament.json()['contents'])):
        match = Match(tournament.json()['contents'][i])
        # match.save()
    #     db.session.add(match)
    # db.session.commit()
    print(match)
    # flash(f"Результаты матчей добавлены в базу данных", "success")
    # return redirect(url_for("admin.index", admin_links=admin_links))

get_results(tournament)
