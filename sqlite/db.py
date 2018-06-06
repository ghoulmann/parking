import sqlite3
from flask import g

DATABASE = '../data/parking_app.db'
SQL_FILE = '../data/parking_app.sql'
def get_db():
    db = getattr(g, '_database', None)
    db.row_factory = sqlite3.Row
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)

    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def init_db(sql_file):
    with app.app_context():
        db = get_db()
        with app.open_resource(sql_file, mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
