import psycopg2


def add_student(conn, name, grade):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, grade) VALUES (%s, %s)",
        (name, grade)
    )
    conn.commit()


def get_student(conn, student_id):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, name, grade FROM students WHERE id = %s",
        (student_id,)
    )
    return cursor.fetchone()


def average_grade(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(grade) FROM students")
    result = cursor.fetchone()
    return float(result[0])