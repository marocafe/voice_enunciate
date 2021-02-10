import xml.etree.ElementTree as ET
import urllib.request
import urllib.parse

# YahooAPIによる文章校正
def YahooAPI(text):
    # XMLのタグについてくるもの
    kousei_name = "{urn:yahoo:jp:jlp:KouseiService}"
    
    API = "https://jlp.yahooapis.jp/KouseiService/V1/kousei"
    APPID = "{発行したアプリID}"
    values = {
        'appid': APPID,
        'sentence': text,
        'filter_group': "",
        'no_filter': ""
    }
    
    # 結果から弾きたいものをリスト化
    repel_filter = [
        "当て字",
        "表外漢字あり",
        "用字",
        "助詞否定の可能性あり",
        "二重否定"
    ]
    
    # URLを作成
    params = urllib.parse.urlencode(values)
    url = API + "?" + params
    
    # リクエスト
    response = urllib.request.urlopen(url).read()
    
    # 返ってきた XML を utf-8 で出力
    xml_string = response.decode("utf-8")
    print(xml_string)
    
    # ここからxml解析
    root = ET.fromstring(xml_string)
    
    result = []
    for element in list(root):
        startPos = int(element.findtext(kousei_name + 'StartPos'))      # 対象文字列の開始位置 (先頭からの文字数)
        length = int(element.findtext(kousei_name + 'Length'))          # 対象文字列の長さ (対象文字数)
        endPos = startPos + length                                      # 対象文字列の終了位置
        surface = element.findtext(kousei_name + 'Surface')             # 対象文字列の表記
        shitekiWord = element.findtext(kousei_name + 'ShitekiWord')     # 言い換え候補文字列（予測）
        shitekiInfo = element.findtext(kousei_name + 'ShitekiInfo')     # 指摘内容を表す
        
        result.append({
            'StartPos': startPos,
            'EndPos': endPos,
            'Length': length,
            'Surface': surface,
            'ShitekiWord': shitekiWord,
            'ShitekiInfo': shitekiInfo,
        })
    
    print(result)
    
    # 結果からテキストを修正
    if len(result) == 0:
        print("これは正しい文章です")
    else:
        for i in range(len(result)):
            dict_result = result[i]
            if dict_result['ShitekiInfo'] in repel_filter:
                pass
            else:
                text = text.replace(dict_result['Surface'], dict_result['ShitekiWord'])
    
    return text