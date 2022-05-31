#import tkinter as tk
#import tkinter as ttk

from cgi import test
from itertools import count
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import mysql.connector

height = 450
width = 800

dbConfig = {
  'user': 'maybe',
  'password': 'butter',
  'host': 'localhost',
  'database': 'crud',
  'raise_on_warnings': True
}
# mydb = connection.MySQLConnection(user="maybe", password="butter", host="localhost", database="crud")
# user="root", password="huli"


def connection():
    global dbconn, cursor
    try:
      dbconn  = mysql.connector.connect(**dbConfig)

      sql_select_Query = "select * from articulos"
      cursor = dbconn.cursor()
      cursor.execute(sql_select_Query)

      records = cursor.fetchall()
      print("Total de articulos: ", cursor.rowcount)

    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)

def close():
        if dbconn.is_connected():
            dbconn.close()
            cursor.close()
            print("MySQL connection is closed")

root = Tk()
root.title("HOLLY HULI")

def func1():
    connection()
    frame2.place(relwidth=1, relheight=1)
    label1.place(relheight=0.2, relwidth=1)
    label2.place(rely=0.15, relx=0.04, relheight=0.18, relwidth=0.36)
    data1.place(rely=0.28, relx=0.06, relheight=0.07, relwidth=0.35)
    label3.place(rely=0.38, relx=0.04, relheight=0.07, relwidth=0.4)
    data2.place(rely=0.46, relx=0.06, relheight=0.07, relwidth=0.35)
    label4.place(rely=0.15, relx=0.52, relheight=0.18, relwidth=0.36)
    data3.place(rely=0.28, relx=0.56, relheight=0.07, relwidth=0.36)
    label5.place(rely=0.38, relx=0.52, relheight=0.07, relwidth=0.45)
    data4.place(rely=0.46, relx=0.56, relheight=0.07, relwidth=0.36)
    boton3.place(rely=0.68, relx=0.56, relheight=0.14, relwidth=0.2)
    nope.place(rely=0.68, relx=0.21, relheight=0.14, relwidth=0.2)

def func2():
    connection()
    frame3.place(relwidth=1, relheight=1)
    label6.place(relheight=0.18, relwidth=1)
    data5.place(rely=0.18, relx=0.13, relheight=0.06, relwidth=0.6)
    boton4.place(rely=0.45, relx=0.75, relheight=0.13, relwidth=0.2)
    boton5.place(rely=0.65, relx=0.75, relheight=0.13, relwidth=0.2)
    table.place(rely=0.3, relx=0.04, relheight=0.63, relwidth=0.65)
    buscar.place(rely=0.18, relx=0.74, relheight=0.06, relwidth=0.12)

def func3():
    connection()
    frame1.place(relwidth=1, relheight=1)
    busqueda.place(rely=0.07, relx=0.04, relheight=0.06, relwidth=0.6)
    search.place(rely=0.07, relx=0.65, relheight=0.06, relwidth=0.12)  
    table1.place(rely=0.3, relx=0.04, relheight=0.65, relwidth=0.75)
    titulo.place(rely=0.18, relx=0.08, relheight=0.08, relwidth=0.6)
    guardar.place(rely=0.5, relx=0.82, relheight=0.1, relwidth=0.15)
    salir.place(rely=0.7, relx=0.82, relheight=0.1, relwidth=0.15)

def salir1():
    frame3.place_forget()
    data5.delete(0, 100)
    close()
    frame.place()

def func5():
    nombre = str(data1.get())
    desc = str(data2.get())
    contenido = str(data4.get())
    precio = str(data3.get())

    if(nombre=="" or desc=="" or contenido=="" or precio==""):
      messagebox.showwarning("INCORRECTO","Todos los campos deben ser llenados")
    else:
      cursor.execute("INSERT INTO `articulos` (nombre, detalle, precio, contenido) VALUES(%s, %s, %s, %s)",
                (nombre, desc, precio, contenido))
      cursor.execute("commit")

    frame2.place_forget()
    data1.delete(0, 100)
    data2.delete(0, 100)
    data3.delete(0, 100)
    data4.delete(0, 100)
    id_pop.delete(0, 100)
    close()
    frame.place()
    messagebox.showinfo("GUARDADO","Se guardo el registro\t")

