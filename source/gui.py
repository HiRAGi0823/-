from source import calc as calc
from source import sql as sql
from source import plot as plot
#import sql as sql
#import calc as calc
import PySimpleGUI as sg
import datetime
dt = datetime.date.today()
sg.theme('SandyBeach')#デザインテーマの指定
def listToString(str_list):
    result = ""
    for s in str_list:
        result += s + " "
    return result.strip()

def lryn():
        sg.theme('SandyBeach')
        layout=[[sg.Text('課題研究用の家計簿のアカウントをお持ちですか？')],                     
                [sg.Button('Yes'),sg.Button('No')]
        ]
        window=sg.Window('Do you have an Account?',layout)
        while True:
                event=window.read()
                if event=='Yes'or event==sg.WIN_CLOSED:
                        window.close()
                        a2=event
                        break
                else:
                        window.close()
                        a2=event
                        break
        return a2

def login():
        sg.theme('SandyBeach')
        layout =[
                [sg.Text('メールアドレス')],
                [sg.InputText()],
                [sg.Text('パスワード')],
                [sg.InputText(password_char='●')],    
                [sg.Button('ログイン')]
        ]
        window=sg.Window('Login',layout)
        while True:
                event,value=window.read()
                if event=='ログイン'or event==sg.WIN_CLOSED:
                        window.close()
                        userdata=value
                        break
        return userdata

def contir():
    sg.theme('SandyBeach')
    layout=[
            [sg.Text('既に使われているメールアドレス又はユーザー名です')],
            [sg.Button('再入力')]
        ]
    window=sg.Window('※注意',layout)
    while True:
        event,value=window.read()
        if event=='再入力'or event==sg.WIN_CLOSED:
            window.close()
            break

def contil():
    sg.theme('SandyBeach')
    layout=[
            [sg.Text('メールアドレス又はパスワードが間違っています')],
            [sg.Button('再入力')]
        ]
    window=sg.Window('※注意',layout)
    while True:
        event,value=window.read()
        if event=='再入力'or event==sg.WIN_CLOSED:
            window.close()
            login()
            break

def registar():
        sg.theme('SandyBeach')
        layout=[
                [sg.Text('メールアドレス')],
                [sg.InputText()],
                [sg.Text('ユーザー名')],
                [sg.InputText()],    
                [sg.Text('パスワード'),],
                [sg.InputText(password_char='●')],    
                [sg.Button('新規作成')]
        ]
        window=sg.Window('Registar',layout)
        while True:
                event,value=window.read()
                if event=='新規作成'or event==sg.WIN_CLOSED:
                        window.close()
                        sinkidata=value
                        break
        return sinkidata

def shohin(zndk,user,hiduke):
    sg.theme('SandyBeach')
    choices = ['食費', '生活用品費', '嗜好品費', '交通費', '教養費', '通信費','保健衛生費','交際費','雑費']
    choices2= {
            '食費':['外食','弁当惣菜','食材','パン','果物','その他'],
            '生活用品費':['衣料','雑貨','電気機器','その他'],
            '嗜好品費':['スナック','飲料','酒類','喫茶','煙草'],
            '交通費':['電車','バス','タクシー','ガソリン','有料道路','駐車場'],
            '教養費':['雑誌','書籍','映画','旅行','CD/DVD','その他'],
            '通信費':['電話','郵便料金','接続料','その他'],
            '保健衛生費':['医療','医薬品','理髪代','化粧品','その他'],
            '交際費':['慶弔費','おみやげ','飲み会','食事会','その他'],
            '雑費':['文具','消耗品','趣味','その他']
        }
    layout=[
        [sg.Text('項目'),sg.Text('と'),sg.Text('内訳')],
        [sg.Listbox(choices,size=(30, 9),select_mode=sg.LISTBOX_SELECT_MODE_SINGLE,enable_events=True,key='-k-'),sg.Listbox(values=[""],size=(30,9),key='-u-')],
        [sg.Text('商品名')],
        [sg.InputText()],
        [sg.Text('金額')],
        [sg.InputText()],
        [sg.Button('確定'),sg.Button('終了')]
    ]
    window = sg.Window('金額の入力', layout)
    while True:
        event,value=window.read()
        s=listToString(value['-k-'])
        window.FindElement('-u-').Update(values=choices2[s])        
        
        if event=='確定':
                if value['-k-']=='':
                        sg.popup('項目を選択してください。')
                elif value[1]=='':
                        sg.popup('金額を入力してください')
                else:             
                        koumoku=listToString(value['-k-'])
                        utiwake=listToString(value['-u-'])
                        shohin=value[0]
                        kingaku=value[1]
                        zndk=calc.znadakam(zndk,kingaku)
                        sql.shohin(hiduke,koumoku,utiwake,shohin,kingaku,user)
                        alldata=sql.call(user)
                        alldata[koumoku] = alldata[koumoku]-int(kingaku)
                        sql.syouhi(alldata['食費'],alldata['生活用品費'],alldata['嗜好品費'],alldata['交通費'],alldata['教養費'],alldata['保健衛生費'],alldata['交際費'],alldata['雑費'],user)
                        sg.popup("データの書き込みが完了しました。")
                        window.close()
                        kmain(user)
                        break
