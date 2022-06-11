from tkinter import Tk
import git

try:
    git.Git().clone(Tk().clipboard_get())
except:
    print("Error: Could not clone repository")
finally:
    print("Clipboard: " + Tk().clipboard_get())