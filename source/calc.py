from source import sql
#import sql
def znadakam(zndk,kakaku):
    zandaka=int(zndk)-int(kakaku)
    return zandaka

def zandakap(zndk,kyuryo):
    zandaka=int(zndk)+int(kyuryo)
    return zandaka

def zandaka(user):
    zndk=0
    p=0
    m=0
    alldata=sql.alldata(user)
    for i in range(len(alldata)):
        if '給料'==alldata[i][2]:
            p+=alldata[i][5]
        else:
            m+=alldata[i][5]
    zndk=p-m
    return zndk

def wariai(values):
    #平均食費は手取りの約10％
    syokuhi = int(values * 0.1 / (365/12/7))
    #平均生活用品費は手取りの約10％
    seikatuyouhinhi = int(values * 0.1 / (365/12/7))
    #平均嗜好費は手取りの約10％
    sikouhinhi = int(values * 0.1 / (365/12/7))
    #平均交通費は手取りの約3％
    koutuhi = int(values * 0.03 / (365/12/7))
    #平均教養費は手取りの約10％
    kyoyohi = int(values * 0.1 / (365/12/7))
    #平均食通信費は手取りの約3％
    tusinhi = int(values * 0.03 / (365/12/7))
    #平均保健衛生費は手取りの約2.5％
    hokeneiseihi = int(values * 0.025 / (365/12/7))
    #平均交際費は手取りの約5％
    kousaihi = int(values * 0.05 / (365/12/7))
    #平均雑費は手取りの約20％
    zappi = int(values * 0.20 / (365/12/7))
    
    wariai = {
        'syokuhi' : syokuhi,
        'seikatuyouhinhi' : seikatuyouhinhi,
        'sikouhinhi' : sikouhinhi,
        'koutuhi' : koutuhi,
        'kyoyohi' : kyoyohi,
        'tusinhi' : tusinhi,
        'hokeneiseihi' : hokeneiseihi,
        'kousaihi' : kousaihi,
        'zappi' : zappi
    }
    return wariai