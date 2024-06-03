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
    
    genero_entrada_var = StringVar() #RECEBE O VALOR DA ENTRADA DO GENERO E COLOCA EM STRING
    
    #TEXTO PRINCIPAL
    label_titulo = Label(janela_calculadora, text="CALCULADORA DE TAXA METABÓLICA BASAL")
    
    # TEXTO E ENTRADA DO PESO
    label_peso = Label(janela_calculadora, text="Peso em kg:")
    peso_entrada = Entry(janela_calculadora)
    
    # TEXTO E ENTRADA DA ALTURA
    label_altura = Label(janela_calculadora, text="Altura em cm:")
    altura_entrada = Entry(janela_calculadora)
    
    # TEXTO E ENTRADA DA IDADE
    label_idade = Label(janela_calculadora, text="Idade:")
    idade_entrada = Entry(janela_calculadora)

    # TEXTO E AS DUAS OPÇÕES DE BOTÃO DO GENERO
    label_genero = Label(janela_calculadora, text="Gênero:")
    botao_var1 = Radiobutton(janela_calculadora, text="Masculino", variable=genero_entrada_var, value="0")
    botao_var2 = Radiobutton(janela_calculadora, text="Feminina", variable=genero_entrada_var, value="1")


    # BOTAO QUE EFETUA O CALCULO ( O QUE EXECUTA A FUNÇÃO "TAXA" )
    botao = Button(janela_calculadora, text="CALCULAR", command=taxa)

    # TEXTO MOSTRANDO O RESULTADO DO CALCULO
    resultado = Label(janela_calculadora, text="", fg="red")

      #LAYOUT DO PROGRAMA ( POSIÇÃO DE CADA ELEMENTO NA INTERFACE GRÁFICA )

    label_titulo.grid(column=0, row=0, padx=200, pady=40) #POSIÇÃO DO TEXTO PRINCIPAL

    label_peso.grid(column=0, row=1, padx=200, pady=15, sticky=W) #POSIÇÃO DO TEXTO DO PESO
    peso_entrada.grid(column=0, row=1, padx=200, pady=15, sticky=E) #POSIÇÃO DA ENTRADA DO PESO

    label_altura.grid(column=0, row=2, padx=200, pady=15, sticky=W) #POSIÇÃO DO TEXTO DA ALTURA
    altura_entrada.grid(column=0, row=2, padx=200, pady=15, sticky=E) #POSIÇÃO DA ENTRADA DA ALTURA 

    label_idade.grid(column=0, row=3, padx=200, pady=15, sticky=W) #POSIÇÃO DO TEXTO DA IDADE
    idade_entrada.grid(column=0, row=3, padx=200, pady=15, sticky=E) #POSIÇÃO DA ENTRADA DA IDADE

    label_genero.grid(row=4, column=0, padx=0, pady=15) #POSIÇÃO DO TEXTO DO GENERO
    botao_var1.grid(row=5, column=0, padx=0, pady=0) #POSIÇÃO DO PRIMEIRO BOTAO DO GENERO
    botao_var2.grid(row=6, column=0, padx=0, pady=4) #POSIÇÃO DO SEGUNDO BOTAO DO GENERO

    botao.grid(column=0, row=7, padx=200, pady=30) #POSIÇÃO DO BOTAO PRINCIPAL

    resultado.grid(column=0, row=8, padx=200, pady=40) #POSIÇÃO DO RESULTADO
    

janela = Tk() #CRIA A JANELA INICIAL DA INTERFACE

janela.title("TMB") #TITULO DA JANELA
janela.geometry("900x600") #TAMANHO DA JANELA

#BOTAO PARA ABRIR A OUTRA JANELA ( EXECUTANDO A FUNÇÃO CALCULADORA ), JUNTO DA SUA POSIÇÃO
titulo = Button(janela, text="CALCULADORA DE TAXA METABÓLICA BASAL", command=calculadora, font="Times 20 bold", fg="black", bg="#ccccff").grid(column=0, row=0, padx=125, pady=225) 

janela.mainloop() #CRIA O LOOP DA JANELA ( PODENDO CALCULAR QUANTAS VEZES QUISER )
