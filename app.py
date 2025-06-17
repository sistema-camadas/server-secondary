from flask import Flask
from controllers.user_controller import user_blueprint
from controllers.health_controller import health_blueprint
from models.database import Database
import os

def create_app():
    app = Flask(__name__)
    
    # Load configuration from environment variables
    app.config['SERVER_PORT'] = int(os.getenv('SERVER_PORT', 8000))
    app.config['SERVER_NAME'] = os.getenv('SERVER_NAME', 'SERVER1')
    
    # Initialize the database
    Database.init_app(app)
    
    # Register blueprints
    app.register_blueprint(user_blueprint, url_prefix='/users')
    app.register_blueprint(health_blueprint)
    
    return app

if __name__ == '__main__':
    app = create_app()
    port = app.config['SERVER_PORT']
    server_name = app.config['SERVER_NAME']

    print(f"🚀 Iniciando {server_name} na porta {port}")
    app.run(host='0.0.0.0', port=port, debug=True)
