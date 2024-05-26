entry_time = 3 # 密碼輸入次數
password = 'a123456'

while entry_time > 0:
    entry_time = entry_time - 1
    input_pwd = input('請輸入密碼：')
    
    if input_pwd != password:
        print('密碼錯誤!')
        if entry_time > 0:
            print('還有', entry_time, '次機會')
        else:
            print('帳號已被鎖')
    else:
        print('登入成功')
        break