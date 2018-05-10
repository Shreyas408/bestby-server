from sqlalchemy import Column, String
from .basedb import Base

class Recipe(Base):
    name = Column(String(255))
    def to_view(self):
        return {
            'id':self.id,
            'name':self.name
        }




