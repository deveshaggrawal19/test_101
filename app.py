from flask import Flask, request, url_for, jsonify, Response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Test, Base
import json


engine = create_engine('postgresql+psycopg2://test_user:test_password@localhost/test_101')
Base.metadata.bind = engine
Data_session = sessionmaker(bind=engine)
session = Data_session()
app = Flask(__name__)

# config
app.config['SECRET_KEY'] = 'kdajfoiwarjai3uriufoisdkjvaiowru09weiufajoiwehrfw3iuefjo'

@app.route('/post_location', methods=['POST'])
def post_location():
    data = request.json
    if data.get('lat') and data.get('lng') and data.get('name'):
        new = Test()
        new.name = data['name']
        new.lat = data['lat']
        new.lng = data['lng']
        try:
            session.add(new)
            session.commit()
            data = {'Response': 'Data successfully added to database'}
        except Exception as e:
            session.rollback()
            data = {'Response': 'Error'}
    else:
        data = {'Response': 'Please post correct data'}
    resp = jsonify(data)
    return resp


@app.route('/get_using_postgres', methods=['GET'])
def get_postgres():
    if request.args.get('lat') and request.args.get('lng'):
        lat = request.args['lat']
        lng = request.args['lng']
        data = {'Response': 'request successful'}
    else:
        data = {'Respone': 'request unsuccessfull'}
    resp = jsonify(data)
    return resp


@app.route('/get_using_self', methods=['GET'])
def get_self():
    pass

if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1')
