import sqlite3
import pandas as pd

conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# Remove old tables (important)
cursor.execute("DROP TABLE IF EXISTS interns")
cursor.execute("DROP TABLE IF EXISTS mentors")

# Create interns table (3 columns only)
cursor.execute("""
CREATE TABLE interns (
    intern_id INTEGER PRIMARY KEY,
    intern_name TEXT,
    track TEXT
)
""")

# Create mentors table
cursor.execute("""
CREATE TABLE mentors (
    mentor_id INTEGER PRIMARY KEY,
    mentor_name TEXT,
    track TEXT
)
""")

# Insert interns data
cursor.executemany("""
INSERT INTO interns (intern_id, intern_name, track)
VALUES (?, ?, ?)
""", [
    (101, 'Rahul', 'Data Science'),
    (102, 'Ananya', 'Web Development'),
    (103, 'Vikram', 'Cyber Security'),
    (104, 'Sneha', 'Data Science')
])

# Insert mentors data
cursor.executemany("""
INSERT INTO mentors (mentor_id, mentor_name, track)
VALUES (?, ?, ?)
""", [
    (1, 'Mr. Sharma', 'Data Science'),
    (2, 'Ms. Iyer', 'Web Development'),
    (3, 'Mr. Khan', 'Cyber Security')
])

conn.commit()

# INNER JOIN query
query = """
SELECT i.intern_name, i.track, m.mentor_name
FROM interns i
INNER JOIN mentors m
ON i.track = m.track
"""

df = pd.read_sql_query(query, conn)

print(df)

conn.close()