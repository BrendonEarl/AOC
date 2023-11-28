class MyFile():
    
    def __init__(self,name,parent=None,isDir=True,size=0) -> None:
        self.name = name
        self.parent = parent
        self.isDir = isDir
        self.size = size
        self.children = {}
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.name
    
    def add_child(self, childFile):
        self.children[str(childFile)] = childFile
    
    def updateSize(self):
        self.updateSizeHelper(self)
    
    def updateSizeHelper(self, file):
        if not file.isDir:
            file.parent.size += file.size
            return

        for child in file.children.values():
            file.updateSizeHelper(child)
        
        if file.parent:
            file.parent.size += file.size

    def prettyPrint(self):
        self.printChildrenHelper(self)

    def printChildrenHelper(self, myfile, spacing = ""):
        print(f'{spacing}{str(myfile)}:{myfile.isDir}:{myfile.size}')

        for child in self.children.values():
            child.printChildrenHelper(child,spacing + "|   ")


def execute(commands):
    HOME = current_directory = MyFile("/")
    files = {str(current_directory) : current_directory}
    
    for index, command in enumerate(commands):
        zero, one = command[0], command[1]
        two = command[2] if len(command) >2 else None
        
        if index == 0: 
            continue

        if zero.isnumeric():
            name = one
            while name in files.keys():
                name += "+"
            newFile = MyFile(name,current_directory,False,int(zero))
            if newFile not in current_directory.children:
                current_directory.add_child(newFile)
                files.update({str(newFile) : newFile})
        
        elif zero == "dir":
            name = one
            while name in files.keys():
                name += "+"
            newFile = MyFile(name,current_directory)
            if newFile not in current_directory.children:
                current_directory.add_child(newFile)
                files.update({str(newFile) :newFile})
        
        elif zero == "$":
            if one == "cd":
                if two == "..":
                    current_directory = current_directory.parent
                else:
                    findName = two
                    for child in current_directory.children.keys():
                        if findName == child.strip("+"):
                            findName = child
                    current_directory = files[findName]
            
    
    HOME.updateSize()
    # HOME.prettyPrint()
    prob1, freeUp, prob2 = 0, 30000000 -(70000000 - HOME.size), HOME.size

    for file in files.values():
        if(file.size <= 100000 and file.isDir):
            prob1 += file.size
        if freeUp < file.size < prob2:
            prob2 = file.size

    print(f' problem 1: {prob1} \n'
          f' problem 2: {prob2}')


def main(filename):
    commands = [line.strip().split() for line in open(filename).readlines()]
    execute(commands)


main(filename:="2022/resources/input_7.txt")