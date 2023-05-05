"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaak43hp8u791gupi50-a.oregon-postgres.render.com",
        database="todo_k5qa",
        user="todo_k5qa_user",
        password="Q1UnTrEbZC1ZXi7txtxrxAWOc4t3tL35")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
