from tkinter import *
from rosstat import main  as get_rosstat
from showdata import main  as get_showdata
from check_dir import check_dirs


dirnames = [
    'chromedriver',
    'rosstat',
    'showdata'
]

check_dirs(dirnames)

def on_stop():
   global running
   running = False


root = Tk()
root.title('Reports parser')
root.geometry('280x240')

rosstat_btn = Button(text="Get rosstat report", 
            width=15, height=3, command=get_rosstat)
rosstat_btn.pack()

showdata_btn = Button(text="Get showdata report", 
            width=15, height=3, command=get_showdata)
showdata_btn.pack()


# Define a function to stop the loop


root.mainloop()