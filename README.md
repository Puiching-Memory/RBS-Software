# >介绍

RBS是一个应用于教育行业的工具箱软件

# >提示

- 作者的母语是中文,所有文档都基于中文版翻译得来
- 中文:[README_Zh_CN.md](https://github.com/Puiching-Memory/RBS-Software/blob/main/README_cn.md) 2022/4/11
- English:[README_EN.md](https://github.com/Puiching-Memory/RBS-Software/blob/main/README.md) ----/-/-

# >程序结构

|            | 入口               | 主程序  | 模块     |
| ---------- | ------------------ | ------- | -------- |
| 逻辑       | Preparation.py     | Main.py | M_*.py   |
| 可视化界面 | GUI_Preparation.py | GUI.py  | GUI_*.py |

*每个模块都有其相对应的GUI程序(所有名字中带有'GUI'的文件)

# >在Python3.8环境下运行

##### 运行库列表

```
beautifulsoup4==4.10.0
bs4==0.0.1
certifi==2021.10.8
charset-normalizer==2.0.12
cmake==3.22.2
colorama==0.4.4
idna==3.3
numpy==1.22.2
Pillow==9.0.1
psutil==5.9.0
pydub==0.25.1
pynput==1.7.6
pypinyin==0.46.0
python-jsonrpc-server==0.4.0
python-language-server==0.36.2
pywin32==303
qrcode==7.3.1
requests==2.27.1
six==1.16.0
soupsieve==2.3.1
urllib3==1.26.8
wxPython==4.1.1
xlrd==2.0.1
xlwt==1.3.0
zhconv==1.4.3
zhdate==0.1
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
pyinstaller -D Preparation.py -i ICOV4.ico --upx-dir UPX -y -n RBS_Software -w --exclude-module tkinter --exclude-module lxml
```

##### 提示

1. 打包程序需要使用上ICO文件和图像文件.确保它们在正确的位置 (通常来说默认的位置就是正确的)
2. 如果发生错误，请及时反馈问题
3. 打包需要用到UPX. 请准备好UPX,将其放置在一个文件夹中并命名为'UPX',然后放在根目录上
4. 下载UPX>>>[https://github.com/upx/upx](https://github.com/upx/upx)

# >插件

你可以在plug-in文件夹中添加插件,程序的插件功能基于python的函数exec()运行.

每个插件应开设独立命名的文件夹，并带有Info.cfg文件作为识别信息

你可以参考官方示例插件，位于./plug-in/Example

# >主题

RBS使用的颜色主题读取于一组外部文件(通常是.cfg)，其数据结构为十六进制颜色

你可以自己尝试修改这些文件，用以获取自定义的颜色效果，例如：全黑的黑夜模式

文件路径：./DATA/Main/Theme/*

# 维护者

[@PuichingMemory](https://github.com/Puiching-Memory "用户个人空间链接")

# >更新日志

##### 只显示最近的更新(我知道你不关心这个)😛

['2022/04/03', 'Ver022.04.03']
-----RBS_Software update log(项目更新日志)-----
+改进:
1.主界面及部分子模块界面优化
2.为'随机数'模块,随机学号功能添加了多线程,皆在解决GUI阻塞问题
3.BUG修复：为'Bing壁纸'模块添加了多线程(IS022.0312B)
4.'元素周期表'模块数据录入已完成
5.为'Music'模块添加了多线程
6.剔除多余的库文件以减少打包文件大小
7.为'历史上的今天'添加了多线程
8.移除了初始化后不再使用的变量,减小内存占用
-问题:
1.(IS09191) -> wxGL库打包错误,可能由于某些库的缺失导致启动失败(IS022.0208A)
2.由于pi值精度过高导致的浮点数计算BUG(IS09181)
3.'值日表'模块的实现算法已过时
4.'基因库'算法已过时
5.载入插件并将插件文件夹手动移除后将导致问题(IS022.0227A)
6.插件在关闭后无法释放内存(IS022.0312A)
7.在windows Server2012(远程链接)中字体显示会缺损
8.在启动'Bing壁纸'模块后清理缓存会导致设置壁纸操作错误
9.'历史上的今天'api请求缺少ssl验证(IS022.0327A)
?计划：
1.数学统计(import statistics)
2.bilibili api(import bilibili_api)
$实验：
1.窗口背景透明效果：win7毛玻璃/win10亚克力效果
2.窗口阴影
||信息:
ALL:--MB
DIST:--MB
ZIP:--MB
NSIS:--MB
