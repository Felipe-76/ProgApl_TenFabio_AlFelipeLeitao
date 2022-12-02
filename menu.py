import tkinter as tk
from tkinter import RIGHT, Button, ttk
import numpy as np
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from mudar_tab import mudar_tab
from geradores import *

gerador=Gerador()

# root window
root = tk.Tk()
root.iconbitmap('eletrica.ico')

# Adquirir tamanho da tela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

width=screen_width-650
heigth=screen_height-150
root.geometry(f"{width}x{heigth}")

# root.geometry('800x600')
root.configure(bg="white")
root.title('Simulador de Geradores')

# Criando um notebook (Widget para manusear diferentes abas)
notebook = ttk.Notebook(root, height= screen_height, width=screen_width)
notebook.pack(pady=0, expand=False)

# Criando as abas
frame1 = ttk.Frame(notebook, width=800 , height=600)
frame2 = ttk.Frame(notebook, width=800 , height=600)
frame3 = ttk.Frame(notebook, width=800 , height=600)
frame4 = ttk.Frame(notebook, width=800 , height=600)


frame1.pack(fill='both', expand=True)  # Menu
frame2.pack(fill='both', expand=True)  # Gerador Excitação independente
frame3.pack(fill='both', expand=True)  # Gerador Shunt
frame4.pack(fill='both', expand=True)  # Gerador Série

# add frames to notebook

notebook.add(frame1, text='Menu')
notebook.add(frame2, text='Gerador de excitação independente')
notebook.add(frame3, text='Gerador Shunt')
notebook.add(frame4, text='Gerador Série')

# add buttons to frames


# Menu

## Foto do menu 
img_menu = ImageTk.PhotoImage(Image.open("menu_img.png"))
texto_menu = tk.Label(frame1, image=img_menu)
texto_menu.grid(row = 0, column = 0, columnspan=3,pady=20, padx=20, sticky="WE")

## Frame para armazenar as variáveis
variaveis = tk.LabelFrame(frame1, text= "Insira aqui as variáveis: ", padx=50, pady=10)
variaveis.grid(row = 1, column=0, padx=20)

## Variáveis
label_RA = tk.Label(variaveis,text='RA:').grid(row=0, column=0)
caixa_RA = tk.Entry(variaveis, width=7)
caixa_RA.grid(row=0, column=1)

label_Raj = tk.Label(variaveis,text='Raj:').grid(row=1, column=0)
caixa_Raj = tk.Entry(variaveis, width=7)
caixa_Raj.grid(row=1, column=1)

label_RF = tk.Label(variaveis,text='Rf:').grid(row=2, column=0)
caixa_RF = tk.Entry(variaveis, width=7)
caixa_RF.grid(row=2, column=1)

label_Vb = tk.Label(variaveis,text='Vb:').grid(row=3, column=0)
caixa_Vb = tk.Entry(variaveis, width=7)
caixa_Vb.grid(row=3, column=1)

label_w = tk.Label(variaveis,text='w:').grid(row=4, column=0)
caixa_w = tk.Entry(variaveis, width=7)
caixa_w.grid(row=4, column=1)

label_Rload = tk.Label(variaveis,text='Rload:').grid(row=5, column=0)
caixa_Rload = tk.Entry(variaveis, width=7)
caixa_Rload.grid(row=5, column=1)

label_IL = tk.Label(variaveis,text='IL:').grid(row=6, column=0)
caixa_IL = tk.Entry(variaveis, width=7)
caixa_IL.grid(row=6, column=1)


