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
        print("Folder name is : "+FolderName)

        for subf in SubFolderNames:
            print("SubFolder name is : "+subf)

        for fname in FileNames:
            print("File name is : "+fname)


def main():
    print("Enter the name of directory that you want to travel : ")
    DirName = input()

    DirectoryWatcher(DirName)

if __name__ == "__main__":
    main()