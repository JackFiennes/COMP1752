import pygame
import tkinter
from tkinter.filedialog import askdirectory
import os

player = tkinter.Tk
player.title("Video Player")
player.geometry("310x325")

var = tkinter.StringVar()
var.set("Select video to play")

os chdir(askdirectory())
songlist = os.listdir()

playing = tkinter.Listbox(player, font = "Helvetica 12 bold", width=28, bg="black", fg = "white", selectmode=tkinter.SINGLE)

for item in songlist:
    playing.insert(0, item)

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playing.get(tkinter.ACTIVE))
    name = playing

def pause(): 
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()
