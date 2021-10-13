import random
def toranpu_():
    torannpu = []
    suuti = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    ma_ku = ["♡","♤","♧","♢"]
    for i in suuti:
        for j in ma_ku:
            torannpu.append(i+j)
    return torannpu
def haifu(torannpu,fs_list,count=5):
    fs_list = []
    for i in range(count):
        fs = random.choice(torannpu)
        fs_list.append(fs)
        torannpu.remove(fs)
    return fs_list


torannpu = toranpu_()
pl_list = []
dl_list = []

pl = haifu(torannpu,pl_list)
dl = haifu(torannpu,dl_list)
print(pl)
ko = list(map(int,input("このうち捨てるカードを選択してください*右から(0,1,2,3,4)*カンマ区切りで入力、ない場合は５を入力 >").split(",")))
print(ko)