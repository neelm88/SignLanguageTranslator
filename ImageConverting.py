import glob
import PIL
import os
from PIL import Image
LETTER = 'a'
for filepath in glob.iglob(LETTER + '/*.jpg'):
    img = Image.open(filepath)
    img = img.resize((64, 64), PIL.Image.ANTIALIAS)
    i = filepath.index("\\")
    endfilepath = filepath[0:i] + "2\\" + filepath[i+1:len(filepath)]
    img.save(endfilepath)
for filepath in glob.iglob(LETTER + '/*.jpeg'):
    img = Image.open(filepath)
    img = img.resize((64, 64), PIL.Image.ANTIALIAS)
    i = filepath.index("\\")
    endfilepath = filepath[0:i] + "2\\" + filepath[i+1:len(filepath)]
    img.save(endfilepath)
