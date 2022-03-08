import pandas as pd
import datetime
import numpy as np

dt_now = datetime.datetime.now()

path = "source.csv"
txt_path = "pay.txt"
# 商品クラス


class Item:
    def __init__(self, item_code, item_name, price):
        self.item_code = str(item_code)
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
        self.amount = 0
        self.view_order_dict = {}
        self.item_code = ""

    def add_create_dict(self):
        for item in self.item_master:
            self.item_order_dict.update({item[0]: [item[1], item[2]]})

    def add_item_order(self, item_code, amount):
        self.amount = amount
        for item in self.item_master:
            if item[0] in item_code:
                self.item_order_list.append(
                    [item[0], item[1], int(item[2]), int(self.amount)])
                self.view_order_dict.update(
                    {item[0]: [item[1], item[2], int(self.amount)]})

    def view_item_list(self, item_code):
        for item in self.item_order_list:
            return "商品コード:{}".format(
                item_code), "商品名:{}".format(item[1]), "価格:{}".format(item[2])

    def view_total_price(self):
        for item in self.item_order_list:
            self.total_price.append(item[2] * item[3])
            return f"合計金額は{sum(self.total_price)}円です。"

    def view_total_pay(self, pay):
        self.pay = pay
        self.change = self.pay - sum(self.total_price)
        return f"支払額は{self.pay}円で、お返しは{self.change}円でございます。"

    def create_receipt(self):
        with open(txt_path, mode='a') as f:
            f.write(f"\n商品コード:{', '.join([item_code[0] for item_code in self.item_order_list])}\n商品名:{', '.join([item_code[1] for item_code in self.item_order_list])}\n個数:{sum([item_code[3] for item_code in self.item_order_list])}個\n合計金額:{sum(self.total_price)}円\n支払額:{self.pay}円\nお釣り:{self.change}円\n日付:{dt_now.strftime('%Y年%m月%d日 %H:%M:%S')}\n--------------------------------------------------------")
