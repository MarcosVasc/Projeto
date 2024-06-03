from tkinter import *

def calculadora(): #FUNÇÃO PARA ABRIR A SEGUNDA JANELA

    def taxa(): #FUNÇÃO PARA CALCULAR A TAXA METABÓLICA BASAL

        peso = float(peso_entrada.get())
        altura = int(altura_entrada.get())
        idade = int(idade_entrada.get())
        genero = genero_entrada_var.get()

        if genero == "0":
            form = 66 + (13.8 * peso) + (5 * altura) - (6.8 * idade)

        else:
            form = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)

        resultado["text"] = f"A taxa metabólica basal é : {form:.2f} Kcal/dia"


    
    janela_calculadora = Toplevel(janela) #CRIA A JANELA SECUNDÁRIA
    janela_calculadora.title("Calculadora") #TITULO DA JANELA SECUNDÁRIA
    janela_calculadora.geometry("640x600") #TAMANHO DA JANELA SECUNDÁRIA