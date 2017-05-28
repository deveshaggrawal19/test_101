from flask import Flask, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Subscribe, Base, Query


engine = create_engine('postgresql+psycopg2://test_user:test_password@localhost/test_101')
Base.metadata.bind = engine
Data_session = sessionmaker(bind=engine)
session = Data_session()
app = Flask(__name__)

# config
app.config['SECRET_KEY'] = 'kdajfoiwarjai3uriufoisdkjvaiowru09weiufajoiwehrfw3iuefjo'

@app.route('/post_location', methods=['POST'])
def post_location():
    pass


@app.route('/get_using_postgres', methods=['GET'])
def get_postgres():
    pass


@app.route('/get_using_self', methods=['GET'])
def get_self():
    pass

if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1')
