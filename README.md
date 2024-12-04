# bad-rp2040

第一版 还要修修

## 使用教程

虽然名字叫做bad-rp2040，但理论上它可以支持其他能够使用CircuitPython的板子。

* 第一步
  按住BOOT按键进入烧入模式从[这里](https://circuitpython.org/board/raspberry_pi_pico/)找到合适的CircuitPython固件烧入

* 第二步
  烧入完成后再下载项目文件，修改payload.txt为你想要的内容，之后写入磁盘模式的开发板

* 第三步
  重新插拔开发板，不出意外开发板会自动模拟按键输入编写好的payload


## payload语法

> 目前尚在开发中，很多功能并不全面画横线的表示正在开发中

示例
```badusb
setTime 0.3 
POWERSHELL
ECHO HelloWord
ECHO PASS
POWERSHELL
ECHO 123123
```
内置了快捷使用的模组
* POWERSHELL
* ~~WINDOWS~~
* ~~LINUX~~
* ~~CMD~~
* ~~SHELL~~

根据需求调用即可，echo语句用于输出字符串

#### 语法表

| 命令     | 作用                       |
-----------|---------------------------|
| ~~setTime~~  | ~~设置按键间隔时间~~     |

### 后续开发计划

短期
* 完成目前列出的所有模组
* 完成计划的语法

长期
* 是否可以做到监听键盘输入

![run](https://s2.loli.net/2024/12/04/d4NjluG9nEImwUB.png)