from database.users import add_user
from database.qrs import add_qr

# add_user("test@test.com", "qwerty123")

f = open("image.png", "rb")
data = f.read()
f.close()

print(data)

add_qr(data, 1)
