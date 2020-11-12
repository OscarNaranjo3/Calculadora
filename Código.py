import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def init_window():

    window = tk.Tk() # Crear pantalla
    window.title('Calculadora') # Titulo de la pantalla
    # Establecer el tamanio de la pnatalla (ancho: 400px y largo: 250px)
    window.geometry('400x250')

    # Crear una etiqueta con fuente Arial bold y tamanio 15
    label = tk.Label(window, text='Calculadora', font=('Arial bold', 15))
    # Ubicar la etiqueta en la columna y fila 0 de la pantalla
    label.grid(column=0, row=0)

    # Agregar dos campos de texto
    entrada1 = tk.Entry(window, width=10)
    entrada2 = tk.Entry(window, width=10)

    entrada1.grid(column=1, row=1)
    entrada2.grid(column=1, row=2)

    # Agregar dos etiqetas para indicarle al usuario los valores que debe ingresar
    label_entrada1 = tk.Label(window, text = 'Ingrese primer numero:', font=('Arial bold', 10))
    label_entrada1.grid(column=0, row=1)

    label_entrada2 = tk.Label(window, text='Ingrese segundo numero:', font=('Arial bold', 10))
    label_entrada2.grid(column=0, row=2)

    # Crear una etiqueta para el seleccionador (combobox)
    label_operador = tk.Label(window, text='Escoja un operador', font=('Arial bold', 10))
    label_operador.grid(column=0, row=3)

    # Crear un seleccionador (combobox)
    combo_operadores = ttk.Combobox(window)
    # Asignar los valores del seleccinador a traves de su atributo values
    combo_operadores['values'] = ['+', '-', '*', '/', 'pow']
    #Asignar por defecto una opcion seleccionada: 0 es el indice de los valores
    combo_operadores.current(0) #set the selected item
    # Ubicar el seleccionador
    combo_operadores.grid(column=1, row=3)

    # Agregar etiqueta para mostrar el resultado de la operacion en pantalla
    label_resultado = tk.Label(window, text='Resultado: ', font=('Arial bold', 15))
    label_resultado.grid(column=0, row=5)

    # Boton calcular
    boton = tk.Button(window,
                      command=lambda: click_calcular(
                          label_resultado,
                          entrada1.get(),
                          entrada2.get(),
                          combo_operadores.get(), parte_entera.get()),
                      text='Calcular',
                      bg='purple',
                      fg='white')
    boton.grid(column=1, row=4)

    parte_entera = tk.BooleanVar()
    parte_entera.set(False)
    chk = tk.Checkbutton(window, text='Tomar solo la parte entera', var=parte_entera)
    chk.grid(column=0, row=6)

    boton_color = tk.Button(window,command= lambda: color(window),text='Cambiar color de fondo',bg='blue',fg='white')
    boton_color.grid(column=0, row=7)

    boton_color2 = tk.Button(window, command=lambda: color_incial(window), text='Volver al color inicial', bg='blue', fg='white')
    boton_color2.grid(column=0, row=8)


    window.mainloop()

def calculadora(num1, num2, operador, parte_entera):

    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = round(num1 / num2, 2)
    else:
        resultado = num1 ** num2
    if parte_entera == True:
        resultado = int(resultado)

    return resultado

def click_calcular(label, num1, num2, operador, parte_entera):
    cont1 = 0
    cont2 = 0
    for numero1 in num1:
        ascci = ord(numero1)
        if ascci >= 46 and ascci <= 57 and ascci != 47:
            cont1 += 1
    for numero2 in num2:
        ascci2 = ord(numero2)
        if ascci2 >= 46 and ascci2 <= 57 and ascci2 != 47:
            cont2 += 1
    if cont1 == len(num1) and cont2 == len(num2):
        # Conversion de valores
        valor1 = float(num1)
        valor2 = float(num2)

        # Calculo dados los valores y el operador
        res = calculadora(valor1, valor2, operador, parte_entera)

        # Actualizacion del texto en la etiqueta
        label.configure(text='Resultado: ' + str(res))
    else:
        messagebox.showerror('Error', 'Asegúrese que esté ingresando números y usando el punto como decimal')

def color_incial(window):
    mycolor = "#%02x%02x%02x" % (240, 240, 237)
    window.config(bg=mycolor)

def color(window):
    window.config(bg='red')

def main():
    init_window()
main()