def salir2():
    frame2.place_forget()
    data1.delete(0, 100)
    data2.delete(0, 100)
    data3.delete(0, 100)
    data4.delete(0, 100)
    id_pop.delete(0, 100)
    close()
    frame.place()

def func7():
    frame3.place_forget()

    #guardar el campo antes de vaciarlo

    data5.delete(0, 100)
    close()
    frame.place()
    messagebox.showinfo("GUARDADO","Se ha guadado los cambios\t")

def inicio_save():
    frame1.place_forget()

    
    selecteditem = int(id.get())################
    cursor.execute("DELETE FROM `articulos` WHERE `id` = %d" % selecteditem)


    busqueda.delete(0,100)
    close()
    frame.place()
    messagebox.showinfo("GUARDADO","Se ah borrado la fila\t")

def inicio_can():
    frame1.place_forget()
    busqueda.delete(0,100)
    close()
    frame.place()

#### This is the main frame ####

canvas = Canvas(root, height=height, width=width)
canvas.pack()

frame = Frame(root, bg="#222831")
frame.place(relwidth=1, relheight=1)

label = Label(frame, text="¿Qué le gustaría hacer?", bg="#222831", fg="gray", font="Ubuntu 20 bold", padx=20, pady=20)
label.place(relheight=0.5, relwidth=1)

boton1 = Button(frame, text="Agregar Productos", bg="#00ADB5", fg="black", font="Raleway 11 bold", padx=7, pady=7, activebackground="black",\
                    activeforeground="white", relief="flat", highlightcolor="#112D4E", command=func1)
boton1.place(rely=0.6, relx=0.12, relheight=0.15, relwidth=0.22)

boton2 = Button(frame, text="Editar Productos", bg="#00ADB5", fg="black", font="Raleway 11 bold", padx=7, pady=7, activebackground="black",\
                    activeforeground="white", relief="flat", highlightcolor="#112D4E", command=func2)
boton2.place(rely=0.6, relx=0.39, relheight=0.15, relwidth=0.22)

boton2 = Button(frame, text="Eliminar Fila", bg="#00ADB5", fg="black", font="Raleway 11 bold", padx=7, pady=7, activebackground="black",\
                    activeforeground="white", relief="flat", highlightcolor="#112D4E", command=func3)
boton2.place(rely=0.6, relx=0.66, relheight=0.15, relwidth=0.22)

#### This is the secund frame ####

frame2 = Frame(root, bg="#222831")
label1 = Label(frame2, text="Ingrese los datos necesarios", bg="#222831", fg="gray", font="Ubuntu 18 bold", padx=20, pady=20)
label2 = Label(frame2, text="Ingrese el nombre del producto:", bg="#222831", fg="gray", font="Poppins 11 bold", padx=20, pady=20)
data1 = Entry(frame2, bg="#0D7377", font="Poppins 11 bold", fg="white", relief="flat", justify="center")
label3 = Label(frame2, text="Ingrese la descripcion del producto:", bg="#222831", fg="gray", font="Poppins 11 bold", padx=20, pady=20)
data2 = Entry(frame2, bg="#0D7377", font="Poppins 11 bold", fg="white", relief="flat", justify="center")
label4 = Label(frame2, text="Ingrese el precio producto:", bg="#222831", fg="gray", font="Poppins 11 bold", padx=20, pady=20)
data3 = Entry(frame2, bg="#0D7377", font="Poppins 11 bold", fg="white", relief="flat", justify="center")
label5 = Label(frame2, text="Cantidad de contenido del producto:", bg="#222831", fg="gray", font="Poppins 11 bold", padx=20, pady=20)
data4 = Entry(frame2, bg="#0D7377", font="Poppins 11 bold", fg="white", relief="flat", justify="center")
boton3 = Button(frame2, text="GUARDAR", bg="#00ADB5", fg="black", font="Raleway 12 bold", padx=7, pady=7,activebackground="black", \
                   activeforeground="white", relief="flat", highlightcolor="#112D4E", command=func5)
