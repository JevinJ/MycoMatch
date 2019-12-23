from .base import Base
from sqlalchemy import Column, Enum, Integer, ForeignKey


class Smell(Base):
    __tablename__ = 'smells'
    mushroom_id = Column(Integer, ForeignKey('mushrooms.id'), primary_key=True)
    smell = Column(Enum)