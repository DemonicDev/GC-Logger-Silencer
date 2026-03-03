import os
os.system("color b")
print("Thx for using DemonicEagle143's PocketMine-MP Garbage Collector Spam Remover <3 \n")
nat_path = os.getcwd();
def update_php_file(file_path):
    # Read the file content
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Update the specific lines
    found = False
    with open(file_path, 'w') as file:
        for line in lines:
            if '$this->logger->info' in line and not found:
                line = r"/**" + line
                found = True
            if ';' in line and found:
                line = line + r"**/"
                found = False
            file.write(line)
   
def Build(var):
    php_file_path = nat_path + fr"\{var}\src\GarbageCollectorManager.php"
    update_php_file(php_file_path)
    print(fr"Updated {php_file_path} to no GarbageCollector outputs ")  
def getPmFolder():
    a = []
    files = [f for f in os.listdir() if os.path.isdir(f)]
    for i in files:
        print(i)
        if checkIfPmFolder(i):
            a.append(i)
    print(a)
    ac = len(a)
    if ac > 0:
        if ac == 1:
            return a[0]
        else:
            for i in range(0, len(a)):
                print("[",i,"]", a[i])
            g = VerInput(a)
            return a[g]
    else:
        exit("no Pocketmine Source Folder found [GarbageCollectorManager.php not found]")
def VerInput(a):
        j = input("choose which too build:")
        if(j.isnumeric()):
            g = int(j)
        else:
            print("Int is requiered")
            return VerInput(a)
        if (g > len(a)-1) or (g < 0):
            print("out of range!!!")
            return VerInput(a)
        return g
def checkIfPmFolder(folder):
    return os.path.exists(nat_path + fr"\{folder}\src\GarbageCollectorManager.php")
Build(getPmFolder())
exit("Thx for using this Programm <3 \nfeel free to open an issue, for feedback or ideas :D")
