# Database setup for Catalog App
# python3 - using SQLAlchemy
import datetime, random, string
from sqlalchemy import DateTime, ForeignKey, Index
from sqlalchemy import Column,Integer,String,DateTime,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
#from passlib.apps import custom_app_context as pwd_context
from sqlalchemy import *
from sqlalchemy.schema import DDLElement
from sqlalchemy.sql import table
from sqlalchemy.ext import compiler
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

Base = declarative_base()
secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))

advo = "Advocacy"
excel = "Excel with a Mentor"
comm = "Community Partnerships"

# USER Base MODEL
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    picture = Column(String(250))
    bio = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password_hash = Column(String(64))

    def __repr__(self):
        return "<User(name='%s', bio='%s', email='%s')>" % (self.username, self.bio, self.email)


    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
    	s = Serializer(secret_key, expires_in = expiration)
    	return s.dumps({'id': self.id })

    @staticmethod
    def verify_auth_token(token):
    	s = Serializer(secret_key)
    	try:
    		data = s.loads(token)
    	except SignatureExpired:
    		#Valid Token, but expired
    		return None
    	except BadSignature:
    		#Invalid Token
    		return None
    	user_id = data['id']
    	return user_id

class Catagory(Base):
    __tablename__ = 'catagory'

    cat_id = Column(Integer, primary_key=True)
    cat_code = Column(String(3), nullable=False)
    cat_name = Column(String(250), nullable=False)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
        'cat_id' : self.cat_id,
        'catName' : self.catName,
            }

# Testimonies
class Testimony(Base):
    __tablename__ = 'testimony'
    test_id = Column(Integer, primary_key=True)
    pic_descript = Column(String(255))
    picture = Column(String(250))
    testimony = Column(String(250), nullable=False)
    keywords = Column(String(250), nullable=False)
    cat_id = Column(Integer, nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
        'testimony' : self.testimony,
        'picture' : self.picture,
        'pic_descript' : self.pic_descript,
        'keywords' : self.keywords,
        'cat_id' : self.cat_id,
            }


class Event(Base):
    __tablename__ = 'event'

    event_id = Column(Integer, primary_key=True)
    eventName = Column(String(250), nullable=False)
    cat_id = Column(Integer, nullable=False)
    start_date = Column(DateTime, default=datetime.datetime.utcnow)
    end_date = Column(DateTime, default=datetime.datetime.utcnow)
    start_time = Column(DateTime, default=datetime.datetime.utcnow)
    end_time = Column(DateTime, default=datetime.datetime.utcnow)
    location = Column(String(250), nullable=False)
    POC_name = Column(String(255))
    POC_phone = Column(String(15))
    attendee = Column(String(255))


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
        'event_id' : self.event_id,
        'catagory_id' : self.cat_id,
        'start_date' : self.start_date,
        'end_date' : self.end_date,
        'start_time' : self.start_time,
        'end_time' : self.end_time,
        'location' : self.location,
        'POC_name' : self.POC_name,
        'POC_phone' : self.POC_phone,
        'attendee' : self.attendee,
            }


class Corporation(Base):
    __tablename__ = 'corporation'

    corp_id = Column(Integer, primary_key=True)
    corp_name = Column(String(250), nullable=False)
    addr_1 = Column(String(250), nullable=False)
    addr_2 = Column(String(250), nullable=False)
    city = Column(String(250), nullable=False)
    state = Column(String(15), nullable=False)
    zip_code = Column(String(15), nullable=False)
    POC_name = Column(String(250), nullable=False)
    POC_phone = Column(String(15), nullable=False)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
        'corp_id' : self.corp_id,
        'corp_name' : self.corp_name,
        'addr_1' : self.addr_1,
        'addr_2' : self.addr_2,
        'city' : self.city,
        'state' : self.state,
        'zip_code' : self.zip_code,
        'POC_name' : self.POC_name,
        'POC_phone' : self.POC_phone,
            }

class Client(Base):
    __tablename__ = 'client'

    client_id = Column(Integer, primary_key=True)
    cat_id = Column(Integer, nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    addr_1 = Column(String(250), nullable=False)
    addr_2 = Column(String(250), nullable=False)
    city = Column(String(250), nullable=False)
    state = Column(String(15), nullable=False)
    zip_code = Column(String(15), nullable=False)
    h_phone = Column(String(15), nullable=False)
    c_phone = Column(String(15), nullable=False)
    w_phone = Column(String(15), nullable=False)
    preference = Column(String(4), nullable=False)
    w_email = Column(String(250), nullable=False)
    p_email = Column(String(250), nullable=False)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
        'client_id' : self.client_id,
        'cat_id' : self.cat_id,
        'first_name' : self.first_name,
        'last_name' : self.last_name,
        'addr_1' : self.addr_1,
        'addr_2' : self.addr_2,
        'city' : self.city,
        'state' : self.state,
        'zip_code' : self.zip_code,
        'h_phone' : self.h_phone,
        'c_phone' : self.c_phone,
        'w_phone' : self.w_phone,
        'preference' : self.preference,
        'w_email' : self.w_email,
        'p_email' : self.p_email,
            }

