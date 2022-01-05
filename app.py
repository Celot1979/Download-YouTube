from pytube import YouTube
import os
from tkinter import *
import tkinter


root = Tk()
root.geometry("800x400")
root.title("YOUTUBE video downloads")
#Direccion =StringVar()
videourl = StringVar()
#Directorio =StringVar()
path = StringVar()
Licencia= Label(root, text ="Program created by Daniel Gil",background="azure",font=("Monaco",12))
Licencia.place(x=280, y=380)

def downloadYouTube(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

Texto_Etiqueta= Label(root, text ="Copy and paste the link of the video you want to download",background="azure",font=("Monaco",12))
Texto_Etiqueta.place(x=200, y=80)

Casilla_enlace= Entry(root, width=50, textvariable=videourl, background="azure")
Casilla_enlace.place(x=150, y= 120)

Texto_Directorio= Label(root, text ="Select the directories where you want to save the video",background="azure",font=("Monaco",12))
Texto_Directorio.place(x=200, y=180)

Casilla_Directorio= Entry(root, width=50, textvariable=path, background="azure")
Casilla_Directorio.place(x=150, y= 220)

conectar = Button(root, text="Download", width= 8, background="blue", activebackground="blue", command=lambda: downloadYouTube(videourl.get(),path.get()))
conectar.place(x=350, y=260)

root.mainloop()

"""def downloadYouTube(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

downloadYouTube('https://www.youtube.com/watch?v=zNyYDHCg06c', '/Users/danielgil/Desktop/Videos')"""








