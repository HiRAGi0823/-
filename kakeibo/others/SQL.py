from datetime import date
import mysql.connector
def sql(uname,t,k,s,p,all):
    cnx = None
    username=uname
    try:
        cnx = mysql.connector.connect(
            user='root',  # ユーザー名
            password='',  # パスワード
            host='localhost',  # ホスト名(IPアドレス）
            database='kakeibo'  # データベース名
        )

        cursor = cnx.cursor()

        sql = ('''
        INSERT INTO kakeibo
            (投資,回収,収支,収支率,総合収支,ユーザー)
        VALUES 
            (%s, %s, %s, %s, %s, %s)
        ''')
        
        data = [(t,k,s,p,all,username)]
        
        cursor.executemany(sql, data);
        cnx.commit()

        print(f"{cursor.rowcount} records inserted.")

        cursor.close()

    except Exception as er:
        print(f"Error Occurred: {er}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()

def users(e,n,p):
    cnx = None
    
    try:
        cnx = mysql.connector.connect(
            user='root',  # ユーザー名
            password='',  # パスワード
            host='localhost',  # ホスト名(IPアドレス）
            database='kakeibo'  # データベース名
        )

        cursor = cnx.cursor()

        sql = ('''
        INSERT INTO user
            (name,password,Email)
        VALUES 
            (%s, %s, %s)
        ''')
        data = [(n,p,e)]
        
        cursor.executemany(sql, data);
        cnx.commit()

        print(f"{cursor.rowcount} records inserted.")

        cursor.close()

    except Exception as er:
        print(f"Error Occurred: {er}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()

def nsql(uname):
    cnx = None
    username=uname
    try:
        cnx = mysql.connector.connect(
            user='root',  # ユーザー名
            password='',  # パスワード
            host='localhost',  # ホスト名(IPアドレス）
            database='kakeibo'  # データベース名
        )

        cursor = cnx.cursor()

        sql = ('''
        INSERT INTO kakeibo
            (投資,回収,収支,収支率,総合収支,ユーザー)
        VALUES 
            (%s, %s, %s, %s, %s, %s)
        ''')
        
        data = [(0,0,0,'0%',0,username)]
        
        cursor.executemany(sql, data);
        cnx.commit()

        print(f"{cursor.rowcount} records inserted.")

        cursor.close()

    except Exception as er:
        print(f"Error Occurred: {er}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()

def allshusi(username):
    cnx = None

    try:
        cnx = mysql.connector.connect(
            user='root',  # ユーザー名
            password='',  # パスワード
            host='localhost',  # ホスト名(IPアドレス）
            database='kakeibo'  # データベース名
        )

        cursor = cnx.cursor()

        sql = ('''
        SELECT  総合収支, ユーザー
        FROM    kakeibo
        WHERE   ユーザー = %s
        ''')

        param = (username,)

        cursor.execute(sql, param)

        for (総合収支,ユーザー) in cursor:
            print(f"{総合収支} ({ユーザー})")
        allshusi = 総合収支
        cursor.close()

    except Exception as er:
        print(f"Error Occurred: {er}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()
    return allshusi