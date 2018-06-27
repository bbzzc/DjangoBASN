#!/usr/bin/env python3
# Database setup for Catalog App
# python3 - using SQLAlchemy
# -*- coding: utf-8 -*-
# from flask import Flask, render_template, request
# from flask import redirect, jsonify, url_for, flash
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship, sessionmaker
# from sqlalchemy import create_engine, asc
# from sqlalchemy.sql import text
# import operator, os, sys
# from basuDB import Base, Testimony, Catagory, Event
# from basuDB import Corporation, Client, ExcelMil, ExcelEd
# from basuDB import NonNeg, Concerns, Certification
# from basuDB import CareerInterest, Research, Goal, DreamJob
# from flask import session as login_session
# import random, string, httplib2, json, requests, os
# from oauth2client.client import flow_from_clientsecrets
# from oauth2client.client import FlowExchangeError
# from flask import make_response
# from flask_httpauth import HTTPBasicAuth
# #from flask_debug import Debug
# from flask import send_from_directory
# from sqlalchemy import *
# from sqlalchemy.schema import DDLElement
# from sqlalchemy.sql import table
# from sqlalchemy.ext import compiler

import os
import sys
# auth = HTTPBasicAuth()


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dg_basu.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
