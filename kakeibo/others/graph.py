from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import PySimpleGUI as sg

def gp():
    sg.theme('Light Blue 2')

    def draw_plot(x,y):
        plt.plot(x,y)
        plt.show(block=False)
        #block=Falseの指定をしないと、その間コンソールは何も入力を受け付けなくなり、GUI を閉じないと作業復帰できない。

    def check_file(file_name):
        p = Path(file_name)
        print(p.suffix)
        if p.suffix == '.csv':
            df = pd.read_csv(p) 
            x = df.iloc[:,0]
            y = df.iloc[:,1]

            return x, y

        else:
            print('Wrong data file, data must be CSV')  
            return None, None

    layout = [[sg.Text('Enter csv data')],
            [sg.Text('File', size=(8, 1)),sg.Input(key='-file_name-'), sg.FileBrowse()],
            [sg.Submit()],
            [sg.Button('Plot'), sg.Cancel()],
            [sg.Button('Popup')]]

    window = sg.Window('Plot', layout)

    while True:
        event, values = window.read()

        if event in (None, 'Cancel'):
            break
        elif event in 'Submit':
            print('File name:{}'.format(values['-file_name-']))
            x,y = check_file(values['-file_name-'])

            if x[0] == None:
                sg.popup('Set file is not CSV')

        elif event == 'Plot':
            draw_plot(x,y)

        elif event == 'Popup':
            sg.popup('Yes, your application is still running')
    window.close()