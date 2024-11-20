#Importando biblioteca 
from tkinter import *
from tkinter import messagebox


#Dimensões, posição, cor, titulo e icone da janela
todolist = Tk()
todolist.title("Gerenciador de Tarefas")
todolist["bg"] = "#8092FA"
todolist.geometry("400x600+650+200")
todolist.iconbitmap("iconejanela.ico")
todolist.resizable(False, False)

#Função para adicionar task
def adicionartask():
    try:
        tarefa = entryTask.get()
        
        # Verifica se a tarefa não é uma string vazia ou composta apenas por espaços
        if tarefa.strip(): 
            lbTarefas.insert(END, tarefa)
            entryTask.delete(0, END)
            messagebox.showinfo("Aviso", "Tarefa adicionada!")
        
        # Levanta uma exceção personalizada
        else:
            raise ValueError("Tarefa vazia")  
    
    except ValueError:
        messagebox.showwarning("Aviso", "Digite uma tarefa para continuar!")

#Função para deletar task
def deletartask():  
    try: 
        indexselect = lbTarefas.curselection()[0]
        lbTarefas.delete(indexselect)
        messagebox.showinfo("Aviso", "Tarefa excluída!")    
    
    except IndexError: 
        exception_occurred = True
        messagebox.showwarning("Aviso", "Selecione uma tarefa para excluir!")

#Função para concluir a task 
def concluirtask():
    try:
        # Obtém o índice da tarefa selecionada
        indexselect = lbTarefas.curselection()[0]
        
        # Altera a cor de fundo da tarefa selecionada para verde
        lbTarefas.itemconfig(indexselect, {'bg': '#60E68E'})
    
        # Exibe uma mensagem de confirmação
        messagebox.showinfo("Aviso", "Tarefa concluída!")
  
    except IndexError:
        # Mostra uma mensagem de aviso caso nenhuma tarefa esteja selecionada
        messagebox.showwarning("Aviso", "Selecione uma tarefa para concluir!")
        
#Titulo da pagina 
labelTitle = Label(todolist, text = "GERENCIADOR DE TAREFAS", font = ("Arial", 15), width = 50, bg = "#8092FA", background = '#9ECBE5', pady = 20)

#Campo e botão para adicionar task
entryTask = Entry(todolist, width = 30)
btnAddTask = Button(todolist, text = "Adicionar tarefa", command = adicionartask, bg = '#9ECBE5')

#Botão para deletar task
btnDelTask = Button(todolist, text = "Excluir tarefa", command = deletartask, bg = '#E56D69')

#Botão para concluir a task 
btnConcluirTask = Button(todolist, text = "Concluir tarefa", command = concluirtask, bg = '#36E391')

#Listbox 
lbTarefas = Listbox(todolist, height = 20, width = 50)


#packs 
labelTitle.pack(pady = 10)
entryTask.pack(pady = 5)
btnAddTask.pack(pady = 5)
lbTarefas.pack(pady = 15)
btnConcluirTask.pack(pady = 5)
btnDelTask.pack(pady = 0)
todolist.mainloop()