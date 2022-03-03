from tkinter import N
from tkinter.messagebox import YES
import pandas as pd
import datetime

dt_now = datetime.datetime.now()

path = "study-04-pos-system-01/source.csv"
txt_path = "study-04-pos-system-01/pay.txt"
# 商品クラス


class Item:
    def __init__(self, item_code, item_name, price):
        self.item_code = item_code
        self.item_name = item_name
        self.price = price

    def get_price(self):
        return self.price

# オーダークラス


class Order:
    def __init__(self, item_master):
        self.item_order_dict = {}
        self.item_order_list = []
        self.item_master = item_master
        self.total_price = []
        self.pay = 0
        self.change = 0

    def add_create_dict(self):
        for item in self.item_master:
            self.item_order_dict.update(
                {item.item_code: [item.item_name, item.price]})

    def add_item_order(self, item_code):
        amount = int(input('個数は？'))
        for item in self.item_master:
            if item.item_code in item_code:
                self.item_order_list.append(
                    [item.item_code, item.item_name, item.price, amount])

    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード:{}".format(item[0]), "商品名:{}".format(
                item[1]), "価格:{}".format(item[2]), "個数:{}".format(item[3]))
            self.total_price.append(item[2] * item[3])
        print(f"合計金額は{sum(self.total_price)}円です。")

        self.total_pay()

    def total_pay(self):
        self.pay = int(input('支払額？'))
        self.change = self.pay - sum(self.total_price)
        print(f"支払額は{self.pay}円で、お返しは{self.change}円でございます。")

        self.create_receipt()

    def create_receipt(self):
        with open(txt_path, mode='a') as f:
            f.write(f"\n商品コード:{', '.join([item_code[0] for item_code in self.item_order_list])}\n商品名:{', '.join([item_code[1] for item_code in self.item_order_list])}\n個数:{sum([item_code[3] for item_code in self.item_order_list])}個\n合計金額:{sum(self.total_price)}円\n支払額:{self.pay}円\nお釣り:{self.change}円\n日付:{dt_now.strftime('%Y年%m月%d日 %H:%M:%S')}\n--------------------------------------------------------")
        # f"商品コード:{', '.join([item_code[0] for item_code in self.item_order_list])}\n商品名:{', '.join([item_code[1] for item_code in self.item_order_list])}\n個数:{sum([item_code[2] for item_code in self.item_order_list])}個\n合計金額:{sum(self.total_price)}円\n支払額:{self.pay}円\nお釣り:{change}円\n日付:{dt_now.strftime('%Y年%m月%d日 %H:%M:%S')}\n--------------------------------------------------------")

# メイン処理


def main():
    # マスタ登録
    item_master = []
    item_master.append(Item("001", "りんご", 100))
    item_master.append(Item("002", "なし", 120))
    item_master.append(Item("003", "みかん", 150))

    data = []
    for item in item_master:
        data.append([item.item_code, item.item_name, item.price])

    df = pd.read_csv(path, encoding="utf_8-sig", sep=',',
                     index_col=False, dtype=str).values.tolist()

    # オーダー登録
    order = Order(item_master)
    order.add_create_dict()

    while True:
        choice = input('商品を選びますか？y?n?')
        if choice == 'y':
            code = input('商品コードは？')
            if code in order.item_order_dict:
                order.add_item_order(code)
            else:
                print('見つかりません')
        else:
            break

    # オーダー表示
    order.view_item_list()


if __name__ == "__main__":
    main()
