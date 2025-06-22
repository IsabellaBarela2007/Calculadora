import tkinter as tk
from calculadora_lógica import Calculadora

class CalculadoraApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        master.geometry("400x550")
        master.configure(bg="#222831")

        self.calc = Calculadora()  # Instância da lógica

        master.rowconfigure(1, weight=1)
        master.columnconfigure(0, weight=1)

        self.display = tk.Label(master, text="", anchor='e', bg="#393E46", fg="#EEEEEE",
                                font=("Helvetica", 40), relief="sunken", bd=3, padx=10, pady=20)
        self.display.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        self.btn_frame = tk.Frame(master, bg="#222831")
        self.btn_frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

        for i in range(5):
            self.btn_frame.rowconfigure(i, weight=1)
        for j in range(4):
            self.btn_frame.columnconfigure(j, weight=1)

        botoes = [
            ('C', '#EEEEEE', '#00ADB5'),
            ('←', '#EEEEEE', '#00ADB5'),
            ('%', '#EEEEEE', '#00ADB5'),
            ('÷', '#EEEEEE', '#393E46'),

            ('7', '#EEEEEE', '#393E46'),
            ('8', '#EEEEEE', '#393E46'),
            ('9', '#EEEEEE', '#393E46'),
            ('×', '#EEEEEE', '#393E46'),

            ('4', '#EEEEEE', '#393E46'),
            ('5', '#EEEEEE', '#393E46'),
            ('6', '#EEEEEE', '#393E46'),
            ('-', '#EEEEEE', '#393E46'),

            ('1', '#EEEEEE', '#393E46'),
            ('2', '#EEEEEE', '#393E46'),
            ('3', '#EEEEEE', '#393E46'),
            ('+', '#EEEEEE', '#393E46'),

            ('00', '#EEEEEE', '#393E46'),
            ('0', '#EEEEEE', '#393E46'),
            ('.', '#EEEEEE', '#393E46'),
            ('=', '#EEEEEE', '#00ADB5'),
        ]

        row = 0
        col = 0
        for (text, fg, bg) in botoes:
            btn = tk.Button(self.btn_frame, text=text, fg=fg, bg=bg, font=("Helvetica", 24, "bold"),
                            relief="flat", bd=0,
                            command=lambda t=text: self.botao_clicado(t))
            btn.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def botao_clicado(self, valor):
        if valor == 'C':
            self.calc.limpar()
            self.atualizar_display()
        elif valor == '←':
            self.calc.apagar_ultimo()
            self.atualizar_display()
        elif valor == '=':
            resultado = self.calc.calcular()
            self.display.config(text=resultado)
        elif valor == '%':
            resultado = self.calc.calcular_porcentagem()
            self.display.config(text=resultado)
        else:
            self.calc.inserir(valor)
            self.atualizar_display()

    def atualizar_display(self):
        self.display.config(text=self.calc.expressao)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()
