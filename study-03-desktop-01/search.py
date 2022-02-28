import pandas as pd
import eel
import os
import sys

# デスクトップアプリ作成課題
dpath = os.path.dirname(sys.argv[0])


def kimetsu_search(word, csv_name):
    # 検索対象取得
    df = pd.read_csv(f"{dpath}/source.csv")
    source = list(df["name"])
    # 検索
    if word in source:
        print("『{}』はあります".format(word))
        eel.view_log_js(f"『{word}』はあります")
    else:
        print("『{}』はありません".format(word))
        eel.view_log_js(f"『{word}』はありません")
        # 追加
        # add_flg = input("追加登録しますか？(0:しない 1:する)　＞＞　")
        # if add_flg == "1":
        source.append(word)

    # CSV書き込み
    df = pd.DataFrame(source, columns=["name"])
    df.to_csv(f"{dpath}/{csv_name}.csv", encoding="utf_8-sig")
    print(source)
