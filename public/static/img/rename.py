import os

n = 0
for filename in os.listdir('.'):
    if not filename.endswith('jpg'):
        continue
    oldname= '.' + os.sep + filename
    tempname = '.' + os.sep + str(n+1) + '_temp.jpg'
    os.rename(oldname, tempname)
    n += 1

n = 0
for filename in os.listdir('.'):
    if not filename.endswith('jpg'):
        continue
    oldname= '.' + os.sep + filename
    newname= '.' + os.sep + str(n+1) + '.jpg'
    os.rename(oldname, newname)
    n += 1
