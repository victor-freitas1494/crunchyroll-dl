#!/bin/python3

import os

retorno = False
files = []

def SearchFFmpeg():
    global retorno
    BinFile = os.listdir("/bin")
    for bin in range(len(BinFile)):
        if BinFile[bin].count("ffmpeg") == True:
            retorno = True


def SearchFiles():
    global files
    tmpfile = os.listdir("./temp/")
    for ifile in range(len(tmpfile)):
        if tmpfile[ifile].count(".mp4") == True or tmpfile[ifile].count(".ptBR.ass") == True:
            files.append("\\ ".join(tmpfile[ifile].split()))
    files.sort()   

def ConvertFFmpeg():
    global files
    os.system(f"ffmpeg -i temp/{files[0]} -vf ass=temp/{files[1]} -s 1280x720 -sws_flags lanczos -c:v libx265 -pix_fmt yuv420p10le -preset slow -x265-params crf=22:profile=main10 -c:a aac -b:a 128k {files[0]}.mkv")

if __name__ == "__main__":
    SearchFFmpeg()
    if retorno == False:
        print("estar faltando ffmpeg")
        os.system("sudo apt-get install ffmpeg -y")
    else:
        SearchFiles()
        ConvertFFmpeg()
    pass