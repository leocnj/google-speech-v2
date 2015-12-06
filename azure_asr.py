#!/usr/bin/python
#
# azure_asr.py
#
# 
#
import requests
import json
import wave

url = "https://speech.platform.bing.com/recognize"

# from project of oxford
"""
POST /query? scenarios=catsearch&appid=f84e364c-ec34-4773-a783-73707bd9a585&locale=en-US&device.os=wp7&version=3.0&format=xml&requestid=1d4b6030-9099-11e0-91e4-0800200c9a66&instanceid=1d4b6030-9099-11e0-91e4-0800200c9a66 HTTP/1.1
Host: speech.platform.bing.com/recognize/query
Content-Type: audio/wav; samplerate=8000

(audio data)
"""

params = {
    'scenarios' : 'smd',
    'appid' : 'D4D52672-91D7-4C74-8AD8-42B1D98141A5',
    'locale' : 'en-US',
    'device.os' : 'wp7',
    'version' : '3.0',
    'format' : 'json',
    'instanceid' : '565D69FF-E928-4B7E-87DA-9A750B96D9E3',
    'requestid' : '1d4b6030-9099-11e0-91e4-0800200c9a66'
}

headers = {'contentType' : 'audio/wav; samplerate=16000'}

w = wave.open("/home/pi/Jobs.wav", "rb")
binary_data = w.readframes(w.getnframes())
w.close()

files = {'/home/pi/Jobs.wav':binary_data}

r = requests.post(url, params=params, data=json.dumps(data), headers=headers)
