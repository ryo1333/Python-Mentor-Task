import requests
import urllib
import csv
import pandas as pd


def get_api(url, params: dict):
    result = requests.get(url, params=params)
    return result.json()


def main():
    keyword = "鬼滅"
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"

    # パラメータを記述
    params = {
        "format": "json",
        "keyword": keyword,
        "applicationId": "1019079537947262807",
        "minPrice": 111
    }

    # print(get_api(url, params=params))
    api = get_api(url, params=params)
    # print(api["Items"][0]["Item"]["itemName"])
    for item in api["Items"]:
        pass
        # print(item["Item"]["itemName"])
        # print(f"{item['Item']['itemPrice']}円")

    product_url = "https://app.rakuten.co.jp/services/api/Product/Search/20170426"
    product_api = get_api(product_url, params=params)

    for product in product_api["Products"]:
        pass
        # print(f"{product['Product']['productName']}")
        # print(f"最高値↑ {product['Product']['maxPrice']}円")
        # print(f"最小値↓ {product['Product']['minPrice']}円")

    ranking_url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628"
    ranking_api = get_api(ranking_url, params=params)
    ranking_list = []
    for ranking in ranking_api["Items"]:
        ranking_list.append([ranking["Item"]["rank"], ranking["Item"]
                            ["itemName"], ranking["Item"]["itemPrice"]])

    df = pd.DataFrame(ranking_list,
                      columns=['ランキング', 'タイトル', '価格'])
    df.to_csv("rakuten_ranking.csv", index=False)


main()
