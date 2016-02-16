import os
import array
def FileReplace(filename):
print(filename)
file=open(filename,"rb")
lines=file.readlines()
file.seek(0)
file.close()
os.remove(filename)
newfile=open(filename,'wb')
for line in lines:
strline=line.replace(b'\r\n',b'\n')
newfile.write(strline)
newfile.close()

def DirReplace(dirname):
if os.path.isdir(dirname)==False:
print("%s is not dir " % dirname)
else:
for file in os.listdir(dirname):
filename=dirname + "\\" + file
if os.path.isdir(filename):
DirReplace(filename)
else:
FileReplace(filename)
print("File has changed!")
