import os
from flask import Flask


def create_app():
    app = Flask(__name__)
    from routes import bp
    app.register_blueprint(bp)
    return app


def _str_to_bool(value: str) -> bool:
    return str(value).strip().lower() in {'1', 'true', 't', 'yes', 'y', 'on'}


if __name__ == '__main__':
    app = create_app()
    debug = _str_to_bool(os.getenv('FLASK_DEBUG', 'false'))
    host = os.getenv('FLASK_HOST', '127.0.0.1')
    port = int(os.getenv('FLASK_PORT', '5000'))
    app.run(host=host, port=port, debug=debug)
