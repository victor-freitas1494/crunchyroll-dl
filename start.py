import os


def LsArquivos():
    ffmpeg = os.listdir("/bin/")
    ass = None

    mp4 = None
    ass_convert = None
    mp4_convert = None
    arquivos = os.listdir("./temp/")
    for x in range(len(arquivos)):
        if arquivos[x].count(".mp4") == True:
            mp4 = arquivos[x].split()
            mp4_convert = "\\ ".join(mp4)
            
            pass
        if arquivos[x].count(".ptBR.ass") == True:
            ass = arquivos[x].split()
            ass_convert = "\\ ".join(ass)
            pass
    print(mp4_convert)
    os.system(f"ffmpeg -i temp/{mp4_convert} -vf ass=temp/{ass_convert} -s 1280x720 -sws_flags lanczos -c:v libx265 -pix_fmt yuv420p10le -preset slow -x265-params crf=22:profile=main10 -c:a aac -b:a 128k {mp4_convert}.mkv")
    os.system("rm temp/*")        
    pass

def SearchFFmpeg(bin):
    for i in range(len(bin)):
        if bin[i].count("ffmpeg") == True:
            return True
    


if __name__ == "__main__":
    diruser = os.system("pwd")
    if os.path.isdir("temp/") == False:
        os.mkdir("./temp")
    pass

    if SearchFFmpeg(ffmpeg) == True:
        LsArquivos()
        

    pass