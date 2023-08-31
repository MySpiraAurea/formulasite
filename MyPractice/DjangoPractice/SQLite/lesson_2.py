import sqlite3 as sq

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute('''DROP TABLE IF EXISTS users
    ''')
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_ TEXT NOT NULL,
    sex INTEGER NOT NULL DEFAULT 1,
    old_ INTEGER,
    score INTEGER
    )
    ''')

#with sq.connect('games.db') as con:
#    cur = con.cursor()
#    cur.execute('''DROP TABLE IF EXISTS games
#    ''')
#    cur.execute('''CREATE TABLE IF NOT EXISTS games (
#    user_id TEXT NOT NULL,
#    score INTEGER DEFAULT 0,
#    time_ INTEGER
#    )
#    ''')