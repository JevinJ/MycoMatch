from database.db_base import BaseModel
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy_utils.types.url import URLType


class WikipediaUrl(BaseModel):
    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)
    value = Column(URLType)
