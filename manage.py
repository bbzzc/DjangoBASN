#!/usr/bin/env python
# Database setup for Catalog App
# python3 - using SQLAlchemy
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from flask import redirect, jsonify, url_for, flash
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, asc
from sqlalchemy.sql import text
import operator, os, sys
from basuDB import Base, Testimony, Catagory, Event
from basuDB import Corporation, Client, ExcelMil, ExcelEd
from basuDB import NonNeg, Concerns, Certification
from basuDB import CareerInterest, Research, Goal, DreamJob
from flask import session as login_session
import random, string, httplib2, json, requests, os
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from flask import make_response
from flask_httpauth import HTTPBasicAuth
#from flask_debug import Debug
from flask import send_from_directory
from sqlalchemy import *
from sqlalchemy.schema import DDLElement
from sqlalchemy.sql import table
from sqlalchemy.ext import compiler


auth = HTTPBasicAuth()

# Connect to Database and create database session
engine = create_engine('sqlite:///basu.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)
#Debug(app)

# CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Boots and Suits United"

testExcel = str("EXC")
testAdvo = str("VCY")
testComm = str("CPS")

state_abrev = ["AL", "AK","AZ","AR","CA","CO","CT","DE","DC","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MO","MS","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WV","WI","WY"]

branch = ["United States Air Force", "United States Army", "United States Navy", "United States Marine Corps", "United States Coast Guard"]
pay_grade = ["E1","E2","E3","E4","E5","E6","E7","E8","E9","O1","O2","O3","O4","O5","O6","O7","O8","O9","O10"]

@app.route('/')
@app.route('/basn')
def showHome():


    sql = text("SELECT cat_name, Catagory.cat_id, pic_descript, picture, testimony, keywords" \
        " FROM Catagory, Testimony" \
        " WHERE Catagory.cat_id = Testimony.cat_id" \
        " AND (cat_code = 'EXC'" \
        " OR cat_code = 'VCY'" \
        " OR cat_code = 'CPS')")

    test_all = session.execute(sql)
#    test_all = session.query(Catagory, Testimony).filter_by(Catagory.cat_id=Testimony.cat_id).filter(or_(cat_code = "EXC", cat_code = "VCY", cat_code = "CPS")).all()
    counter = 0

    for x in test_all:
        output = ''
        output += "Pic Descript: "
        output += x.pic_descript
        counter += 1
        output += " /n counter: "
        output += str(counter)
        print (output)

    counter = 0

    for x in test_all:
        if x.cat_name == testExcel:
            if x.picture == Null:
                entry = {'picture': "fontenelle.jpg", 'pic_descript': "Fontenelle Forest Boardwalk"}
                test_all.append(entry)
                counter += 1
            if x.cat_name == testAdvo:
                if x.picture == Null:
                    entry = {'picture': "omaha.jpg", 'pic_descript': "Downtown Omaha"}
                    test_all.append(entry)
                    counter += 1
            if x.cat_name == testComm:
                if x.picture == Null:
                    entry = {'picture': "jungle.jpeg", 'pic_descript': "Lied Jungle Rope Bridge"}
                    test_all.append(entry)
                    counter += 1

    return render_template('basu.html', testimony=test_all)

# Display the excel program
@app.route('/basn/excel')
def showExcel():

    return render_template('excel.html')

# Register a new client - first generic
@app.route('/basn/excel/new', methods=['GET', 'POST'])
def newClient():

    if request.method == 'POST':
        preference = request.form['phone-pref']
        status = request.form['status']
        stat =  session.query(Catagory).filter(cat_code=testExcel).one()

        addClient = Client(
            first_name=request.form['f_name'], last_name=request.form['l_name'],
            addr_1=request.form['addr-1'], addr_2=request.form['addr-2'],
            city=request.form['city'], state=request.form['state'],
            zip=request.form['zip'], p_email=request.form['p_email'],
            w_email=request.form['w_email'], h_phone=request.form['h-phone'],
            c_phone=request.form['c-phone'], w_phone=request.form['w-phone'],
            cat_id=stat, preference=preference)

        session.add(addClient)
        session.commit()
        flash('New Client Successfully Created')

        sql = text("SELECT client_id" \
            " FROM Client" \
            " WHERE cat_id = stat" \
            " AND first_name = request.form['f_name']" \
            " AND last_name = request.form['l_name']")

        newClientID = session.execute(sql)

        if request.form['school_name'] != Null:
            school_name = request.form['school_name']
        if request.form['school_city'] != Null:
            city = request.form['school_city']
        if request.form['sch_addr-1'] != Null:
            addr_1 = request.form['sch_addr-1']
        if request.form['sch_addr-2'] != Null:
            addr_2 = request.form['sch_addr-2']
        if request.form['school_state'] != Null:
#            for x in state_abrev:
#                if state_abrev[x] == request.form['school_state']
            state = request.form['school_state']
        if request.form['school_zip'] != Null:
            zip_code = request.form['school_zip']
        if request.form['degree'] != Null:
            degree = request.form['degree']
        if request.form['major'] != Null:
            major = request.form['major']
        if request.form['minor'] != Null:
            minor = request.form['minor']
        if request.form['start_date'] != Null:
            start_date = request.form['start_date']
        if request.form['end_date'] != Null:
            end_date = request.form['end_date']
        if request.form['status'] != Null:
            status = request.form['status']

        if request.form['school_name2'] != Null:
            school_name2 = request.form['school_name2']
        if request.form['school_city2'] != Null:
            city2 = request.form['school_city2']
        if request.form['sch2_addr-1'] != Null:
            addr2_1 = request.form['sch2_addr-1']
        if request.form['sch2_addr-2'] != Null:
            addr2_2 = request.form['sch2_addr-2']
        if request.form['school_state2'] != Null:
#            for x in state_abrev:
#                if x == request.form['school_state2']
            state2 = request.form['school_state2']
        if request.form['school_zip2'] != Null:
            zip_code2 = request.form['school_zip2']
        if request.form['degree2'] != Null:
            degree2 = request.form['degree2']
        if request.form['major2'] != Null:
            major2 = request.form['major2']
        if request.form['minor2'] != Null:
            minor2 = request.form['minor2']
        if request.form['start_date2'] != Null:
            start_date2 = request.form['start_date2']
        if request.form['end_date2'] != Null:
            end_date2 = request.form['end_date2']
        if request.form['status2'] != Null:
            status2 = request.form['status2']

        if school_name != Null:
            addEd1 = ExcelEd(
                client_id=newClientID, school_name=school_name,
                start_date=start_date, addr_1=addr_1, addr_2=addr_2,
                city=city, state=state, zip=zip_code, end_date=end_date,
                degree=degree, major=major, minor=minor, status=status)

            session.add(addEd1)
            session.commit()
            flash('New Client with Education Created')

        if school_name2 != Null:
            addEd2 = ExcelEd(
                client_id=newClientID, school_name=school_name2,
                start_date=start_date2, addr_1=addr2_1, addr_2=addr2_2,
                city=city2, state=state2, zip=zip_code2, end_date=end_date2,
                degree=degree2, major=major2, minor=minor2, status=status2)

            session.add(addEd2)
            session.commit()
            flash('New Client with Education Created')

        if status == 'Spouse':
            return redirect(url_for('newClientGen'))
        else:
            return redirect(url_for('newClientMil'))
    else:
        return render_template('excel-form1.html')

# Register a new client - second generic
@app.route('/basn/excel/new2', methods=['GET', 'POST'])
def newClientGen():

        return render_template('excel-formG.html')

# Display the excel program
@app.route('/basn/advocacy')
def showAdvocacy():

    return render_template('advocacy.html')

# Display the excel program
@app.route('/basn/advocacy/new')
def newAdvocacy():

    return render_template('advocacy.html')

# Display the community partnership program
@app.route('/basn/community')
def showComm():

    return render_template('community.html')

@app.route('/basn/community/new')
def newComm():

    return render_template('community.html')

# Display the community partnership program
@app.route('/basn/blog')
def showBlog():

    return render_template('blog.html')

# Display the community partnership program
@app.route('/basn/careers')
def showCareers():

    return render_template('careers.html')

# Display the community partnership program
@app.route('/basn/calendar')
def showCalendar():

    return render_template('calendar.html')

# Display the community partnership program
@app.route('/basn/Contributors')
def showContrib():

    return render_template('contrib.html')

# Display the community partnership program
@app.route('/basn/photos')
def showPhotos():

    return render_template('photos.html')

# Display the community partnership program
@app.route('/basn/about-us')
def showAboutUs():

    return render_template('aboutUs.html')

# Display the community partnership program
@app.route('/basn/contacts')
def showContactUs():

    return render_template('contactUs.html')


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

#    app.secret_key = 'super_secret_key'
#    app.debug = True
    app.run(host='0.0.0.0', port=8000)
