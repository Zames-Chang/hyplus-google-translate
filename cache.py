import os, sys
import moviepy.editor as mp
path1 = "G:/text/1114/"
file1 = os.listdir( path1 )
print(file1)
path2 = "G:/text/1114_1800_weiting/"
file2 = os.listdir( path2 )

out1 = "G:/out/1114/"
out2 = "G:/out/1114_next/"
for file in file1:
    print(path1+file)
    clip = mp.VideoFileClip(path1+file)
    clip.audio.write_audiofile(out1+file[:-4]+".mp3")
for file in file2:
    clip = mp.VideoFileClip(path2+file)
    clip.audio.write_audiofile(out2+file[:-4]+".mp3")