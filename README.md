## 创高校园校园跑脚本
# 仅限学习交流使用，本项目完全开源，如使用过程中涉及法律问题请自行承担责任！！！
#### 使用条件
1. 雷电模拟器
2. Android adb
3. python3
4. pip库:numpy、frida
5. frida
### 使用教程
1. 雷电模拟器开启root,开启adb调试
2. 将frida-server二进制文件放到模拟器的/data/local/tmp目录下，重命名为www
3. 根据模拟器数量修改main.py中的线程
4. 运行main.py
### 运行成功截图
![image](https://github.com/Amorter/HenuRun/assets/63935225/f62ee565-3aca-4a7f-ac2c-a4d496e5ec9e)
### 常见错误
1. 如果报错，多半是leidian.py里面runFridaServer函数底下那两条命令的问题，不同的雷电模拟器版本命令有差别，建议自己adb手动试试能不能用.
2. 自创高版本2.9.8开始，检测瞬时速度好像发生了一些微妙的变化，本项目功能失效
### 2.9.8后的问题本项目不在维护，永久停止更新，能用到什么时候算什么时候吧
