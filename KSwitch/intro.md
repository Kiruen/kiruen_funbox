# KSwitch

A mini system based on esp-8266 which can boot your PC by a website remotely.
这是个硬件+软件的小项目：
硬件部分基于esp01/esp-8266，使用micropython编程，在物理层面实现了PC的开机和关机，当然也可以实现普通的开关功能。
软件部分使用Flask搭建了一个超简易网站，可以对外提供一个接口来操作远程节点。支持多节点管理。

本项目还进行过拓展，比如外接舵机实现了一个远程/定时喂猫装置（柯西被喵破坏了。。）