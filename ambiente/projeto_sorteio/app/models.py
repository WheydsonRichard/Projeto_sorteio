#Modelos de Dados
from app import db

class Participante(db.Model):
    cpf = db.Column(db.String(14), primary_key=True, unique=True, nulllable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Lottery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant_id'), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)