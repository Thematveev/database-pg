from . import cursor, connection


def add_user(email, pwd):
    cursor.execute("INSERT INTO users(email, pwd) VALUES (%s, %s);", [email, pwd])
    connection.commit()
