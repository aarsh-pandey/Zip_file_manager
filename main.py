import extract, ls, os, help, sys, re, zipfile

def get_platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]
plform = get_platform()

print()
print("Enter help for more information")
print()

path = None

while True:
    try:
        command = input("Zip_file_manager $ >>> ")
        if "path" in command :
            if plform == "OS X" :
                try:
                    path = re.compile(r"path(\s+)?(.+)").search(command).group(2).strip().replace("\\","")
                except AttributeError:
                    print("please give the right path")
            elif plform == "Windows" :
                try:
                    path = re.compile(r"path(\s+)?(.+)").search(command).group(2).strip()
                except AttributeError:
                    print("please give the right path")
            else :
                print("This program will not work in",sys.platform)
            print(path)
        elif command.strip() == "exit":
            print()
            sys.exit()
        elif command.strip() == "help":
            print()
            help.help()
        elif command.strip() == "eaf":
            print()
            if path == None :
                print("** Please set the path **")
                continue
            extract.extractallfiles(path)
            print()
        elif command.strip()=="ls":
            print()
            if path == None :
                print("** Please set the path **\n")
                continue
            ls.ls(path)
            print()
        elif command.strip()=="eof":
            print()
            if path == None :
                print("** Please set the path **\n")
                continue
            extract.extractsinglefile(path)
            print()
        elif command.strip()=="clear":
            if plform == "OS X" :
                os.system("clear")
            elif plform == "Windows" :
                os.system("cls")
        else:
            print(f"{command} : This command is not available")
    except Exception :
        print("** Something Went Wrong **")