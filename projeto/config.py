import os


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'super-secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///testes.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_SALT = 'your-salt-here'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'EMAIL_USER'
    MAIL_PASSWORD = 'EMAIL_PASS'

    # Configuração das mensagens do Flask-Security
    SECURITY_MSG_UNAUTHORIZED = ('Você não tem permissão para ver esse recurso.', 'error')
    SECURITY_MSG_CONFIRM_REGISTRATION = ('Instruções de confirmação foram enviadas para %(email).', 'success')
    SECURITY_MSG_EMAIL_CONFIRMED = ('Seu email foi confirmado.', 'success')
    SECURITY_MSG_ALREADY_CONFIRMED = ('Seu email já foi confirmado.', 'info')
    SECURITY_MSG_INVALID_CONFIRMATION_TOKEN = ('Token de confirmação inválido.', 'error')
    SECURITY_MSG_EMAIL_ALREADY_ASSOCIATED = ('%(email) já está associado a uma conta.', 'error')
    SECURITY_MSG_PASSWORD_MISMATCH = ('Senha não corresponde', 'error')
    SECURITY_MSG_RETYPE_PASSWORD_MISMATCH = ('As senhas não coincidem', 'error')
    SECURITY_MSG_INVALID_REDIRECT = ('Redirecionamentos fora do domínio são proibidos', 'error')
    SECURITY_MSG_PASSWORD_RESET_REQUEST = ('Instruções para redefinir sua senha foram enviadas para %(email)s.', 'info')
    SECURITY_MSG_PASSWORD_RESET_EXPIRED = ('Você não redefiniu sua senha em %(within)s. '
                                           'Novas instruções foram enviadas para %(email)s.', 'error')
    SECURITY_MSG_INVALID_RESET_PASSWORD_TOKEN = ('Token de senha de redefinição inválido.', 'error')
    SECURITY_MSG_CONFIRMATION_REQUIRED = ('E-mail requer confirmação.', 'error')
    SECURITY_MSG_CONFIRMATION_REQUEST = ('Instruções de confirmação foram enviadas para %(email)s.', 'info')
    SECURITY_MSG_CONFIRMATION_EXPIRED = ('Você não confirmou seu e-mail em %(within)s. Novas instruções para '
                                         'confirmar seu e-mail foram enviadas para %(email)s.', 'error')
    SECURITY_MSG_LOGIN_EXPIRED = ('Você não fez login em %(within)s. Novas instruções para login foram '
                                  'enviadas para %(email)s.', 'error')
    SECURITY_MSG_LOGIN_EMAIL_SENT = ('Instruções para o login foram enviadas para %(email)s.', 'success')
    SECURITY_MSG_INVALID_LOGIN_TOKEN = ('Token de login inválido.', 'error')
    SECURITY_MSG_DISABLED_ACCOUNT = ('Conta está desabilitada.', 'error')
    SECURITY_MSG_EMAIL_NOT_PROVIDED = ('E-mail não fornecido.', 'error')
    SECURITY_MSG_INVALID_EMAIL_ADDRESS = ('Endereço de email inválido.', 'error')
    SECURITY_MSG_PASSWORD_NOT_PROVIDED = ('Senha não fornecida.', 'error')
    SECURITY_MSG_PASSWORD_NOT_SET = ('Nenhuma senha está definida para este usuário.', 'error')
    SECURITY_MSG_PASSWORD_INVALID_LENGTH = ('A senha deve ter pelo menos 6 caracteres.', 'error')
    SECURITY_MSG_USER_DOES_NOT_EXIST = ('Usuário especificado não existe.', 'error')
    SECURITY_MSG_INVALID_PASSWORD = ('Senha inválida.', 'error')
    SECURITY_MSG_PASSWORDLESS_LOGIN_SUCCESSFUL = ('Você fez login com sucesso.', 'success')
    SECURITY_MSG_FORGOT_PASSWORD = ('Esqueceu a senha?', 'info')
    SECURITY_MSG_PASSWORD_RESET = ('Você redefiniu sua senha com sucesso e fez login automaticamente.', 'success')
    SECURITY_MSG_PASSWORD_IS_THE_SAME = ('Sua nova senha deve ser diferente da senha anterior.', 'error')
    SECURITY_MSG_PASSWORD_CHANGE = ('Você mudou sua senha com sucesso.', 'success')
    SECURITY_MSG_LOGIN = ('Por favor, faça o login para acessar esta página.', 'info')
    SECURITY_MSG_REFRESH = ('Por favor reautenticar para acessar esta página.', 'info')


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    ENV = 'dev'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///testes.db'
    SECRET_KEY = 'a9eec0e0-23b7-4788-9a92-318347b9a39f'


class ProductionConfig(BaseConfig):
    DEBUG = False
    ENV = 'prod'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://user:pass@localhost/testes'
    SECRET_KEY = '8c0caeb1-6bb2-4d2d-b057-596b2dcab18e'


config = {
    "dev": "projeto.config.DevelopmentConfig",
    "prod": "projeto.config.ProductionConfig",
}


def configure_app(app):
    config_name = os.getenv('FLASK_CONFIGURATION', 'dev')
    app.config.from_object(config[config_name])


