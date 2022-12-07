import pathlib
import sys
from typing import Union, List


class Directory:
    # name: str = "/"
    # parent: Union["Directory", None] = None
    # contents: List[Union["Directory", "File"]] = []

    def __init__(self, name: str = "/", parent: Union["Directory", None] = None):
        self.name = name
        self.parent = parent
        self.contents: List[Union["Directory", "File"]] = []

    def addDirectory(self, directory: "Directory"):
        directory.parent = self
        self.contents.append(directory)

    def addFile(self, file: "File"):
        file.parent = self
        self.contents.append(file)

    def calculateSize(self, _size: int = 0):
        size = _size
        dirs = list(filter(lambda x: type(x) == Directory, self.contents))
        files = list(filter(lambda x: type(x) == File, self.contents))
        for i in files:
            _size += i.size
        for i in dirs:
            _size += i.calculateSize(0)
        return _size

    def cd(self, input: str):
        dirs = list(filter(lambda x: type(x) == Directory, self.contents))
        for i in dirs:
            if i.name == input:
                return i
        else:
            raise ValueError

    def printTree(self):
        spaces = 2*self.distToRoot()*" "
        print(f"{spaces}- {self.name} (dir)")
        for i in self.contents:
            spaces = 2*i.distToRoot()*" "
            if type(i) is File:
                print(f"{spaces}- {i.name} (file, size={i.size})")
            if type(i) is Directory:
                i.printTree()

    def root(self):
        t = self
        while True:
            if t.parent:
                t = t.parent
            else:
                return t

    def distToRoot(self):
        t = self
        c = 0
        while True:
            if t.parent:
                t = t.parent
                c += 1
            else:
                return c

    def recursiveDirSearch(self, allDirs: List["Directory"] = []):
        dirs = list(filter(lambda x: type(x) == Directory, self.contents))
        allDirs = allDirs + dirs
        if len(dirs) > 0:
            # print(len(dirs), dirs)
            for i in dirs:
                t = i.recursiveDirSearch()
                for j in t:
                    allDirs.append(j)
        else:
            return []
        return allDirs

    def __repr__(self):
        return f"<{self.name} (dir)>"


class File:
    # name: str = ""
    # size: int = 0
    # parent: Directory = None

    def __init__(self, name: str = "/", size: int = 0, parent: Union["Directory", None] = None):
        self.name = name
        self.size = size
        self.parent = parent

    def __repr__(self):
        return f"<{self.name} (file, size={self.size})>"

    def distToRoot(self):
        t = self
        c = 0
        while True:
            if t.parent:
                t = t.parent
                c += 1
            else:
                return c


def parse(input_file):
    f = open(input_file)
    x = f.readlines()
    for i in range(len(x)):
        x[i] = x[i].replace("\n", "")
    f.close()
    y = Directory()
    cwd = y
    for i in x[1:]:
        if i == '$ cd ..':
            cwd = cwd.parent
        elif i[0:4] == "$ cd":
            cwd = cwd.cd(i.split(" ")[2])
        elif i[0:3] == "dir":
            cwd.addDirectory(Directory(i.split(" ")[1], cwd))
        elif i == "$ ls":
            pass
        else:
            cwd.addFile(File(i.split(" ")[1], int(i.split(" ")[0])))
    return cwd.root()


def part1(input: Directory):
    cwd = input
    dirs = cwd.recursiveDirSearch()
    out = 0
    if cwd.calculateSize() < 100000:
        out += cwd.calculateSize()
    for i in dirs:
        if i.calculateSize() < 100000:
            out += i.calculateSize()
    return out


def part2(input: Directory):
    cwd = input
    dirs = cwd.recursiveDirSearch()
    out = 0
    freeSpace = 70000000 - cwd.calculateSize()
    neededSpace = 30000000 - freeSpace
    outs = []
    for i in dirs:
        if i.calculateSize() > neededSpace:
            outs.append(i.calculateSize())
    return min(outs)


# x = parse("input.txt")
# x.printTree()
# print(x.recursiveDirSearch())