nope = Button(frame2, text="CANCELAR", bg="#EA5455", fg="white", font="Raleway 12 bold", padx=7, pady=7,activebackground="gray", \
                   activeforeground="black", relief="flat", highlightcolor="#112D4E", command=salir2)
label_pop = Label(frame2, text="Ingrese el nummero ID:", bg="#222831", fg="gray", font="Poppins 11 bold", padx=20, pady=20)
id_pop = Entry(frame2, bg="#0D7377", font="Poppins 11 bold", fg="white", relief="flat", justify="center")


#### This is the third frame ####

frame3 = Frame(root, bg="#222831")
label6 = Label(frame3, text="Edita los Productos", bg="#222831", fg="gray", font="Ubuntu 18 bold", padx=20, pady=20)
data5 = Entry(frame3, bg="#0D7377", font="Poppins 13 bold", fg="white", relief="flat", justify="left")
table = ttk.Treeview(frame3)
boton4 = Button(frame3, text="GUARDAR", bg="#00ADB5", fg="black", font="Raleway 12 bold", padx=7, pady=7, activebackground="black", \
                   activeforeground="white", relief="flat", highlightcolor="#112D4E", command=func7)
boton5 = Button(frame3, text="CANCELAR", bg="#EA5455", fg="white", font="Raleway 12 bold", padx=7, pady=7,activebackground="gray", \
                   activeforeground="black", relief="flat", highlightcolor="#112D4E", command=salir1)
buscar = Button(frame3, text="Buscar", bg="#205375", fg="#EFEFEF", font="Raleway 12 bold", padx=7, pady=7, activebackground="black", \
                   activeforeground="white", relief="flat", highlightcolor="#112D4E") 

#### This is the forth frame ####

frame1 = Frame(root, bg="#222831")
titulo = Label(frame1, text="Selecciona la fila que quieres borrar y dale al boton aceptar", bg="#222831", fg="gray", font="Ubuntu 12 bold", padx=20, pady=20)
busqueda = Entry(frame1, bg="#0D7377", font="Poppins 13 bold", fg="white", relief="flat", justify="left")
table1 = ttk.Treeview(frame1)
guardar = Button(frame1, text="ACEPTAR", bg="#00ADB5", fg="black", font="Raleway 12 bold", padx=7, pady=7, activebackground="black", \
                   activeforeground="white", relief="flat", highlightcolor="#112D4E", command=inicio_save)
salir = Button(frame1, text="CANCELAR", bg="#EA5455", fg="white", font="Raleway 12 bold", padx=7, pady=7,activebackground="gray", \
                   activeforeground="black", relief="flat", highlightcolor="#112D4E", command=inicio_can)
search = Button(frame1, text="Buscar", bg="#205375", fg="#EFEFEF", font="Raleway 12 bold", padx=7, pady=7, activebackground="black", \
                   activeforeground="white", relief="flat", highlightcolor="#112D4E")     
table1['columns'] = ("Id", "Nombre", "Descripcion", "Precio", "Contenido")

table1.column("#0", width=0, stretch="NO")
table1.column("Id", width=40, minwidth=40, anchor="center", stretch="NO")
table1.column("Nombre", width=125, minwidth=125, anchor="w", stretch="NO")
table1.column("Descripcion", width=250, minwidth=250, anchor="w", stretch="NO")
table1.column("Precio", width=87, minwidth=87, anchor="center", stretch="NO")
table1.column("Contenido", width=100, minwidth=100, anchor="w", stretch="NO")

table1.heading("#0", text="", anchor="w")
table1.heading("Id", text="Id", anchor="center")
table1.heading("Nombre", text="Nombre", anchor="center")
table1.heading("Descripcion", text="Descripcion", anchor="center")
table1.heading("Precio", text="Precio", anchor="center")
table1.heading("Contenido", text="Contenido", anchor="center")

#records = cursor.fetchall()
#print("Total de articulos: ", cursor.rowcount)

count = 1
while count <= cursor.rowcount():
  table1.insert(parent="", index="end", iid=0, text="1", values=())
  count = count + 1

table1.insert(parent="", index="end", iid=count, text="1", values=(1, "Gatorade", "Bebida Energetica", 27, "400ml"))

root.mainloop()