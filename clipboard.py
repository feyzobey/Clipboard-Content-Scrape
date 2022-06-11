from tkinter import Tk
import git

try:
    # in which directory you want to clone, type its path into Git() method   
    git.Git("../").clone(Tk().clipboard_get())
except:
    print("Error: Could not clone repository")
finally:
    print("Clipboard: " + Tk().clipboard_get())