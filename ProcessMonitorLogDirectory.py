import psutil
import os
import time

def CreateLog(FolderName):
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")

    FileName = os.path.join(FolderName, "Marvellous%s.log" %(timestamp))

    fobj = open(FileName, 'w')

    border = "-" * 80
    fobj.write(border)
    fobj.write("\n\t\t Kaustubh's Process Log\n")
    fobj.write("\n\t\t Log file is created at : "+time.ctime()+"\n")
    fobj.write(border)

def ProcessDisplay():
    Border = "*" * 25
    print(Border)
    print("Information of currently running processess : ")
    print(Border)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid','name','username'])
            info ['vms'] = proc.memory_info().vms / (1024 * 1024)
            print(info)
        except Exception:
            print("Exception Occured")


def main():
    CreateLog("MarvellousProcess")

if __name__ == "__main__":
    main()