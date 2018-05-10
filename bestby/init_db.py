from schema.db import _engine
from schema.recipe import Recipe
from schema.basedb import Base

if __name__ == "__main__":
    Base.metadata.create_all(_engine)
