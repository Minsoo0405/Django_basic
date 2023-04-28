from django.shortcuts import render
from ..models import Player
import MySQLdb
import csv

def player_list(request):
    players = Player.objects.all()[150:200]
    print(players)
    return render(request, 'pybo/Bundesliga.html', {'players': players})


def insert_players_from_csv(request):
    # MySQL 데이터베이스 연결
    db = MySQLdb.connect(host="localhost", user="root", passwd="Tlsakvh1!", db="marketproject", connect_timeout=10, autocommit=True)

    # 커서 생성
    with db.cursor() as cursor:

        # 기존의 players 테이블 삭제
        cursor.execute("DROP TABLE IF EXISTS players")

        # 새로운 players 테이블 생성
        cursor.execute("""CREATE TABLE players (
                          number INT NOT NULL,
                          name VARCHAR(50) NOT NULL,
                          position VARCHAR(50) NOT NULL,
                          age varchar(50) NOT NULL,
                          nation VARCHAR(50) NOT NULL,
                          team VARCHAR(50) NOT NULL,
                          value VARCHAR(50) NOT NULL,
                          league VARCHAR(50) NOT NULL,
                          PRIMARY KEY (number)
                       )""")

        # CSV 파일 읽어들이기
        csv_files = [
            '/Users/kimminsoo/PycharmProjects/miniProject/mysite/pybo/views/market_csv/PL_50.csv',
            '/Users/kimminsoo/PycharmProjects/miniProject/mysite/pybo/views/market_csv/LaLiga_50.csv',
            '/Users/kimminsoo/PycharmProjects/miniProject/mysite/pybo/views/market_csv/Bundesliga_50.csv',
            '/Users/kimminsoo/PycharmProjects/miniProject/mysite/pybo/views/market_csv/SeriaA_50.csv',
            '/Users/kimminsoo/PycharmProjects/miniProject/mysite/pybo/views/market_csv/Ligue1_50.csv',
            '/Users/kimminsoo/PycharmProjects/miniProject/mysite/pybo/views/market_csv/KLeague1_50.csv'
        ]

        for file in csv_files:
            with open(file, 'r') as csvfile:
                # CSV 파일 읽기
                csv_data = csv.reader(csvfile)

                # CSV 파일의 각 행을 순회하며 MySQL 데이터베이스에 삽입
                for row in csv_data:
                    # INSERT 쿼리 실행
                    try:
                        values = (int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    except ValueError:
                        # number 컬럼에 정수가 아닌 값이 들어온 경우
                        continue

                    # "number" 컬럼이 같은 값을 가진 행이 이미 있는지 확인
                    query = "SELECT * FROM players WHERE number = %s"
                    cursor.execute(query, (int(row[0]),))
                    result = cursor.fetchone()
                    if result is not None:
                        # 같은 "number" 값을 가진 행이 이미 있는 경우 건너뜀
                        continue

                    query = """INSERT INTO players (number, name, position, age, nation, team, value, league) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                    cursor.execute(query, values)

        # SELECT 쿼리 실행
        query = "SELECT * FROM players"
        cursor.execute(query)
        players = cursor.fetchall()

    # MySQL 데이터베이스 연결 종료
    db.close()

    # 템플릿 렌더링
    return render(request, 'market_value.html', {'players': players})