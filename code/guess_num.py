import random

r = random.randint(1, 100)
while True:
    num = int(input('猜猜數字：'))
    if r > num:
        print('再大一點')
    elif r < num:
        print('再小一點')
    else:
        print('猜對了')
        break    