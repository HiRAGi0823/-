import mysql.connector
import csv
import pandas
def a():
    cnx = mysql.connector.connect(
        user='root',  # ユーザー名
        password='',  # パスワード
        host='localhost',  # ホスト名(IPアドレス）
        database='kakeibo'  # データベース名
    )
        #SQL
    sql = ('''
        SELECT * FROM    kakeibo
        ''')
        #実行結果をデータフレームへ
    df = pandas.read_sql(sql,cnx)
        #データフレームからCSVへ
    df.to_csv(
        path_or_buf='C:\\Users\\Hiragi\\Desktop\\kakeibo\\csv\\kakeibo.csv',
        encoding='utf-8_sig',
        index=False,
        quoting=csv.QUOTE_ALL)
        #後始末
    cnx.close()