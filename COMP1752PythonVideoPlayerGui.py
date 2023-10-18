from tkinter import *
import datetime
import tkinter as tk 
from tkinter import filedialog

root = tk.Tk()
root.title("Simple Video Player")
root.geometry("800x700x290x10")


frame =tk.frame(root)
frame.pack()

image_icon = PhotoImage(file="VPImage.jpg")
root.iconphoto(False, image_icon)


lower_frame = tk.Frame(root, bg = "#FFFFFF")
lower_frame.pack(fill = "both", side = BOTTOM)

load_btn = tk.Button(root, text = "Browse", bg = "#FFFFFF", font = ("calibri", 12, "bold"), command = load_video)
load_btn.pack(ipadx=12, ipady=4, anchor= tk.NW)

vid_player = TkinterVideo(root, scaled = True)
vid_player.pack(expand = True, fill = "both")

Buttonbackward = PhotoImage(file = "BackwardsButton.jpg")
back = tk.Button(lower_frame, image = Buttonbackward, bd = 0, height = 50, width = 50, command = lambda:skip(-5)).pack(side= LEFT)


