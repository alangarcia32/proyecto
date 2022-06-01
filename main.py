from tkinter import *
from tkinter import messagebox

import tkinter.ttk as ttk
import mysql.connector
import tkinter.messagebox as tkMessageBox
from tkinter.messagebox import showinfo

height = 450
width = 800

dbConfig = {
  'user': 'admin',
  'password': 'rotoplas77',
  'host': 'crud.copdm5l66brq.us-east-1.rds.amazonaws.com',
  'database': 'crud',
  'raise_on_warnings': True
}
# mydb = connection.MySQLConnection(user="maybe", password="butter", host="localhost", database="crud")
# user="root", password="huli"
articulos = []

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

def dbList():
    connection()
    cursor.execute("SELECT * FROM `articulos` ORDER BY `nombre` DESC")
    fetch = cursor.fetchall()
    
    articulos.clear()
    for data in fetch:
        articulos.append((data[0], data[1], data[2], data[3], data[4]))
    print("Successfully read the data from database")
    close()

def tabla():
   
    tree.place(rely=0.3, relx=0.04, relheight=0.65, relwidth=0.75)

    tree.heading('id', text='Id')
    tree.heading('nombre', text='Nombre')
    tree.heading('desc', text='Descripcion')
    tree.heading('precio', text='Precio')
    tree.heading('content', text='Contenido')

    dbList()
    tree.delete(*tree.get_children())
    # add data to the treeview
    for articulo in articulos:
        tree.insert('', 'end', values=articulo)

    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=0, column=0, sticky='nsew')
    tree.place(rely=0.3, relx=0.04, relheight=0.65, relwidth=0.75)

root = Tk()
root.title("HOLLY HULI")

def ventana1():
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

def ventana2():
    tabla()
    frame1.place(relwidth=1, relheight=1)
    busqueda.place(rely=0.07, relx=0.04, relheight=0.06, relwidth=0.6)
    search.place(rely=0.07, relx=0.65, relheight=0.06, relwidth=0.12)  
    titulo.place(rely=0.18, relx=0.04, relheight=0.08, relwidth=0.75)
    borrar.place(rely=0.4, relx=0.81, relheight=0.1, relwidth=0.17)
    editar.place(rely=0.6, relx=0.81, relheight=0.1, relwidth=0.17)
    salir.place(rely=0.8, relx=0.81, relheight=0.1, relwidth=0.17)

def DBguardar():
    nombre = str(data1.get())
    desc = str(data2.get())
    contenido = str(data4.get())
    precio = str(data3.get())

    if(nombre=="" or desc=="" or contenido=="" or precio==""):
      messagebox.showwarning("INCORRECTO","Todos los campos deben ser llenados")
    else:
      connection()
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

def DBedit():
    pop_up.deiconify()
    name.place(rely=0.25, relx=0.04, relheight=0.15, relwidth=0.2)
    detail.place(rely=0.25, relx=0.25, relheight=0.15, relwidth=0.2)
    price.place(rely=0.25, relx=0.5, relheight=0.15, relwidth=0.2)
    neto.place(rely=0.25, relx=0.65, relheight=0.15, relwidth=0.2)
    save.place(rely=0.65, relx=0.2, relheight=0.2, relwidth=0.22)
    exit.place(rely=0.65, relx=0.6, relheight=0.2, relwidth=0.22)

def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        #showinfo(title='Information', message=','.join(record))


def DBdelete():
    if not tree.selection():
        messagebox.showwarning("ERROR", "Favor de seleccionar una fila")
    else:
        result = tkMessageBox.askquestion('CANCELAR', 'Estas seguro que quieres borrar la fila', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            
            connection()
            cursor.execute("DELETE FROM `articulos` WHERE `id` = %d" % selecteditem[0])
            cursor.execute("commit")
            messagebox.showinfo(text="Registro ah sido borrado")

            tree.delete(curItem)
            close()
            frame1.place_forget()
            frame.place()

def salir2():
    frame2.place_forget()
    data1.delete(0, 100)
    data2.delete(0, 100)
    data3.delete(0, 100)
    data4.delete(0, 100)
    frame.place()

def salir0():
    frame1.place_forget()
    busqueda.delete(0,100)
    frame.place()

def escape():
    name.delete(0, 100)
    detail.delete(0, 100)
    price.delete(0, 100)
    neto.delete(0, 100)
    pop_up.withdraw()
    frame.place()

def CloseWindow():
    root.quit()

#### This is the main frame ####

canvas = Canvas(root, height=height, width=width)
canvas.pack()

frame = Frame(root, bg="#222831")
frame.place(relwidth=1, relheight=1)

label = Label(frame, text="¿Qué le gustaría hacer?", bg="#222831", fg="gray", font="Ubuntu 20 bold", padx=20, pady=20)
label.place(relheight=0.5, relwidth=1)

boton1 = Button(frame, text="Agregar Productos", bg="#00ADB5", fg="black", font="Raleway 11 bold", padx=7, pady=7, activebackground="black",\
                    activeforeground="white", relief="flat", highlightcolor="#112D4E", command=ventana1)
boton1.place(rely=0.6, relx=0.1, relheight=0.15, relwidth=0.22)

boton2 = Button(frame, text="Editar Tablas", bg="#00ADB5", fg="black", font="Raleway 11 bold", padx=7, pady=7, activebackground="black",\
                    activeforeground="white", relief="flat", highlightcolor="#112D4E", command=ventana2)
boton2.place(rely=0.6, relx=0.4, relheight=0.15, relwidth=0.22)

cerrar= Button(frame, text="Cerra el Programa", bg="#00ADB5", fg="black", font="Raleway 11 bold", padx=7, pady=7, activebackground="black",\
                    activeforeground="white", relief="flat", highlightcolor="#112D4E", command=CloseWindow)
cerrar.place(rely=0.6, relx=0.7, relheight=0.15, relwidth=0.22)

#### This is the first frame ####

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
                   activeforeground="white", relief="flat", highlightcolor="#112D4E", command=DBguardar)
