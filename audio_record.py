import pyaudio
import wave
import time
import keyboard
import sys

def recording():

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    #RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()
    print("Press \"s\" to start recording")

    while True:
        if keyboard.is_pressed('s'):
            print("Recording...Press \"e\" to end recording ")
            break
        if keyboard.is_pressed('esc'):
            sys.exit()

    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    frames = []

    start_time = time.time()
    inter_time = time.time()
    while True:
        if keyboard.is_pressed('esc'):
            sys.exit()
        data = stream.read(CHUNK)
        frames.append(data)
        if time.time() >= 60 + start_time:
            print("You have exceed the 60-second limit. Recording ends.")
            break
        if keyboard.is_pressed('e'):
            print("Recording ends.")
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
