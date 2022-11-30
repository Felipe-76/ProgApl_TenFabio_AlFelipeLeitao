import tkinter as tk
from tkinter import RIGHT, Button, ttk
import numpy as np
from PIL import Image, ImageTk
import matplotlib.pyplot as plt


class Gerador:
    def __init__(self, RA=0,Raj=0,Rajlim=0,RF=0,w=0,Rload=0,IL=0,Vf=0,Vb=0):
        # if RA <0 or Raj<0 or Rajlim<0 : raise ValueError('invalido')
        self.RA= RA
        self.Raj=Raj
        self.Rajlim=Rajlim
        self.RF= RF
        self.Vb= Vb
        self.w= w
        self.Rload= Rload
        self.IL= IL
        self.Vf= Vf
        self.RA= RA
        def simular():
            print(RA+Raj)

    
    
gerador=Gerador()


# global RA, Raj, Rajlim,RF,Vb,w,Rload,IL,Vf
# Rajlim=0
X=1;Y=1

fig, ax = plt.subplots()
ax.plot(X,Y) 

fig.savefig("grafico.jpeg")


# root window
root = tk.Tk()
root.iconbitmap('eletrica.ico')

# Adquirir tamanho da tela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# root.geometry('800x600')
root.configure(bg="white")
root.title('Simulador de Geradores')

# create a notebook
notebook = ttk.Notebook(root, height= screen_height, width=screen_width)
notebook.pack(pady=0, expand=False)

# create frames
frame1 = ttk.Frame(notebook, width=800 , height=600)
frame2 = ttk.Frame(notebook, width=800 , height=600)
frame3 = ttk.Frame(notebook, width=800 , height=600)
frame4 = ttk.Frame(notebook, width=800 , height=600)
frame5 = ttk.Frame(notebook, width=800 , height=600)


frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
frame4.pack(fill='both', expand=True)
frame5.pack(fill='both', expand=True)

# add frames to notebook

notebook.add(frame1, text='Menu')
notebook.add(frame2, text='Gerador de excitação independente')
notebook.add(frame3, text='Gerador Shunt')
notebook.add(frame4, text='Gerador Série')
notebook.add(frame5, text='Gerador Composto')

# add buttons to frames


#menu
variaveis = tk.LabelFrame(frame1, text= "Insira aqui as variáveis: ", padx=50, pady=10)
variaveis.grid()


label_RA= tk.Label(variaveis,text='RA:').grid(row=0, column=0, sticky="W")
caixa_RA= tk.Entry(variaveis, width=7)
caixa_RA.grid(row=0, column=1)


label_Raj=tk.Label(variaveis,text='Raj:').grid(row=1, column=0)
caixa_Raj= tk.Entry(variaveis, width=7)
caixa_Raj.grid(row=1, column=1)

label_RF=tk.Label(variaveis,text='RF:').grid(row=2, column=0)
caixa_RF= tk.Entry(variaveis, width=7)
caixa_RF.grid(row=2, column=1)

label_Vb=tk.Label(variaveis,text='Vb:').grid(row=3, column=0)
caixa_Vb= tk.Entry(variaveis, width=7)
caixa_Vb.grid(row=3, column=1)

label_w=tk.Label(variaveis,text='w:').grid(row=4, column=0)
caixa_w= tk.Entry(variaveis, width=7)
caixa_w.grid(row=4, column=1)

label_Rload=tk.Label(variaveis,text='Rload:').grid(row=5, column=0)
caixa_Rload= tk.Entry(variaveis, width=7)
caixa_Rload.grid(row=5, column=1)

label_IL=tk.Label(variaveis,text='IL:').grid(row=6, column=0)
caixa_IL= tk.Entry(variaveis, width=7)
caixa_IL.grid(row=6, column=1)


labelteste=tk.Label(frame1,text='IL:')


 
def armazenar():   
    gerador.RA=caixa_RA.get()
    print (gerador.RA)
    gerador.Raj=caixa_Raj.get()
    gerador.Rajlim=caixa_Raj.get()
    label_escalaRaj1=tk.Label(frame2,text='Selecione a Resistencia de Ajuste do Campo').grid(row=2, column=1)
    global escala_Raj
    escala_Raj = tk.Scale(frame2, from_=0,to=gerador.Rajlim)
    escala_Raj.grid(row=3, column=1)
    
    gerador.RF=caixa_RF.get()
    gerador.Vb=caixa_Vb.get()
    gerador.w=caixa_w.get()
    gerador.Rload=caixa_Rload.get()
    gerador.IL=caixa_IL.get()
    
    labelRA= tk.Label(frame1, text='Resistencia de Armadura :'+gerador.RA+'ohms' )
    labelRA.grid(row=8, column=0)  
    
    # labelRA= tk.Label(frame1, text='Resistencia de Armadura :'+RA+'ohms' )
    # labelRA.grid(row=8, column=0)
      
    
    # labelRA= tk.Label(frame1, text='Resistencia de Armadura :'+RA+'ohms' )
    # labelRA.grid(row=8, column=0)
      
    
    # labelRA= tk.Label(frame1, text='Resistencia de Armadura :'+RA+'ohms' )
    # labelRA.grid(row=8, column=0)
      
    
    # labelRA= tk.Label(frame1, text='Resistencia de Armadura :'+RA+'ohms' )
    # labelRA.grid(row=8, column=0)
      
    
    # labelRA= tk.Label(frame1, text='Resistencia de Armadura :'+RA+'ohms' )
    # labelRA.grid(row=8, column=0)
    return

button_armazenar = tk.Button(frame1, text='Armazenar', command=armazenar)
button_armazenar.grid(row = 1, column = 0)



# my_img1 = ImageTk.PhotoImage(Image.open("eletrica.ico"))
# mylabel= tk.Label(frame1,image=my_img1).grid(row=3, column=3)




#Exc ind

def simularexcind():
    gerador.Raj= escala_Raj.get()
    print('simulando exc ind')
    return


# label_nomejpeg=tk.Label(frame2,text='Digite o nome do arquivo .jpeg').grid(row=0, column=0)
# caixa_nomejpeg=tk.Entry(frame2).grid(row=0, column=1)
# button_salvarjpeg = Button(frame2, bg="green", text = "Salvar como .jpeg"
#                            ).grid(row=0, column=2)


# label_nomejpeg=tk.Label(frame2,text='Digite o nome do arquivo .jpeg').grid(row=0, column=0)
# caixa_nomejpeg=tk.Entry(frame2).grid(row=0, column=1)
# button_salvarjpeg = Button(frame2, bg="green", text = "Salvar como .jpeg"
#                            ).grid(row=0, column=2)

# label_nomecsv =tk.Label(frame2,text='Digite o nome do arquivo .csv').grid(row=1, column=0)
# caixa_nomecsv =tk.Entry(frame2).grid(row=1, column=1)
# button_salvarcsv  = Button(frame2, bg="green", text = "Salvar como .csv"
#                             ).grid(row=1, column=2)



label_escalaRaj=tk.Label(frame2,text='Selecione a Tensao do Campo').grid(row=2, column=0)
escala_Vf = tk.Scale(frame2, from_=0, to=200)
escala_Vf.grid(row=3, column=0 )

button_simularexcind = tk.Button(frame2, text='Simular!', command=simularexcind)
button_simularexcind.grid(row=4, column=0, columnspan=2)

# ckt_excind = ImageTk.PhotoImage(Image.open("excind.jpg"))
# ckt_excindd= tk.Label(frame2, image=ckt_excind)
# ckt_excindd.grid(row=0, column=0)



#serie








root.mainloop()

