import MySQLdb

# MySQL 데이터베이스 연결
db = MySQLdb.connect(host="localhost", user="root", passwd="Tlsakvh1!", db="marketproject")

# 데이터베이스 커서 생성
cursor = db.cursor()

# 기존의 players 테이블 삭제
cursor.execute("DROP TABLE IF EXISTS players")

# 새로운 players 테이블 생성
cursor.execute("""CREATE TABLE PL (
                  number varchar(50) NOT NULL,
                  name VARCHAR(50) NOT NULL,
                  position VARCHAR(50) NOT NULL,
                  age varchar(50) NOT NULL,
                  nation VARCHAR(50) NOT NULL,
                  team VARCHAR(50) NOT NULL,
                  value INT NOT NULL,
                  league VARCHAR(50) NOT NULL,
                  PRIMARY KEY (number)
               )""")

# 변경 사항 저장
db.commit()

# MySQL 데이터베이스 연결 종료
db.close()
