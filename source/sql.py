from datetime import date
import mysql.connector
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

def shohin(hi,ko,ut,sn,ka,un):
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
        INSERT INTO kakeibo2
            (hiduke,koumoku,utiwake,shohinmei,kakaku,user)
        VALUES 
            (%s, %s, %s, %s, %s, %s)
        ''')
        
        data = [(hi,ko,ut,sn,ka,un)]
        
        cursor.executemany(sql, data);
        cnx.commit()

        print(f"{cursor.rowcount} records inserted.")

        cursor.close()

    except Exception as er:
        print(f"Error Occurred: {er}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()
            
def kyuryo(hi,ky,un):
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
        INSERT INTO kakeibo2
            (hiduke,kakaku,user)
        VALUES 
            (%s, %s, %s)
        ''')
        
        data = [(hi,ky,un)]
        
        cursor.executemany(sql, data);
        cnx.commit()

        print(f"{cursor.rowcount} records inserted.")

        cursor.close()

    except Exception as er:
        print(f"Error Occurred: {er}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()

def rinji(hi,ri,un):
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
        INSERT INTO kakeibo2
            (hiduke,rinjishunyu,user)
        VALUES 
            (%s, %s, %s)
        ''')
        
        data = [(hi,ri,un)]
        
        cursor.executemany(sql, data);
        cnx.commit()

        print(f"{cursor.rowcount} records inserted.")

        cursor.close()

    except Exception as er:
        print(f"Error Occurred: {er}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()

def alldata(username):
    # DBへ接続
    conn = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database='kakeibo'
    )

    # DBの接続確認
    if not conn.is_connected():
        raise Exception("MySQLサーバへの接続に失敗しました")

    cur = conn.cursor()
    sql = ('''
           SELECT id,hiduke,koumoku,utiwake,shohinmei,kakaku,rinjishunyu
           FROM kakeibo2 
           WHERE user = %s
           ORDER BY hiduke''')
    param=(username,)
    cur.execute(sql,param)
    data=[]
    i=0
    for (id,hiduke,koumoku,utiwake,shohinmei,kakaku,rinjishunyu) in cur:
        data+=[id,hiduke,koumoku,utiwake,shohinmei,kakaku,rinjishunyu],
    cur.close()
    #入力されたデータと登録されたデータが間違っていないかの検証
    return data

def update(henko):
    print(henko)
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
        UPDATE kakeibo2 SET koumoku=%s,utiwake=%s,shohinmei=%s,kakaku=%s,rinjishunyu=%s
        WHERE id=%s
        ''')
        param=[(henko[1],henko[2],henko[3],henko[4],henko[5],henko[0],)]
        
        cursor.executemany(sql,param)
        cnx.commit()

        print(f"{cursor.rowcount} record updated.")

        cursor.close()

    except Exception as er:
        print(f"Error Occurred: {er}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()

def syouhi(syo,sei,kout,sik,ky,hok,kous,zap,us):    
    cnx = None
    try:
        cnx = mysql.connector.connect(
            user='root',  # ユーザー名
            password='',  # パスワード
            host='localhost',  # ホスト名(IPアドレス）
            database='kakeibo' # データベース名
        )
            
        cursor = cnx.cursor()
                
        sql = ('''
            INSERT INTO meyasu
                (syokuhi,seikatuyouhinhi,sikouhinhi,koutuhi,kyoyouhi,hokeneiseihi,kousaihi,zappi,user)
            VALUES
                (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ''')
            
        data = [(syo,sei,kout,sik,ky,hok,kous,zap,us)]
        cursor.executemany(sql,data);
            
        cnx.commit()
        cursor.close()
    except Exception as er:
        print(f"Error Occurred: {er}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()

def call(username):
    cnx = None
    try:
        cnx = mysql.connector.connect(
            user='root',  # ユーザー名
            password='',  # パスワード
            host='localhost',  # ホスト名(IPアドレス）
            database='kakeibo' # データベース名
        )
   
        cursor = cnx.cursor()
            
        sql = ('''
                SELECT syokuhi,seikatuyouhinhi,sikouhinhi,koutuhi,kyoyouhi,hokeneiseihi,kousaihi,zappi
                FROM meyasu
                WHERE user = %s
        ''')
        us = (username,)
        cursor.execute(sql,us)
        for (syo,sei,kout,sik,ky,hok,kous,zap) in cursor:
            allsyo = syo
            allsei = sei
            allkout = kout
            allsik = sik
            allky = ky
            allhok = hok
            allkous = kous
            allzap = zap
        cursor.close()
        alldata = {
            '食費' : allsyo,
            '生活用品費' : allsei,
            '交通費' : allkout,
            '嗜好品費' : allsik,
            '教養費' : allky,
            '保健衛生費' : allhok,
            '交際費' : allkous,
            '雑費' : allzap
        }  
    except Exception as er:
            print(f"Error Occurred: {er}")

    finally:
            if cnx is not None and cnx.is_connected():
                cnx.close()           
    return alldata

def kensyou(user):
    cnx = None
    try:
            cnx = mysql.connector.connect(
                user='root',  # ユーザー名
                password='',  # パスワード
                host='localhost',  # ホスト名(IPアドレス）
                database='kakeibo' # データベース名
            )
            
            cursor = cnx.cursor()
            
            sql = '''
                  SELECT koumoku,kakaku
                  FROM kakeibo2
                  WHERE user = %s
            '''
            us = (user,)
            
            list = []
            cursor.execute(sql,us)
            for (kou,ka) in cursor.fetchall():
                list.append({'項目': kou,'価格': ka})
            return list
            
    except Exception as er:
            print(f"Error Occurred: {er}")

    finally:
            if cnx is not None and cnx.is_connected():
                cnx.close()

def goukei(user):
    cnx = None
    try:
            cnx = mysql.connector.connect(
            user='root',  # ユーザー名
            password='',  # パスワード
            host='localhost',  # ホスト名(IPアドレス）
            database='kakeibo' # データベース名
            )
            
            cursor = cnx.cursor()
            
            sql = '''
                  SELECT kakaku
                  FROM kakeibo2
                  WHERE user = %s
            '''
            us = (user,)
            goukei = 0
            cursor.execute(sql,us)
            for ka in cursor.fetchall():
                goukei = goukei + ka[0]
            return goukei
            
    except Exception as er:
            print(f"Error Occurred: {er}")

    finally:
            if cnx is not None and cnx.is_connected():
                cnx.close()

def hyouzi(user):
    cnx = None
    try:
            cnx = mysql.connector.connect(
                user='root',  # ユーザー名
                password='',  # パスワード
                host='localhost',  # ホスト名(IPアドレス）
                database='kakeibo' # データベース名
            )
            
            cursor = cnx.cursor()
            
            sql = '''
                  SELECT koumoku,sum(kakaku)
                  FROM kakeibo2
                  WHERE user = %s
                  GROUP BY koumoku
            '''
            
            us = (user,)
            cursor.execute(sql,us)
            listX = []
            listY = []
            for (k1,k2) in cursor.fetchall():
                listX.append(k1)
                listY.append(k2)
            return listX,listY
        
    except Exception as er:
                print(f"Error Occurred: {er}")

    finally:
            if cnx is not None and cnx.is_connected():
                cnx.close()
def delete(id):
    print(id)
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
            DELETE FROM kakeibo2 WHERE id=%s
        ''')
        param=[(id,)]
        
        cursor.executemany(sql,param)
        cnx.commit()

        print(f"{cursor.rowcount} record deleted.")

        cursor.close()

    except Exception as er:
        print(f"Error Occurred: {er}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()