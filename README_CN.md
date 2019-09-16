# 音频数据集制作工具

首先安装python，安装pyaudio工具包：

https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

根据python版本下载对应的whl文件，如 `PyAudio‑0.2.11‑cp38‑cp38‑win_amd64.whl`

在下载文件所在目录执行：

```
pip install PyAudio‑0.2.11‑cp38‑cp38‑win_amd64.whl
```

如果需要中文支持，在`main.py`中修改"Chinese_mode = True"。然后：

```
python main.py
```

其中类别数量可以修改`main.py`中的变量`num_class = 4`，具体的类别名称和每一类的清单可以修改`config.ini`。

录制完成后，注意保存和备份音频文件。

更详细的介绍请参考[英文版说明](./README.md)。

参考文献：

[PyAudio 实现录音 自动化交互实现问答](https://www.cnblogs.com/DragonFire/p/9212935.html)
