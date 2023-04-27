from tkinter import *
import boto3
from tkinter.ttk import *

client = boto3.client("sns")

window_obter_arn = Tk()
window_obter_arn.title("Buscando topicos na conta")
window_obter_arn.geometry("550x400")


def imprimir():
    print(str(lb_arn.get(ACTIVE)))


lista_topicos = {'Topics': [{'TopicArn': "topico 1"}, {'TopicArn': "topico 2"}, {'TopicArn': "topico 3"}]}

list_arn = []

for i in lista_topicos['Topics']:
    list_arn.append(i['TopicArn'])

lb_arn = Listbox(window_obter_arn, width=100, height=10, justify="center")

for i in list_arn:
    lb_arn.insert(END, i)

lb_arn.pack()

btn_arn = Button(window_obter_arn, text="Imprimir Arn", command=imprimir, width=12)
btn_arn.pack()

window_obter_arn.mainloop()

window = Tk()
window.title("Escolha uma opção")
window.geometry("500x300")

selecao = IntVar()


def botao():
    print(selecao.get())
    var = selecao.get()
    if var == 1:
        print("var 1")
        cadastro_usuario()
    if var == 2:
        print("var 2")
        deletar_usuario()


rad1 = Radiobutton(window, text='Inserir novo email', value=1, variable=selecao)
rad1.grid(column=0, row=1, padx=5, pady=5, sticky=NSEW)
rad2 = Radiobutton(window, text='Deletar email', value=2, variable=selecao)
rad2.grid(column=0, row=2, padx=5, pady=5, sticky=NSEW)

btn = Button(window, text="Finalizar", command=botao, width=12)
btn.grid(column=0, row=3, padx=10, pady=10, sticky=NSEW)


def cadastro_usuario():
    window_cadastrar_arn = Tk()
    window_cadastrar_arn.title("CADASTRO DE USUARIO NO TOPICO")
    window_cadastrar_arn.geometry("700x250")

    def enviar_usuario():
        topic = entry_topic.get()
        endpoint = entry_endpoint.get()
        protocol = entry_protocol.get()

        print("enviando usuario para o topico: ", topic, endpoint, protocol)
        window_cadastrar_sucesso = Tk()
        window_cadastrar_sucesso.title("Resultado do cadastro")
        window_cadastrar_sucesso.geometry("200x100")
        mensagem = Label(window_cadastrar_sucesso, text="Cadastrado com sucesso")
        mensagem.grid(row=0, column=0, padx=35, pady=30)

    label_topic = Label(window_cadastrar_arn, width=10, text="Arn do topico:", anchor="w")
    label_topic.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    entry_topic = Entry(window_cadastrar_arn, width=100)
    entry_topic.grid(row=0, column=1, padx=0, pady=5)

    label_protocol = Label(window_cadastrar_arn, width=10, text="Protocolo:", anchor="w")
    label_protocol.grid(row=1, column=0, padx=5, pady=5, sticky=NSEW)
    entry_protocol = Entry(window_cadastrar_arn, width=100)
    entry_protocol.grid(row=1, column=1, padx=0, pady=5)

    label_endpoint = Label(window_cadastrar_arn, width=10, text="Endpoint:", anchor="w")
    label_endpoint.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    entry_endpoint = Entry(window_cadastrar_arn, width=100)
    entry_endpoint.grid(row=2, column=1, padx=0, pady=5)

    bnt_inserir = Button(window_cadastrar_arn, text="INSERIR", command=enviar_usuario, width=12)
    bnt_inserir.grid(row=3, column=1, padx=5, pady=5, sticky=E)


def deletar_usuario():
    window_deletar = Tk()
    window_deletar.title("DELETANDO UM USUARIO DO TOPICO")
    window_deletar.geometry("520x100")

    def deletando_usuario():
        endpoint = entry_endpoint.get()
        # client.delete

        print("enviando usuario para o topico: ", endpoint)
        window_del_sucesso = Tk()
        window_del_sucesso.title("Resultado do cadastro")
        window_del_sucesso.geometry("200x100")
        mensagem = Label(window_del_sucesso, text="Deletado com sucesso")
        mensagem.grid(row=0, column=0, padx=35, pady=30)

    label_endpoint = Label(window_deletar, width=28, text="Endpoint que será DELETADO:", anchor="w")
    label_endpoint.grid(row=0, column=0, padx=2, pady=5, sticky=NSEW)
    entry_endpoint = Entry(window_deletar, width=50)
    entry_endpoint.grid(row=0, column=1, padx=0, pady=5)

    bnt_inserir = Button(window_deletar, text="DELETAR", command=deletando_usuario, width=12)
    bnt_inserir.grid(row=3, column=1, padx=5, pady=5, sticky=E)


window.mainloop()