from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)

def db_conn():
    conn = None
    try:
        conn = sqlite3.connect("housing_db.db")
    except sqlite3.error as e:
        print(e)
    return conn

