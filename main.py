import tkinter as tk
from tkinter import messagebox
from modelos.categoria import Categoria
from modelos.desktop import Desktop
from modelos.notebook import Notebook # type: ignore

categorias = {
    "Desktop": Categoria(1, "Desktop"),
    "Notebook": Categoria(2, "Notebook")
}

def cadastrar_produto():
    tipo = tipo_var.get()
    modelo = entry_modelo.get()
    cor = entry_cor.get()
    preco = float(entry_preco.get())

    if tipo == "Desktop":
        fonte = entry_extra.get()
        d = Desktop(modelo, cor, preco, categorias["Desktop"], fonte)
        d.cadastrar()
        messagebox.showinfo("Cadastro", d.getInformacoes())

    elif tipo == "Notebook":
        bateria = entry_extra.get()
        n = Notebook(modelo, cor, preco, categorias["Notebook"], bateria)
        n.cadastrar()
        messagebox.showinfo("Cadastro", n.getInformacoes())

# GUI
root = tk.Tk()
root.title("Cadastro de Produtos")

tk.Label(root, text="Tipo:").grid(row=0, column=0)
tipo_var = tk.StringVar()
tipo_menu = tk.OptionMenu(root, tipo_var, "Desktop", "Notebook")
tipo_menu.grid(row=0, column=1)

tk.Label(root, text="Modelo:").grid(row=1, column=0)
entry_modelo = tk.Entry(root)
entry_modelo.grid(row=1, column=1)

tk.Label(root, text="Cor:").grid(row=2, column=0)
entry_cor = tk.Entry(root)
entry_cor.grid(row=2, column=1)

tk.Label(root, text="Preço:").grid(row=3, column=0)
entry_preco = tk.Entry(root)
entry_preco.grid(row=3, column=1)

tk.Label(root, text="Fonte/Bateria:").grid(row=4, column=0)
entry_extra = tk.Entry(root)
entry_extra.grid(row=4, column=1)

tk.Button(root, text="Cadastrar", command=cadastrar_produto).grid(row=5, columnspan=2)

root.mainloop()
