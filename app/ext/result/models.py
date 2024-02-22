class MatchResult(db.Model):
    id: int
    title: str(255)
    result: str(5)
    deadline: datetime


class MatchPredict(db.Model):
    id: int
    match_id: int -> fk MatchResult.id
    user_id: int -> fk User.id
    predict: str(5)
    dt_predict: datetime
