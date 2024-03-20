from sqlalchemy import String, Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.extensions import db
from app.models import ModelMixin
from app.ext.core.models import User

class Season(db.Model, ModelMixin):
    __tablename__ = "seasons"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    date_start = db.Column(db.DateTime)
    tours = db.relationship("Tour", back_populates="season")


class Tour(db.Model, ModelMixin):
    __tablename__ = "tours"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    season_id = db.Column(db.Integer, db.ForeignKey(Season.id))
    date_start = db.Column(db.DateTime)
    season = db.relationship("Season", back_populates="tours")
    matches = db.relationship("Match", back_populates="tour")


class Match(db.Model, ModelMixin):
    __tablename__ = "matches"
    id = db.Column(db.Integer, primary_key=True)
    # title = db.Column(db.String(255))
    tour_name = db.Column(db.String(10))
    tour_id = db.Column(db.Integer, db.ForeignKey(Tour.id))
    name1 = db.Column(db.String(25))
    name2 = db.Column(db.String(25))
    goal1 = db.Column(db.Integer)
    goal2 = db.Column(db.Integer)
    date_start = db.Column(db.DateTime)
    tour = db.relationship("Tour", back_populates="matches")
    predicts = db.relationship("Predict", back_populates="match")

    def __init__(self, data):
        self.id = data['id']
        self.tour_name = data['stageName']
        self.tour_id = data['stage']
        self.name1 = data['name1']
        self.name2 = data['name2']
        self.goal1 = data['goal1'] if data['goal1'] else "_"
        self.goal2 = data['goal2'] if data['goal2'] else "_"
        self.date = data['date']

    def __repr__(self):
        return f"Матч с id: {self.id}, {self.tour_name}: {self.name1} - {self.name2} {self.goal1}:{self.goal2} , {self.date}"

class Predict(db.Model, ModelMixin):
    __tablename__ = "predicts"
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey(Match.id))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    goal1 = db.Column(db.Integer)
    goal2 = db.Column(db.Integer)
    dt_predict = db.Column(db.DateTime)
    user = db.relationship("User", back_populates="predicts")
    match = db.relationship("Match", back_populates="predicts")

    def getResults():
        return results

