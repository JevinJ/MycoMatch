from database.db_base import BaseModel
import sqlalchemy as db


class Color(BaseModel):
    __tablename__ = 'colors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    hex_value = db.Column(db.String(7))