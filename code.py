import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

import Rpayload

# 创建一个键盘对象
keyboard = Keyboard(usb_hid.devices)

# 字符到 Keycode 的映射
key_map = {
    'WINDOWS': Keycode.WINDOWS, 'GUI': Keycode.GUI,
    'APP': Keycode.APPLICATION, 'MENU': Keycode.APPLICATION, 'SHIFT': Keycode.SHIFT,
    'ALT': Keycode.ALT, 'CONTROL': Keycode.CONTROL, 'CTRL': Keycode.CONTROL,
    'DOWNARROW': Keycode.DOWN_ARROW, 'DOWN': Keycode.DOWN_ARROW, 'LEFTARROW': Keycode.LEFT_ARROW,
    'LEFT': Keycode.LEFT_ARROW, 'RIGHTARROW': Keycode.RIGHT_ARROW, 'RIGHT': Keycode.RIGHT_ARROW,
    'UPARROW': Keycode.UP_ARROW, 'UP': Keycode.UP_ARROW, 'BREAK': Keycode.PAUSE,
    'PAUSE': Keycode.PAUSE, 'CAPSLOCK': Keycode.CAPS_LOCK, 'DELETE': Keycode.DELETE,
    'END': Keycode.END, 'ESC': Keycode.ESCAPE, 'ESCAPE': Keycode.ESCAPE, 'HOME': Keycode.HOME,
    'INSERT': Keycode.INSERT, 'NUMLOCK': Keycode.KEYPAD_NUMLOCK, 'PAGEUP': Keycode.PAGE_UP,
    'PAGEDOWN': Keycode.PAGE_DOWN, 'PRINTSCREEN': Keycode.PRINT_SCREEN, 'ENTER': Keycode.ENTER,
    'SCROLLLOCK': Keycode.SCROLL_LOCK, 'SPACE': Keycode.SPACE, 'TAB': Keycode.TAB,
    'BACKSPACE': Keycode.BACKSPACE,
    'a': Keycode.A, 'b': Keycode.B, 'c': Keycode.C, 'd': Keycode.D, 'e': Keycode.E,
    'f': Keycode.F, 'g': Keycode.G, 'h': Keycode.H, 'i': Keycode.I, 'j': Keycode.J,
    'k': Keycode.K, 'l': Keycode.L, 'm': Keycode.M, 'n': Keycode.N, 'o': Keycode.O,
    'p': Keycode.P, 'q': Keycode.Q, 'r': Keycode.R, 's': Keycode.S, 't': Keycode.T,
    'u': Keycode.U, 'v': Keycode.V, 'w': Keycode.W, 'x': Keycode.X, 'y': Keycode.Y,
    'z': Keycode.Z,
    'A': (Keycode.SHIFT, Keycode.A), 'B': (Keycode.SHIFT, Keycode.B),
    'C': (Keycode.SHIFT, Keycode.C), 'D': (Keycode.SHIFT, Keycode.D),
    'E': (Keycode.SHIFT, Keycode.E), 'F': (Keycode.SHIFT, Keycode.F),
    'G': (Keycode.SHIFT, Keycode.G), 'H': (Keycode.SHIFT, Keycode.H),
    'I': (Keycode.SHIFT, Keycode.I), 'J': (Keycode.SHIFT, Keycode.J),
    'K': (Keycode.SHIFT, Keycode.K), 'L': (Keycode.SHIFT, Keycode.L),
    'M': (Keycode.SHIFT, Keycode.M), 'N': (Keycode.SHIFT, Keycode.N),
    'O': (Keycode.SHIFT, Keycode.O), 'P': (Keycode.SHIFT, Keycode.P),
    'Q': (Keycode.SHIFT, Keycode.Q), 'R': (Keycode.SHIFT, Keycode.R),
    'S': (Keycode.SHIFT, Keycode.S), 'T': (Keycode.SHIFT, Keycode.T),
    'U': (Keycode.SHIFT, Keycode.U), 'V': (Keycode.SHIFT, Keycode.V),
    'W': (Keycode.SHIFT, Keycode.W), 'X': (Keycode.SHIFT, Keycode.X),
    'Y': (Keycode.SHIFT, Keycode.Y), 'Z': (Keycode.SHIFT, Keycode.Z),
    '0': Keycode.ZERO, '1': Keycode.ONE, '2': Keycode.TWO, '3': Keycode.THREE,
    '4': Keycode.FOUR, '5': Keycode.FIVE, '6': Keycode.SIX, '7': Keycode.SEVEN,
    '8': Keycode.EIGHT, '9': Keycode.NINE,
    ' ': Keycode.SPACE, '-': Keycode.MINUS, '/': Keycode.FORWARD_SLASH,
    '.': Keycode.PERIOD, ':': (Keycode.SHIFT, Keycode.SEMICOLON),
    ';': Keycode.SEMICOLON, '\'': Keycode.QUOTE, '"': (Keycode.SHIFT, Keycode.QUOTE),
    '(': (Keycode.SHIFT, Keycode.NINE), ')': (Keycode.SHIFT, Keycode.ZERO),
    '_': (Keycode.SHIFT, Keycode.MINUS), '=': Keycode.EQUALS,
    '!': (Keycode.SHIFT, Keycode.ONE), '@': (Keycode.SHIFT, Keycode.TWO),
    '#': (Keycode.SHIFT, Keycode.THREE), '$': (Keycode.SHIFT, Keycode.FOUR),
    '%': (Keycode.SHIFT, Keycode.FIVE), '^': (Keycode.SHIFT, Keycode.SIX),
    '&': (Keycode.SHIFT, Keycode.SEVEN), '*': (Keycode.SHIFT, Keycode.EIGHT),
    '+': (Keycode.SHIFT, Keycode.EQUALS),
    '[': Keycode.LEFT_BRACKET, ']': Keycode.RIGHT_BRACKET,
    '{': (Keycode.SHIFT, Keycode.LEFT_BRACKET), '}': (Keycode.SHIFT, Keycode.RIGHT_BRACKET),
    '\\': Keycode.BACKSLASH, '|': (Keycode.SHIFT, Keycode.BACKSLASH),
    '<': (Keycode.SHIFT, Keycode.COMMA), '>': (Keycode.SHIFT, Keycode.PERIOD),
    '?': (Keycode.SHIFT, Keycode.FORWARD_SLASH), '"': (Keycode.SHIFT, Keycode.QUOTE)
}

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

