!/usr/bin/env python3

from PIL import Image
import os
import sys
folder = "/home/student-04-e281aa9955e8/supplier-data/images/"
def reformat():
    for item in os.listdir(folder):
        f, e = os.path.splitext(item)
        if e == ".tiff":
            if os.path.isfile(folder+item):
                #im.convert("RGB")
                im = Image.open(folder+item)
                im.convert("RGB")
                f, e = os.path.splitext(item)
                imResize = im.resize((600,400), Image.ANTIALIAS)
                imResize.save(folder +f+ ".jpeg", quality=90)

reformat()
