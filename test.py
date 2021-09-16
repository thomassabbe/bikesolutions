from library2 import detect
from os import walk


#Second step: gather current object positions and Time.
conf = 0.4
nms = 0.5
for (dirpath, dirnames, filenames) in walk('img'):
    list = filenames
    break
for name in list:
    imagepath = 'img/'+name
    try:
        detect(conf, nms, imagepath)
    except Exception:
        print(Exception)
