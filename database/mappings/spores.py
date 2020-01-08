from ..mixins import HasWidth, HasLength
from database.db_base import BaseModel
from database.mappings.color import FungusColorMapping
from database.mappings.tag import FungusTagMapping, Tag
from sqlalchemy import Column, Enum, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Spores(BaseModel):
    """Description of a mushrooms' spores."""
    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)
    color = relationship('Color', secondary='spore_color')
    mezlers_reaction = Column(Enum)
    dimensions = relationship('SporeDimensions')
    shape = relationship('SporeShape', secondary='fungus_spore_shape')
    ornamentation = relationship('SporeOrnamentation', secondary='fungus_spore_ornamentation')


class SporeDimensions(BaseModel, HasWidth, HasLength):
    id = Column(Integer, primary_key=True)
    fungus_id = Column(Integer, ForeignKey('spores.fungus_id'), primary_key=True)


class SporeColor(FungusColorMapping):
    fungus_id = Column(Integer, ForeignKey('spores.fungus_id'), primary_key=True)


class FungusSporeShape(FungusTagMapping):
    fungus_id = Column(Integer, ForeignKey('spores.fungus_id'), primary_key=True)


class FungusSporeOrnamentation(FungusTagMapping):
    fungus_id = Column(Integer, ForeignKey('spores.fungus_id'), primary_key=True)


class SporeShape(Tag): pass
class SporeOrnamentation(Tag): pass

