from flask import Flask, render_template, request, redirect
from pymongo import
app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['student_database']

@app.route('/')
