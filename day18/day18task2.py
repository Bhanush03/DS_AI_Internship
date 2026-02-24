import sqlite3
import pandas as pd

conn = sqlite3.connect("internship.db")

# 1. Filter query
q1 = """
SELECT *
FROM interns
WHERE track = 'Data Science'
AND stipend > 5000
"""

# 2. Average stipend per track
q2 = """
SELECT track, AVG(stipend) AS avg_stipend
FROM interns
GROUP BY track
"""

# 3. Count interns per track
q3 = """
SELECT track, COUNT(*) AS intern_count
FROM interns
GROUP BY track
"""

df_filter = pd.read_sql_query(q1, conn)
df_avg = pd.read_sql_query(q2, conn)
df_count = pd.read_sql_query(q3, conn)

print("Filtered Interns:")
print(df_filter)

print("\nAverage Stipend per Track:")
print(df_avg)

print("\nIntern Count per Track:")
print(df_count)

conn.close()