def kyuryo(user,zndk,hiduke):
    sg.theme('SandyBeach')
    layout=[
        [sg.Text('1ヶ月の給料を入力してください')],
        [sg.InputText()],
        [sg.Button('確定'),sg.Button('終了')]
    ]
    window = sg.Window('給料', layout)
    while True:
        event,value=window.read()
        if event=='確定':
            window.close()
            kyuryo=int(value[0])
            atai = calc.wariai(kyuryo)  
            zndk=calc.zandakap(zndk,kyuryo)
            sql.kyuryo(hiduke,kyuryo,user)
            window.close()
            meyasu(atai,user)
            break
        elif event==sg.WIN_CLOSED or event =='終了':
                window.close()
                kmain(user)
                break

def meyasu(atai,user):
        sg.theme('SandyBeach')
        sql.syouhi(atai['syokuhi'],atai['seikatuyouhinhi'],atai['sikouhinhi'],atai['koutuhi'],atai['kyoyohi'],atai['hokeneiseihi'],atai['kousaihi'],atai['zappi'],user)
        layout = [
                [sg.Text('一週間の平均食費額です。')],
                [sg.Text('金額', size=(15, 1)), sg.Text(atai['syokuhi'])],
                [sg.Text('一週間の平均生活用品費額です。')],
                [sg.Text('金額', size=(15, 1)), sg.Text(atai['seikatuyouhinhi'])],   
                [sg.Text('一週間の平均嗜好品費です。')],
                [sg.Text('金額', size=(15, 1)), sg.Text(atai['sikouhinhi'])],
                [sg.Text('一週間の平均交通費額です。')],
                [sg.Text('金額', size=(15, 1)), sg.Text(atai['koutuhi'])],
                [sg.Text('一週間の平均教養費額です。')],
                [sg.Text('金額', size=(15, 1)), sg.Text(atai['kyoyohi'])],
                [sg.Text('一週間の平均保健衛生費額です。')],
                [sg.Text('金額', size=(15, 1)), sg.Text(atai['hokeneiseihi'])],
                [sg.Text('一週間の平均交際費額です。')],
                [sg.Text('金額', size=(15, 1)), sg.Text(atai['kousaihi'])],
                [sg.Text('一週間の平均雑費額です。')],
                [sg.Text('金額', size=(15, 1)), sg.Text(atai['zappi'])],
                [sg.Submit(button_text='確認')]
        ]
        window = sg.Window('一週間の目安', layout)
        while True:
                event, value = window.read()
                
                if event==sg.WIN_CLOSED:
                        window.close()
                        break
                if event == '確認':
                        window.close()
                        kmain(user)
                        break

def nokori(user):
    keikoku=None
    sg.theme('SandyBeach')
    alldata=sql.call(user)
    choices = ['食費', '生活用品費', '嗜好品費', '交通費', '教養費','保健衛生費','交際費','雑費']
    for i in range(len(choices)):
        if  alldata[choices[i]] < 0:
            keikoku=[sg.Text('※使いすぎています。節約を心がけましょう。', text_color='red')]
        
          
    if keikoku==None:
        layout = [
            [sg.Text('残りの目安:')],
            [sg.Text('食費:'), sg.Text(alldata['食費']), sg.Text('円')],
            [sg.Text('生活用品費:'), sg.Text(alldata['生活用品費']), sg.Text('円')],
            [sg.Text('交通費：'), sg.Text(alldata['嗜好品費']), sg.Text('円')],
            [sg.Text('嗜好品費：'), sg.Text(alldata['交通費']), sg.Text('円')],
            [sg.Text('教養費：'), sg.Text(alldata['教養費']), sg.Text('円')],
            [sg.Text('保健衛生費：'), sg.Text(alldata['保健衛生費']), sg.Text('円')],
            [sg.Text('交際費：'), sg.Text(alldata['交際費']), sg.Text('円')],
            [sg.Text('雑費：'), sg.Text(alldata['雑費']), sg.Text('円')],
            [sg.Submit(button_text='確認')]    
        ]
    else:
        layout = [
            [keikoku],
            [sg.Text('残りの目安:')],
            [sg.Text('食費:'), sg.Text(alldata['食費']), sg.Text('円')],
            [sg.Text('生活用品費:'), sg.Text(alldata['生活用品費']), sg.Text('円')],
            [sg.Text('交通費：'), sg.Text(alldata['嗜好品費']), sg.Text('円')],
            [sg.Text('嗜好品費：'), sg.Text(alldata['交通費']), sg.Text('円')],
            [sg.Text('教養費：'), sg.Text(alldata['教養費']), sg.Text('円')],
            [sg.Text('保健衛生費：'), sg.Text(alldata['保健衛生費']), sg.Text('円')],
            [sg.Text('交際費：'), sg.Text(alldata['交際費']), sg.Text('円')],
            [sg.Text('雑費：'), sg.Text(alldata['雑費']), sg.Text('円')],
            [sg.Submit(button_text='確認')]
        ]
    
    window = sg.Window('meyasu', layout)
    while True: 
        event,value= window.read()
        if event == '確認' or event==sg.WIN_CLOSED:
                kmain(user)
                window.close()
                break

