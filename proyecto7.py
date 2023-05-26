from tkinter import *
import random
pg = Tk()
pg.geometry("500x500")
pg.title("Selector de Contraseñas")
pg.configure(background="#264653")

a1 = [[1,2,3,4,5,6,7,8,9,0],
      ["hola","cabeza","computadora","botella","mochila","comida"],
      ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","I","J","K","L","Z","X","C","V","B","N","M"],
      ["!","@","#","^","&","$","*","?","-","/"]]
def fn1():
    v1 = random.randint(0,9)
    v2 = random.randint(0,5)
    v3 = random.randint(0,25)
    t1 = a1[0][v1]
    t2 = a1[1][v2]
    t3 = a1[2][v3]
    t4 = a1[3][v1]
    lb1["text"] = str(t1) + str(t2) + str(t3) + str(t4)
    print(v1,v2,v3)
    print(t1,t2,t3,t4)

bt1 = Button(pg, text="Ejecutar", bg="#e76f51", fg="white", command=fn1)
bt1.place(relx=0.5, rely=0.45, anchor=CENTER,)

lb1 = Label(pg, text=".", bg="#e76f51", fg="white", font=200)
lb1.place(relx=0.5, rely=0.55, anchor=CENTER,)

pg.mainloop()