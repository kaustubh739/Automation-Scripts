import os
import hashlib
# Anghol
def main():
    print("Enter file name : ")
    filename = input()

    fobj = open(filename, 'rb') # read in binary # badhali

    hobj = hashlib.md5()

    buffer = fobj.read(1024) # magga

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()

    print("Checksum of file is : ",hobj.hexdigest())
if __name__ == "__main__":
    main()