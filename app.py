from flask import Flask
from models.database import init_db, db
from controllers.user_controller import user_bp
from controllers.health_controller import health_bp
import os


app = Flask(__name__)

# Inicializa o banco
init_db(app)

# Cria as tabelas se não existirem
with app.app_context():
    db.create_all()

# Registra rotas
app.register_blueprint(user_bp)
app.register_blueprint(health_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
