from others import GUI as gui
from others import calc as calc
from others import SQL as sql
from others import csvr as csvr
from others import userdata as logreg
from others import graph as graph
gui.probar()
#ユーザーデータの受け取りと処理
while True:
    user=gui.lryn()
    user=user[0]
    print(user)
    if user=='Yes':#ログイン処理
        print("確認中")
        while True:
            ndata=gui.login()
            print(ndata)
            elogin=ndata[0]
            plogin=ndata[1]
            username=logreg.login(elogin,plogin)
            if username==0:
                print("ログイン出来ませんでした。")
                continue
            print(username,"でログインしました。")
            break
    else:#アカウントの作成処理
        print("新規アカウントの作成の準備中")
        while True:
            rdata=gui.registar()
            print(rdata)
            rmail=rdata[0]
            rname=rdata[1]
            rpass=rdata[2]
            registuser=logreg.register(rmail,rname)
            if registuser!=0:
                print("既に使われているメールアドレス,又はユーザー名です。")
                continue
            break
        sql.users(rmail,rname,rpass)
        sql.nsql(rname)
    if user=='Yes':
        break
#GUIメソッドの呼び出し
value=gui.s()
value2=gui.k()
value=value[0]
value2=value2[0]

#計算メソッドの呼び出し
x=calc.syushi(value,value2)
p=calc.pa(value,value2)
asyushi=sql.allshusi(username)
all=calc.asyushi(asyushi,x)
#SQLにデータを送信するメソッドの呼び出し
ps=str(p)+"%"
value=float(value);value2=float(value2);x=float(x)
sql.sql(username,value,value2,x,ps,all)
csvr.a()
#graph.gp()