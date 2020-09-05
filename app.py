import psycopg2

connection = psycopg2.connect(
    host="0.0.0.0",
    database='db_name',
    user='db_username',
    password='password'
)
cursor = connection.cursor()
# file = open('data.sql', 'r')
# cursor.execute(file.read())
a = input('Istediyiniz emeliyati daxil edin - ', )
#
if a == 'save':
    name = input('Adinizi daxil edin -', )
    surname = input('Soyadinizi daxil edin-', )
    cursor.execute(f"INSERT INTO students (name,surname) VALUES ('{name}','{surname}')")
    connection.commit()

elif a == 'delete':
    id = input('Silmek istediyiniz idni daxil edin!-', )
    cursor.execute(f"DELETE FROM students WHERE id={id}")
    connection.commit()
    print('Ugurla silindi!')
#
elif a == 'all':

    cursor.execute("SELECT * FROM students")
    print(cursor.fetchall())

elif a == 'update':
    user = input('Istifadecinin idsini daxil edin!-',)
    new_name = input('Yeni ad-',)
    new_surname = input('Yeni soyad-',)
    cursor.execute(f"UPDATE students SET name = '{new_name}' ,surname = '{new_surname}' ")
    connection.commit()
    print('Ugurla Update olundu!')
