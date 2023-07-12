import tkinter as tk
from clean import Teste

class MyDataAnalysisApp():
    def __init__(self):
        window = tk.Tk()
        self.text_box = tk.Entry(window, width=30)
        self.text_box.pack()
        criar = Teste()
        def button_action():
            input_text = self.text_box.get()
            criar.criar(input_text)
        
        
        
        button = tk.Button(window, text="Clique aqui", command=button_action)
        button.pack()
    
        window.mainloop()

testeaaa = MyDataAnalysisApp()