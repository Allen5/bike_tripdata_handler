from asyncore import read
import csv

import urllib.request as req

with open('./datas/files.csv', 'r') as datas:
    reader = csv.reader(datas)
    for item in reader:
        if "http" not in item[1]:
            continue
        print("downloading: " + item[1])
        req.urlretrieve(item[1], "./datas/" + item[0])
        print("download complete: " + item[1])