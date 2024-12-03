from flask import Flask
from flasgger import Swagger
# from dotenv import load_dotenv
from api.v1.routes import v1_blueprint
from api.v1.logger import success_message
# from config.envs import get_server_host, get_server_port
import logging
from config.envs import get_server_host, get_server_port


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


# app = Flask(__name__)
# app.register_blueprint(v1_blueprint)

def create_app():
    """Cria e configura a aplicação Flask."""
    app = Flask(__name__)
    Swagger(app, template_file='../swagger.yml')

    # Configurar logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    # Registrar blueprints
    app.register_blueprint(v1_blueprint)

    # Configurações adicionais (se necessário)
    app.config['DEBUG'] = False  # Exemplo de configuração
    return app


if __name__ == "__main__":
    app = create_app()
    protocol = 'http'
    host = get_server_host() or '127.0.0.1'
    port = get_server_port() or 5000

    success_message(f"""Server running at:
                  - {protocol}://{host}:{port}
        """)
    app.run(host=host, port=port)