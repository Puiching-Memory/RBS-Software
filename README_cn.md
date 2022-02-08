# >介绍

RBS是一个应用于教育行业的工具箱软件

# >提示

- 作者的母语是中文,所有README都基于中文版翻译得来,一切歧义最终应查看本文解释
- 中文:[README_cn.md](https://github.com/Puiching-Memory/RBS-Software/blob/main/README_cn.md) 2022/2/7
- English:[README.md](https://github.com/Puiching-Memory/RBS-Software/blob/main/README.md) ----/-/-

# >程序结构

|            | 入口               | 主程序  | 模块     |
| ---------- | ------------------ | ------- | -------- |
| 逻辑       | Preparation.py     | Main.py | M_*.py   |
| 可视化界面 | GUI_Preparation.py | GUI.py  | GUI_*.py |

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

1. 在文件夹根目录下打开控制台
2. 检测你是否已经能够在Python环境下成功运行
3. 安装Pyinstaller库
4. 使用Pyinstaller打包
5. 将名为'copy'文件夹中的所有文件拷贝到打包生成的.exe文件的根目录中 (注意不是拷贝单一的文件夹!)

##### 通过pip安装

```
pip install pyinstaller
```

##### 打包命令

```
pyinstaller -D Preparation.py -i ICOV4.ico --upx-dir UPX -y -n RBS_Software -w
```

##### 提示

1. 打包程序需要使用上ICO文件和图像文件.确保它们在正确的位置 (通常来说默认的位置就是正确的)
2. 如果发生错误，请及时反馈问题
3. 打包需要用到UPX. 请准备好UPX,将其放置在一个文件夹中并命名为'UPX',然后放在根目录上
4. 下载UPX>>>[https://github.com/upx/upx](https://github.com/upx/upx)

# >插件

你可以在plug-in文件夹中添加插件,程序的插件功能基于python的函数exec()运行.

# 维护者

[@PuichingMemory](https://github.com/Puiching-Memory)

# >更新日志

##### 只显示最近的两次更新(我知道你不关心这个)😛

['2022/02/05', 'Ver022.02.05']
-----RBS_Software update log(项目更新日志)-----
+改进:
1.主界面部分细节改进
2.添加了'性能监视器'模块
3.清理了过时文件
4.模块'简繁转换'数据库已更新
5.'音频分析器'模块已完善,支持导入MP3、wav、flac、ogg文件，可导出ogg、wav、MP3文件
6.'随机数'模块已更新至V4
-问题:
1.OpenGL在初始化进程中引发错误导致软件卡在启动界面(IS09191)
2.由于pi值精度过高导致的浮点数计算BUG(IS09181)
3.'文件管理器'清理文件时遇到占用冲突[WinError 32](IS12251)
4.主界面ping模块暂时禁用(IS12312)
5.'数学画板'关闭按钮不能正常工作(IS01011)
6.log等文件可能会因为编码格式(utf-8)而导致中文出现乱码(IS01141)
7.'值日表'模块的实现算法已过时
||信息:
ALL:--MB
DIST:--MB
ZIP:--MB
NSIS:--MB

---

['2022/01/24', 'Ver022.01.24']
-----RBS_Software update log(项目更新日志)-----
+改进:
1.'关于'界面改进
2.BUG修复:主界面'CMD功能'无法使用(IS12252)
3.代码规范优化-进度1
4.'RBS_DDT'项目已作为模块'M_DDT'进行集成
5.'RBS_PLC'部分功能集成
6.插件功能已重写,现在使用.py文件接口(#200)
7.主界面'快速启动'功能长期缺少维护,现已删除(IS12253)
8.文件结构优化
9.BUG修复:必应壁纸模块不能正常工作(IS12255)
-问题:
1.OpenGL在初始化进程中引发错误导致软件卡在启动界面(IS09191)
2.由于pi值精度过高导致的浮点数计算BUG(IS09181)
3.'文件管理器'清理文件时遇到占用冲突[WinError 32](IS12251)
4.主界面ping模块暂时禁用(IS12312)
5.'数学画板'关闭按钮不能正常工作(IS01011)
6.log等文件可能会因为编码格式(utf-8)而导致中文出现乱码(IS01141)
7.'值日表'模块的实现算法已过时
||信息:
ALL:482MB
DIST:40.7MB
ZIP:--MB
NSIS:--MB

---
