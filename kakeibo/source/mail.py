import smtplib
import random
from email.mime.text import MIMEText
from email.utils import formatdate
def mail(mail):
    sendAddress = 'q.t.i.corpolation@gmail.com'
    password = 'dwdwzyaroqbfkmbf'
    r=''
    for i in range(4):
        s=random.randint(0,9)
        r+=str(s)
    print(r)

    subject = '会員登録のご確認'
    bodyText = 'この度は会員登録依頼をいただきまして、有り難うございます。\n現在は仮登録の状態です。\n本会員登録を完了するには下記番号をアプリに入力してください。\n※入力されたお客様の情報はSSL暗号化通信により保護されます。\n------------------------------------------------\n'+r+'\n------------------------------------------------\n上記番号の入力にて本会員登録が完了いたしましたら確認作業は終わります。\n■お願いとご注意事項について\n----------------------------\n上記の会員登録に心あたりがない場合は、\n本メールの削除をして下さい。\n番号を第三者にお教えしなければ本登録はされません。\n------------------------------------------------'
    fromAddress = 'q.t.i.corpolation@gmail.com'
    toAddress = mail

    # SMTPサーバに接続
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.starttls()
    smtpobj.login(sendAddress, password)

    # メール作成
    msg = MIMEText(bodyText)
    msg['Subject'] = subject
    msg['From'] = fromAddress
    msg['To'] = toAddress
    msg['Date'] = formatdate()

    # 作成したメールを送信
    smtpobj.send_message(msg)
    smtpobj.close()
    return r