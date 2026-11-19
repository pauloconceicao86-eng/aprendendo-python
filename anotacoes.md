# Minhas anotações de Python

Cola de consulta. Não precisa decorar, é só consultar quando precisar.

---

## 1. Terminal (Mac)

| Comando | O que faz |
|---|---|
| `pwd` | mostra em qual pasta você está |
| `ls` | lista os arquivos e pastas |
| `cd nome-da-pasta` | entra em uma pasta |
| `cd ~/aprendendo-python` | vai direto para a pasta do projeto |
| `cd ..` | volta uma pasta |
| `mkdir nome` | cria uma pasta |
| `touch arquivo.py` | cria um arquivo vazio |
| `open -a "Visual Studio Code" .` | abre a pasta atual no VS Code |

**Dica:** o terminal do VS Code (**Terminal > New Terminal**) já abre na pasta do projeto.

---

## 2. Rodar um programa Python

```
python3 arquivo.py
```

- No Mac, use `python3` (e não `python`).
- Antes de rodar, salve o arquivo com `Cmd + S`.
- Para ver a versão: `python3 --version`.

---

## 3. Git e GitHub

### Rotina de salvar um exercício

```
git add arquivo.py
git commit -m "Descrição do que fiz"
git push
```

| Comando | O que faz |
|---|---|
| `git add arquivo.py` | escolhe o arquivo que entra no próximo registro |
| `git commit -m "texto"` | salva um registro (*commit*) com uma mensagem |
| `git push` | envia os commits para o GitHub |
| `git log` | mostra o histórico (aperte `q` para sair) |
| `git status` | mostra o que mudou e o que falta salvar |

### Configuração inicial (já feita, só uma vez)

```
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
git config --global init.defaultBranch main
```

### Criar um repositório novo

```
git init
git branch -m main
git remote add origin https://github.com/SEU-USUARIO/NOME-DO-REPO.git
git push -u origin main
```

**Sempre que aparecer erro:** copie a mensagem inteira. Ela diz o que deu errado.

---

## 4. Python: o básico

### print()

Mostra algo na tela.

```python
print("Olá")
print(42)
```

### String (`str`)

Texto. Sempre entre aspas.

```python
cidade = "Palhoça"
```

### Variable

Um nome que **guarda** um valor. O `=` significa "guarde isto".

```python
nome = "Paulo"
idade = 39
```

### Types (tipos)

| Type | O que é | Exemplo |
|---|---|---|
| `str` | texto | `"Paulo"` |
| `int` | número inteiro | `39` |
| `float` | número com decimais (usa **ponto**) | `50.00` |
| `bool` | verdadeiro ou falso | `True`, `False` |

Para descobrir o type de algo: `print(type(idade))`

### Contas

| Símbolo | Operação |
|---|---|
| `+` | soma |
| `-` | subtração |
| `*` | multiplicação |
| `/` | divisão |

```python
preco = 50.00
quantidade = 500
total = preco * quantidade
print(total)
```

---

## 5. Regras que eu já aprendi

1. **Texto leva aspas, número não.** `"500"` é texto, `500` é número.
2. **Decimal usa ponto**, e não vírgula: `19.90`.
3. **`print("total")` mostra a palavra total.** `print(total)` mostra o valor guardado na variable `total`.
4. **Guardar e mostrar são coisas diferentes.** A variable guarda, o `print()` mostra.
5. **O Python lê de cima para baixo.** A variable precisa ser criada antes de ser usada.
6. **Ler o erro ajuda.** A mensagem diz a linha (`line 3`) e o tipo do erro.

---

## 6. Erros que já vi

| Erro | O que significa | Como resolver |
|---|---|---|
| `SyntaxError: invalid syntax` | o código foi escrito de um jeito que o Python não entende | veja a linha indicada: faltam aspas, parênteses ou vírgula? |
| `NameError: name 'x' is not defined` | usei uma variable que ainda não existe | crie a variable antes de usá-la, ou confira a grafia |

---

## 7. Vocabulário

| Termo | Significado |
|---|---|
| *variable* | nome que guarda um valor |
| *string* | texto |
| *function* | bloco de código que faz uma tarefa (ex.: `print()`) |
| *syntax* | a "gramática" da linguagem |
| *repository* | pasta com histórico do Git |
| *commit* | registro salvo no histórico |
| *branch* | linha do histórico (a principal se chama `main`) |
| *push* | enviar commits para o GitHub |

---

*Atualizo este arquivo ao final de cada aula.*
