from .database import db
from datetime import datetime

class Transaccion(db.Model):
    __tablename__ = 'transacciones'
    
    id = db.Column(db.Integer, primary_key=True)
    bebida = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "bebida": self.bebida,
            "cantidad": self.cantidad,
            "total": self.total,
            "fecha": self.fecha.isoformat()
        }

class CatalogoMenu(db.Model):
    __tablename__ = 'catalogo_menu'
    
    product_id = db.Column(db.String(50), primary_key=True)
    unit_price = db.Column(db.Numeric(10, 2))
    product_category = db.Column(db.String(100))
    product_type = db.Column(db.String(100))
    product_detail = db.Column(db.String(255))

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "unit_price": float(self.unit_price), 
            "product_category": self.product_category,
            "product_type": self.product_type,
            "product_detail": self.product_detail
        }