#!/usr/bin/env python
# --*--coding=utf-8--*--
# pip install pybluez

import time
import bluetooth

#列表，用于存放已搜索过的蓝牙名称
alreadyFound = []

devices = bluetooth.discover_devices(lookup_names=True)
print(devices)