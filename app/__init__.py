from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.controllers.user_controller import user_bp
    app.register_bluepreint(user_bp)

    return app