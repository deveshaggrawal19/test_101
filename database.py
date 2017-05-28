from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine


Base = declarative_base()


class Test(Base):
    __tablename__ = 'test'
    name = Column(String(80), nullable=False, unique=False)
    lat = Column(Float nullable=False)
    lng = Column(Float nullable=False)


engine = create_engine('mysql+pymysql://root:toor@127.0.0.1:3306/blockriti')
Base.metadata.create_all(engine)
