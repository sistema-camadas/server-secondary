from flask import Flask
from models.database import init_db
from controllers.user_controller import user_bp
from controllers.health_controller import health_bp

app = Flask(__name__)

# Inicializa o banco
init_db(app)

# Registra rotas
app.register_blueprint(user_bp)
app.register_blueprint(health_bp)

if __name__ == '__main__':
    app.run(port=8000)
