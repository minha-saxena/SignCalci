import sqlite3

conn = sqlite3.connect("gesture_db.db")
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS gesture (
    g_id INTEGER PRIMARY KEY,
    g_name TEXT NOT NULL
)
''')

#mapping (A-Z: 0-25, 0-9: 26-35, best of luck: 36, yo: 37)
gestures = [
    (i, chr(65 + i)) for i in range(26)  # A-Z
] + [
    (i, str(i - 26)) for i in range(26, 36)  # 0-9
] + [
    (36, "Best of Luck"),
    (37, "Yo")
]

cursor.executemany("INSERT INTO gesture (g_id, g_name) VALUES (?, ?)", gestures)

conn.commit()
conn.close()

print("Gesture database created successfully!")
