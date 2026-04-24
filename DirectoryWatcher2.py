import os

def main():
    print("Enter the name of Directory : ")
    DirName = input()

    ret = os.path.isabs(DirName)

    if (ret == True):
        print("Input is absolute path")

    else:
        print("Input is relative path")
        NewPath = os.path.abspath(DirName)
        print("updated path is : ",NewPath)

if __name__ == "__main__":
    main()