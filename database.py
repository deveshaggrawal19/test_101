from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy import create_engine


Base = declarative_base()


class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)


engine = create_engine('postgresql+psycopg2://test_user:test_password@localhost/test_101')
Base.metadata.create_all(engine)
