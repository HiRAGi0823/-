import matplotlib.pyplot as plt
from source import sql
import PySimpleGUI as sg

def plot(user):
    listX,listY = sql.hyouzi(user)

    def make_data_fig(listX,listY):
        # 表示するデータ
        Y = listY
        X = range(len(Y))

        # グラフの大きさ指定
        plt.figure(figsize=(10, 5))

        # 棒グラフを中央寄せで表示
        plt.barh(X, Y, align="center", height=0.8)

        # グラフのラベル
        plt.yticks(X, listX,fontsize = 10, fontname = 'MS Gothic') # データXがy軸に表示されていることに注意

        # XとYのラベル
        plt.xlabel('消費合計',fontsize = 10, fontname = 'MS Gothic')
        plt.ylabel('消費項目',fontsize = 10, fontname = 'MS Gothic')

        # タイトル表示
        plt.title('消費項目別合計値',fontsize = 10, fontname = 'MS Gothic')

        # グリッド線を表示
        plt.grid(False)


    def draw_plot(fig):

        plt.show(block=False)
        # block=Falseに指定。これが重要
        # コンソールは何も入力を受け付けなくなり、GUI を閉じないと作業復帰できない。

    def del_plot(fig):

        # plt.cla(): Axesをクリア
        # plt.clf(): figureをクリア
        # plt.close(): プロットを表示するためにポップアップしたウィンドウをクローズ

        plt.close()


    sg.theme('SandyBeach')

    layout = [[sg.Text('グラフでも見る')],
            [sg.Button('グラフの作成',key='-display-'), sg.Button('グラフの削除',key='-clear-'), sg.Cancel()]
            ]

    window = sg.Window('グラフで収支を見よう', layout, location=(100, 100), finalize=True)

    while True:
        event, values = window.read()

        if event in (None, 'Cancel'):
            break

        elif event == '-display-':
            fig_ = make_data_fig(listX,listY)
            draw_plot(fig_)

        elif event == '-clear-':
            del_plot(fig_)

    window.close()
