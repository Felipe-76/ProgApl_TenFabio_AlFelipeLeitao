import tkinter as tk
from tkinter import RIGHT, Button, ttk
import numpy as np
from PIL import Image, ImageTk
from mudar_tab import mudar_tab
from geradores import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)


gerador = Gerador(r_a=0.19, r_f = 24, w = 1800, r_adj = 10)

# root window
root = tk.Tk()
root.iconbitmap('Images/eletrica.ico')

# Adquirir tamanho da tela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

width=screen_width-650
heigth=screen_height-250
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


# Menu

## Foto do menu 
img_menu = ImageTk.PhotoImage(Image.open("Images/menu_img.png"))
texto_menu = tk.Label(frame1, image=img_menu)
texto_menu.grid(row = 0, column = 0, columnspan=3,pady=20, padx=20, sticky="WE")

## Frame para armazenar as variáveis
variaveis = tk.LabelFrame(frame1, text= "Insira aqui as variáveis: ", padx=50, pady=10)
variaveis.grid(row = 1, column=0, padx=20)

## Variáveis
label_RA = tk.Label(variaveis,text='RA:').grid(row=0, column=0)
caixa_RA = tk.Entry(variaveis, width=7)
caixa_RA.insert(0, 0.19)
caixa_RA.grid(row=0, column=1)

label_Raj = tk.Label(variaveis,text='Raj:').grid(row=1, column=0)
caixa_Raj = tk.Entry(variaveis, width=7)
caixa_Raj.insert(0, 10)
caixa_Raj.grid(row=1, column=1)

label_RF = tk.Label(variaveis,text='Rf:').grid(row=2, column=0)
caixa_RF = tk.Entry(variaveis, width=7)
caixa_RF.insert(0, 24)
caixa_RF.grid(row=2, column=1)

label_w = tk.Label(variaveis,text='w:').grid(row=4, column=0)
caixa_w = tk.Entry(variaveis, width=7)
caixa_w.insert(0, 1800)
caixa_w.grid(row=4, column=1)

label_Rload = tk.Label(variaveis,text='Rload:').grid(row=5, column=0)
caixa_Rload = tk.Entry(variaveis, width=7)
caixa_Rload.insert(0, 0)
caixa_Rload.grid(row=5, column=1)



def armazenar():
    gerador.r_a=float(caixa_RA.get())
    gerador.r_adj=float(caixa_Raj.get())
    gerador.r_f=float(caixa_RF.get())
    gerador.w=float(caixa_w.get())
    gerador.Rload=float(caixa_Rload.get())

    global valores_menu, valores_exc_ind, valores_shunt
    valores_menu.grid_forget()
    valores_exc_ind.grid_forget()
    valores_shunt.grid_forget()

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
    tk.Label(valores_menu, text=f"w = {gerador.w}").grid()
    tk.Label(valores_menu, text=f"Rload = {gerador.Rload}").grid()

    tk.Label(valores_shunt, text=f"RA = {gerador.r_a}").grid()
    tk.Label(valores_shunt, text=f"Raj = {gerador.r_adj}").grid()
    tk.Label(valores_shunt, text=f"RF = {gerador.r_f}").grid()
    tk.Label(valores_shunt, text=f"w = {gerador.w}").grid()
    tk.Label(valores_shunt, text=f"Rload = {gerador.Rload}").grid()

    tk.Label(valores_exc_ind, text=f"RA = {gerador.r_a}").grid()
    tk.Label(valores_exc_ind, text=f"Raj = {gerador.r_adj}").grid()
    tk.Label(valores_exc_ind, text=f"RF = {gerador.r_f}").grid()
    tk.Label(valores_exc_ind, text=f"w = {gerador.w}").grid()
    tk.Label(valores_exc_ind, text=f"Rload = {gerador.Rload}").grid()
    
    tk.Label(valores_serie, text=f"RA = {gerador.r_a}").grid()
    tk.Label(valores_serie, text=f"Raj = {gerador.r_adj}").grid()
    tk.Label(valores_serie, text=f"RF = {gerador.r_f}").grid()
    tk.Label(valores_serie, text=f"w = {gerador.w}").grid()
    tk.Label(valores_serie, text=f"Rload = {gerador.Rload}").grid()


