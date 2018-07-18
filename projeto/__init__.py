from flask import Flask, render_template, request, current_app
from flask_security import SQLAlchemyUserDatastore, Security
from flask_security.utils import hash_password

from projeto.config import configure_app
from projeto.models import db, Pessoa, User, Role
from projeto.pessoas.routes import pessoas

app = Flask(__name__)
configure_app(app)
users = SQLAlchemyUserDatastore(db, User, Role)
app.security = Security(app, users)
db.init_app(app)


# Cria um usuário para acessar o sistema. Descomentar ao rodar pela primeira vez, depois comentar
# @app.before_first_request
# def create_user():
#     db.drop_all()
#     db.create_all()
#     users.create_user(email='user@mail.com', password=hash_password('password'))
#     db.session.commit()


@app.errorhandler(404)
def page_not_found(error):
    current_app.logger.error('Página não encontrada: %s', (request.path, error))
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    current_app.logger.error('Erro no servidor: %s', error)
    return render_template('500.html'), 500


@app.errorhandler(Exception)
def unhandled_exception(error):
    current_app.logger.error('Exceção não tratada: %s', error)
    return render_template('500.html'), 500


app.register_blueprint(pessoas, url_prefix='')
