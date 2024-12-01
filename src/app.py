from flask import Flask
# from dotenv import load_dotenv
from api.v1.routes import v1_blueprint
from api.v1.logger import successmessage
# from config.envs import get_server_host, get_server_port
import logging
from config.envs import get_server_host, get_server_port


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


app = Flask(__name__)
app.register_blueprint(v1_blueprint)

if __name__ == "__main__":
    protocol = 'http'
    successmessage(f"""Server run in
              - {protocol}://{get_server_host()}:{get_server_port()}
    """)
    app.run(host='0.0.0.0', port=5000)
