# >介绍

RBS是一个应用于教育行业的工具箱软件

# >提示

- 作者的母语是中文,所有README都基于中文版翻译得来,一切歧义最终应查看本文解释
- 中文版本:[README_cn.md](https://github.com/Puiching-Memory/RBS-Software/blob/main/README_cn.md)
- English version:[README.md](https://github.com/Puiching-Memory/RBS-Software/blob/main/README.md)

# >程序结构

| 入口               | 主程序  | 模块(逻辑部分) | 模块(可视化界面部分) |
| ------------------ | ------- | -------------- | -------------------- |
| Preparation.py     | Main.py | M_QRcode.py    | GUI_QRcode.py        |
| GUI_Preparation.py | GUI.py  | M_Timer.py     | GUI_Timer.py         |
|                    |         | M_Roll.py      | GUI_Roll.py          |
|                    |         | M_***.py       | GUI_***.py           |

*每个模块都有其相对应的GUI程序(所有名字中带有'GUI'的文件)

# >在Python3.8环境下运行

##### 运行库列表

```
autopep8==1.5.7
beautifulsoup4==4.9.3
bs4==0.0.1
certifi==2021.5.30
charset-normalizer==2.0.4
cmake==3.21.1.post1
colorama==0.4.4
idna==3.2
numpy==1.21.1
opencv-python==4.5.3.56
Pillow==8.3.1
ping3==3.0.1
psutil==5.8.0
pyflakes==2.3.1
pynput==1.7.3
pypinyin==0.42.0
python-jsonrpc-server==0.4.0
python-language-server==0.36.2
pywin32==301
qrcode==7.2
requests==2.26.0
rope==0.19.0
simpleaudio==1.0.4
six==1.16.0
soupsieve==2.2.1
ujson==4.0.2
urllib3==1.26.6
wxPython==4.1.1
xlrd==2.0.1
xlwt==1.3.0
```

##### pip 批量安装

```
pip install -r requirements.txt
```

# >打包到.exe文件

##### 跟随以下步骤!

1. 在文件夹根目录下打开控制台
2. 检测你是否已经能够在Python环境下成功运行
3. 安装Pyinstaller库
4. 使用Pyinstaller打包
5. 将名为'copy'文件夹中的所有文件拷贝到打包生成的.exe文件的根目录中 (注意不是拷贝单一的文件夹!)

##### 通过pip安装

```
pip install pyinstaller==4.5.1
```

```
pip install tinyaes==1.0.1
```

##### 打包命令

完整版 ↓↓↓

```
pyinstaller -D Preparation.py -i ICOV4.ico --upx-dir UPX -y -n RBS_Software2021  --key ZKPuichingMemory -w --collect-submodules pynput
```

轻量版 ↓↓↓

```
pyinstaller -D Preparation.py -y -n RBS_Software2021 -w --collect-submodules pynput
```

##### 提示

1. 打包程序需要使用上ICO文件和图像文件.确保它们在正确的位置 (通常来说默认的位置就是正确的,这里担心有些人把它们移动到其它位置上)
2. 如果所需文件没有准备好,打包的过程中会发生错误(废话)
3. 打包需要用到UPX. 请准备好UPX,将其放置在一个文件夹中并命名为'UPX',然后放在根目录上
4. 下载UPX>>>[https://github.com/upx/upx](https://github.com/upx/upx)
5. 如果你选择轻量版,你不需要关心以上的任何事.🤣

# 维护者

[@PuichingMemory](https://github.com/Puiching-Memory)

# >更新日志

##### 只显示最近的两次更新(我知道你不关心这个)😛

['2021/07/17', 'Ver021.07.17']
+改进:
1.'BMI'模块现在已经更新至V2
2.'设置'模块添加对主界面的'透明度'控制
3.'进制转换'模块已经更新至V2
4.主界面添加了'网络延迟检测'模块
5.主界面添加了'天气'模块
6.Python版本已升级至3.8.10
7.WALP引擎已整合入'地理'分区
8.'设置'模块现在可以控制程序日志的保存位置
9.'更新日志'模块已更新至V2
-问题:
1.在线更新模块仍不可用
2.'下载器'模块进行修复,但无法定义文件位置和类型
||信息:
ALL:174MB
DIST:37.0MB
ZIP:25.3MB
NSIS:24.2MB

---

['2021/07/03', 'Ver021.07.03']
+改进:
1.主界面左上角图标现在可以正常显示
2.主界面现在支持文件拖拽
3.主界面GUI优化,修复BUG
4.添加两个临时功能模块,完成度20%(没有明显提示,但你仍可以打开它)
5.主界面"USER"模块已经完成
6.'随机数生成器'已经重写
-问题:
1.在线更新模块仍不可用
2.'下载器'模块完全无法使用
3.右侧侧边栏优化未完成
4.部分API接口未完成
5.'值日表'模块存在一个已知的恶性BUG
||信息:
ALL:129MB
DIST:37.4MB
ZIP:26.7MB
NSIS:25.6MB

---
