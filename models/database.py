import sqlite3
from contextlib import contextmanager

class Database:
    DB_FILE = 'user.db'

    @classmethod
    def init_app(cls):
        "Inicializa o banco de dados criando a tabela de usuário"
        with sqlite3.connect(cls.DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE
                )
            ''')
            conn.commit()

    @classmethod
    @contextmanager
    def get_connection(cls):
        "Context manager para obter uma conexão com o banco de dados"
        conn = sqlite3.connect(cls.DB_FILE)
        conn.row_factory = sqlite3.Row 
        try:
            yield conn
        finally:
            conn.close()

