from tkinter import Tk
import git
git.Git().clone(Tk().clipboard_get())
print("Clipboard: " + Tk().clipboard_get()) # Prints the clipboard contents
