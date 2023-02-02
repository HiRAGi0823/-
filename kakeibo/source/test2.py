import PySimpleGUI as sg
import sql
user='admin'
sg.theme('SandyBeach')
layout = [
    [sg.Button('集計'),sg.Button('終了')]
]

window = sg.Window('データ集計', layout)
listx,listy = sql.hyouzi(user)
i=0
listx.reverse()
print(listx)
listy.reverse()
print(listy)
listz = []
for i in range(len(listx)):
    listz.append(str(listx[i])+','+str(listy[i]))
    print(listz)
goukei = sql.goukei(user)

while True:
    event,value=window.read()
    if event=='集計':
        # layout2 = [
        #     [sg.Text('支出項目')],
        #     [sg.Text(listz)],
        #     [sg.Text('支出合計')],
        #     [sg.Text(goukei),sg.Text('円'), ] 
        # ]
        layout2=[]
        listc = []
        listd = []
        layout2.append([sg.Text('支出項目')])
        for i in range(len(listx)):
            layout2.append([sg.Text(str(listx[i])+','+str(listy[i]))])
            
        
        layout2.append([sg.Text('支出合計')])
        layout2.append([sg.Text(goukei)])
        window = sg.Window('支出集計', layout2)
        
    if event==sg.WIN_CLOSED or event=='終了':
        break