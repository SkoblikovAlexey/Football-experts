class Tour(db.Model):
    id: int (pk)
    title: str(255)

class MatchResult(db.Model):
    id: int (pk)
    tour_id: int -> fk Tour.id
    title: str(255)
    result: str(5)
    deadline: datetime


class MatchPredict(db.Model):
    id: int (pk)
    match_id: int -> fk MatchResult.id
    user_id: int -> fk User.id
    predict: str(5)
    dt_predict: datetime

    def getResults():
        return results
