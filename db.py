import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Calculator@123",  # Your actual MySQL password
    database="student_tracker"
)
cursor = conn.cursor()

def add_student(roll_no, name):
    try:
        cursor.execute("INSERT INTO students (roll_no, name) VALUES (%s, %s)", (roll_no, name))
        conn.commit()
    except mysql.connector.IntegrityError:
        print("Student already exists.")

def add_marks(roll_no, subject, marks):
    cursor.execute("INSERT INTO marks (roll_no, subject, marks) VALUES (%s, %s, %s)", (roll_no, subject, marks))
    conn.commit()
