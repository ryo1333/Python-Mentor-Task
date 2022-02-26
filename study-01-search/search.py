import os

path = 'study-01-search/source.csv'

# 検索ツールサンプル
# これをベースに課題の内容を追記してください

# 検索ソース
source = ["ねずこ", "たんじろう", "きょうじゅろう", "ぎゆう", "げんや", "かなお", "ぜんいつ"]

# 検索ツール


def search():
    word = input("鬼滅の登場人物の名前を入力してください >>> ")

    # ここに検索ロジックを書く
    if not os.path.isfile(path):
        csv_write(word, source)

    else:
        with open(path) as f:
            l_strip = [s.strip() for s in f.readlines()]
            print(l_strip)
        csv_write(word, l_strip)


def csv_write(word, source):
    if word in source:
        print(f"{word}が見つかりました")
    else:
        source.append(word)
        print("見つかりませんでした")
        with open(path, mode='w') as f:
            f.write('\n'.join(source))


if __name__ == "__main__":
    search()
