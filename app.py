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

# Interface gráfica com cores
janela = tk.Tk()
janela.title("Cadastro de Usuários")
janela.configure(bg="#E0F7FA")  # Fundo azul claro

# Função para criar rótulos e entradas com cor
def criar_label_entrada(texto, linha):
    tk.Label(janela, text=texto, bg="#E0F7FA", font=("Arial", 10)).grid(row=linha, column=0, sticky='w', padx=10, pady=4)
    entrada = tk.Entry(janela, width=30)
    entrada.grid(row=linha, column=1, padx=10, pady=4)
    return entrada

entry_nome = criar_label_entrada("Nome:", 0)
entry_nascimento = criar_label_entrada("Data de Nascimento:", 1)
entry_email = criar_label_entrada("E-mail:", 2)
entry_cpf = criar_label_entrada("CPF:", 3)
entry_telefone = criar_label_entrada("Telefone:", 4)
entry_genero = criar_label_entrada("Gênero:", 5)

# Estilo dos botões
btn_style = {
    "bg": "#0288D1",  # Azul forte
    "fg": "white",
    "padx": 10,
    "pady": 5,
    "font": ("Arial", 10, "bold"),
    "width": 15
}

tk.Button(janela, text="Cadastrar", command=cadastrar_usuario, **btn_style).grid(row=6, column=0, padx=10, pady=6)
tk.Button(janela, text="Listar", command=listar_usuarios, **btn_style).grid(row=6, column=1, padx=10, pady=6)
tk.Button(janela, text="Alterar", command=alterar_usuario, **btn_style).grid(row=7, column=0, padx=10, pady=6)
tk.Button(janela, text="Excluir", command=excluir_usuario, **btn_style).grid(row=7, column=1, padx=10, pady=6)
tk.Button(janela, text="Sortear", command=sortear_usuario, **btn_style).grid(row=8, columnspan=2, pady=10)

carregar_dados()
janela.mainloop()
