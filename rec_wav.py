import pyaudio
import wave

# マイクで音声録音(wav出力)
def rec_wav(rec_time):     # 録音時間[s]
    file_path = "{任意の保存先パス}/output.wav"  # 音声を保存するファイル名
    fmt = pyaudio.paInt16  # 音声のフォーマット
    ch = 1                 # チャンネル1(モノラル)
    sampling_rate = 44100  # サンプリング周波数
    chunk = 2**11          # チャンク（データ点数）
    audio = pyaudio.PyAudio()
    index = 1              # 録音デバイスのインデックス番号（デフォルト1）
    
    stream = audio.open(format=fmt,
                        channels=ch,
                        rate=sampling_rate,
                        input=True,
                        input_device_index = index,
                        frames_per_buffer=chunk)
    
    print("---録音 開始---")
    
    # 録音処理
    frames = []
    for i in range(0, int(sampling_rate / chunk * rec_time)):
        data = stream.read(chunk)
        frames.append(data)
    
    print("---録音 終了---")
    
    # 録音終了処理
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    # 録音データをファイルに保存
    wav = wave.open(file_path, 'wb')
    wav.setnchannels(ch)
    wav.setsampwidth(audio.get_sample_size(fmt))
    wav.setframerate(sampling_rate)
    wav.writeframes(b''.join(frames))
    wav.close()