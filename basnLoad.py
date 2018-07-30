# -*- coding: utf-8 -*-
# Database setup for Boots & Suits United App
# pyton3 - using SQLAlchemy
# code: utf-8

import os, random, string, sys, datetime
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
from basuDB import Base, Testimony, Catagory, Event
from basuDB import Corporation, Client, ExcelMil, ExcelEd
from basuDB import NonNeg, Concerns, Certification
from basuDB import CareerInterest, Research, Goal, DreamJob
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from sqlalchemy import DateTime
from sqlalchemy import Column,Integer,String,DateTime,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
import random, string
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)


engine = create_engine('sqlite:///basu.db')
conn = engine.connect()
trans = conn.begin()
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Catagories
cat1 = Catagory(cat_name="Retired", cat_code="RET")
session.add(cat1)
session.commit()

cat2 = Catagory(cat_name="Spouse", cat_code="DEP")
session.add(cat2)
session.commit()

cat3 = Catagory(cat_name="Seperated", cat_code="SEP")
session.add(cat3)
session.commit()

cat4 = Catagory(cat_name="Seperating Soon (18 months)", cat_code="S18")
session.add(cat4)
session.commit()

cat5 = Catagory(cat_name="Excel with a Mentor", cat_code="EXC")
session.add(cat5)
session.commit()

cat6 = Catagory(cat_name="Advocacy", cat_code="VCY")
session.add(cat6)
session.commit()

cat7 = Catagory(cat_name="Community Partnerships", cat_code="CPS")
session.add(cat7)
session.commit()

cat1 = session.query(Catagory).filter_by(cat_code="RET").one()
cat2 = session.query(Catagory).filter_by(cat_code="DEP").one()
cat3 = session.query(Catagory).filter_by(cat_code="SEP").one()
cat4 = session.query(Catagory).filter_by(cat_code="S18").one()
cat5 = session.query(Catagory).filter_by(cat_code="EXC").one()
cat6 = session.query(Catagory).filter_by(cat_code="VCY").one()
cat7 = session.query(Catagory).filter_by(cat_code="CPS").one()

test1 = Testimony(pic_descript="Smelling Flowers", picture="/static/pic1.jpg", testimony="Excel with a Mentor the the best thing that ever happened to me!!!  My transition from the military to the civilian sector went so smoothly!", keywords="Best Thing That Ever Happened to Me", cat_id=cat5.cat_id)

session.add(test1)
session.commit()

test2 = Testimony(pic_descript="Lighthouse", picture="/static/lighthouse.jpg", testimony="The team help me find resourses that I didn't know existed.  They helped me navigate the VA.", keywords="Helped me find Resources", cat_id=cat6.cat_id)

session.add(test2)
session.commit()

test3 = Testimony(pic_descript="Bachelor Button Purple", picture="/static/pic3.jpg", testimony="We have been so pleased with the talent we have hired from Offutt AFB.  The personnel have exceded our expectations.", keywords="So Pleased with the Talent", cat_id=cat7.cat_id)

session.add(test3)
session.commit()

testimony = session.query(Testimony).all()
for i in testimony:
    output = ''
    output += "Testimony: "
    output += i.testimony
    output += '\n \n ID: '
    output += str(i.test_id)
    output += "Keyword: "
    output += i.keywords
    output += '\n \n cat_ID: '
    output += str(i.cat_id)
    print(output)

print ("Catagories Added!")
