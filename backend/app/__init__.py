from flask import Flask, jsonify
from .database import db
import os

def create_app():
    app = Flask(__name__)
    
    db_user = os.environ.get('POSTGRES_USER', 'postgres')
    db_pass = os.environ.get('POSTGRES_PASSWORD', 'bellidiel123')
    db_name = os.environ.get('POSTGRES_DB', 'bellidiel_db')
    db_host = os.environ.get('DB_HOST', 'db')
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_pass}@{db_host}:5432/{db_name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    with app.app_context():
        from . import models
        db.create_all()

    # Ruta de prueba 
    @app.route('/status', methods=['GET'])
    def status():
        return jsonify({"estado": "Servidor BelliDiel Activo", "base_de_datos": "Conectada"})

    

    @app.route('/api/menu', methods=['GET'])
    def obtener_menu():
        from .models import CatalogoMenu
        productos = CatalogoMenu.query.all()
        return jsonify([producto.to_dict() for producto in productos])

    return app