import speech_recognition as sr

# 音声ファイル文字起こし
def voice_to_text(Audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(Audio_file) as source:
        audio = r.record(source)
    
    # 日本語で文字起こし
    audio_text = r.recognize_google(audio, language = "ja")
    
    print("音声データの文字起こし結果：\n\n",audio_text)
    
    print(len(audio_text))
    
    return audio_text