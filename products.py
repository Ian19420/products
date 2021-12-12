def user_input():
    products = []
    while True:
        name = input("請輸入商品名稱(按q結束輸入):")
        if name == "q":
            break
        price = input("請輸入商品價格:")
        products.append([name, price])
        
    return products


def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

def write_file(filename, products):
    print('存取商品內容...')
    with open(filename, 'w', encoding = 'utf8') as f:
        f.write('商品, 價格\n')
        for p in products:
            f.write(p[0]+ ','+ p[1]+ '\n')

def read_file(filename):
    print('讀取商品內容...')
    products_input = []
    with open(filename, encoding = 'utf8') as f:
        for line in f:
            if "商品, 價格" in line:
                continue
            products_input += line.strip().split(',')
    print(products_input)


def main():
    products = user_input()
    print_products(products)
    write_file('products.csv', products)
    import os
    filename = 'products.csv'
    if os.path.isfile(filename):
        print("找到檔案了")
        read_file(filename)
    else:
        print("找不到檔案")
main()