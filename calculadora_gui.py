import tkinter # importa biblioteca tkinter

from tkinter import * 
root = Tk()
equacao = ""
def mostra(valor):
    global equacao
    equacao += valor
    label_resultado.config(text = equacao)
def limpa():
    global equacao
    equacao = ""
    label_resultado.config(text = equacao)
def calcula():
    global equacao
    resultado = ""
    if equacao != "":
        try:
            resultado = eval(equacao)

        except:
            resultado = "erro"
            equacao = ""
    label_resultado.config(text = resultado)


root.geometry("520x600+100+200")#define tamanho da janela
root.title("Calculadora") # define titulo
root.configure(bg="#17161b")# pinta a preto a tela
label_resultado = Label(root, width = 25, height = 2, text ="",font = ("arial",30))
label_resultado.pack()
Button(root, text = "C", width=5, height=1,font = ("arial",30, "bold"), bd = 1, fg="#fff", bg = "#3697f5",command=lambda: limpa()).place(x=10, y = 100)#cria o botao com cores, tamanho e sitio
Button(root, text = "/", width = 5, height= 1, font = ("arial", 30, "bold"), bd =1, fg ="#fff", bg = "#3697f5",command = lambda: mostra("/")).place(x = 150 , y =100)
Button(root, text = "%" , width = 5, height= 1,font = ("arial", 30, "bold"), bd =1, fg ="#fff", bg = "#3697f5",command=lambda: calcula()).place(x = 290 , y =100)
Button(root, text = "*" , width = 5, height= 1,font = ("arial", 30, "bold"), bd =1, fg ="#fff", bg = "#3697f5",command = lambda: calcula()).place(x = 430 , y =100)

Button(root, text = "9", width=5, height=1,font = ("arial",30, "bold"), bd = 1, fg="#fff", bg = "#3697f5", command = lambda: mostra("9")).place(x=10, y = 200)#cria o botao com cores, tamanho e sitio
Button(root, text = "8", width = 5, height= 1, font = ("arial", 30, "bold"), bd =1, fg ="#fff", bg = "#3697f5", command = lambda: mostra("8")).place(x = 150 , y =200)
Button(root, text = "7" , width = 5, height= 1,font = ("arial", 30, "bold"), bd =1, fg ="#fff", bg = "#3697f5", command = lambda: mostra("7")).place(x = 290 , y =200)
Button(root, text = "6" , width = 5, height= 1,font = ("arial", 30, "bold"), bd =1, fg ="#fff", bg = "#3697f5", command = lambda: mostra("6")).place(x = 430 , y =200)

Button(root, text = "5", width=5, height=1,font = ("arial",30, "bold"), bd = 1, fg="#fff", bg = "#3697f5", command = lambda: mostra("5")).place(x=10, y = 300)#cria o botao com cores, tamanho e sitio
Button(root, text = "4", width = 5, height= 1, font = ("arial", 30, "bold"), bd =1, fg ="#fff", bg = "#3697f5", command = lambda: mostra("4")).place(x = 150 , y =300)
Button(root, text = "3", width = 5, height= 1, font = ("arial", 30, "bold"), bd =1, fg ="#fff", bg = "#3697f5", command = lambda: mostra("3")).place(x = 290 , y=300)
Button(root, text = "2" , width = 5, height= 1,font = ("arial", 30, "bold"), bd =1, fg ="#fff", bg = "#3697f5", command = lambda: mostra("2")).place(x = 430 , y =300)

Button(root, text = "1" , width = 5, height= 1,font = ("arial", 30, "bold"), bd =1, fg ="#fff", bg = "#3697f5", command = lambda: mostra("1")).place(x = 10 , y =400)
Button(root, text = "0" , width = 5, height= 1,font = ("arial", 30, "bold"), bd =1, fg ="#fff", bg = "#3697f5", command = lambda: mostra("0")).place(x = 150 , y =400)
Button(root, text = "=" , width = 5, height= 1,font = ("arial", 30, "bold"), bd =1, fg ="#fff", bg = "#3697f5", command = lambda: calcula()).place(x = 290, y =400)
Button(root, text = "+" , width = 5, height= 1,font = ("arial", 30, "bold"), bd =1, fg ="#fff", bg = "#3697f5", command = lambda: mostra("+")).place(x = 10, y =500)
Button(root, text = "-" , width = 5, height= 1,font = ("arial", 30, "bold"), bd =1, fg ="#fff", bg = "#3697f5", command = lambda: mostra("-")).place(x = 150, y =500)
root.mainloop()