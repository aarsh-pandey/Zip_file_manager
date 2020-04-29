import zipfile, os
def ls(path):   
    try:
        path = os.path.split(path)
        os.chdir(path[0])
    except Exception:
        print("Path not found")
    try:
        zip = zipfile.ZipFile(path[1])
        for i, file in enumerate(zip.namelist(),start=1):
            print(i,file)
    except Exception:
        print("Unknown Error...")


def lsr(path):
        path = os.path.split(path)
        os.chdir(path[0])
        zip = zipfile.ZipFile(path[1])
        dict_list = {}
        for i, file in enumerate(zip.namelist(),start=1):
            dict_list[i] = file
        return dict_list