def rinji(hi,zndk,user):
    sg.theme('DarkBrown')
    layout=[
        [sg.Text('金額の入力をしてください')],
        [sg.InputText()],
        [sg.Button('確定')]
    ]
    window = sg.Window('臨時収入', layout)
    while True:
        event,value=window.read()
        if event=='確定':
            window.close()
            kyuryo=value[0]
            zndk=calc.zandakap(zndk,kyuryo)
            sql.rinji(hi,kyuryo,user)
            kmain(user)
            break
        
        elif event==sg.WINDOW_CLOSED:
            window.close()
            break

def selectKorSorR(user,zndk,hiduke):
    sg.theme('SandyBeach')
    layout=[
        [sg.Text('給料の入力か商品の入力を選択してください')],
        [sg.Text('給料以外での収入があった場合は臨時収入を押してください')],
        [sg.Button('給料'),sg.Button('商品'),sg.Button('臨時収入'),sg.Button("終了")]
    ]

    window = sg.Window('給料', layout)
    while True:
        event,value=window.read()

        if event==sg.WIN_CLOSED or event=='終了':
                window.close()
                kmain(user)
                break
        if event=='給料':
                window.close()
                kyuryo(user,zndk,hiduke)
                break
        elif event=='商品':
                window.close()
                shohin(zndk,user,hiduke)
                break
        elif event=='臨時収入':
                window.close()
                rinji(hiduke,zndk,user)
                break

def probar():
        sg.theme('SandyBeach')
        BAR_MAX = 700
        layout = [
                [sg.Text('家計簿アプリのデータを参照中')],
                [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,20), key='-PROG-')]
            ]
        window = sg.Window('家計簿', layout)

        for i in range(BAR_MAX):
                event, values = window.read(timeout=1)
                window['-PROG-'].update(i+1)

        window.close()

def mail(password):
    sg.theme('SandyBeach')
    layout=[
        [sg.Text('届いたコードを入力して下さい')],
        [sg.InputText()],
        [sg.Button('確定')]
    ]

    window = sg.Window('メール認証', layout)
    while True:
        event,value=window.read()
        if event=='確定':
                if value[0]!=password:                
                        sg.popup('コードが間違っています。正しく入力してください')
                else:
                        sg.popup('アカウントの認証が正常に行われました。')
                        break
        elif event==sg.WIN_CLOSED:
                window.close()
                break

def kmain(user):
        sg.theme('SandyBeach')
        zndk=calc.zandaka(user)
        data=sql.alldata(user)
        lavel=['id','日付','項目','内訳','商品名','金額','ボーナス!?']
        layout=[
                [sg.Text(dt)],[sg.Table(data,headings=lavel,def_col_width=8, auto_size_columns=False, vertical_scroll_only=False,enable_events=True)],
                [sg.Frame('現在の残高', [[sg.Text(str(zndk)+"円")]]),
                 sg.Input(key='-text_date-', size=(20,1)),
                 sg.CalendarButton('日付選択',
                                   locale='ja_JP',
                                   format='%Y-%m-%d',
                                   default_date_m_d_y=(dt.month,dt.day,dt.year),
                                   key='-button_calendar-',
                                   target='-text_date-')
                ],
                [sg.Button('入力'),sg.Button('検索'),sg.Button('目安の確認'),sg.Button('収支の集計とグラフ')],
                [sg.Button('終了')]
        ]
        window=sg.Window('家計簿',layout)
        while True:
                event,value=window.read()
                if event =='終了' or event==sg.WIN_CLOSED:
                        window.close()
                        break
                if event=='入力':
                        if value['-text_date-']=="":
                                sg.popup('日付を選択してください',title='')
                        else:
                                hiduke=value['-text_date-']
                                selectKorSorR(user,zndk,hiduke)
                                window.close()
                                break
                if event =='検索':
                        kensaku(user)
                        window.close()
                        break
                if event=='目安の確認':
                        nokori(user)
                        window.close()        
                        break
                if event=='収支の集計とグラフ':
                        shukei(user)
                        window.close()
                        break


