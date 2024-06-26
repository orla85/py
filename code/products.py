import os # operating system

products = []
if os.path.isfile('products.csv'): #檢查檔案是否存在
    print('found')
    #讀取檔案 
    with open('products.csv','r',encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name,price])
    print(products)
else:
    print('not found')


#使用者輸入
while True:
    name = input('請輸入商品名稱：')
    if(name == 'q'):
        break
    price = input('請輸入商品價格：')
    products.append([name, price])
print(products)

with open('products.csv','w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')