#!/usr/bin/env python
#-*- coding:UTF-8 -*-
num_class = 25           # classes to create
Chinese_mode = False    # For Chinese users, set to "True"

import sys
import os
try:
    import pyaudio
except ModuleNotFoundError:
    # We shall need to download first and install offline, since directly pip install would go crash in python>=3.7
    sys.exit('>>> Please download and install: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio  e.g. PyAudio‑0.2.11‑cp38‑cp38‑win_amd64.whl')

def get_line(file_id):
    s = file_id.readline()
    # skip the comments
    while s.startswith('#'):
        s = file_id.readline()
    # remove the '\n' at the end of the line
    while s[-1] == '\n':
        s = s[:-1]
    return s

path_names = list()
item_names = list()

if Chinese_mode:
    codec = "utf-8"
else:
    codec = None

with open("./config.ini", 'r', encoding = codec) as config_file:
    for i in range(num_class):
        # get class names
        line = get_line(config_file)
        path_names.append(line)
        # get content names
        line = get_line(config_file)
        item_names.append(line.split(','))

assert len(path_names) == num_class

# Create dictionaries
for path_name in path_names:
    if not os.path.exists(path_name):
        # try to create the path
        try:
            os.makedirs(path_name)
        except:
            raise Exception("Error create path :", path_name)

# Initialization
WAVE_OUTPUT_FILENAMES = list()

# Generate the file names
for i in range(num_class):
    for rubbish_name in item_names[i]:
        WAVE_OUTPUT_FILENAMES.append(path_names[i] + '/' + rubbish_name + ".wav")

import wave

CHUNK = 1024        # chunk_size
FORMAT = pyaudio.paInt16    # I do not know what it is
CHANNELS = 2        # stereo
RATE = 44100        # sampling rate
RECORD_SECONDS = 3  # seconds to record

# define the recording function
def record_single_file(file_name):
    global CHUNK, FORMAT, CHANNELS, RATE, RECORD_SECONDS
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    if Chinese_mode:
        print("\n>>> 开始录音，请讲话......\n")
    else:
        print("\n>>> Start recording...\n")

    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    if Chinese_mode:
        print("\n>>> 录音结束，请闭嘴！\n")
    else:
        print("\n>>> End.\n")
    

    stream.stop_stream()
    stream.close()
    p.terminate()

    audio_file = wave.open(file_name, 'wb')
    audio_file.setnchannels(CHANNELS)
    audio_file.setsampwidth(p.get_sample_size(FORMAT))
    audio_file.setframerate(RATE)
    audio_file.writeframes(b''.join(frames))
    audio_file.close()
    return 0

# record every file
for file_name_i in WAVE_OUTPUT_FILENAMES:
    os.system("cls")
    if Chinese_mode:
        print("下一个要读的词：", file_name_i.split('/')[1].split('.')[0])
    else:
        print("Next word: ", file_name_i.split('/')[1].split('.')[0])
    if Chinese_mode:
        _stdin = input("\n敲回车开始录音，输入字母q不录了 >>> ")
    else:
        _stdin = input("\nPress Enter to start recording, or 'q' to quit. >>> ")
    if (_stdin == 'q') or (_stdin == 'Q'):
        break
    record_single_file(file_name_i)
if Chinese_mode:
    print("录音结束，请整理数据集文件！")
else:
    print("Finish. Please save and backup your dateset.")
