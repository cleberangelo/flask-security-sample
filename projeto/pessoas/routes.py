from flask import Blueprint, render_template, request, jsonify, flash, url_for
from flask_login import login_required
from werkzeug.utils import redirect
from projeto.models import db, Pessoa

pessoas = Blueprint('pessoas', __name__, template_folder='templates')


# Url inicial só pode ser acessada mendiante login
@pessoas.route('/')
@login_required
def home():
    persons = Pessoa.query.all();
    return render_template('index.html', persons=persons)


# Chamada json
@pessoas.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    name = data['name']
    password = data['password']
    email = data['email']

    try:
        person = Pessoa(name=name, email=email)
        person.set_password(password)

        db.session.add(person)
        db.session.commit()
        return jsonify(msg='Salvo com sucesso', person_id=person.id), 200
    except AssertionError as exception_message:
        return jsonify(msg='Erro: {}. '.format(exception_message)), 400


@pessoas.route('/save', methods=['POST'])
@login_required
def save():
    name = request.form.get('name')
    password = request.form.get('password')
    email = request.form.get('email')

    try:
        person = Pessoa(name=name, email=email)
        person.set_password(password)

        db.session.add(person)
        db.session.commit()
        flash('Salvo com id {}'.format(person.id), 'success')
        return redirect(url_for('pessoas.home'))
    except AssertionError as exception_message:
        flash('{}'.format(exception_message), 'danger')
        return redirect(url_for('pessoas.home'))