## Botões
button_armazenar = tk.Button(frame1, text='Armazenar valores', command=armazenar, pady=10)
button_armazenar.grid(pady=10, row = 2, column = 0)

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
valores_menu.grid(row=1, column=1, padx=100)

valores_exc_ind = tk.LabelFrame(frame2, padx=50, pady=10, border=0) 
valores_shunt = tk.LabelFrame(frame3, padx=50, pady=10, border=0) 
valores_serie = tk.LabelFrame(frame4, padx=50, pady=10, border=0)


### Texto dento do frame com os valores atuais

tk.Label(valores_menu, text=f"RA = {gerador.r_a}").grid()
tk.Label(valores_menu, text=f"Raj = {gerador.r_adj}").grid()
tk.Label(valores_menu, text=f"RF = {gerador.r_f}").grid()
tk.Label(valores_menu, text=f"w = {gerador.w}").grid()
tk.Label(valores_menu, text=f"Rload = {gerador.Rload}").grid()

tk.Label(valores_shunt, text=f"RA = {gerador.r_a}").grid()
tk.Label(valores_shunt, text=f"Raj = {gerador.r_adj}").grid()
tk.Label(valores_shunt, text=f"RF = {gerador.r_f}").grid()
tk.Label(valores_shunt, text=f"w = {gerador.w}").grid()
tk.Label(valores_shunt, text=f"Rload = {gerador.Rload}").grid()

tk.Label(valores_exc_ind, text=f"RA = {gerador.r_a}").grid()
tk.Label(valores_exc_ind, text=f"Raj = {gerador.r_adj}").grid()
tk.Label(valores_exc_ind, text=f"RF = {gerador.r_f}").grid()
tk.Label(valores_exc_ind, text=f"w = {gerador.w}").grid()
tk.Label(valores_exc_ind, text=f"Rload = {gerador.Rload}").grid()

tk.Label(valores_serie, text=f"RA = {gerador.r_a}").grid()
tk.Label(valores_serie, text=f"Raj = {gerador.r_adj}").grid()
tk.Label(valores_serie, text=f"RF = {gerador.r_f}").grid()
tk.Label(valores_serie, text=f"w = {gerador.w}").grid()
tk.Label(valores_serie, text=f"Rload = {gerador.Rload}").grid()


def simular_exc_ind(gerador):
    r_a = gerador.r_a
    r_adj = gerador.r_adj
    r_f = gerador.r_f
    w = gerador.w
    Rload = gerador.Rload
    Vf = float(escala_Vf.get())

    gerador_temp = Excind(r_a=r_a, r_adj=r_adj,r_adjlim=30,r_f=r_f, w = w, Rload = Rload, Vf = Vf)
    IL, VT = gerador_temp.simular()

    # Frame para colocar o grafico
    frame_grafico = tk.LabelFrame(frame2, padx=50, pady=50, border=0)
    frame_grafico.grid(row=1,column=1, columnspan=3)

    fig = Figure(figsize = (3.3, 3.3), dpi = 100)
    
    # Subplot
    plot1 = fig.add_subplot(111)
    plot1.set_ylim(0, max(VT) + 15)
    plot1.set_title("Característica terminal (Vt x IL)")
  
    # Plotando o gráfico
    plot1.plot(IL, VT, "r-")
    plot1.grid()

    # Canvas do Tkinter que contém a figura
    canvas = FigureCanvasTkAgg(fig, master = frame_grafico)
    canvas.draw()

    # Colocando o Canvas na janela
    canvas.get_tk_widget().pack()
  
    # Menu abaixo do gráfico
    toolbar = NavigationToolbar2Tk(canvas,frame_grafico)
    toolbar.update()


