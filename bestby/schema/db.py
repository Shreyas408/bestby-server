from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

_engine = create_engine('mysql+pymysql://devuser:password@localhost/bestby2')
Session = sessionmaker(bind=_engine)


