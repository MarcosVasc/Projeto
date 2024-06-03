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