def kensaku(user):
        sg.theme('SandyBeach')
        values=[]
        lavel=['id','日付','項目','内訳','商品名','金額','ボーナス!?']
        layout=[
                [sg.Text('検索したい文字を入力して下さい。')],
                [sg.Button('検索'),sg.Input()],
                [sg.Table(values,headings=lavel,def_col_width=15, auto_size_columns=False, vertical_scroll_only=False,key='-t-')],
                [sg.Text('項目　　　　　　　'),sg.Text('内訳　　　　　　　'),sg.Text('商品名　　　　　　'),sg.Text('金額　　　　　　　'),sg.Text('ボーナス!?'),],
                [sg.InputText(key='項目',size=(18,50)),sg.InputText(key='内訳',size=(18,50)),sg.InputText(key='商品名',size=(18,50)),sg.InputText(key='金額',size=(18,50)),sg.InputText(key='ボーナス!?',size=(18,50))],
                [sg.Button('編集'),sg.Button('削除'),sg.Button('確定')],
                [sg.Button('終了')]
        ]
        window=sg.Window('検索',layout,)
        while True:
                event,value=window.read()
                if event =='終了' or event ==sg.WIN_CLOSED:
                        window.close()
                        kmain(user)
                        break
                if event == '検索':
                        if value[0]=='':
                                alldata=sql.alldata(user)
                                
                        key=value[0]
                        henko=[]
                        alldata=sql.alldata(user)
                        for i in range(len(alldata)):
                                result =key in alldata[i]
                                if result == True:
                                        henko+=[alldata[i]]
                        window['-t-'].Update(values=henko)
                if event=='編集':
                        if value['-t-']==[]:
                                sg.popup('編集するデータを選択してください',title='注意')
                        else:
                                moto=henko[value['-t-'][0]]
                                print(moto)
                                window['項目'].Update(moto[2])
                                window['内訳'].Update(moto[3])
                                window['商品名'].Update(moto[4])
                                window['金額'].Update(moto[5])
                                window['ボーナス!?'].Update(moto[6])
                if event=='確定':
                        if value['項目']=='':
                                sg.popup('※これは編集機能のボタンです。\n編集したいデータを選び、編集ボタンを押してください',title='注意')
                        else:
                                henko = [moto[0],value['項目'],value['内訳'],value['商品名'],int(value['金額']),int(value['ボーナス!?'])]
                                sql.update(henko)
                                sg.popup('MySQLにデータを送信しました。',title='完了')
                if event=='削除':
                        if value['項目']=='':
                                sg.popup('※これは編集機能のボタンです。\n編集したいデータを選び、編集ボタンを押してください',title='注意')
                        else:
                                id=moto[0]
                                sql.delete(id)
def shukei(user):
        sg.theme('SandyBeach')
        hyouzi = sql.hyouzi(user)
        goukei = sql.goukei(user)
        koumoku=hyouzi[0]
        kakaku=hyouzi[1]
        layoutdata=[]
        for i in range(len(koumoku)):
                if koumoku[i]!='給料':
                        layoutdata+=[sg.Text(koumoku[i],font=('Arial',20)),sg.Text(':',font=('Arial',20)),sg.Text(kakaku[i],font=('Arial',20)),sg.Text('円',font=('Arial',20))],
                else:
                        kyuryo=kakaku[i]
        layout = [
                [sg.Text('支出項目,値',font=('Arial',20))],
                layoutdata,
                [sg.Text('支出合計',font=('Arial',20))],
                [sg.Text(goukei-kyuryo,font=('Arial',20)),sg.Text('円',font=('Arial',20)), ],
                [sg.Button('グラフでも見る')] 
        ]
        
        window = sg.Window('収支集計', layout)
        while True:
                event,value=window.read()                        
                if event==sg.WIN_CLOSED or event=='終了':
                        window.close()
                        kmain(user)
                        break
                if event=='グラフでも見る':
                        plot.plot(user)