# Первоначальные наброски по логике подсчета очков

# str1 = "1:1"
# str2 = "0:0"

# def calc_points(predict: str, res: str):
#     points = 0
#     if predict == res:
#         points += 4
#     else:
#         diff_predict = int(predict.split(":")[0]) - int(predict.split(":")[1])
#         diff_res = int(res.split(":")[0]) - int(res.split(":")[1])
#         if diff_predict == diff_res:
#             points += 3
#         elif (diff_predict > 0 and diff_res > 0) or (diff_predict < 0 and diff_res < 0):
#             points += 2
#     return points

# a = calc_points(str1, str2)
# print(a)

# Получаем из БД информацию о прогнозе пользователя и фактических результатах, формируем из неё списки.
# Допустим, получили эти списки:

tour_1_predictions = ["1:0", "1:1", "2:0", "0:1", "0:0", "0:2", "3:0", "2:3"]
tour_1_results = ["1:0", "1:2", "2:1", "0:1", "1:0", "1:2", "2:3", "2:3"]

tour_2_predictions = ["1:0", "1:1", "2:0", "0:1", "0:0", "0:2", "3:0", "3:3"]
tour_2_results = ["1:3", "0:2", "2:2", "0:1", "1:2", "0:2", "2:1", "3:3"]

def calc_points(predict: list, res: list):
    points = 0
    for i in range(len(res)):
        if predict[i] == res[i]:
            points += 4
        else:
            diff_predict = int(predict[i].split(":")[0]) - int(predict[i].split(":")[1])
            diff_res = int(res[i].split(":")[0]) - int(res[i].split(":")[1])
            if diff_predict == diff_res:
                points += 3
            elif (diff_predict > 0 and diff_res > 0) or (diff_predict < 0 and diff_res < 0):
                points += 2
    return points
class test_user:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def calc_tour_points(self, tour_predict: list, tour_res: list):
        self.points += calc_points(tour_predict, tour_res)
        return calc_points(tour_predict, tour_res)

    points = 0

alex = test_user("Alex", "Sk")


def calc_user_points(user: object, tour_predict: list, tour_res: list):
    user_tour_points = user.calc_tour_points(tour_predict, tour_res)
    print(f"Пользователь {user.firstname} {user.lastname} за первый тур набрал {user_tour_points} очков, всего у него {user.points} очков)")

calc_user_points(alex, tour_1_predictions, tour_1_results)
calc_user_points(alex, tour_2_predictions, tour_2_results)