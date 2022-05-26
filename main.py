import tkinter as tk
import MySQL.connector
#mydb = connection.MySQLConnection(user="maybe", password="ydI4I5Bg", host="localhost", database="proyecto")

height = 450
width = 800

root = tk.Tk()
root.title("HOLLY HULI")

def func2():
    frame2.place(relwidth=1, relheight=1)
    label1.place(relheight=0.2, relwidth=1)
    label2.place(rely=0.15, relx=0.04, relheight=0.18, relwidth=0.36)
    data1.place(rely=0.28, relx=0.06, relheight=0.07, relwidth=0.35)
    label3.place(rely=0.38, relx=0.04, relheight=0.07, relwidth=0.36)
    data2.place(rely=0.46, relx=0.06, relheight=0.07, relwidth=0.35)
    label4.place(rely=0.15, relx=0.52, relheight=0.18, relwidth=0.36)
    data3.place(rely=0.28, relx=0.56, relheight=0.07, relwidth=0.36)
    label5.place(rely=0.38, relx=0.53, relheight=0.07, relwidth=0.35)
    data4.place(rely=0.46, relx=0.56, relheight=0.07, relwidth=0.36)
    boton3.place(rely=0.68, relx=0.56, relheight=0.14, relwidth=0.2)
    nope.place(rely=0.68, relx=0.21, relheight=0.14, relwidth=0.2)

def func3():
    frame3.place(relwidth=1, relheight=1)
    label6.place(relheight=0.18, relwidth=1)
    data5.place(rely=0.18, relx=0.15, relheight=0.06, relwidth=0.7)
    boton6.place(rely=0.46, relx=0.75, relheight=0.13, relwidth=0.2)
    boton4.place(rely=0.64, relx=0.75, relheight=0.13, relwidth=0.2)
    boton5.place(rely=0.82, relx=0.75, relheight=0.13, relwidth=0.2)

def func4():
    frame3.place_forget()
    data5.delete(0, 100)
    frame.place()

def func5():
    frame2.place_forget()

    #tengo que poner que guarde loque tiene los campos y luego que los vacie

    data1.delete(0, 100)
    data2.delete(0, 100)
    data3.delete(0, 100)
    data4.delete(0, 100)
    frame.place()

def func6():
    frame2.place_forget()
    data1.delete(0, 100)
    data2.delete(0, 100)
    data3.delete(0, 100)
    data4.delete(0, 100)
    frame.place()

def func7():
    frame3.place_forget()

    #guardar el campo antes de vaciarlo

    data5.delete(0, 100)
    frame.place()

#### This is the main frame ####

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

frame = tk.Frame(root, bg="#222831")
frame.place(relwidth=1, relheight=1)

label = tk.Label(frame, text="¿Qué le gustaría hacer?", bg="#222831", fg="gray", font="Ubuntu 20 bold", padx=20, pady=20)
label.place(relheight=0.5, relwidth=1)

boton1 = tk.Button(frame, text="Agregar Productos", bg="#00ADB5", fg="black", font="Raleway 12 bold", padx=7, pady=7, activebackground="black",\
                    activeforeground="white", relief="flat", highlightcolor="#112D4E", command=func2)
boton1.place(rely=0.6, relx=0.21, relheight=0.15, relwidth=0.22)


boton2 = tk.Button(frame, text="Editar Productos", bg="#00ADB5", fg="black", font="Raleway 12 bold", padx=7, pady=7, activebackground="black",\
                    activeforeground="white", relief="flat", highlightcolor="#112D4E", command=func3)
boton2.place(rely=0.6, relx=0.56, relheight=0.15, relwidth=0.22)

#### This is the first frame  ####

frame1 = tk.Frame(root, bg="#222831")
label0 = tk.Label(frame1, text="Seleccione lo que le gustaria comprar", bg="#222831", fg="gray", font="Ubuntu 18 bold", padx=20, pady=20)
yes = tk.Button(frame1, text="COMPRAR", bg="#00ADB5", fg="black", font="Raleway 12 bold", padx=7, pady=7, activebackground="black", \
                activeforeground="white", relief="flat", highlightcolor="#112D4E", command=func4)

#### This is the secund frame ####

frame2 = tk.Frame(root, bg="#222831")
label1 = tk.Label(frame2, text="Ingrese los datos necesarios", bg="#222831", fg="gray", font="Ubuntu 18 bold", padx=20, pady=20)
label2 = tk.Label(frame2, text="Ingrese el nombre del producto:", bg="#222831", fg="gray", font="Poppins 13 bold", padx=20, pady=20)
data1 = tk.Entry(frame2, bg="#0D7377", font="Poppins 13 bold", fg="white", relief="flat", justify="center")
label3 = tk.Label(frame2, text="Ingrese la cantidad de inventario:", bg="#222831", fg="gray", font="Poppins 13 bold", padx=20, pady=20)
data2 = tk.Entry(frame2, bg="#0D7377", font="Poppins 13 bold", fg="white", relief="flat", justify="center")
label4 = tk.Label(frame2, text="Ingrese el precio producto:", bg="#222831", fg="gray", font="Poppins 13 bold", padx=20, pady=20)
data3 = tk.Entry(frame2, bg="#0D7377", font="Poppins 13 bold", fg="white", relief="flat", justify="center")
label5 = tk.Label(frame2, text="Producto NETO del producto:", bg="#222831", fg="gray", font="Poppins 13 bold", padx=20, pady=20)
data4 = tk.Entry(frame2, bg="#0D7377", font="Poppins 13 bold", fg="white", relief="flat", justify="center")
boton3 = tk.Button(frame2, text="GUARDAR", bg="#00ADB5", fg="black", font="Raleway 12 bold", padx=7, pady=7,activebackground="black", \
                   activeforeground="white", relief="flat", highlightcolor="#112D4E", command=func5)
nope = tk.Button(frame2, text="CANCELAR", bg="#EA5455", fg="white", font="Raleway 12 bold", padx=7, pady=7,activebackground="gray", \
                   activeforeground="black", relief="flat", highlightcolor="#112D4E", command=func6)

#### This is the secund frame ####

frame3 = tk.Frame(root, bg="#222831")
label6 = tk.Label(frame3, text="Seleccione el producto que va eliminar", bg="#222831", fg="gray", font="Ubuntu 18 bold", padx=20, pady=20)
data5 = tk.Entry(frame3, bg="#0D7377", font="Poppins 13 bold", fg="white", relief="flat", justify="left")
boton6 = tk.Button(frame3, text="EDITAR", bg="#00ADB5", fg="black", font="Raleway 12 bold", padx=7, pady=7, activebackground="black", \
                   activeforeground="white", relief="flat", highlightcolor="#112D4E")
boton4 = tk.Button(frame3, text="GUARDAR", bg="#00ADB5", fg="black", font="Raleway 12 bold", padx=7, pady=7, activebackground="black", \
                   activeforeground="white", relief="flat", highlightcolor="#112D4E", command=func7)
boton5 = tk.Button(frame3, text="CANCELAR", bg="#EA5455", fg="white", font="Raleway 12 bold", padx=7, pady=7,activebackground="gray", \
                   activeforeground="black", relief="flat", highlightcolor="#112D4E", command=func4)

root.mainloop()
