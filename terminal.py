def tree(currentFolder, tabs, row):
    for obj in currentFolder.content:
        if type(obj) is File:
            print(str(row * "|" + tabs * "_" + obj.name))
        elif type(obj) is Folder:
            print(str(row * "|" + tabs * "_" + obj.name))
            tree(obj, tabs+1, 1)

class File:
    def __init__(self, name, owner, permissions):
        self.name = name
        self.owner = owner
        self.permissions = permissions
        self.content = ""

class Folder:
    def __init__(self, parent, name, owner, permissions):
        self.parent = parent
        self.name = name
        self.owner = owner
        self.permissions = permissions
        self.content = []

command = ""
currentFolder = Folder(0, "/", "Eddie", "rwx")

while (True):
    command = input("# ")
    command = command.split()

    if command[0] == "touch":
        if len(command) != 2:
                print("chyba")
        else: 
            found = False

            for obj in currentFolder.content:
                if obj.name == command[1]:
                    found = True
                    print("chyba")
            if not found:       
                currentFolder.content.append(File(command[1], "Eddie", "rwx"))
    elif command[0] == "ls":
        if currentFolder.parent != 0:
            if currentFolder.parent.permissions.find('r') == -1:
                print("chyba")
            else:
                if len(currentFolder.content) == 0:
                    print("ziaden subor")
                else:
                    for obj in currentFolder.content:
                        print(str(obj.name + "\t" + str(obj.owner) +
                            "\t" + str(obj.permissions)))
        else:
            if len(currentFolder.content) == 0:
                print("ziaden subor")
            else:
                for obj in currentFolder.content:
                    print(str(obj.name + "\t" + str(obj.owner) +
                                "\t" + str(obj.permissions)))
    elif command[0] == "rm":
        if len(command) != 2:
            print("chyba")
        else:              
            found = False

            for index, obj in enumerate(currentFolder.content):
                if obj.name == command[1]:
                    currentFolder.content.pop(index)
                    found = True

            if not found:
                print("chyba")
    elif command[0] == "zapis":
        if len(command) != 3:
            print("chyba")
        else:
            found = False

            for index, obj in enumerate(currentFolder.content):
                if obj.name == command[1]:
                    found = True

                    if obj.permissions.find('w') > -1:
                        if type(obj) is Folder:
                            print("ok")
                        else:
                            obj.content = command[2]
                    else:
                        print("chyba")
                        
            if not found:
                print("chyba")
    elif command[0] == "vypis":
        if len(command) != 2:
            print("chyba")
        else:
            found = False

            for index, obj in enumerate(currentFolder.content):
                if obj.name == command[1]:
                    found = True

                    if obj.permissions.find('r') > -1:
                        if type(obj) is Folder:
                            print("ok")
                        else:    
                            print(str(obj.content))
                    else:
                        print("chyba")

            if not found:
                print("chyba")
    elif command[0] == "chmod":
        if len(command) != 3:
            print("chyba")
        else:
            found = False

            for index, obj in enumerate(currentFolder.content):
                if obj.name == command[2]:
                    found = True

                    if command[1] == '0':
                        obj.permissions = "---"
                    elif command[1] == '1':       
                        obj.permissions = "--x"
                    elif command[1] == '2':       
                        obj.permissions = "-w-"
                    elif command[1] == '3':       
                        obj.permissions = "-wx"
                    elif command[1] == '4':       
                        obj.permissions = "r--"
                    elif command[1] == '5':       
                        obj.permissions = "r-x"
                    elif command[1] == '6':       
                        obj.permissions = "rw-"
                    elif command[1] == '7':       
                        obj.permissions = "rwx"
                    else:
                        print("chyba")        

            if not found:
                print("chyba")
    elif command[0] == "chown":
        if len(command) != 3:
            print("chyba")
        else:
            found = False

            for index, obj in enumerate(currentFolder.content):
                if obj.name == command[2]:
                    obj.owner = command[1]
                    found = True

            if not found:
                    print("chyba")
    elif command[0] == "spusti":
        if len(command) != 2:
            print("chyba")
        else:
            found = False

            for obj in currentFolder.content:
                if obj.name == command[1]:
                    found = True

                    if obj.permissions.find('x') > -1:
                        print("ok")
                    else:
                        print("chyba")    

            if not found:
                print("chyba")
    elif command[0] == "mkdir":
        if len(command) != 2:
            print("chyba")
        else:
            found = False

            for obj in currentFolder.content:
                if obj.name == command[1]:
                    found = True
                    print("chyba")
            if not found:
                currentFolder.content.append(Folder(currentFolder, command[1], "Eddie", "rwx"))
    elif command[0] == "cd":
        if len(command) != 2:
            print("chyba")
        else:
            if command[1] == "..":
                if currentFolder.parent != 0:
                    currentFolder = currentFolder.parent
            elif command[1] == "/":
                while currentFolder.parent != 0:
                    currentFolder = currentFolder.parent 
            else:
                if command[1].find('/') > -1:
                    path = command[1].split('/')

                    path.remove('')
                    
                    for dir in path:
                        found = False

                        for obj in currentFolder.content:
                            if obj.name == dir and type(obj) is Folder and obj.permissions.find('x') > -1:
                                found = True
                                currentFolder = obj

                        if not found:
                            while currentFolder.parent != 0:
                                currentFolder = currentFolder.parent

                            print("chyba")
                            break
                else:    
                    found = False

                    for index, obj in enumerate(currentFolder.content):
                        if obj.name == command[1] and type(obj) is Folder and obj.permissions.find('x') > -1:
                            found = True
                            currentFolder = obj

                    if not found:
                            print("chyba")
    elif command[0] == "tree":
        tree(currentFolder, 0, 0)
    elif command[0] == "quit":
        exit(0)
    else:
        print("chyba")
