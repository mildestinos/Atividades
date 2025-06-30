
## 📋 **README – Cadastro de Usuários (Atividade 09)**

### ✅ **Descrição do Projeto**

Este é um sistema simples de **cadastro de usuários** feito em Python, que permite as seguintes operações:

1. Cadastrar novos usuários
2. Listar todos os usuários cadastrados
3. Alterar dados de um usuário existente
4. Sortear um usuário aleatoriamente
5. Excluir um usuário
6. Sair do programa

O cadastro coleta informações como: nome, data de nascimento, e-mail, CPF, telefone, gênero, além da data e hora do cadastro.

---

### 🗂️ **Estrutura do Usuário (Campos cadastrados)**

Cada usuário cadastrado é armazenado como um dicionário Python com as seguintes chaves:

* `Nome`
* `Data de Nascimento`
* `E-mail`
* `CPF`
* `Telefone`
* `Gênero`
* `Data de Cadastro`
* `Hora de Cadastro`

---

### 🧠 **Dicionário de Termos**

| Termo                  | Significado / Função                                                |
| ---------------------- | ------------------------------------------------------------------- |
| `lista_de_usuarios`    | Lista que armazena todos os dicionários de usuários cadastrados.    |
| `usuario`              | Dicionário que representa os dados de um único usuário.             |
| `tupla_chaves_usuario` | Tupla com os nomes fixos dos campos de um usuário.                  |
| `append()`             | Método que adiciona um novo item ao final de uma lista.             |
| `input()`              | Função que recebe entrada do usuário pelo teclado.                  |
| `os.system('cls')`     | Comando que limpa o terminal no Windows; `'clear'` para Unix/macOS. |
| `random.choice()`      | Sorteia aleatoriamente um item de uma lista.                        |
| `datetime.now()`       | Retorna a data e hora atual do sistema.                             |
| `strftime()`           | Formata a data/hora em string legível (ex: `"%d/%m/%Y"`).           |
| `match/case`           | Estrutura condicional semelhante ao `switch` (Python 3.10+).        |
| `try/except`           | Bloco para tratamento de exceções/erros.                            |
| `chave` (dicionário)   | Nome do campo em um dicionário (`ex: "Nome"`).                      |
| `valor` (dicionário)   | Conteúdo associado à chave (`ex: "Eric Vieira"`).                   |

---

### 🛠️ **Pré-requisitos**

* Python 3.10 ou superior (por causa do uso de `match/case`)
* Terminal ou IDE como VSCode, PyCharm, Thonny etc.

---

### ▶️ **Como executar**

1. Salve o código em um arquivo `.py` (por exemplo: `cadastro_usuarios.py`)
2. No terminal, execute:

   ```bash
   python cadastro_usuarios.py
   ```
3. Siga as opções do menu no terminal.

---

### 💡 **Melhorias futuras sugeridas**

* Validação de CPF e e-mail
* Exportação para CSV
* Interface gráfica (GUI)
* Salvamento em arquivo (persistência)

