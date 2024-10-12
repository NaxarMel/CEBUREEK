import os

from flask import Flask, request
from configparser import ConfigParser
from blueprints import register_blueprint


def create_app():
    flask_app = Flask(__name__)
    flask_app.secret_key = os.urandom(24)

    config = ConfigParser()
    config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
    config.read(config_file)

    flask_config = config['flask']
    flask_app.config['DEBUG'] = flask_config.getboolean('DEBUG')

    register_blueprint(flask_app)

    return flask_app



if __name__ == '__main__':
    app = create_app()
    app.run()
