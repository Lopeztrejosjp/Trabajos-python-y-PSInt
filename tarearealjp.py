from tkinter import *

def dibujar_corazon_compacto_frames():
    root = Tk()
    root.title("Corazón Pixel Art Compacto (Frames)")
    root.resizable(False, False)
    root.configure(bg="black") 

    PX_SIZE = 20
    ROJO = "red"
    
    Frame(root, width=PX_SIZE, height=PX_SIZE, bg=ROJO).grid(row=1, column=3)
    Frame(root, width=PX_SIZE, height=PX_SIZE, bg=ROJO).grid(row=1, column=5)

    for col in range(1, 8):
        Frame(root, width=PX_SIZE, height=PX_SIZE, bg=ROJO).grid(row=2, column=col)
    for fila in range(3, 7):
        for col in range(0, 9):
            Frame(root, width=PX_SIZE, height=PX_SIZE, bg=ROJO).grid(row=fila, column=col)
    
    for col in range(1, 8):
        Frame(root, width=PX_SIZE, height=PX_SIZE, bg=ROJO).grid(row=7, column=col)

    for col in range(2, 7):
        Frame(root, width=PX_SIZE, height=PX_SIZE, bg=ROJO).grid(row=8, column=col)

    for col in range(3, 6):
        Frame(root, width=PX_SIZE, height=PX_SIZE, bg=ROJO).grid(row=9, column=col)

    Frame(root, width=PX_SIZE, height=PX_SIZE, bg=ROJO).grid(row=10, column=4)


    root.mainloop()

dibujar_corazon_compacto_frames()