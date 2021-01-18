#파이썬 데이터베이스 연동(SQLite)
#테이블 생성 및 삽입

import sqlite3
import datetime

#삽입 날짜 생성
now = datetime.datetime.now()
print('now: ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)
#sqlite3
print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqite_version: ', sqlite3.sqlite_version)

#DB 생성 및 Auto Commit(<=>Rollback)
conn = sqlite3.connect('C:/Users\PC\Desktop\DB_PRACTICE/database.db', isolation_level=None)

# Cursor
c = conn.cursor()
print('Cursor Type: ', type(c))

#테이블 생성(Data Type: TEXT, NUMERIC INTEGER REAL BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

#데이터 삽입
#c.execute("INSERT INTO users VALUES(1, 'Seol', 'shg5977@naver.com', '01054149478', 'Seol.com', ?)",(nowDatetime,))
#c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)", (2, 'seolhuigwan', 'sss@hufs.ac.kr', '01054149999', 'naver.com', nowDatetime))

# Many 삽입(튜플, 리스트)
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
    (4, 'Cho', 'Cho@daum.net', '010-3333-3333', 'cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@google.com', '010-4444-4444', 'Yoo.net', nowDatetime)
)

#c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)", userList)

#테이블 데이터 삭제
#conn.execute("DELETE FROM users")
#print("users db deleted: ", conn.execute("DELTE FROM users").rowcount))
#conn.commit()
#conn.rollback()

conn.close()