import tkinter as tk
from tkinter import messagebox

class WelcomePage:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Welcome - SkinGlow Beauty")
        self.window.geometry("1000x800")
        self.window.resizable(True, True)
        self.window.configure(bg='#f8f0f3')

        self.center_window()
        self.create_widgets()

    def center_window(self):
        self.window.update_idletasks()
        width = 1000
        height = 800
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')

    def create_fancy_button(self, parent, text, bg_color, text_color, command):
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            bg=bg_color,
            fg=text_color,
            font=("Segoe UI", 13, "bold"),
            relief='flat',
            cursor='hand2',
            width=30,
            height=2
        )
        btn.pack(pady=5)

        btn.bind("<Enter>", lambda e: btn.config(bg="#c93b6e"))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg_color))

    def create_widgets(self):
        main_container = tk.Frame(self.window, bg='#f8f0f3')
        main_container.pack(expand=True, fill='both')

        card = tk.Frame(main_container, bg='white', width=500, height=650)
        card.place(relx=0.5, rely=0.5, anchor='center', width=500, height=650)


        top_strip = tk.Frame(card, bg='#e75480', height=10)
        top_strip.pack(fill='x', side='top')

        content = tk.Frame(card, bg='white')
        content.pack(expand=True, fill='both', padx=40, pady=40)

        tk.Label(content, text="🌸", font=("Segoe UI", 60), bg='white', fg='#e75480').pack(pady=(0, 10))

        tk.Label(
            content,
            text="SkinGlow",
            font=("Segoe UI", 40, "bold"),
            bg='white',
            fg='#e75480'
        ).pack()

        tk.Label(
            content,
            text="B E A U T Y   &   C A R E",
            font=("Segoe UI", 12, "bold"),
            bg='white',
            fg='#01224f'
        ).pack(pady=(0, 40))

        self.create_fancy_button(
            content,
            text="Log In to Dashboard",
            bg_color="#01224f",
            text_color="white",
            command=self.open_login
        )

        tk.Label(content, bg='white', height=1).pack()

        self.create_fancy_button(
            content,
            text="Create New Account",
            bg_color="#e75480",
            text_color="white",
            command=self.open_signup
        )

        tk.Label(
            content,
            text="Version 1.0.0",
            font=("Segoe UI", 8),
            bg='white',
            fg='gray'
        ).pack(side='bottom', pady=(30, 0))

    def open_signup(self):
        self.window.destroy()
        from Sign_up_page import SignUpPage
        SignUpPage().window.mainloop()

    def open_login(self):
        self.window.destroy()
        from Log_in_page import LogInPage
        LogInPage().window.mainloop()

if __name__ == "__main__":
    app = WelcomePage()
    app.window.mainloop()