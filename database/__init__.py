import psycopg2

connection = psycopg2.connect(
    host="snuffleupagus.db.elephantsql.com",
    port=5432,
    user="vhjfgeue",
    database="vhjfgeue",
    password="78ViallG19Tr14hc_Wy9-SovdrZHksIM"
)

cursor = connection.cursor()

with open("schemas/create_users.sql") as schema:
    cursor.execute(schema.read())

with open("schemas/create_qrs.sql") as schema:
    cursor.execute(schema.read())

connection.commit()

