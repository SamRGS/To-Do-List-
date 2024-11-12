#Importando biblioteca 
from tkinter import *
from tkinter import messagebox


#Dimensões, posição, cor, titulo e icone da janela
todolist = Tk()
todolist.title("Gerenciador de tarefas")
todolist["bg"] = "#8092FA"
todolist.geometry("400x600+650+200")
todolist.iconbitmap("iconejanela.ico")
todolist.resizable(False, False)

#Função para adicionar task
def adicionartask(): 
    tarefa = entryTask.get()

    if tarefa != '': 
        lbTarefas.insert(END, tarefa)
        entryTask.delete(0, END)
    else:
        messagebox.showwarning("Aviso", "Digite uma tarefa para continuar!")


#Função para deletar task
def deletartask(): 
    try: 
        indexselect = lbTarefas.curselection()[0]
        lbTarefas.delete(indexselect)
    except IndexError: 
        messagebox.showwarning("Aviso", "Selecione uma tarefa para excluir!")

#Função para concluir a task 
#def concluirtask(): 
    



#Titulo da pagina 
labelTitle = Label(todolist, text = "GERENCIADOR DE TAREFAS", font = ("Working", 12), width = 50, bg = "#8092FA", )

#Campo e botão para adicionar task
entryTask = Entry(todolist, width = 30)
btnAddTask = Button(todolist, text = "Adicionar tarefa", command = adicionartask, bg = '#9ECBE5')

#Botão para deletar task
btnDelTask = Button(todolist, text = "Excluir tarefa", command = deletartask, bg = '#E56D69')

#Botão para concluir a task 
btnConcluirTask = Button(todolist, text = "Concluir tarefa", bg = '#36E391')

#Listbox 
lbTarefas = Listbox(todolist, height = 20, width = 50)


labelTitle.pack(pady = 10)
entryTask.pack(pady = 5)
btnAddTask.pack(pady = 5)
lbTarefas.pack(pady = 15)
btnConcluirTask.pack(pady = 5)
btnDelTask.pack(pady = 0)
todolist.mainloop()