import mysql.connector
def register(Eregister,Nregister):
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

    cur = conn.cursor(dictionary=True)  # 取得結果を辞書型で扱う設定

    query__for_fetching = """
    SELECT
        user.Email   AS id,
        user.name AS name
    FROM user
    ORDER BY user.name
    ;
    """
    email_list=[]
    username_list=[]
    cur.execute(query__for_fetching)
    for fetched_line in cur.fetchall():
        id = fetched_line['id']
        name = fetched_line['name']
        email_list.append(id)
        username_list.append(name)
    print(email_list)
    print(username_list)
    ck=0
    for i in range(len(email_list)):
        if email_list[i]==Eregister:
            ck=1
            break
    for i in range(len(username_list)):
        if username_list[i]==Nregister:
            if ck==1:
                ck=3
            else:
                ck=2
            break
    if ck==1:
        return ck
    elif ck==2:
        return ck
    elif ck==3:
        return ck
    else:
        print("正常に処理が実行されました。")
        return ck

def login(Elogin,Plogin):
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

    cur = conn.cursor(dictionary=True)  # 取得結果を辞書型で扱う設定

    query__for_fetching = """
    SELECT
        user.Email   AS id,
        user.name AS name,
        user.password AS pass
    FROM user
    ORDER BY user.name
    ;
    """
    email_list=[]
    username_list=[]
    pass_list=[]
    cur.execute(query__for_fetching)
    for fetched_line in cur.fetchall():
        id = fetched_line['id']
        name = fetched_line['name']
        passwd = fetched_line['pass']
        email_list.append(id)
        username_list.append(name)
        pass_list.append(passwd)
    print(email_list)
    print(username_list)
    Ei=-1
    Pi=-2
    #入力されたデータと登録されたデータが間違っていないかの検証
    for i in range(len(email_list)):
        if email_list[i]==Elogin:
            Ei=i
            break
    for i in range(len(pass_list)):
        if pass_list[i]==Plogin:
            Pi=i
            break
    if  Ei==Pi:
        print("入力データの整合性が確認出来ました。")
        username=username_list[Ei]
        return  username
    else:
        print("入力データの整合性が確認出来ませんでした。")
        return 0