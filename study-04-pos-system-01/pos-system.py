import pandas as pd
import datetime

dt_now = datetime.datetime.now()
# print(dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))

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

    def add_item_order(self, item_code):
        amount = int(input('個数は？'))
        for item in self.item_master:
            if item.item_code in item_code:
                self.item_order_list.append(
                    [item.item_code, item.item_name, item.price, amount])
                self.item_order_dict.update(
                    {item.item_code: [item.item_name, item.price, amount]})

        total_price = self.item_order_dict[item_code][2] * \
            self.item_order_dict[item_code][1]
        print(
            f"商品名は{self.item_order_dict[item_code][0]}で、\n個数は{self.item_order_dict[item_code][2]}個で、\n合計金額は{total_price}円です。")

        pay = int(input('支払額？'))
        change = pay - total_price
        print(f"支払額は{pay}円で、お返しは{change}円でございます。")

        with open(txt_path, mode='a') as f:
            f.write(
                f"商品コード:{self.item_order_list[0][0]}\n商品名:{self.item_order_list[0][1]}\n個数:{self.item_order_list[0][3]}個\n合計金額:{total_price}円\n支払額:{pay}円\nお釣り:{change}円\n日付:{dt_now.strftime('%Y年%m月%d日 %H:%M:%S')}\n--------------------------------------------------------")

    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード:{}".format(item[0]), "商品名:{}".format(
                item[1]), "価格:{}".format(item[2]))

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

    # CSV書き込み
    # df = pd.DataFrame(data, columns=["商品コード", "商品名", "価格"])
    # df.to_csv(path,
    #           encoding="utf_8-sig", index=False)

    # オーダー登録
    order = Order(item_master)
    code = input('商品コードは？')
    for d in df:
        if d[0] in code:
            order.add_item_order(code)

    # オーダー表示
    order.view_item_list()


if __name__ == "__main__":
    main()
