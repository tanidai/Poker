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
    for i in range(count):
        fs = random.choice(torannpu)
        fs_list.append(fs)
        torannpu.remove(fs)
    return fs_list
def dlira(dl):
    hogolist = []
    for i in dl:
        for l in dl:
            if i[0] == l[0] and i != l:
                hogolist.append(i)

    count = 5 - len(hogolist)
    dl_deta = haifu(torannpu,hogolist,count)
    return dl_deta
torannpu = toranpu_()
pl_list = []
dl_list = []
pl = haifu(torannpu,pl_list)
dl = haifu(torannpu,dl_list)
print("プレイヤー")
print(pl)
print("ディーラー")
print(dl)
ko = list(map(int,input("このうち捨てるカードを選択してください*右から(0,1,2,3,4)*カンマ区切りで入力、ない場合は５を入力,全ての場合は６を入力 >").split(",")))
print("ディーラー")
print(dlira(dl))
ko = ko[::-1]
if ko != [5] and ko != [6]:
    for i in ko:    
        k = pl[i]
        pl.remove(k)
    count = 5 - len(pl)
    pl_2 = haifu(torannpu,pl,count)
    print("プレイヤー")
    print(pl_2)
elif ko == [5]:
    print("プレイヤー")
    print(pl)
elif ko == [6]:
    pl = []
    pl = haifu(torannpu,pl)
    print("プレイヤー")
    print(pl)

print(torannpu)