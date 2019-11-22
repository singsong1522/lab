import glob
import os

paths = 'c:/windows'
print(paths)
allDirs = os.path.join(paths, '*/*.dll')
print(allDirs)

for dll in glob.glob(allDirs):
    print(dll)