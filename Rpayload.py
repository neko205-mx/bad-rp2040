
paylist = [] # 使用列表存储payload
# payload 读取函数
def Rpayload():
    
    with open ('payload.txt','r') as payload:
        for line in payload:
            line = line.strip()
            
            if line == "WINDOWS":
                win()
            elif line == "LINUX":
                linux()
            elif line == "POWERSHELL":
                powershell()
            elif line == "CMD":
                cmd()
            elif line[:4] == "ECHO":
                paylist.append(line[5:])
            print(paylist)
    return paylist
        


def main():
    Rpayload()

# 处理函数
def win():
    print("test")


def linux():
    print("test")

def powershell():
    print("test_powershell")
    paylist.append("powershell")

def cmd():
    print("test_cmd")
    paylist.append("cmd")



if __name__ == '__main__':
    main()
