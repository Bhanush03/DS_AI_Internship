import sqlite3

# ----- Create / connect to database -----
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# ----- Create table -----
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")

# ----- Insert sample data -----
data = [
    (1, "Amit", "Data Science", 15000),
    (2, "Sneha", "Web Dev", 12000),
    (3, "Rahul", "AI/ML", 18000),
    (4, "Priya", "Cyber Security", 14000),
    (5, "Kiran", "Data Science", 16000)
]

cursor.executemany("INSERT INTO interns VALUES (?, ?, ?, ?)", data)

conn.commit()

# ----- Query: Retrieve only name and track -----
cursor.execute("SELECT name, track FROM interns")

rows = cursor.fetchall()

for row in rows:
    print(row)

# ----- Close connection -----
conn.close()