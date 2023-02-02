import PySimpleGUI as sg
sg.theme('Light Blue 2')#デザインテーマの指定
def s():
        #ウィンドウに配置するコンポーネント
        layout =[[sg.Text('投資(k単位 1k=1000円)')],
                [sg.InputText()],
                [sg.Button('OK')]
        ]
        #ウィンドウの生成
        window=sg.Window('投資',layout)
        #イベントループ
        while True:
                event,value=window.read()
                if event=='OK':
                        vt=value
                        window.close()
                        break
        return vt

def k():
        layout2 =[[sg.Text('回収(k単位 1k=1000円)')],
                [sg.InputText()],
                [sg.Button('OK')]
        ] 
        window=sg.Window('回収',layout2)
        while True:
                event,value2=window.read()
                if event=='OK':
                        vk=value2
                        window.close()
                        break
        return vk

def conif():
        layout3=[[sg.Text('データの入力を続けますか')],
                [sg.Button('Yes'),sg.Button('No')]
        ]
        window=sg.Window('Yes or No',layout3)
        while True:
                event=window.read()
                if event=='Yes':
                        window.close()
                        a=1
                        break
                else:
                        window.close()
                        a=0
                        break
        return a
def lryn():
        layout4=[[sg.Text('課題研究用の家計簿のアカウントをお持ちですか？')],
                [sg.Button('Yes'),sg.Button('No')]
        ]
        window=sg.Window('Do you have an Account?',layout4)
        while True:
                event=window.read()
                if event=='Yes':
                        window.close()
                        a2=event
                        break
                else:
                        window.close()
                        a2=event
                        break
        return a2
def login():
        layout5 =[
                [sg.Text('メールアドレス')],
                [sg.InputText()],
                [sg.Text('パスワード')],
                [sg.InputText(password_char='●')],    
                [sg.Button('ログイン')]
        ]
        window=sg.Window('Login',layout5)
        while True:
                event,value3=window.read()
                if event=='ログイン':
                        window.close()
                        userdata=value3
                        break
        return userdata
def registar():
        layout6=[
                [sg.Text('メールアドレス')],
                [sg.InputText()],
                [sg.Text('ユーザー名')],
                [sg.InputText()],    
                [sg.Text('パスワード'),],
                [sg.InputText(password_char='●')],    
                [sg.Button('新規作成')]
        ]
        window=sg.Window('Login',layout6)
        while True:
                event,value4=window.read()
                if event=='新規作成':
                        window.close()
                        sinkidata=value4
                        break
        return sinkidata
def probar():
        BAR_MAX = 1000
        #　レイアウト（1段目：テキスト、2段目：プログレスバー、3段目：ボタン）
        layout = [[sg.Text('家計簿アプリのデータを参照中')],
                [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,20), key='-PROG-')],
                [sg.Cancel('中断')]]
        #　ウィンドウの生成
        window = sg.Window('家計簿', layout)

        for i in range(BAR_MAX):
                #　入力待ち（10msでタイムアウトして、次の処理へ進む）
                event, values = window.read(timeout=3)
                #　キャンセルボタンか、ウィンドウの右上の×が押された場合の処理
                if event == '中断' or event == sg.WIN_CLOSED:
                        break
                #　プログレスバーの表示更新（カウンタ(i)をインクリメントして表示）
                window['-PROG-'].update(i+1)

        window.close()