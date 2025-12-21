import math
import sys
import subprocess
import tkinter as tk
from tkinter import messagebox


class SignUpPage:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sign Up - SkinGlow Beauty")
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

    def create_styled_entry(self, parent, placeholder_text, is_password=False):

        frame = tk.Frame(parent, bg='#f8f0f3')
        frame.pack(fill='x', pady=10)

        tk.Label(frame, text=placeholder_text, font=("Segoe UI", 11), bg='#f8f0f3', fg='#8a6d5b', anchor='w').pack(
            fill='x')

        entry = tk.Entry(
            frame, font=("Segoe UI", 12), bg='#f8f0f3', fg='#01224f', relief='flat',
            show="*" if is_password else ""
        )

        entry.pack(fill='x', pady=(5, 0))

        tk.Frame(frame, bg='#c3a4b4', height=2).pack(fill='x', pady=(2, 0))
        return entry

    def create_widgets(self):
    #================================ left side for the photo =========================================================#
        self.left_frame = tk.Frame(self.window, bg='white', width=500)
        self.left_frame.pack(side='left', fill='both', expand=True)

        self.original_img = tk.PhotoImage(file="images/photo.png")
        img_w = self.original_img.width()
        img_h = self.original_img.height()

        # Ensure we only downscale when the image is larger than the frame
        factor_x = max(1, math.ceil(img_w / 500))
        factor_y = max(1, math.ceil(img_h / 800))
        factor = max(factor_x, factor_y)

        self.final_image = (
            self.original_img.subsample(factor, factor)
            if factor > 1
            else self.original_img
        )

        img_label = tk.Label(self.left_frame, image=self.final_image, bg='white')
        img_label.pack(expand=True)

    #==================================right side for the form=========================================================#

        self.right_frame = tk.Frame(self.window, bg='#f8f0f3', width=500)
        self.right_frame.pack(side='right', fill='both', expand=True)

        form_container = tk.Frame(self.right_frame, bg='#f8f0f3')
        form_container.pack(expand=True, padx=50)

        title_lbl = tk.Label(
            form_container,
            text="Sign Up",
            font=("Segoe UI", 30, "bold"),
            bg='#f8f0f3',
            fg='#e75480'
        )
        title_lbl.pack(pady=(0, 40))

        self.username_entry = self.create_styled_entry(form_container, "Username")
        self.password_entry = self.create_styled_entry(form_container, "Password", is_password=True)
        self.confirm_entry = self.create_styled_entry(form_container, "Confirm Password", is_password=True)

        signup_btn = tk.Button(
            form_container,
            text="Sign up",
            command=self.perform_signup,
            bg='#e75480',
            fg='white',
            font=("Segoe UI", 12, "bold"),
            relief='flat',
            cursor='hand2',
            width=25,
            height=2
        )
        signup_btn.pack(pady=30)

        signup_btn.bind("<Enter>", lambda e: signup_btn.config(bg='#c93b6e'))
        signup_btn.bind("<Leave>", lambda e: signup_btn.config(bg='#e75480'))

        login_frame = tk.Frame(form_container, bg='#f8f0f3')
        login_frame.pack()

        tk.Label(login_frame, text="Already have an account ? ", font=("Segoe UI", 10), bg='#f8f0f3', fg='gray').pack(
            side='left')

        sign_in_link = tk.Label(
            login_frame,
            text="Log in",
            font=("Segoe UI", 10, "bold"),
            bg='#f8f0f3',
            fg='#01224f',
            cursor="hand2"
        )
        sign_in_link.pack(side='left')
        sign_in_link.bind("<Button-1>", lambda e: self.go_to_login())

    def perform_signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm = self.confirm_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please fill all fields")
            return
    
        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        try :
          with open ("users.txt","a") as file :
            file.write (f"{username},{password}\n")
        except:
            pass

        messagebox.showinfo("Success", f"Account created! Welcome, {username}")  #maybe commented if wanted
        self.window.destroy()
        # opening the dashboard
        from main_dashboard import MainDashboard
        MainDashboard(username).run()
        
    def go_to_login(self):
        self.window.destroy()
        from Log_in_page import LogInPage
        LogInPage().window.mainloop()

if __name__ == "__main__":
    app = SignUpPage()
    app.window.mainloop()
