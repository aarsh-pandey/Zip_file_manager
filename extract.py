import zipfile as zf
import os, ls, pprint
def extractallfiles(zip_file_path):
    zip = zf.ZipFile(zip_file_path)
    print("Do you want continue", end=" ") 
    extract_file_boolen = input("(y/n) : ")
    if(extract_file_boolen == "y" or extract_file_boolen == "Y"):
        cwd = os.getcwd()
        print(f"\nDo you want to extract all files in the following path :-  {cwd} \nEnter n for different path",end=" ")
        ans = input("(y/n) :")
        if(ans=="y" or ans=="Y"):
            zip.extractall()
        elif(ans=="n" or ans=="N"):
            path = input("Please enter path of folder where you want to extract the files :").strip()
            zip.extractall(path)


def extractsinglefile(zip_file_path):
    zip = zf.ZipFile(zip_file_path)
    print("Do you want continue", end=" ") 
    extract_file_boolen = input("(y/n) : ")
    dic = ls.lsr(zip_file_path)
    pprint.pprint(dic)
    filenm = input("please give the name or No of file : ").strip()
    
    if int(filenm) in list(dic.keys()):
        filenm = dic[int(filenm)]
    if(extract_file_boolen == "y" or extract_file_boolen == "Y"):
        cwd = os.getcwd()
        print(f"\nDo you want to extract file in the following path :-  {cwd} \nEnter n for different path",end=" ")
        ans = input("(y/n) :").strip()
        if(ans=="y" or ans=="Y"):
            zip.extract(filenm)
        elif(ans=="n" or ans=="N"):
            path = input("Please enter path of folder where you want to extract the files :").strip()
            zip.extract(filenm, path)