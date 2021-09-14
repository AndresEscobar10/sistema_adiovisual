import tkinter

def ventana(texto):
    from tkinter import mainloop,Label,Tk
    ## Crea la ventana para la aplicación
    root = Tk()
    while True:
        ## Establece un título y un tamaño para la ventana
        root.title('Actividad Del Microfono')
        root.geometry('200x200')
        ## Crea una etiqueta.
        Label(root, text='Esta es la ventana principal').pack(pady=10)
        Label(root, text=texto).pack(pady=10)
        
        root.wm_attributes("-topmost", 1)
        root.mainloop()  
        return 


 
