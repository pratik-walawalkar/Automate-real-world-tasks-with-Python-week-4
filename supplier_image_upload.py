
#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"

folder = "/home/student-04-e281aa9955e8/supplier-data/images/"
def upload():
    for item in os.listdir(folder):
        f, e = os.path.splitext(item)

        if e == ".jpeg":
            with open(folder+item, 'rb') as opened:
                r = requests.post(url, files={'file': opened})
upload()

