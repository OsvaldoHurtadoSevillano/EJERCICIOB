from tkinter import*
from PIL import ImageTk,Image
root= Tk()

ventanaprincipal=Frame(root,bg="#ffc400")
ventanaprincipal.grid()
contras=StringVar()
confirmo=StringVar()


def contraseñas():
    if contras.get()==confirmo.get():
        print("SESION INICIADA")
        ventanaprincipal.config(bg="#42ab49")
        

        
    else:
        print("CONTRASEÑA INCORRECTA")
        ventanaprincipal.config(bg="red")


img=Image.open("redbull.ico")
imagen=img.resize((100,65))
imag=ImageTk.PhotoImage(imagen)
mititulo=Label(ventanaprincipal,image=imag)
mititulo.grid(row=1,column=1,padx=10,pady=20,columnspan=2,rowspan=2)


titulo=Label(ventanaprincipal,text="LOG IN",font=("roboto",20))
titulo.grid(row=3,column=1,columnspan=2)


nombre=Label(ventanaprincipal,text="NOMBRE:",
             font=("roboto",15)).grid(row=4,column=1,padx=30,pady=30)
textonombre=Entry(ventanaprincipal,font=("roboto",15)).grid(row=4,column=2,padx=30,pady=15)


contraseña=Label(ventanaprincipal,text="CONTRASEÑA:",
                 font=("roboto",15)).grid(row=5,column=1,padx=15,pady=10)
textocontra=Entry(ventanaprincipal,
                  font=("roboto",15),textvariable=contras).grid(row=5,column=2,padx=30,pady=15)


confirmar=Label(ventanaprincipal,text="CONFIRMAR CONTRASEÑA:",
                font=("roboto",15)).grid(row=6,column=1,padx=15,pady=30)
textoconfir=Entry(ventanaprincipal,
                  font=("roboto",15),textvariable=confirmo).grid(row=6,column=2,padx=30,pady=15)


casillahombre=IntVar()
hombre=Checkbutton(ventanaprincipal, text="HOMBRE",variable=casillahombre,font=("roboto",10))
hombre.grid(row=7,column=0)

casillamujer=IntVar()
mujer=Checkbutton(ventanaprincipal, text="MUJER",variable=casillamujer,font=("roboto",10))
mujer.grid(row=7,column=1)

control3=IntVar()
aceptar=Checkbutton(ventanaprincipal, text="ACEPTO TERMINOS",variable=control3,font=("roboto",10))
aceptar.grid(row=8,column=3)
INICIAR=Button(ventanaprincipal,text="INICIAR",command=contraseñas,width=20,height=2).grid(row=12,column=1,columnspan=2)


root.mainloop()