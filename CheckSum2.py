import os
import hashlib

def CalculateCheckSum(X):
    fobj = open(X, 'rb') # read in binary

    hobj = hashlib.md5()
    
    buffer = fobj.read(1024)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def main():
    print("Enter file name : ")
    filename = input()

    ret = CalculateCheckSum(filename)

    print("checksum is : ", ret)

if __name__ == "__main__":
    main()
