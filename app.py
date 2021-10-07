from flask import Flask
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from api.route.home import home_api
from config import DevelopmentConfig as Config


def create_app():
    app = Flask(__name__)
    db = SQLAlchemy()
    migrate = Migrate()

    app.config['SWAGGER'] = {
        'title': 'API Docs',
    }

    swagger = Swagger(app)

    # Initialize Config

    app.config.from_object(Config())
    app.register_blueprint(home_api, url_prefix='/api')
    db.init_app(app)
    migrate.init_app(app, db)

    return app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)
