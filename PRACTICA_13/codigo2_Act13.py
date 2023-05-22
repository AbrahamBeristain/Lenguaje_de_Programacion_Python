from tkinter import *
import tkinter as tk
import math

ventana = Tk()
ventana.title("Calculadora Pedorra")
ventana.geometry("315x390")
ventana.iconbitmap("calculadora.ico")
ventana.resizable(0,0)
ventana.config(bg="white")

def Ent_Valores(tecla):
    try:
        if tecla >= "0" and tecla <= "9" or tecla == ".":
            Ent_Win.set(Ent_Win.get() + tecla)
            
        if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-":
            if tecla == "*":
                Ent_Win.set(Ent_Win.get() + "*")
            elif tecla == "/":
                Ent_Win.set(Ent_Win.get() + "/")
            elif tecla == "+":
                Ent_Win.set(Ent_Win.get() + "+")
            elif tecla == "-":
                Ent_Win.set(Ent_Win.get() + "-")
    except:
        Ent_Win.set("ERROR")


def Mos_Res(tecla, *args):
    try:
        resultado = eval(Ent_Win.get())
        Ent_Win.set(resultado)
    except:
        Ent_Win.set("ERROR")


def Raiz_Cuadrada():
    try:
        resultado = math.sqrt(float(Ent_Win.get()))
        Ent_Win.set(resultado)
    except:
        Ent_Win.set("ERROR")


def Del(*args):
    inicio = 0
    final = len(Ent_Win.get())
    Ent_Win.set(Ent_Win.get()[inicio:final-1])


def C_Borrar(*args):
    Ent_Win.set("")


def Mmas():
    try:
        resultado = eval(Ent_Win.get()) + float(Ent_Win.get())
        Ent_Win.set(resultado)
    except:
        Ent_Win.set("ERROR")


def Mc():
    Ent_Win.set("")


def Mr_Ms():
    try:
        resultado = eval(Ent_Win.get())
        Ent_Win.set(resultado)
    except:
        Ent_Win.set("ERROR")



Ent_Win = StringVar()
Win_res = Entry(ventana, font=("Arial", 25), width=15, justify=RIGHT, textvariable=Ent_Win, bd=2)
Win_res.place(x=15, y=5)

Btn_Mc = Button(ventana, text="MC", width=7, height=3, bg="white", command=lambda: Mc())
Btn_Mc.place(x=10, y=65)
Btn_Mr = Button(ventana, text="MR", width=7, height=3, bg="white", command=lambda:Mr_Ms())
Btn_Mr.place(x=70, y=65)
Btn_Ms = Button(ventana, text="MS", width=7, height=3, bg="white", command=lambda: Mr_Ms())
Btn_Ms.place(x=130, y=65)
Btn_Mmas = Button(ventana, text="M+", width=7, height=3, bg="white", command=lambda: Mmas())
Btn_Mmas.place(x=190, y=65)
Btn_Sqr = Button(ventana, text="sqr", width=7, height=3, bg="white", command=lambda: Raiz_Cuadrada())
Btn_Sqr.place(x=250, y=65)

Btn_Num7 = Button(ventana, text="7", width=7, height=3, bg="white", command=lambda: Ent_Valores("7"))
Btn_Num7.place(x=10, y=130)
Btn_Num8 = Button(ventana, text="8", width=7, height=3, bg="white", command=lambda: Ent_Valores("8"))
Btn_Num8.place(x=70, y=130)
Btn_Num9 = Button(ventana, text="9", width=7, height=3, bg="white", command=lambda: Ent_Valores("9"))
Btn_Num9.place(x=130, y=130)
Btn_Div = Button(ventana, text="/", width=7, height=3, bg="white", command=lambda: Ent_Valores("/"))
Btn_Div.place(x=190, y=130)
Btn_Del = Button(ventana, text="DEL", width=7, height=3, bg="white", command=lambda: Del())
Btn_Del.place(x=250, y=130)

Btn_Num4 = Button(ventana, text="4", width=7, height=3, bg="white", command=lambda: Ent_Valores("4"))
Btn_Num4.place(x=10, y=195)
Btn_Num5 = Button(ventana, text="5", width=7, height=3, bg="white", command=lambda: Ent_Valores("5"))
Btn_Num5.place(x=70, y=195)
Btn_Num6 = Button(ventana, text="6", width=7, height=3, bg="white", command=lambda: Ent_Valores("6"))
Btn_Num6.place(x=130, y=195)
Btn_Mul = Button(ventana, text="*", width=7, height=3, bg="white", command=lambda: Ent_Valores("*"))
Btn_Mul.place(x=190, y=195)
Btn_C = Button(ventana, text="C", width=7, height=3, bg="white", command=lambda: C_Borrar())
Btn_C.place(x=250, y=195)

Btn_Num1 = Button(ventana, text="1", width=7, height=3, bg="white", command=lambda: Ent_Valores("1"))
Btn_Num1.place(x=10, y=260)
Btn_Num2 = Button(ventana, text="2", width=7, height=3, bg="white", command=lambda: Ent_Valores("2"))
Btn_Num2.place(x=70, y=260)
Btn_Num3 = Button(ventana, text="3", width=7, height=3, bg="white", command=lambda: Ent_Valores("3"))
Btn_Num3.place(x=130, y=260)
Btn_Menos = Button(ventana, text="-", width=7, height=3, bg="white", command=lambda: Ent_Valores("-"))
Btn_Menos.place(x=190, y=260)

Btn_Num0 = Button(ventana, text="0", width=15, height=3, bg="white", command=lambda: Ent_Valores("0"))
Btn_Num0.place(x=10, y=325)
Btn_Punto = Button(ventana, text=".", width=7, height=3, bg="white", command=lambda: Ent_Valores("."))
Btn_Punto.place(x=130, y=325)
Btn_Mas = Button(ventana, text="+", width=7, height=3, bg="white", command=lambda: Ent_Valores("+"))
Btn_Mas.place(x=190, y=325)
Btn_Igual = Button(ventana, text="=", width=7, height=7, bg="white", command=lambda: Mos_Res("="))
Btn_Igual.place(x=250, y=260)


ventana.mainloop()