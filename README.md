# 创高校园校园跑脚本

> 仅限学习交流使用，本项目完全开源。如使用过程中涉及法律问题请自行承担责任！！！

## 使用条件

- 雷电模拟器
- Android adb
- Python 3
- Pip 库: numpy、frida
- Frida

## 使用教程

1. 雷电模拟器开启 root，并启用 adb 调试。
2. 将 Frida-Server [二进制文件](https://github.com/frida/frida/releases) 放置于模拟器的 `/data/local/tmp` 目录下，并重命名为 `www`。
3. 根据模拟器数量修改 `main.py` 中的线程数。
4. 运行 `main.py`
