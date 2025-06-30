import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
import random
import json

usuarios = []
ARQUIVO_DADOS = "usuarios.json"

def carregar_dados():
    global usuarios
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            usuarios = json.load(f)
    except FileNotFoundError:
        usuarios = []

def salvar_dados():
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=4)

def cadastrar_usuario():
    usuario = {
        "Nome": entry_nome.get(),
        "Data de Nascimento": entry_nascimento.get(),
        "E-mail": entry_email.get(),
        "CPF": entry_cpf.get(),
        "Telefone": entry_telefone.get(),
        "Gênero": entry_genero.get(),
        "Data de Cadastro": datetime.now().strftime("%d/%m/%Y"),
        "Hora de Cadastro": datetime.now().strftime("%H:%M:%S")
    }
    usuarios.append(usuario)
    salvar_dados()
    messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
    limpar_campos()

def listar_usuarios():
    if not usuarios:
        messagebox.showinfo("Lista de Usuários", "Nenhum usuário cadastrado.")
        return
    texto = ""
    for i, u in enumerate(usuarios):
        texto += f"\n[{i}] " + ", ".join([f"{k}: {v}" for k, v in u.items()]) + "\n"
    messagebox.showinfo("Lista de Usuários", texto)

def excluir_usuario():
    if not usuarios:
        messagebox.showinfo("Excluir", "Nenhum usuário para excluir.")
        return
    try:
        indice = simpledialog.askinteger("Excluir", "Digite o índice do usuário:")
        if indice is not None and 0 <= indice < len(usuarios):
            nome = usuarios[indice]['Nome']
            del usuarios[indice]
            salvar_dados()
            messagebox.showinfo("Excluir", f"Usuário '{nome}' excluído com sucesso!")
        else:
            messagebox.showwarning("Erro", "Índice inválido.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def sortear_usuario():
    if not usuarios:
        messagebox.showinfo("Sorteio", "Nenhum usuário cadastrado.")
        return
    sorteado = random.choice(usuarios)
    texto = "\n".join([f"{k}: {v}" for k, v in sorteado.items()])
    messagebox.showinfo("Sorteado", texto)

def alterar_usuario():
    if not usuarios:
        messagebox.showinfo("Alterar", "Nenhum usuário cadastrado.")
        return
    try:
        indice = simpledialog.askinteger("Alterar", "Digite o índice do usuário:")
        if indice is None or not (0 <= indice < len(usuarios)):
            messagebox.showwarning("Erro", "Índice inválido.")
            return

        campos = list(usuarios[indice].keys())
        campo = simpledialog.askstring("Alterar", f"Digite o campo para alterar:\n{', '.join(campos)}")
        if campo not in campos:
            messagebox.showwarning("Erro", f"Campo '{campo}' não encontrado.")
            return

        novo_valor = simpledialog.askstring("Alterar", f"Novo valor para '{campo}':")
        usuarios[indice][campo] = novo_valor
        salvar_dados()
        messagebox.showinfo("Alterar", f"Usuário alterado com sucesso!")

    except Exception as e:
        messagebox.showerror("Erro", str(e))

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_nascimento.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_genero.delete(0, tk.END)

# Interface gráfica
janela = tk.Tk()
janela.title("Cadastro de Usuários")

tk.Label(janela, text="Nome:").grid(row=0, column=0)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)

tk.Label(janela, text="Data de Nascimento:").grid(row=1, column=0)
entry_nascimento = tk.Entry(janela)
entry_nascimento.grid(row=1, column=1)

tk.Label(janela, text="E-mail:").grid(row=2, column=0)
entry_email = tk.Entry(janela)
entry_email.grid(row=2, column=1)

tk.Label(janela, text="CPF:").grid(row=3, column=0)
entry_cpf = tk.Entry(janela)
entry_cpf.grid(row=3, column=1)

tk.Label(janela, text="Telefone:").grid(row=4, column=0)
entry_telefone = tk.Entry(janela)
entry_telefone.grid(row=4, column=1)

tk.Label(janela, text="Gênero:").grid(row=5, column=0)
entry_genero = tk.Entry(janela)
entry_genero.grid(row=5, column=1)

tk.Button(janela, text="Cadastrar", command=cadastrar_usuario).grid(row=6, column=0)
tk.Button(janela, text="Listar", command=listar_usuarios).grid(row=6, column=1)
tk.Button(janela, text="Alterar", command=alterar_usuario).grid(row=7, column=0)
tk.Button(janela, text="Excluir", command=excluir_usuario).grid(row=7, column=1)
tk.Button(janela, text="Sortear", command=sortear_usuario).grid(row=8, columnspan=2)

carregar_dados()
janela.mainloop()
