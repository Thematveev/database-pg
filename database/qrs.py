from . import cursor, connection


def add_qr(image_data, user_id):
    cursor.execute("INSERT INTO qrs(image_data, user_id) VALUES (%s, %s);", [image_data, user_id])
    connection.commit()
