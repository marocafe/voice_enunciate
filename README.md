# 滑舌を改善しちゃいたい
## 概要
### YahooAPIにてアプリIDを発行する必要があります。
マイクから受け取った音声を文字起こしし、YahooAPI 校正支援を利用し文章を校正したのち合成音声として出力する。<br>
「正常に文字起こしされなかった部分を修正すれば滑舌を改善できるのでは」の考えのもと制作。<br>
GUIアプリとして実行し簡単に操作できるように。<br>
## 使用ライブラリ
・PyAudio
・speech_recognition
・Google Text-to-Speech
・Pygame
・tkinter
## 使用API
・YahooAPI 校正支援
## 参考サイト
・マイクの音を録音してWAVEファイルに保存  https://algorithm.joho.info/programming/python/pyaudio-record/<br>
・ElementTreeを使ってXMLの解析に挑戦しよう  https://www.sejuku.net/blog/74013<br>
・PythonでMP3音源を再生する  https://qiita.com/kekeho/items/a0b93695d8a8ac6f1028
