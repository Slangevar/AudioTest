import audio_record
import keyboard
import sys
import os
import websocket
import datetime
import hashlib
import base64
import hmac
import json
from urllib.parse import urlencode
import time
import ssl
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import _thread as thread
import socket
import re
from xf_demo import *

NAME = "output.txt"

if __name__ == "__main__":

    print("Welcome to a useless app! Press \"space\" to continue or \"esc\" " +
    "to quit.")
    while True:
        if keyboard.is_pressed('space'):
            break
        if keyboard.is_pressed('esc'):
            sys.exit()

    while True:
        with open(file=NAME, mode="w+"):
            pass
            
        audio_record.recording()
        os.system("ffmpeg -hide_banner -loglevel panic -y -i output.wav -acodec " +
        "pcm_s16le -f s16le -ac 1 -ar 16000 output.pcm")
        socket.getaddrinfo('localhost', 8080)


        websocket.enableTrace(False)
        wsUrl = wsParam.create_url()
        ws = websocket.WebSocketApp(wsUrl, on_message=on_message, on_error=on_error, on_close=on_close)
        ws.on_open = on_open
        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
