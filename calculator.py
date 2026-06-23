import time
import tkinter as tk
from threading import Thread

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("YT: @earllieethecoder")
        
        width, height = 400, 700 
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        self.root.resizable(False, False)
        self.root.configure(bg="black")
        
        self.equation = ""

        self.display = tk.Label(root, text="0", anchor="e", font=("Helvetica", 40), 
                                fg="white", bg="black", padx=25, pady=60)
        self.display.pack(fill="x")

        self.btns_frame = tk.Frame(root, bg="black")
        self.btns_frame.pack(fill="both", expand=True, padx=15, pady=15)

        for i in range(4): self.btns_frame.columnconfigure(i, weight=1)
        for i in range(5): self.btns_frame.rowconfigure(i, weight=1)

        self.create_buttons()

    def create_buttons(self):
        GRAY, DARK, ORANGE = "#A5A5A5", "#333333", "#FF9F0A"
        
        layout = [
            ('AC', GRAY, 'black', 0, 0, 1), ('+/-', GRAY, 'black', 0, 1, 1), ('%', GRAY, 'black', 0, 2, 1), ('÷', ORANGE, 'white', 0, 3, 1),
            ('7', DARK, 'white', 1, 0, 1), ('8', DARK, 'white', 1, 1, 1), ('9', DARK, 'white', 1, 2, 1), ('×', ORANGE, 'white', 1, 3, 1),
            ('4', DARK, 'white', 2, 0, 1), ('5', DARK, 'white', 2, 1, 1), ('6', DARK, 'white', 2, 2, 1), ('-', ORANGE, 'white', 2, 3, 1),
            ('1', DARK, 'white', 3, 0, 1), ('2', DARK, 'white', 3, 1, 1), ('3', DARK, 'white', 3, 2, 1), ('+', ORANGE, 'white', 3, 3, 1),
            ('0', DARK, 'white', 4, 0, 2), ('.', DARK, 'white', 4, 2, 1), ('=', ORANGE, 'white', 4, 3, 1)
        ]

        for (txt, bg, fg, r, c, sp) in layout:
            btn = tk.Button(self.btns_frame, text=txt, bg=bg, fg=fg, 
                            font=("Helvetica", 20, "bold"), bd=0,
                            highlightthickness=0, command=lambda t=txt: self.press(t))
            btn.grid(row=r, column=c, columnspan=sp, sticky="nsew", padx=5, pady=5)

    def press(self, key):
        if key == "=":
            if self.equation == "7+8":
                self.btns_frame.pack_forget()
                Thread(target=self.play_centered_lyrics).start()
            else:
                try:
                    self.equation = str(eval(self.equation.replace('×', '*').replace('÷', '/')))
                    self.display.config(text=self.equation)
                except: self.display.config(text="Error")
        elif key == "AC":
            self.equation = ""
            self.display.config(text="0")
        else:
            self.equation += str(key)
            self.display.config(text=self.equation)

    def play_centered_lyrics(self):
        self.display.pack(fill="both", expand=True) 
        self.display.config(anchor="center", justify="center", font=("Helvetica", 22, "bold"))
        
        lines = [
            "Tanging ikaw lamang",
            "Ang aking iibigin", 
            "Walang ibang hiling",
            "Kundi ang yakap",
            "Mo't halik"
        ]

        for line in lines:
            self.display.config(text="")
            curr = ""
            for char in line:
                curr += char
                self.display.config(text=curr)
                self.root.update()
                time.sleep(0.12)
            time.sleep(1.8)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
