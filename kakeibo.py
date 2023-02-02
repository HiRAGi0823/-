from source import gui as gui
from source import calc as calc
from source import sql as sql
from source import userdata as userdata
from source import mail as mail

gui.probar()
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
            username=userdata.login(elogin,plogin)
            
            if username==0:
                gui.contil()
                print("ログイン出来ませんでした。")
                continue
            print(username,"でログインしました。")
            break

    else:#アカウントの作成処理
        while True:
            rdata=gui.registar()
            print(rdata)
            rmail=rdata[0]
            rname=rdata[1]
            rpass=rdata[2]
            registuser=userdata.register(rmail,rname)
            
            if registuser!=0:
                gui.contir()
                print("既に使われているメールアドレス,又はユーザー名です。")
                continue
            break
        
        keta=mail.mail(rmail)
        gui.mail(keta)
        sql.users(rmail,rname,rpass)
    
    if user=='Yes':
        break
gui.kmain(username)