nope = Button(frame2, text="CANCELAR", bg="#EA5455", fg="white", font="Raleway 12 bold", padx=7, pady=7,activebackground="gray", \
                   activeforeground="black", relief="flat", highlightcolor="#112D4E", command=salir2)
label_pop = Label(frame2, text="Ingrese el nummero ID:", bg="#222831", fg="gray", font="Poppins 11 bold", padx=20, pady=20)
id_pop = Entry(frame2, bg="#0D7377", font="Poppins 11 bold", fg="white", relief="flat", justify="center")

#### This is the thrid frame ####

frame1 = Frame(root, bg="#222831")
titulo = Label(frame1, text="Selecciona la fila que quires usar y escoge una de los botenes de la derecha", bg="#222831", \
                   fg="gray", font="Ubuntu 12 bold", padx=20, pady=20)
busqueda = Entry(frame1, bg="#0D7377", font="Poppins 13 bold", fg="white", relief="flat", justify="left")

editar = Button(frame1, text="EDITAR FILA", bg="#00ADB5", fg="black", font="Raleway 12 bold", padx=7, pady=7, activebackground="black", \
                   activeforeground="white", relief="flat", highlightcolor="#112D4E", command=DBedit)
borrar = Button(frame1, text="BORRAR FILA", bg="#00ADB5", fg="black", font="Raleway 12 bold", padx=7, pady=7, activebackground="black", \
                   activeforeground="white", relief="flat", highlightcolor="#112D4E", command=DBdelete)
salir = Button(frame1, text="SALIR", bg="#EA5455", fg="white", font="Raleway 12 bold", padx=7, pady=7,activebackground="gray", \
                   activeforeground="black", relief="flat", highlightcolor="#112D4E", command=salir0)
search = Button(frame1, text="Buscar", bg="#205375", fg="#EFEFEF", font="Raleway 12 bold", padx=7, pady=7, activebackground="black", \
                   activeforeground="white", relief="flat", highlightcolor="#112D4E")     


columns = ('id', 'nombre', 'desc', "precio", "content")
tree = ttk.Treeview(frame1, columns=columns, show='headings')

pop_up = Tk()
pop_up.title("EDITAR")
canvas2 = Canvas(pop_up, height=200, width=700)
canvas2.pack()
taco = Frame(canvas2, bg="#222831")
taco.place(relwidth=1, relheight=1)
pop_up.withdraw()
name = Entry(pop_up, bg="#0D7377", font="Poppins 11 bold", fg="white", relief="flat", justify="center")
detail = Entry(pop_up, bg="#0D7377", font="Poppins 11 bold", fg="white", relief="flat", justify="center")
price = Entry(pop_up, bg="#0D7377", font="Poppins 11 bold", fg="white", relief="flat", justify="center")
neto = Entry(pop_up, bg="#0D7377", font="Poppins 11 bold", fg="white", relief="flat", justify="center")
save = Button(pop_up, text="BORRAR FILA", bg="#00ADB5", fg="black", font="Raleway 12 bold", padx=7, pady=7, activebackground="black", \
                   activeforeground="white", relief="flat", highlightcolor="#112D4E")
exit = Button(pop_up, text="Cancelar", bg="#EA5455", fg="white", font="Raleway 12 bold", padx=7, pady=7,activebackground="gray", \
                   activeforeground="black", relief="flat", highlightcolor="#112D4E", command=escape)

root.mainloop()