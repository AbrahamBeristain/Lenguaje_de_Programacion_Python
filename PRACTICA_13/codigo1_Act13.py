from tkinter import *
import tkinter as tk

ventana =  Tk()
ventana.title("Calculadora Operaciones Basicas")
ventana.geometry('445x265')
ventana.iconbitmap("calculadora.ico")
ventana.resizable(0,0)
ventana.config(bg= "white")

def sumar():
    lbl_signo["text"] = "+"
    num1 = ent_num1.get()
    num2 = ent_num2.get()
    
    if num1 == "" or num2 == "":
        lbl_respuesta["text"] = "ERROR"
    else:
        try:
            respuesta = int(num1) + int(num2)
            lbl_respuesta["text"] = respuesta
        except:
            lbl_respuesta["text"] = "ERROR"

def restar():
    lbl_signo["text"] = "-"
    num1 = ent_num1.get()
    num2 = ent_num2.get()
    
    if num1 == "" or num2 == "":
        lbl_respuesta["text"] = "ERROR"
    else:
        try:
            respuesta = int(num1) - int(num2)
            lbl_respuesta["text"] = respuesta
        except:
            lbl_respuesta["text"] = "ERROR"

def multiplicar():
    lbl_signo["text"] = "*"
    num1 = ent_num1.get()
    num2 = ent_num2.get()
    
    if num1 == "" or num2 == "":
        lbl_respuesta["text"] = "ERROR"
    else:
        try:
            respuesta = int(num1) * int(num2)
            lbl_respuesta["text"] = respuesta
        except:
            lbl_respuesta["text"] = "ERROR"

def dividir():
    lbl_signo["text"] = "/"
    num1 = ent_num1.get()
    num2 = ent_num2.get()
    
    if num1 == "" or num2 == "":
        lbl_respuesta["text"] = "ERROR"
    else:
        try:
            respuesta = int(num1) / int(num2)
            lbl_respuesta["text"] = respuesta
        except:
            lbl_respuesta["text"] = "ERROR"

#OPERACIONES
lf_operaciones = LabelFrame(ventana, text="Operaciones", width=420, height=100, bg="white", fg="black", font=("Arial Black", 12))
lf_operaciones.place(x=10, y=5)

lbl_num1 = Label(ventana, text="Numero 1", bg="white", font=("Arial", 12))
lbl_num1.place(x=25, y=33)

lbl_num2 = Label(ventana, text="Numero 2", bg="white", font=("Arial", 12))
lbl_num2.place(x=169, y=33)

lbl_resultado = Label(ventana, text="Resultado", bg="white", font=("Arial", 12))
lbl_resultado.place(x=307, y=33)

ent_num1 = Entry(ventana, font=("Arial", 12), width=10, justify="center", bd=4)
ent_num1.place(x=25, y=65)

ent_num2 = Entry(ventana, font=("Arial", 12), width=10, justify="center", bd=4)
ent_num2.place(x=160, y=65)

lbl_signo = Label(ventana, text="", bg="white", font=("Arial Black", 14))
lbl_signo.place(x=133, y=60)

lbl_igual = Label(ventana, text="=", bg="white", font=("Arial Black", 14))
lbl_igual.place(x=270, y=60)

lbl_respuesta = Label(ventana, text="", font=("Arial Black", 12), width=10)
lbl_respuesta.place(x=300, y=65)

#OPERADORES ARITMETICOS
lf_operadores = LabelFrame(ventana, text="Operadores Aritmeticos", width=420, height=100, bg="white", font=("Arial Black", 12))
lf_operadores.place(x=10, y=125)

btn_suma = Button(ventana, text="+", font=("Arial Black", 12), width=3, height=1, bg="white", bd=4, command=sumar)
btn_suma.place(x=35, y=165)

btn_resta = Button(ventana, text="-", font=("Arial Black", 12), width=3, height=1, bg="white", bd=4, command=restar)
btn_resta.place(x=140, y=165)

btn_mult = Button(ventana, text="*", font=("Arial Black", 12), width=3, height=1, bg="white", bd=4, command=multiplicar)
btn_mult.place(x=247, y=165)

btn_div = Button(ventana, text="/", font=("Arial Black", 12), width=3, height=1, bg="white", bd=4, command=dividir)
btn_div.place(x=352, y=165)


ventana.mainloop()