import random
rum=random.randint(1,20)
time = 1
last = 5
while time<5:
    a = int(input("請輸入數字?"))
    if a==rum:
        print("恭喜，你猜了" + time + "次")
        break
    else:
        if a > rum:
            print("太大了")
        else:
            print("太小了")
        last = last - 1
        print("加油，你還有" + last + "次")
        time=time + 1
if a != rum:
    print("結束了，你沒猜對，哭阿!")
else:
    print("結束了，恭喜")