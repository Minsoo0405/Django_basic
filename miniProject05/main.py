
import pymysql
import csv
connect = pymysql.connect(host="localhost", user="root", password="Tlsakvh1!", db="pybo", charset="utf8")

curs = connect.cursor()

connect.commit()

f = open('/Users/kimminsoo/PycharmProjects/miniProject/mysite/pybo/views/market_csv/players_value.csv', "r")

csvReader = csv.reader(f)
next(csvReader, None)
count_id = 0

for row in csvReader:

    number = row[0]
    name = row[1]
    position = row[2]
    age = row[3]
    nation = row[4]
    team = row[5]
    value = row[6]
    league = row[7]

    print(number, name, position, age, nation, team, value, league)

    sql = """insert into pybo_player (number, name, position, age, nation, team, value, league) values 
    (%s, %s, %s, %s, %s, %s, %s, %s)"""

    curs.execute(sql, (int(number), name, position, age, nation, team, value, league))

    count_id = count_id + 1

connect.commit()
f.close()
connect.close()
# # 커서 생성
# with db.cursor() as cursor:
#
#     csv_files = [
#         '/Users/kimminsoo/PycharmProjects/miniProject/mysite/pybo/views/market_csv/PL_50.csv',
#     ]
#
#     for file in csv_files:
#         with open(file, 'r') as csvfile:
#             # CSV 파일 읽기
#             csv_data = csv.reader(csvfile)
#
#             # CSV 파일의 각 행을 순회하며 MySQL 데이터베이스에 삽입
#             for row in csv_data:
#                 # INSERT 쿼리 실행
#                 try:
#                     values = (int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7])
#                 except ValueError:
#                     # number 컬럼에 정수가 아닌 값이 들어온 경우
#                     continue
#
#                 # "number" 컬럼이 같은 값을 가진 행이 이미 있는지 확인
#                 query = "SELECT * FROM pybo_players WHERE number = %s"
#                 cursor.execute(query, (int(row[0]),))
#                 result = cursor.fetchone()
#                 if result is not None:
#                     # 같은 "number" 값을 가진 행이 이미 있는 경우 건너뜀
#                     continue
#
#                 query = """INSERT INTO pybo_players (null, number, name, position, age, nation, team, value, league)
#                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
#                 cursor.execute(query, values)
#
#     # SELECT 쿼리 실행
#     query = "SELECT * FROM players"
#     cursor.execute(query)
#     players = cursor.fetchall()
#
# # MySQL 데이터베이스 연결 종료
# db.close()