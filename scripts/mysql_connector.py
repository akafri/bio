#!/usr/bin/python
import mysql.connector


def connect(host, user, passwd, db):
    try:
	mysql.connector.connect(host, user, passwd, db);
    except Exception as e:
	raise e

def disconnect(db):


def execute_query(db, query):


def execute_query_with_res(db, query):



db = mysql.connector.connect(host="localhost", # your host, usually localhost
                     user="akafri", # your username
                     passwd="admin", # your password
                      db="chromosomes_k_mer") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 
