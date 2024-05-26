import random

start = int(input('請輸入隨機數開始值：'))
end = int(input('請輸入隨機數結束值：'))
r = random.randint(start, end)
cnt = 0 #猜測次數

while True:
    num = int(input('猜猜數字：'))
    cnt += 1
    if r > num:
        print('再大一點')
    elif r < num:
        print('再小一點')
    else:
        print('猜對了')
        print('目前猜了', cnt, '次') 
        break
    print('目前猜了', cnt, '次') 
       