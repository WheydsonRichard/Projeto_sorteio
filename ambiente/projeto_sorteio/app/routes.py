#Implementação das rotas e logica de negocios 
from flask import request, jsonify, Blueprint, Flask
from app import db
import random
from .models import Participante, Event, Lottery

api = Flask(__name__)

@api_route('/participants', methods=['POST'])
def create_participant():
    #implementar a logica para criar um novo participante
    data = request.get.jason()

    #verificar se o email ja existe no banco de dados
    existing_email = Participante.query.filter_by(email=data['email']).first()
    #verificar se o cpf ja existe no banco de dados
    existing_cpf = Participante.query.filter_by(cpf=data['cpf']).first()

    if existing_email:
        return jsonify({'error': 'E-mail já cadastrado!'}), 400
    
    if existing_cpf:
        return jsonify({'error': 'CPF já cadastrado!'}), 400
    
    #criar um novo participante 
    new_participant = Participante(
        name=data['name'],
        email=data['email'],
        cpf=data['cpf']
    )

    db.session.add(new_participant)
    db.session.commit()

    return jsonify({'message': 'Participante criado com sucesso!'}), 201
    

@api_route('/events', methods=['POST'])
def create_event():
    #implentar a logica para criar um novo evento
    data = request.get_json()

    #verificar se o evento com o mesmo nome já existe no banco de dados
    existing_event = Event.query.filter_by(name=data['name']).first()

    if existing_event:
        return jsonify({'erro': 'Evento com este nome já cadastrado'}), 400
    
    #criar um novo evento 
    new_event = Event(name=data['name'])

    db.session.add(new_event)
    db.session.commit()

    return jsonify({'message': 'Evento criado com sucesso!'}), 201

@api_route('/lottery/generate', methods=['POST'])
def generate_lottery():
    #Implente a logica para gera um sorteio automatico
    data = request.get_json()

    #verificar se o evento existe
    event_id =data.get('event_id')
    event = Event.query.get(event_id)

    if not event:
        return jsonify({'error':'Evento não encontrado!'}), 404
    
    #verificar de há participantes para o evento 
    participantes = Participante.query.all()

    if not participantes:
        return jsonify({'error':'Não há participantes para o evento!'}), 400
    
    #verificar de o sorteio para este evento ja foi realizado
    existing_lottery =  Lottery.query.filter_by(event_id=event.id).first()

    if existing_lottery:
        return jsonify({'error': 'O sorteio para este evento já foi realizado!'}), 400
    
    #realizar o sorteio aleatório
    winner = random.choice(participantes)

    #criar entrada de sorteiro no banco de dados
    lottery_entry = Lottery(event_id=event_id, participant_id=winner.id, code='XXXXX')

    db.session.add(lottery_entry)
    db.session.commit()

    return jsonify({'message':f'O participante {winner.name} foi sorteado como vencendor!'}), 201
    pass