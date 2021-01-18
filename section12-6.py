import sqlite3

conn = sqlite3.connect('C:/Users/PC/Desktop/DB_PRACTICE/database.db', isolation_level=None)

c = conn.cursor()

#데이터 수정1 (튜플 형태)
c.execute("UPDATE users SET username = ? WHERE id = ?", ('niceman', 2))

#데이터 수정2 (딕셔너리 형태)
c.execute("UPDATE users SET username = :name WHERE id = :id",{"name": "goodman", "id":5})

#데이터 수정3 (string format 형태)
c.execute("UPDATE users SET username = '%s' WHERE id = '%d'" %('badboy', 3))

#중간 데이터 확인1

for user in c.execute("SELECT * FROM users"):
    print(user)

# Row Delete1
c.execute("DELETE FROM users WHERE id = ?",(2,))

# Row Delete2
c.execute("DELETE FROM users WHERE id = :id",{"id": 5})

# Row Delete3
c.execute("DELETE FROM users WHERE id = '%d'" % 4)

#중간 데이터 확인2

for user in c.execute("SELECT * FROM users"):
    print(user)

conn.close()