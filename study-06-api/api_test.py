from api import get_api
import pprint


def test_get_api():
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={PS5}&applicationId=1019079537947262807"
    params = {
        "format": "json",
        "applicationId": "1019079537947262807",
    }
    res = get_api(url=url, params=params)
    print(res)

    # チェック
    # 正常系　→　うまくいった時の処理
    assert len(res["Items"]) >= 1
    assert res["Items"][0]["Item"]["itemCode"]

    # 異常系　→　失敗時の処理
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={PS5ああああああああああ}&applicationId=1019079537947262807"
    res = get_api(url=url)

    assert len(res["Items"]) == 0


def test_2():
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
    params = {
        "format": "json",
        "applicationId": "1019079537947262807",
        "keyword": "PS5",
    }
    res = get_api(url=url, params=params)

    # assert res["Items"] == None
    assert res["Items"]
    assert len(res["Items"]) >= 1
    assert res["Items"][0]["Item"]["itemCode"]
