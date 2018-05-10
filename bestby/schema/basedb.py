from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base(object):
    @declared_attr
    def __tablename__(cls): # pylint: disable=E0213
        return cls.__name__.lower() 
    id = Column(Integer, primary_key=True)

