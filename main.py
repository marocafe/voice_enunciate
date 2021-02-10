import wave
from gtts import gTTS
import tkinter as tk
import sys
from mutagen.mp3 import MP3 as mp3
import pygame
import time
import os
from rec_wav import rec_wav
from voice_to_text import voice_to_text
from YahooAPI import YahooAPI

# テキストを合成音声に変換
def speech_synthesis(text):
    global cnt
    if os.path.exists("{任意の保存先パス}/gousei" + str(cnt) + ".mp3"):
        print("存在します")
        cnt += 1
    
    # 日本語で出力
    language = "ja"
    
    output = gTTS(text=text, lang=language, slow=False)
    output.save("{任意の保存先パス}/gousei" + str(cnt) + ".mp3")
    print("合成出力　終了")

# MP3ファイルを再生
def play_mp3():
    global cnt
    filename = "{任意の保存先パス}/gousei" + str(cnt) + ".mp3" #再生したいmp3ファイル
    pygame.mixer.init()
    pygame.mixer.music.load(filename)           # 音源を読み込み
    mp3_length = mp3(filename).info.length      # 音源の長さ取得
    pygame.mixer.music.play(1)                  # 再生開始。1の部分を変えるとn回再生(その場合は次の行の秒数も×nすること)
    time.sleep(mp3_length + 0.25)               # 再生開始後、音源の長さだけ待つ(0.25待つのは誤差解消)
    pygame.mixer.music.stop()                   # 音源の長さ待ったら再生停止

# GUIラジオボタン用 一つしかボタンが押されないように
def change_radio():
    check = var.get()
    if check == 5:
        radio_2.configure(state='normal')
        radio_3.configure(state='normal')
    elif check == 10:
        radio_1.configure(state='normal')
        radio_3.configure(state='normal')
    elif check == 20:
        radio_1.configure(state='normal')
        radio_2.configure(state='normal')

# GUIアプリで実行したときのもの
def button_click():
    # GUIアプリでの入力を受け取る
    rec_time = var.get()
    # 録音
    rec_wav(int(rec_time))
    # 文字起こし
    text = voice_to_text("{任意の保存先パス}/output.wav")
    # 校正
    YahooAPI(text)
    # 合成音声
    speech_synthesis(text)

# メインコード　GUIアプリ起動
if __name__ == "__main__":
    cnt = 1

    # アプリウィンドウを作成
    window = tk.Tk()
    window.title("滑舌改善したい君")
    window.geometry("450x300")
    
    # ラベル作成
    label = tk.Label(text="録音する時間を選択", font=("MSゴシック", "10", "bold"))
    label.pack(anchor="center")
    
    # 値の受け取り
    var = tk.IntVar()
    var.set(5)
    
    # ラジオボタン作成（5秒、10秒、20秒）
    radio_1 = tk.Radiobutton(text=" 5", value=5, variable=var, command=change_radio)
    radio_1.place(x=100, y=50)
    
    radio_2 = tk.Radiobutton(text="10", value=10, variable=var, command=change_radio)
    radio_2.place(x=200, y=50)
    
    radio_3 = tk.Radiobutton(text="20", value=20, variable=var, command=change_radio)
    radio_3.place(x=300, y=50)
    
    # 録音・文章校正の実行ボタン作成
    button = tk.Button(text="録音・修正", width=13, command=button_click)
    button.place(x=100, y=130)
    
    # 作成した合成音声を再生するボタン作成
    play_button = tk.Button(text="合成音声再生", width=13, command=play_mp3)
    play_button.place(x=100, y=180)
    
    # ウィンドウを閉じるボタン作成
    close_button = tk.Button(text="終了", command=window.destroy)
    close_button.place(x=300, y=230)
    
    # 実行
    window.mainloop()