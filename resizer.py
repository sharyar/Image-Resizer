# Author: Sharyar Memon
# Project: Multi-Image Resizer in Python with a GUI
# Date Started: December 7, 2019
# Editor: Atom

# Import required modules
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image
import glob, os

# Define variables that will be used throught the program

sizes = list()
source_folder = ''
dest_folder = ''



# Main function that resizes Images
def resizer_fun(sizes, source_folder, dest_folder):
    os.chdir(source_folder)
    for infile in glob.glob('*.jpg'):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)

        width, height = im.size

        for value in sizes:
            if width > height:
                width_n = value
                height_n = int(value/width * height)

            else:
                height_n = value
                width_n = int(value/height * width)

            size_n = (width_n, height_n)

            im_s = im.resize(size_n, Image.ANTIALIAS)

            os.chdir(dest_folder)
            im_s.save(file+'resized'+str(size_n[0]) + ext, 'jpeg')

        os.chdir(source_folder)
        



# Folder Selection Functions for source and destination

def select_source():
    global source_folder
    source_folder = filedialog.askdirectory(initialdir = '/', title = 'Please select the directory you would like to use as the source of your images')

def select_dest():
    global dest_folder
    dest_folder = filedialog.askdirectory(initialdir = '/', title = 'Please select the directory you would like your files to be save to')

# Get Size function for get size button. It takes the Stringvar (size_var) and converts it to a list of integers. Its assigned to a button once the user has input their info.

def get_sizes(size_var):
    global sizes
    image_size_str = str(size_var.get())
    sizes = [int(x) for x in image_size_str.strip(' ').split(',')]
    print (sizes)
# Gui for user input
root = Tk()

size_var = StringVar()

# Heading
heading1 = ttk.Label(text = 'Image Resizer Program')
heading1.pack()


# Buttons for source & dest folders

but_source = ttk.Button(root, text = 'Source Folder', command = select_source)
but_source.pack()

but_dest = ttk.Button(root, text = 'Destination Folder', command = select_dest)
but_dest.pack()

size_entry = Entry(root, textvariable = size_var)
size_entry.pack()

but_get_sizes = ttk.Button(root, text = 'Store Sizes', command = lambda: get_sizes(size_var))
but_get_sizes.pack()

but_process = ttk.Button(root, text = 'Process', command = lambda: resizer_fun(sizes, source_folder, dest_folder))
but_process.pack()
# panedwindow = ttk.Panedwindow(root, orient = HORIZONTAL)
# panedwindow.pack(fill = BOTH, expand = True)
# frame1 = ttk.Frame(panedwindow, width = 100, height=300, relief = SUNKEN)
# frame2 = ttk.Frame(panedwindow, width = 100, height=300, relief = SUNKEN)
#
# panedwindow.add(frame1, weight = 1)
# panedwindow.add(frame2, weight = 2)



# initialize Gui
root.mainloop()