def armazenar():
    Gerador.r_a=caixa_RA.get()
    Gerador.r_adj=caixa_Raj.get()
    Gerador.r_f=caixa_RF.get()
    Gerador.Vf=caixa_Vb.get()
    Gerador.w=caixa_w.get()
    Gerador.Rload=caixa_Rload.get()
    Gerador.IL=caixa_IL.get()

    global valores_menu, valores_exc_ind, valores_shunt, valores_serie
    valores_menu.grid_forget()
    valores_exc_ind.grid_forget()
    valores_shunt.grid_forget()
    valores_serie.grid_forget()

    valores_menu = tk.LabelFrame(frame1, padx=50, pady=10, border=0)
    valores_exc_ind = tk.LabelFrame(frame2, padx=50, pady=10, border=0) 
    valores_shunt = tk.LabelFrame(frame3, padx=50, pady=10, border=0) 
    valores_serie = tk.LabelFrame(frame4, padx=50, pady=10, border=0)
    valores_menu.grid(row=1, column=1,padx=100)
    valores_exc_ind.grid(row=0, column=0)
    valores_shunt.grid(row=0, column=0)
    valores_serie.grid(row=0, column=0)

    tk.Label(valores_menu, text=f"RA = {gerador.r_a}").grid()
    tk.Label(valores_menu, text=f"Raj = {gerador.r_adj}").grid()
    tk.Label(valores_menu, text=f"RF = {gerador.r_f}").grid()
    tk.Label(valores_menu, text=f"Vf = {gerador.Vf}").grid()
    tk.Label(valores_menu, text=f"w = {gerador.w}").grid()
    tk.Label(valores_menu, text=f"Rload = {gerador.Rload}").grid()
    tk.Label(valores_menu, text=f"IL = {gerador.IL}").grid()

    tk.Label(valores_shunt, text=f"RA = {gerador.r_a}").grid()
    tk.Label(valores_shunt, text=f"Raj = {gerador.r_adj}").grid()
    tk.Label(valores_shunt, text=f"RF = {gerador.r_f}").grid()
    tk.Label(valores_shunt, text=f"Vf = {gerador.Vf}").grid()
    tk.Label(valores_shunt, text=f"w = {gerador.w}").grid()
    tk.Label(valores_shunt, text=f"Rload = {gerador.Rload}").grid()
    tk.Label(valores_shunt, text=f"IL = {gerador.IL}").grid()

    tk.Label(valores_serie, text=f"RA = {gerador.r_a}").grid()
    tk.Label(valores_serie, text=f"Raj = {gerador.r_adj}").grid()
    tk.Label(valores_serie, text=f"RF = {gerador.r_f}").grid()
    tk.Label(valores_serie, text=f"Vf = {gerador.Vf}").grid()
    tk.Label(valores_serie, text=f"w = {gerador.w}").grid()
    tk.Label(valores_serie, text=f"Rload = {gerador.Rload}").grid()
    tk.Label(valores_serie, text=f"IL = {gerador.IL}").grid()

    tk.Label(valores_exc_ind, text=f"RA = {gerador.r_a}").grid()
    tk.Label(valores_exc_ind, text=f"Raj = {gerador.r_adj}").grid()
    tk.Label(valores_exc_ind, text=f"RF = {gerador.r_f}").grid()
    tk.Label(valores_exc_ind, text=f"Vf = {gerador.Vf}").grid()
    tk.Label(valores_exc_ind, text=f"w = {gerador.w}").grid()
    tk.Label(valores_exc_ind, text=f"Rload = {gerador.Rload}").grid()
    tk.Label(valores_exc_ind, text=f"IL = {gerador.IL}").grid()





## Botões
button_armazenar = tk.Button(frame1, text='Armazenar valores', command=armazenar)
button_armazenar.grid(row = 2, column = 0)

## Frame para armazenar alguns botões
botoes_menu = tk.LabelFrame(frame1, padx=50, pady=10, border=0)
botoes_menu.grid(row = 1, column=2, sticky="E")

### Botões do frame
botao_exc_ind = tk.Button(botoes_menu, text='Gerador excitação independente', command=lambda:mudar_tab(notebook, frame2))
botao_exc_ind.grid(row=0, pady=10, sticky="WE")
botao_shunt = tk.Button(botoes_menu, text='Gerador Shunt', command=lambda:mudar_tab(notebook, frame3))
botao_shunt.grid(row=1, pady=10, sticky="WE")
botao_serie = tk.Button(botoes_menu, text='Gerador Série', command=lambda:mudar_tab(notebook, frame4))
botao_serie.grid(row=2, pady=10, sticky="WE")

## Frame para armazenar os valores atuais das variáveis (Esse frame será usado nas outras abas)
valores_menu = tk.LabelFrame(frame1, padx=50, pady=10, border=0)
valores_exc_ind = tk.LabelFrame(frame2, padx=50, pady=10, border=0) 
valores_shunt = tk.LabelFrame(frame3, padx=50, pady=10, border=0) 
valores_serie = tk.LabelFrame(frame4, padx=50, pady=10, border=0) 
valores_menu.grid(row=1, column=1, padx=100)

