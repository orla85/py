# 密碼輸入次數
entry_time = 3
password = 'a123456'
while entry_time != 0:
    input_pwd = input('請輸入密碼：')
    if input_pwd != password:
        entry_time = entry_time - 1
        if entry_time != 0:
            print('密碼錯誤, 還有', entry_time, '次機會')
    else:
        print('登入成功')
        break