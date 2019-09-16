# Audio Dataset Creating Tools

## Installization

Install python, and then install the `pyaudio` toolbox by opening the URL:

https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

Download the ".whl" file according to the version you need, e.g. `PyAudio‑0.2.11‑cp38‑cp38‑win_amd64.whl` for python 3.8.

Switch to the path of the downloaded file, then:

```
pip install PyAudio‑0.2.11‑cp38‑cp38‑win_amd64.whl
```

## Configuration

1. Open [`main.py`](./main.py), set the `num_class` to the value of your target classes. Then close and save file.

2. Open [`config.ini`](./config.ini), there should be `2 * num_class` valid lines. Each two lines stand for one class.

    The first line is the class name.

    The second line is the items. They should be separated with the sign ",". Attention that there is no space between them. Alternatively, one can modify this sign by changing the code in [`main.py`](./main.py).

## Recording

To start recording data, just simply type:

```
python main.py
```

Note: If you want to quit when creating the dataset, just type "q" when asked (not case sensitive).

After finishing recording, please remember to save and backup your dateset.

## Others

1. (International users can ignore this point.) Chinese version of README is [here](./README_CN.md). If you want to support Chinese names, make sure to set "Chinese_mode = True" in [`main.py`](./main.py).

2. There may be bugs and  in this code. It is very welcome if you could pull a request.
