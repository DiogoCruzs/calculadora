"""
Calculadora Simples - Projeto de Segurança e Auditoria de Sistemas
Interface gráfica com Tkinter
"""

import tkinter as tk
from tkinter import messagebox


# ==================== LÓGICA DA CALCULADORA ====================

def somar(a, b):
    """Realiza a soma de dois números."""
    return a + b


def subtrair(a, b):
    """Realiza a subtração de dois números."""
    return a - b


def multiplicar(a, b):
    """Realiza a multiplicação de dois números."""
    return a * b


def dividir(a, b):
    """Realiza a divisão de dois números. Retorna erro se divisor for zero."""
    if b == 0:
        raise ValueError("Erro: Divisão por zero!")
    return a / b


# ==================== INTERFACE GRÁFICA ====================

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("350x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.expressao = ""
        self.criar_interface()

    def criar_interface(self):
        """Cria todos os elementos visuais da calculadora."""

        # --- Display ---
        frame_display = tk.Frame(self.root, bg="#1e1e2e", pady=20, padx=10)
        frame_display.pack(fill="x")

        self.display = tk.Entry(
            frame_display,
            font=("Segoe UI", 28, "bold"),
            bg="#313244",
            fg="#cdd6f4",
            bd=0,
            justify="right",
            insertbackground="#cdd6f4",
            relief="flat",
        )
        self.display.pack(fill="x", ipady=15, padx=5)

        # --- Botões ---
        frame_botoes = tk.Frame(self.root, bg="#1e1e2e")
        frame_botoes.pack(expand=True, fill="both", padx=10, pady=(0, 10))

        botoes = [
            ("C",  0, 0, "#f38ba8"), ("⌫", 0, 1, "#f38ba8"), ("%",  0, 2, "#cba6f7"), ("÷", 0, 3, "#cba6f7"),
            ("7",  1, 0, "#45475a"), ("8",  1, 1, "#45475a"), ("9",  1, 2, "#45475a"), ("×", 1, 3, "#cba6f7"),
            ("4",  2, 0, "#45475a"), ("5",  2, 1, "#45475a"), ("6",  2, 2, "#45475a"), ("−", 2, 3, "#cba6f7"),
            ("1",  3, 0, "#45475a"), ("2",  3, 1, "#45475a"), ("3",  3, 2, "#45475a"), ("+", 3, 3, "#cba6f7"),
            ("±",  4, 0, "#45475a"), ("0",  4, 1, "#45475a"), (".",  4, 2, "#45475a"), ("=", 4, 3, "#a6e3a1"),
        ]

        for (texto, linha, coluna, cor) in botoes:
            btn = tk.Button(
                frame_botoes,
                text=texto,
                font=("Segoe UI", 18, "bold"),
                bg=cor,
                fg="#1e1e2e" if cor == "#a6e3a1" else "#cdd6f4",
                activebackground=cor,
                activeforeground="#1e1e2e",
                bd=0,
                relief="flat",
                cursor="hand2",
                command=lambda t=texto: self.ao_clicar(t),
            )
            btn.grid(row=linha, column=coluna, sticky="nsew", padx=3, pady=3)

        # Configurar grid para expandir
        for i in range(5):
            frame_botoes.rowconfigure(i, weight=1)
        for j in range(4):
            frame_botoes.columnconfigure(j, weight=1)

    def ao_clicar(self, texto):
        """Lida com o clique de cada botão."""
        if texto == "C":
            self.expressao = ""
            self.atualizar_display("")
        elif texto == "⌫":
            self.expressao = self.expressao[:-1]
            self.atualizar_display(self.expressao)
        elif texto == "=":
            self.calcular()
        elif texto == "±":
            self.inverter_sinal()
        elif texto == "÷":
            self.expressao += "/"
            self.atualizar_display(self.expressao)
        elif texto == "×":
            self.expressao += "*"
            self.atualizar_display(self.expressao)
        elif texto == "−":
            self.expressao += "-"
            self.atualizar_display(self.expressao)
        elif texto == "%":
            self.expressao += "/100"
            self.atualizar_display(self.expressao)
        else:
            self.expressao += texto
            self.atualizar_display(self.expressao)

    def atualizar_display(self, valor):
        """Atualiza o texto mostrado no display."""
        self.display.delete(0, tk.END)
        self.display.insert(0, valor)

    def inverter_sinal(self):
        """Inverte o sinal do número atual."""
        try:
            if self.expressao and self.expressao[0] == "-":
                self.expressao = self.expressao[1:]
            else:
                self.expressao = "-" + self.expressao
            self.atualizar_display(self.expressao)
        except Exception:
            pass

    def calcular(self):
        """Avalia a expressão matemática e mostra o resultado."""
        try:
            # Usar as funções definidas para operações simples
            # Para expressões compostas, eval com validação
            expressao_segura = self.expressao.replace("^", "**")

            # Validação de segurança: só permitir caracteres matemáticos
            caracteres_permitidos = set("0123456789+-*/.() ")
            if not all(c in caracteres_permitidos for c in expressao_segura):
                raise ValueError("Caractere inválido na expressão!")

            resultado = eval(expressao_segura)

            # Formatar resultado (remover .0 de inteiros)
            if isinstance(resultado, float) and resultado == int(resultado):
                resultado = int(resultado)

            self.expressao = str(resultado)
            self.atualizar_display(self.expressao)
        except ZeroDivisionError:
            messagebox.showerror("Erro", "Divisão por zero!")
            self.expressao = ""
            self.atualizar_display("")
        except Exception as e:
            messagebox.showerror("Erro", f"Expressão inválida!\n{e}")
            self.expressao = ""
            self.atualizar_display("")


# ==================== EXECUÇÃO ====================

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
