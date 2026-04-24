import psutil

def ProcessScan():

    listprocess = []

    Border = "*" * 25
    print(Border)
    print("Information of currently running processess : ")
    print(Border)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid','name','username'])
            info ['vms'] = proc.memory_info().vms / (1024 * 1024)
            listprocess.append(info)
        except {psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess}:
            pass
    return listprocess

def main():
    Arr = ProcessScan()

    for value in Arr:
        print(value)

if __name__ == "__main__":
    main()