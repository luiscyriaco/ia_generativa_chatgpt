import tkinter as tk

# Cria a janela principal
janela = tk.Tk()
janela.title("Minha Janela com While/Loop")
janela.geometry("300x200")

# O Tkinter possui seu próprio loop interno embutido (mainloop)
# que funciona exatamente com a mesma lógica de manter a janela rodando:
print("A janela foi aberta. Feche a janela para continuar o programa.")
janela.mainloop()

print("A janela foi fechada pelo usuário!")