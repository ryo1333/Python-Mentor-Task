import eel
import sys
import socket
import pos_system
import pandas as pd

path = "source.csv"


# 定数
ENTRY_POINT = 'html/index.html'
CHROME_ARGS = [
    '--incognit',  # シークレットモード
    '--disable-http-cache',  # キャッシュ無効
    '--disable-plugins',  # プラグイン無効
    '--disable-extensions',  # 拡張機能無効
    '--disable-dev-tools',  # デベロッパーツールを無効にする
]
ALLOW_EXTENSIONS = ['.html', '.css', '.js', '.ico']


app_name = "html"
end_point = "index.html"
size = (700, 600)

df = pd.read_csv(path, encoding="utf_8-sig", sep=',',
                 index_col=False, dtype=str).values.tolist()

# マスタ登録
item_master = []
for master_item in df:
    item_master.append(pos_system.Item(
        master_item[0], master_item[1], master_item[2]))

data = []
for item in item_master:
    data.append([item.item_code, item.item_name, item.price])

# オーダー登録
order = pos_system.Order(df)
order.add_create_dict()


@ eel.expose
def get_code(code_number, amount):
    if code_number in order.item_order_dict:
        order.add_item_order(code_number, amount)
        eel.source_data(order.view_item_list(code_number))
        eel.total_pay_view(order.view_total_price())


@ eel.expose
def pay(pay_amount):
    eel.receipt_view(order.view_total_pay(pay_amount))
    order.create_receipt()


# @ eel.expose
# def clear():
#     eel.order.clear()


def start(appName, endpoint, size):  # 画面生成
    eel.init(appName, allowed_extensions=ALLOW_EXTENSIONS)
    # 未使用ポート取得
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    port = s.getsockname()[1]
    s.close()
    options = {
        'mode': "chrome",
        'close_callback': exit,
        'port': port,
        'cmdline_args': CHROME_ARGS
    }
    eel.start(endpoint, options=options,
              size=size, suppress_error=True)


def exit(arg1, arg2):  # 終了時の処理
    sys.exit(0)


start(app_name, end_point, size)