delay_time = 1.0

# payload = """ """

## 启动函数 从rpayload中获取命令 判断启动方式 执行对应的函数
def main():
    try:
        getMod = Rpayload.Rpayload()
        getLen = len(getMod)
        for i in range(getLen):
            if getMod[i] == "powershell":
                print("powershell")
                check = powershell()
                print(check)
                continue

            elif getMod[i][:5] == "time=":
                print(f"Time set: {getMod[i]}")
                settime = getMod[i][5:]
                setTime(settime)
                continue

            elif getMod[i] == "cmd":
                print("cmd")
                continue
            
            elif getMod[i] == "toggleinput":
                 toggleinput()
                 continue
            
            else:
                payload = getMod[i]
                echo(payload)
    except Exception as e:
        print(f"Error occurred: {e}")
        keyboard.release_all()
        raise
    
def echo(payload):
    global delay_time
    try:
        time.sleep(delay_time)
        for char in payload : # payload
            print(char)
            if char == ":" or char == '"' or char == '(' or char == ')' or char in uppercase_letters:
                test = special_case(char) # 特判函数
                print(test)
                continue  # 跳出
            
            keyboard.press(key_map[char])  # 标准逻辑
            keyboard.release_all()
            time.sleep(0.1)

        keyboard.release_all()
        keyboard.press(Keycode.ENTER)
        keyboard.release_all()
        print("Command has been typed and Enter pressed.")
    except Exception as e:
        print(f"Error occurred: {e}")
        keyboard.release_all()  
        raise


def special_case(char):
    for key in key_map[char]:
        keyboard.press(key)
    keyboard.release_all()
    return "check"
    
def powershell():
    global delay_time
    try:
        time.sleep(delay_time)

        keyboard.press(Keycode.WINDOWS)
        keyboard.press(Keycode.R)
        keyboard.release_all()
        time.sleep(delay_time)

        for char in "powershell":
            print(char)
            keyboard.press(key_map[char])  # 按下字符
            keyboard.release_all()  # 释放所有按键
            time.sleep(0.1)

            # 回车键
        keyboard.press(Keycode.ENTER)
        keyboard.release_all()

    except Exception as e:
        print(f"Error occurred: {e}")
        keyboard.release_all()  
        raise
    return "OK"

def toggleinput():
    try:
        keyboard.press(key_map['CTRL'])
        time.sleep(1)
        keyboard.press(key_map['SPACE'])
        time.sleep(0.5)
        keyboard.release_all()  # 释放所有按键
    except Exception as e:
        print(f"Error occurred: {e}")
        keyboard.release_all()  
        raise

def setTime(settime):
    try:
        global delay_time
        delay_time = float(settime)
    except Exception as e:
        print(f"Error occurred: {e}")
    


if __name__ == "__main__":
    main()
