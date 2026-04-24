import os

def main():
    for FolderName, SubFolderNames, FileNames in os.walk("kaustubh"):
        print("Folder name is : "+FolderName)

        for subf in SubFolderNames:
            print("SubFolder name is : "+subf)

        for fname in FileNames:
            print("File name is : "+fname)

if __name__ == "__main__":
    main()