class ExcelMil(Base):
    __tablename__ = 'excelMil'

    excel_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, nullable=False)
    official_DOS = Column(DateTime, nullable=False)
    terminal_lv = Column(DateTime, nullable=False)
    yr_service = Column(Integer, nullable=False)
    branch = Column(String(100), nullable=False)
    pay_grade = Column(String(100), nullable=False)
    relocate = Column(Boolean, nullable=False)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
        'client_id' : self.client_id,
        'excel_id' : self.excel_id,
        'official_DOS' : self.official_DOS,
        'terminal_lv' : self.terminal_lv,
        'yr_service' : self.yr_service,
        'branch' : self.branch,
        'pay_grade' : self.pay_grade,
        'relocate' : self.relocate,
            }

class ExcelEd(Base):
    __tablename__ = 'excelEd'

    ed_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, nullable=False)
    school_name = Column(String(250), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    degree = Column(String(250), nullable=False)
    major = Column(String(250), nullable=False)
    minor = Column(String(250), nullable=False)
    addr_1 = Column(String(250), nullable=False)
    addr_2 = Column(String(250), nullable=False)
    city = Column(String(250), nullable=False)
    state = Column(String(15), nullable=False)
    zip_code = Column(String(15), nullable=False)
    status = Column(String(255), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
        'client_id' : self.client_id,
        'ed_id' : self.ed_id,
        'school_name' : self.school_name,
        'start_date' : self.start_date,
        'end_date' : self.end_date,
        'degree' : self.degree,
        'major' : self.major,
        'minor' : self.minor,
        'addr_1' : self.addr_1,
        'addr_2' : self.addr_2,
        'city' : self.city,
        'state' : self.state,
        'zip_code' : self.zip_code,
        'status' : self.status,
            }

class NonNeg(Base):
    __tablename__ = 'nonNeg'

    neg_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, nullable=False)
    nonNeg_item = Column(String(250), nullable=False)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
        'client_id' : self.client_id,
        'neg_id' : self.ed_id,
        'excel_id' : self.excel_id,
        'nonNeg_item' : self.nonNeg_item,
            }

class Concerns(Base):
    __tablename__ = 'concerns'

    concern_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, nullable=False)
    concern = Column(String(250), nullable=False)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
        'client_id' : self.client_id,
        'concern_id' : self.concern_id,
        'concern' : self.concern,
            }

class Certification(Base):
    __tablename__ = 'certification'

    cert_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, nullable=False)
    cert = Column(String(250), nullable=False)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
        'client_id' : self.client_id,
        'cert_id' : self.cert_id,
        'cert' : self.cert,
            }

class CareerInterest(Base):
    __tablename__ = 'careerInterest'

    carInt_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, nullable=False)
    careers = Column(String(250), nullable=False)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
        'client_id' : self.client_id,
        'carInt_id' : self.carInt_id,
        'careers' : self.careers,
            }

class Research(Base):
    __tablename__ = 'research'

    reach_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, nullable=False)
    research_comp = Column(String(250), nullable=False)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
        'client_id' : self.client_id,
        'reach_id' : self.reach_id,
        'reserach_comp' : self.research_comp,
            }

class Goal(Base):
    __tablename__ = 'goal'

    goal_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, nullable=False)
    goals = Column(String(250), nullable=False)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
        'client_id' : self.client_id,
        'goal_id' : self.goal_id,
        'goals' : self.goals,
            }

class DreamJob(Base):
    __tablename__ = 'dreamJob'

    dream_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, nullable=False)
    dream_job = Column(String(250), nullable=False)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
        'client_id' : self.client_id,
        'dream_id' : self.goal_id,
        'dream_job' : self.dream_job,
            }

    view1 = "CREATE VIEW test_plus AS" \
         " SELECT testimony, keywords, picture, pic_descript, cat_name" \
         " FROM Catagory, Testimony" \
         " ON Catagory.cat_id = Testimony.cat_id" \
         " WHERE cat_name = advo" \
         " OR cat_name = comm" \
         " OR cat_name = excel"

engine = create_engine('sqlite:///basu.db')

Base.metadata.create_all(engine)

conn = engine.connect()
