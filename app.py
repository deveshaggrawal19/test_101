from flask import Flask, request, url_for, jsonify, Response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Test, Base
import json
from math import cos, asin, sqrt

engine = create_engine('postgresql+psycopg2://test_user:test_password@localhost/test_101')
Base.metadata.bind = engine
Data_session = sessionmaker(bind=engine)
session = Data_session()
app = Flask(__name__)

# config
app.config['SECRET_KEY'] = 'kdajfoiwarjai3uriufoisdkjvaiowru09weiufajoiwehrfw3iuefjo'


def distance(lat1, lng1, lat2, lng2):
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lng2 - lng1) * p)) / 2
    return 12742 * asin(sqrt(a)) #2*R*asin...


def computation(lat, lng, rad=5):
    query = session.query(Test).all()
    response = []
    for i in query:
        tmp_lat = i.lat
        tmp_lng = i.lng
        if distance(tmp_lat, tmp_lng, lat, lng) <= rad:
            response.append(i.name)
        else:
            pass
    return response


@app.route('/post_location', methods=['POST'])
def post_location():
    data = request.json
    print(data)
    if data.get('lat') and data.get('lng') and data.get('name'):
        new = Test()
        new.name = str(data['name'])
        new.lat = float(data['lat'])
        new.lng = float(data['lng'])
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

# select name from test WHERE earth_box(ll_to_earth(40.478,73.987), 50000) @> ll_to_earth(test.lat, test.lng);
@app.route('/get_using_postgres', methods=['GET'])
def get_postgres():
    print(request.args)
    if request.args.get('lat') and request.args.get('lng'):
        lat = float(request.args['lat'])
        lng = float(request.args['lng'])
        if request.args.get('rad'):
            rad = float(request.args.get('rad'))*1000
            result = session.execute('select name from test WHERE earth_box(ll_to_earth(%s,%s), %s) @> ll_to_earth(test.lat, test.lng);' % (str(lat), str(lng), rad))
        else:
            result = session.execute('select name from test WHERE earth_box(ll_to_earth(%s,%s), 50000) @> ll_to_earth(test.lat, test.lng);' % (str(lat), str(lng)))
        tmp = ''
        for i in result:
            tmp += i.name + ';'
        data = {'Response': 'request successful', 'List': tmp}
    else:
        data = {'Respone': 'request unsuccessfull'}
    resp = jsonify(data)
    return resp


@app.route('/get_using_self', methods=['GET'])
def get_self():
    if request.args.get('lat') and request.args.get('lng'):
        lat = float(request.args['lat'])
        lng = float(request.args['lng'])
        if request.args.get('rad'):
            lst = computation(lat, lng, request.args.get('rad'))
        else:
            lst = computation(lat, lng)
        tmp = ''
        for i in lst:
            tmp += i+';'
        data = {'Response': 'request successful', 'List': tmp}
    else:
        data = {'Respone': 'request unsuccessfull'}
    resp = jsonify(data)
    return resp

if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1')
