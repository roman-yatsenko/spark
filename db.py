# Импорт библиотек
import sqlite3

# Data for DB
projects = [
    ('2020-01-01', '2020-01-02'),
    ('2020-01-02', '2020-01-03'),
    ('2020-01-03', '2020-01-04'),
    ('2020-01-04', '2020-01-05'),
    ('2020-01-06', '2020-01-07'),
    ('2020-01-16', '2020-01-17'),
    ('2020-01-17', '2020-01-18'),
    ('2020-01-18', '2020-01-19'),
    ('2020-01-19', '2020-01-20'),
    ('2020-01-21', '2020-01-22'),
    ('2020-01-26', '2020-01-27'),
    ('2020-01-27', '2020-01-28'),
    ('2020-01-28', '2020-01-29'),
    ('2020-01-29', '2020-01-30')
]

# Create DB
try:
    con = sqlite3.connect("projects.sqlite")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS projects (
                    proj_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    proj_start TEXT,
                    proj_end TEXT)""")
    cur.executemany("INSERT INTO projects VALUES(NULL, ?,?)", projects)
    con.commit()
    cur.close()
except sqlite3.Error as err:
    print("Request execution error", err)
finally:
    con.close()
    print("Connection was closed successfully")
