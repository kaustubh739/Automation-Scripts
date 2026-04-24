import os

def DirectoryWatcher(DirectoryName = "Marvellous"):

    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("path is valid but the target is not a directory")
        exit()

    print("absolute path is : "+DirectoryName)

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            print("File name is : "+fname)
            print(os.path.join(FolderName,fname))
            print("File size is : ",os.path.getsize(os.path.join(FolderName,fname))," bytes")

def main():
    print("Enter the name of directory that you want to travel : ")
    DirName = input()

    DirectoryWatcher(DirName)

if __name__ == "__main__":
    main()