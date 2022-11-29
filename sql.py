import sqlite3

def get_connection():
    connection = sqlite3.connect('teatchers.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def create_table():
  try:
    connection = get_connection()
    cursor = connection.cursor()
    query = """
#  CREATE TABLE Students (
#         Student_id INTEGER NOT NULL PRIMARY KEY,
#         Student_Name TEXT NOT NULL,
#         School_id INTEGER NOT NULL
#         );
#         """  
    """INSERT INTO Students (Student_id, Student_Name, School_id)
    VALUES
    ('201', 'Иван', '1'),
    ('202', 'Петр', '2'),
    ('203', 'Анастасия', '3'),
    ('204', 'Игорь', '4')
    """
    cursor.execute(query)
    connection.commit()
    connection.close()
  except (Exception, sqlite3.Error) as error:
        print('Ошибка в получении данных', error)

create_table()  

def get_school_name(school_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM School WHERE School_Id = ?"""
    cursor.execute(select_query, (school_id,))
    record = cursor.fetchone()
    close_connection(connection)
    return record[1] # Наименование школы
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных по школе ", error)


def get_teacher(school_id):
  try:
    school_name = get_school_name(school_id)
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM Students WHERE School_Id = ?"""
    cursor.execute(select_query, (school_id,))
    records = cursor.fetchall()

    print ("Студент из школы ", school_name)
    for row in records:
      print ("ID студента", row[0])
      print ("Имя студента", row[1])
      print ("ID школы", row[2])
      print ("Название школы", school_name, "\n") 
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных по школе ", error)

print ("Самостоятельная работа \n")
get_teacher(1)  
    



