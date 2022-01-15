from tkinter import *
import tkinter as tk
from tkinter import ttk

from scrapereddit import * 

first = Tk()
first.geometry("500x500")
first.title("Reddit Image Scraping")

running = False

# subreddit
labelSub = tk.Label(first, text="Enter subreddit name: ")
labelSub.grid(row=0,column=0)

subInput = tk.Entry(first)
subInput.grid(row=0,column=1)

# num images
labelImageNum = tk.Label(first, text="Number of Images to Retrieve")
labelImageNum.grid(row=1,column=0)

numInput = tk.Entry(first)
numInput.grid(row=1, column=1)

# min width
sortLabel = tk.Label(first, text="Eliminate collected images with: ")
labelWidth = tk.Label(first, text="Minimum Width: ")
sortLabel.grid(row=3, column=0)
labelWidth.grid(row=4,column=0)

widthInput = tk.Entry(first)
widthInput.grid(row=4,column=1)

# min hieght

labelHeight = tk.Label(first, text="Minimum Hieght:")
labelHeight.grid(row=5,column=0)

heightInput = tk.Entry(first)
heightInput.grid(row=5,column=1)

# save path
labelpath = tk.Label(first, text="Folder to save to (path)")
labelpath.grid(row=6, column=0)

savepath = tk.Entry(first)
savepath.grid(row=6, column=1)

# def check_running():
#     if running == True:
#         statuslabel.config(text="Status: Fetching images...")
#     else:
#         statuslabel.config(text="Status: Done")

def getRequestInfo():
    subreddit = subInput.get()
    numImages = int(numInput.get())
    width = int(widthInput.get())
    height = int(heightInput.get())
    path = savepath.get()
    scrapeReddit(subreddit, numImages, width, height, path)

#input button
btnIn = tk.Button(first, text="Scrape!", command=getRequestInfo)
btnIn.grid(row=7, column=1)

# statuslabel = Label(first, text="Status: ")
# statuslabel.grid(row=8, column=0)

first.mainloop()