def simular_shunt(gerador):
    r_a = gerador.r_a
    r_adj = gerador.r_adj
    r_f = gerador.r_f
    w = gerador.w
    Rload = gerador.Rload
    gerador_temp = Shunt(r_a=r_a, r_adj=r_adj,r_adjlim=30,r_f=r_f, w = w, Rload = Rload)
    i_f, Vt, Ea = gerador_temp.Simularshunt()

    # Frame para colocar o grafico
    frame_grafico = tk.LabelFrame(frame3, padx=50, pady=50, border=0)
    frame_grafico.grid(row=1,column=1, padx=10)
    
    fig = Figure(figsize = (3.3, 3.3), dpi = 100)

    # Subplot
    plot1 = fig.add_subplot(111)
    plot1.set_ylim(0, max(Vt) + 15)

    # Plotando o gráfico
    plot1.plot(i_f, Vt, "r-")
    plot1.plot(i_f, Ea, "b-")
    plot1.grid()
    plot1.legend(['Curva de  Magnetização', ' Tensão Terminal'])
    plot1.set_title("(Ea, Vt x IL)")

    # Canvas do Tkinter que contém a figura
    canvas = FigureCanvasTkAgg(fig, master = frame_grafico)
    canvas.draw()

    # Colocando o Canvas na janela
    canvas.get_tk_widget().pack()
  
    # Menu abaixo do gráfico
    toolbar = NavigationToolbar2Tk(canvas,frame_grafico)
    toolbar.update()


def simular_serie(gerador):
    r_a = gerador.r_a
    r_adj = gerador.r_adj
    r_f = gerador.r_f
    w = gerador.w
    Rload = gerador.Rload
    gerador_temp = Serie(r_a=r_a, r_s=r_adj+r_a, w = w, Rload = Rload)


    i_f, Vt, Ea = gerador_temp.simularserie()

    # Frame para colocar o grafico
    frame_grafico = tk.LabelFrame(frame4, padx=50, pady=50, border=0)
    frame_grafico.grid(row=1,column=1, padx=10)
    
    fig = Figure(figsize = (3.3, 3.3), dpi = 100)

    # Subplot
    plot1 = fig.add_subplot(111)
    plot1.set_ylim(0, max(Ea) + 15)

    # Plotando o gráfico
    plot1.plot(i_f, Ea, "b-")
    plot1.plot(i_f, -Vt, "r-")
    plot1.grid()
    plot1.legend(['Curva de  Magnetização', ' Tensão Terminal'])
    plot1.set_title("(Ea, Vt x IL)")

    # Canvas do Tkinter que contém a figura
    canvas = FigureCanvasTkAgg(fig, master = frame_grafico)
    canvas.draw()

    # Colocando o Canvas na janela
    canvas.get_tk_widget().pack()
  
    # Menu abaixo do gráfico
    toolbar = NavigationToolbar2Tk(canvas,frame_grafico)
    toolbar.update()



# Aba gerador excitação independente
botao_menu_1 = tk.Button(frame2, text = "Menu",width=16, height=3,  command = lambda:mudar_tab(notebook, frame1))
botao_menu_1.grid(row=0,column=4)

label_escalaRaj=tk.Label(frame2,width = 30, text='Selecione a Tensao do Campo').grid(row=0, column=1)
escala_Vf = tk.Scale(frame2, from_=0, to=200)
escala_Vf.grid(row=0, column=2)

button_simularexcind = tk.Button(frame2, width=16, height=3, text='Simular!', command = lambda:simular_exc_ind(gerador))
button_simularexcind.grid(row=0, column=3, padx=80)
valores_exc_ind.grid(row=0, column=0)


# Aba gerador Shunt
valores_shunt.grid(row=0, column=0)

button_simularexcind = tk.Button(frame3, width=16, height=3, text='Simular!', command = lambda:simular_shunt(gerador))
button_simularexcind.grid(row=0, column=1, padx=200)

botao_menu_2 = tk.Button(frame3, width=16, height=3, text = "Menu", command = lambda:mudar_tab(notebook, frame1))
botao_menu_2.grid(row=0, column=2)

# Aba gerador Série
valores_serie.grid(row=0, column=0)

button_simularserie = tk.Button(frame4, width=16, height=3, text='Simular!', command = lambda:simular_serie(gerador))
button_simularserie.grid(row=0, column=1, padx=200)

botao_menu_3 = tk.Button(frame4, width=16, height=3, text = "Menu", command = lambda:mudar_tab(notebook, frame1))
botao_menu_3.grid(row=0, column=2)

root.mainloop()