### Texto dento do frame com os valores atuais

tk.Label(valores_menu, text=f"RA = {gerador.r_a}").grid()
tk.Label(valores_menu, text=f"Raj = {gerador.r_adj}").grid()
tk.Label(valores_menu, text=f"RF = {gerador.r_f}").grid()
tk.Label(valores_menu, text=f"Vf = {gerador.Vf}").grid()
tk.Label(valores_menu, text=f"w = {gerador.w}").grid()
tk.Label(valores_menu, text=f"Rload = {gerador.Rload}").grid()
tk.Label(valores_menu, text=f"IL = {gerador.IL}").grid()

tk.Label(valores_shunt, text=f"RA = {gerador.r_a}").grid()
tk.Label(valores_shunt, text=f"Raj = {gerador.r_adj}").grid()
tk.Label(valores_shunt, text=f"RF = {gerador.r_f}").grid()
tk.Label(valores_shunt, text=f"Vf = {gerador.Vf}").grid()
tk.Label(valores_shunt, text=f"w = {gerador.w}").grid()
tk.Label(valores_shunt, text=f"Rload = {gerador.Rload}").grid()
tk.Label(valores_shunt, text=f"IL = {gerador.IL}").grid()

tk.Label(valores_serie, text=f"RA = {gerador.r_a}").grid()
tk.Label(valores_serie, text=f"Raj = {gerador.r_adj}").grid()
tk.Label(valores_serie, text=f"RF = {gerador.r_f}").grid()
tk.Label(valores_serie, text=f"Vf = {gerador.Vf}").grid()
tk.Label(valores_serie, text=f"w = {gerador.w}").grid()
tk.Label(valores_serie, text=f"Rload = {gerador.Rload}").grid()
tk.Label(valores_serie, text=f"IL = {gerador.IL}").grid()

tk.Label(valores_exc_ind, text=f"RA = {gerador.r_a}").grid()
tk.Label(valores_exc_ind, text=f"Raj = {gerador.r_adj}").grid()
tk.Label(valores_exc_ind, text=f"RF = {gerador.r_f}").grid()
tk.Label(valores_exc_ind, text=f"Vf = {gerador.Vf}").grid()
tk.Label(valores_exc_ind, text=f"w = {gerador.w}").grid()
tk.Label(valores_exc_ind, text=f"Rload = {gerador.Rload}").grid()
tk.Label(valores_exc_ind, text=f"IL = {gerador.IL}").grid()







#Exc ind
"""
def simularexcind():
    gerador.r_adj= escala_Raj.get()
    print('simulando exc ind')
    return


label_escalaRaj1=tk.Label(frame2,text='Selecione a Resistencia de Ajuste do Campo').grid(row=1, column=0)
escala_Raj = tk.Scale(frame2, from_=0,to=gerador.r_adjlim)
escala_Raj.grid(row=1, column=1)
"""

botao_menu_1 = tk.Button(frame2, text = "Menu",width=16, height=3,  command = lambda:mudar_tab(notebook, frame1))
botao_menu_1.grid(row=0,column=4)

label_escalaRaj=tk.Label(frame2,width = 30, text='Selecione a Tensao do Campo').grid(row=0, column=1)
escala_Vf = tk.Scale(frame2, from_=0, to=200)
escala_Vf.grid(row=0, column=2)

button_simularexcind = tk.Button(frame2, width=16, height=3, text='Simular!')
button_simularexcind.grid(row=0, column=3, padx=80)
valores_exc_ind.grid(row=0, column=0)


# Shunt
botao_menu_2 = tk.Button(frame3, text = "Menu", command = lambda:mudar_tab(notebook, frame1))
botao_menu_2.grid()
valores_shunt.grid(row=2, column=2)


#série
botao_menu_3 = tk.Button(frame4, text = "Menu", command = lambda:mudar_tab(notebook, frame1))
botao_menu_3.grid()
valores_serie.grid(row=2, column=2)




root.mainloop()
