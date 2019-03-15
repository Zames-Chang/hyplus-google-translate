from main import transcribe_file
import os
import sys
import shutil as s
path = sys.argv[1]
files = os.listdir(path)
timer = int(sys.argv[2])
lang = sys.argv[3]
for myfile in files:
    print(path+myfile)
    transcribe_file(path+myfile,timer,lang,True)
    s.copyfile("output.txt","../Desktop/hyplus-out/{}".format(myfile[:-4]+"txt"))
