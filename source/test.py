import random
import time
zu1=0
zu2=0
zu3=0
l=0
r=0
ren=1
while True:
    while True:
        l+=1
        へそ=round(random.uniform(0,65536),3)
        if へそ<=204.801:
            へそ振り分け=random.randint(0,1)
            if へそ振り分け==0:
                r+=450
                print('  2   2   2')
                print('３Ｒ ４５０発　1/2外すなカス')
                break
            else:
                r+=1500
                print('  7   7   7')
                print('１０Ｒ １５００発　RUSHおめでと～')
                while True:
                    電チュー=round(random.uniform(0,65536),3)
                    転落抽選=電チュー
                    if 電チュー>968.036 and 転落抽選<65331.199:
                        zu1=random.randint(1,9)
                        zu2=random.randint(1,9)
                        zu3=random.randint(1,9)
                        if zu1==zu2 and zu1==zu3:
                            print(' ',zu1,' ',zu2+1,' ',zu3)
                        else:
                            print(' ',zu1,' ',zu2,' ',zu3)
                            
                    if 電チュー<=968.036:
                        r+=1500
                        ren+=1
                        print('  7   7   7',ren,'連荘')
                    elif 転落抽選>=65331.199:
                        電チュー=round(random.uniform(0,65536),3)
                        電チュー1=round(random.uniform(0,65536),3)
                        電チュー2=round(random.uniform(0,65536),3)
                        電チュー3=round(random.uniform(0,65536),3)                    
                        if 電チュー<=968.035 or 電チュー1<=968.035 or 電チュー2<=968.035 or 電チュー3<=968.035:
                            r+=1500
                            ren+=1
                            print('  7   7   7',ren,'連荘')
                            continue
                        else:
                            print('ラッシュ終了')
                            print('result')
                            print(ren,'連荘  ',r,'発')
                            time.sleep(2)
                            break
                break
        else:
            zu1=random.randint(1,9)
            zu2=random.randint(1,9)
            zu3=random.randint(1,9)
            if zu1==zu2 and zu1==zu3:
                print(' ',zu1,' ',zu2+1,' ',zu3)
            else:
                print(' ',zu1,' ',zu2,' ',zu3)