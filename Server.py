from unicodedata import name
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


#engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
engine = create_engine('sqlite:///:memory:', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Tabledata(Base):
    __tablename__ = 'userdata'
    uid = Column(Integer, primary_key=True)
    name = Column(String(50), unique=False)
    birth = Column(String(50), unique=False)
    phone = Column(String(50), unique=True)
    email = Column(String(50), unique=True)

    def __init__(self, name=None, birth=None, phone=None, email=None):
        self.name = name
        self.birth = birth
        self.phone = phone
        self.email = email

    def _to_dict(self):
        dict_ = {"name": self.name,
                 "birth": self.birth,
                 "phone": self.phone,
                 "email": self.email,
                 "uid": self.uid}
        return dict_

    def columns_to_dict(self):
        dict_ = {}
        for key in self.__mapper__.c.keys():
            dict_[key] = getattr(self, key)
        return dict_

    def __repr__(self):
        return f'<User {self.name!r}>'

print(Base.metadata.tables.values())
Base.metadata.create_all(bind=engine)


from flask import Flask
from flask import request
from flask import jsonify
from werkzeug.serving import WSGIRequestHandler
import json

if db_session.query(Tabledata).first() is None:
        i = Tabledata("Seung Gee, Jung","July, 17, 1998", "010-6205-3776", "wjdtmdrl777@naver.com")
        db_session.add(i)
        db_session.commit()

WSGIRequestHandler.protocol_version = "HTTP/1.1"

app = Flask(__name__)

@app.route("/User", methods=['GET'])
def get_data():
    userdata = db_session.query(Tabledata).first()

    if userdata is None:
        return jsonify(success=False)
    else:
        return jsonify(success=True, userdata=userdata._to_dict())


@app.route('/')
def hello_world():
    return 'Hello World!'

app.run(host='127.0.0.1', port=8000)