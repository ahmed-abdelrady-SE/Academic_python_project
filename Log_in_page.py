import math
import os
import tkinter as tk
from tkinter import messagebox
import sqlite3

class LogInPage:
	def __init__(self):
		self.window = tk.Tk()
		self.window.title("Log In - SkinGlow Beauty")
		self.window.geometry("1000x800")
		self.window.resizable(True, True)
		self.window.configure(bg='#f8f0f3')
		# Build our credential store before wiring up the UI
		self.credentials, self.display_usernames = self._build_credentials()
		self.center_window()
		self.create_widgets()

	def _build_credentials(self):
		credentials = {}
		display_names = []
		if not os.path.exists("users.txt"):
			open("users.txt", "a").close()

		with open("users.txt", "r") as file:
			for line in file:
				line = line.strip()
				if not line:
					continue

				try:
					username, password = line.split(",", 1)
				except ValueError:
					continue

				username = username.strip()
				password = password.strip()

				credentials[username.lower()] = {
					"display": username,
					"password": password
				}
				display_names.append(username)

		
		display_names.sort(key=str.lower)

		return credentials, display_names


	def center_window(self):
		# Center the window on the current display
		self.window.update_idletasks()
		width = 1000
		height = 800
		x = (self.window.winfo_screenwidth() // 2) - (width // 2)
		y = (self.window.winfo_screenheight() // 2) - (height // 2)
		self.window.geometry(f'{width}x{height}+{x}+{y}')

	def create_styled_entry(self, parent, placeholder_text, is_password=False):
		# Helper to keep all entry fields visually consistent
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
		# Build the two-pane layout with media on the left and the form on the right
		# left frame for photo
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

		# right frame for form
		self.right_frame = tk.Frame(self.window, bg='#f8f0f3', width=500)
		self.right_frame.pack(side='right', fill='both', expand=True)

		form_container = tk.Frame(self.right_frame, bg='#f8f0f3')
		form_container.pack(expand=True, padx=50)

		title_lbl = tk.Label(
			form_container,
			text="Welcome Back",
			font=("Segoe UI", 30, "bold"),
			bg='#f8f0f3',
			fg='#e75480'
		)
		title_lbl.pack(pady=(0, 40))
		self.username_entry = self.create_styled_entry(form_container, "Username")
		self.password_entry = self.create_styled_entry(form_container, "Password", is_password=True)

		login_btn = tk.Button(
			form_container,
			text="Log in",
			command=self.perform_login,
			bg='#01224f',
			fg='white',
			font=("Segoe UI", 12, "bold"),
			relief='flat',
			cursor='hand2',
			width=25,
			height=2
		)

		login_btn.pack(pady=30)
		login_btn.bind("<Enter>", lambda e: login_btn.config(bg='#274b7a'))
		login_btn.bind("<Leave>", lambda e: login_btn.config(bg='#01224f'))

		signup_frame = tk.Frame(form_container, bg='#f8f0f3')
		signup_frame.pack()
		tk.Label(
			signup_frame,
			text="Need an account? ",
			font=("Segoe UI", 10),
			bg='#f8f0f3',
			fg='gray'
		).pack(side='left')

		sign_up_link = tk.Label(
			signup_frame,
			text="Sign up",
			font=("Segoe UI", 10, "bold"),
			bg='#f8f0f3',
			fg='#e75480',
			cursor="hand2"
		)
		sign_up_link.pack(side='left')
		sign_up_link.bind("<Button-1>", lambda e: self.go_to_signup())

	def perform_login(self):
		# Validate credentials and route successful logins to the dashboard
		username = self.username_entry.get().strip().lower()
		password = self.password_entry.get()

		if not username or not password:
			messagebox.showerror("Error", "Please fill all fields")
			return

		record = self.credentials.get(username)

		if not record or record["password"] != password:
			messagebox.showerror("Error", "Invalid username or password")
			return

		display_name = record["display"]
		messagebox.showinfo("Success", f"Welcome back, {display_name}!")
		self.window.destroy()

		from main_dashboard import MainDashboard
		MainDashboard(display_name).run()

	def go_to_signup(self):
		self.window.destroy()
		from Sign_up_page import SignUpPage
		SignUpPage().window.mainloop()

		
if __name__ == "__main__":
	app = LogInPage()
	app.window.mainloop()
