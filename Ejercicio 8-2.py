#Actividad 5 / Ejercicio 8.2
#Nota: Para la desviación estándar hago uso de la libreria "statistics" solo por preferencia.
import tkinter
import statistics

#Ventana
ventana = tkinter.Tk()
ventana.geometry("500x400")
ventana.resizable(0,0)

#LabelsNota
labNota1 = tkinter.Label(ventana, text= "Nota 1")
labNota1.place(x=140,y=30,width=70,height=25)
labNota2 = tkinter.Label(ventana, text= "Nota 2")
labNota2.place(x=140,y=60,width=70,height=25)
labNota3 = tkinter.Label(ventana, text= "Nota 3")
labNota3.place(x=140,y=90,width=70,height=25)
labNota4 = tkinter.Label(ventana, text= "Nota 4")
labNota4.place(x=140,y=120,width=70,height=25)
labNota5 = tkinter.Label(ventana, text= "Nota 5")
labNota5.place(x=140,y=150,width=70,height=25)

#CajasTextoNota
txtNota1 = tkinter.Entry(ventana)
txtNota1.place(x=260,y=30,width=100,height=25)
txtNota2 = tkinter.Entry(ventana)
txtNota2.place(x=260,y=60,width=100,height=25)
txtNota3 = tkinter.Entry(ventana)
txtNota3.place(x=260,y=90,width=100,height=25)
txtNota4 = tkinter.Entry(ventana)
txtNota4.place(x=260,y=120,width=100,height=25)
txtNota5 = tkinter.Entry(ventana)
txtNota5.place(x=260,y=150,width=100,height=25)

#LabelsResultados
labPromedio = tkinter.Label(ventana, text= "Promedio =")
labPromedio.place(x=140,y=250,width=200,height=25)
labDesvest = tkinter.Label(ventana, text= "Deviación Estándar =")
labDesvest.place(x=140,y=280,width=200,height=25)
labMayor = tkinter.Label(ventana, text= "Valor Mayor = ")
labMayor.place(x=140,y=310,width=200,height=25)
labMenor = tkinter.Label(ventana, text= "Valor Menor = ")
labMenor.place(x=140,y=340,width=200,height=25)

#Funciones
def CalcularTodo():
    N1 = float(txtNota1.get())
    N2 = float(txtNota2.get())
    N3 = float(txtNota3.get())
    N4 = float(txtNota4.get())
    N5 = float(txtNota5.get())
    Datos = [N1, N2, N3, N4, N5]
    Promedio = (N1+N2+N3+N4+N5)/5
    Desvest = round(statistics.stdev(Datos), 3)
    menor = Datos[0]
    mayor = Datos[0]
    for i in Datos:
        if i < menor:
            menor = i
    for i in Datos:
        if i > mayor:
            mayor = i
    labPromedio.config(text=f"Promedio = {Promedio}")
    labDesvest.config(text=f"Desviación Estándar = {Desvest}")
    labMayor.config(text=f"Valor Mayor = {mayor}")
    labMenor.config(text=f"Valor Menor = {menor}")

def Limpiar():
    labPromedio.config(text="Promedio = ")
    labDesvest.config(text="Desviación Estándar = ")
    labMayor.config(text="Valor Mayor = ")
    labMenor.config(text="Valor Menor = ")
    txtNota1.delete(0, tkinter.END)
    txtNota2.delete(0, tkinter.END)
    txtNota3.delete(0, tkinter.END)
    txtNota4.delete(0, tkinter.END)
    txtNota5.delete(0, tkinter.END)

#Botones
btnCalcular = tkinter.Button(ventana, text= "Calcular", command= CalcularTodo)
btnCalcular.place(x=190,y=200,width=70,height=25)
btnBorrar = tkinter.Button(ventana, text= "Limpiar", command= Limpiar)
btnBorrar.place(x=280,y=200,width=70,height=25)

#mainloop
ventana.mainloop()