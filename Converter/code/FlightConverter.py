import tkinter as tk
import pyperclip
from tkinter import ttk

# logic
def Val_input():
    valinput = entry_int.get()
    return valinput

def Convert_ftm():
    ftm_input = Val_input()
    m_output = (ftm_input, 'feet', round(ftm_input / 3.28, 2), "meteres")
    output_string.set(m_output)
    pyperclip.copy(output_string)
    print(pyperclip.paste())
    
def Convert_nmkm():
    nm_input = Val_input()
    km_output = (nm_input,'Nm',round(nm_input * 1.852, 2),'Km')
    output_string.set(km_output)
    
def Convert_gallb():
    gal_input = Val_input()
    lb_output = round(gal_input * 6.02, 2)
    print_output = (gal_input, 'gal', lb_output, 'lb')
    output_string.set(print_output)
    
# window
window = tk.Tk()
window.title('Converter | pfrmn')
window.geometry('480x480')

# header
title_label = ttk.Label(master = window, text = 'Flight convert', font = 'Ubuntu 18 bold')
dnuirf_label = ttk.Label(master = window, text = 'do not use in real flight!', font = 'Ubuntu 10')

title_label.pack()
dnuirf_label.pack()

# input field

input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable=entry_int)
button = ttk.Button(master = input_frame, text = 'ft -> m', command= Convert_ftm)
entry.pack()
button.pack()
input_frame.pack()

input_frame2 = ttk.Frame(master = window)
entry_int2 = tk.IntVar()
button = ttk.Button(master = input_frame2, text = 'Nm -> Km', command= Convert_nmkm)
entry.pack()
button.pack()
input_frame2.pack()

input_framegal = ttk.Frame(master = window)
entry_intgal = tk.IntVar()
button = ttk.Button(master = input_framegal, text = 'gal -> lb', command= Convert_gallb)
entry.pack()
button.pack()
input_framegal.pack()

# output
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window,
    text = "Wynik",
    font = 'Ubuntu 20',
    textvariable= output_string)
output_label.pack()

#run
window.mainloop()