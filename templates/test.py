import __init__
import pandas as pd
import os
from tkinter import filedialog

os.environ['TCL_LIBRARY'] = r"C:\Users\Família\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Família\AppData\Local\Programs\Python\Python313\tcl\tk8.6"

arquivo = filedialog.askopenfilename(
    title= "Selecione um arquivo"
)

print(arquivo)