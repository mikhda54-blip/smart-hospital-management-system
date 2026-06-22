import sqlite3

conn = sqlite3.connect('hospital.db')

cursor = conn.cursor()

# Patients Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS patients(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    phone TEXT
)
''')

# Doctors Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS doctors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    specialization TEXT,
    phone TEXT
)
''')

# Appointments Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS appointments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT,
    doctor_name TEXT,
    appointment_date TEXT,
    appointment_time TEXT
)
''')

# Billing Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS bills(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT,
    treatment TEXT,
    amount REAL,
    bill_date TEXT
)
''')

# Admin Login Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS admins(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
''')

# Default Admin Account
cursor.execute('''
INSERT OR IGNORE INTO admins(id, username, password)
VALUES (1, 'admin', 'admin123')
''')

conn.commit()
conn.close()

print("Hospital Database Created Successfully!")