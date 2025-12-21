import json
import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk

class HairCarePage:
    def __init__(self, dashboard):
        self.dashboard = dashboard
        self.root = tk.Toplevel()
        self.root.title("Hair Care")
        self.root.geometry("1200x700")
        
        self.colors = {
            "bg": "#fbe9e3",
            "card": "#ffffff",
            "pink": "#f4c7b7",
            "coral": "#FFDAB9",
            "yellow": "#F8ECA7",
            "text": "#c5897a",
            "button": "#d89b8c",
            "search_bg": "#FFFFFF",
            "search_border": "#FFB6C1",
            "white": "#FFFFFF"
        }
        
        self.product_descriptions = {
            "Heat Protector": "Protects hair from heat damage caused by blow dryers, straighteners, and curling irons",
            "Hair Serum": "Nourishing serum that adds shine, reduces frizz, and repairs damaged hair",
            "Hair Oil": "Deeply moisturizing oil that strengthens hair and prevents split ends",
            "Shampoo": "Gentle cleansing shampoo that removes buildup without stripping natural oils",
            "Conditioner": "Hydrating conditioner that smooths hair and improves manageability",
            "Hair Mask": "Intensive repair mask that restores moisture and softness to dry or damaged hair",
            "Leave-in Cream": "Lightweight leave-in cream that moisturizes hair and controls frizz all day",
            "Scalp Treatment": "Soothing treatment that nourishes the scalp and promotes healthy hair growth"
        }

        self.products = [
            ("Heat Protector", "$22", "🔥", self.colors["pink"]),
            ("Hair Serum", "$30", "💧", self.colors["coral"]),
            ("Hair Oil", "$26", "🧴", self.colors["yellow"]),
            ("Shampoo", "$18", "🧴", self.colors["pink"]),
            ("Conditioner", "$20","🧴", self.colors["coral"]),
            ("Hair Mask", "$24", "🎭", self.colors["yellow"]),
            ("Leave-in Cream", "$21", "🧴",self.colors["pink"]),
            ("Scalp Treatment", "$28", "🌿", self.colors["coral"])
        ]

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.product_images_paths = {
            "Conditioner": os.path.join(BASE_DIR, "images/conditioner.png"),
            "Hair Mask": os.path.join(BASE_DIR, "images/hairMask.png"),
            "Hair Oil": os.path.join(BASE_DIR, "images/hairOil.png"),
            "Hair Serum": os.path.join(BASE_DIR, "images/HairSerum.png"),
            "Heat Protector": os.path.join(BASE_DIR, "images/heatProtectant.png"),
            "Leave-in Cream": os.path.join(BASE_DIR, "images/LeaveInCream.png"),
            "Scalp Treatment": os.path.join(BASE_DIR, "images/scalpTreatment.png"),
            "Shampoo": os.path.join(BASE_DIR, "images/shampoo.png")
        }

        self.product_images = {}

        self.root.configure(bg=self.colors["bg"])
        self.show_main_page()
    
    def show_main_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        back_button = tk.Button(
            self.root,
            text="← Back",
            font=("Arial", 10, "bold"),
            bg="#27272a",
            fg="white",
            width=10,
            height=1,
            command=self.back_to_dashboard
        )
        back_button.pack(anchor=tk.NW, padx=20, pady=10)
        
        header = tk.Label(
            self.root,
            text="Elite Hair Care.",
            font=("Arial", 45, "bold"),
            bg=self.colors["bg"],
            fg=self.colors["text"],
            justify=tk.CENTER
        )
        header.pack(pady=(10, 15))

        header = tk.Label(
            self.root,
            text="Professional solutions for your hair.",
            font=("Arial", 12),
            bg=self.colors["bg"],
            fg=self.colors["text"],
            justify=tk.CENTER
        )
        header.pack(pady=(0, 80))
        

        search_frame = tk.Frame(self.root, bg=self.colors["bg"])
        search_frame.pack(pady=(0, 20))
        
        self.search_var = tk.StringVar()

        self.search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=("Arial", 11),
            bg=self.colors["search_bg"],
            fg=self.colors["text"],
            relief=tk.FLAT,
            highlightbackground=self.colors["pink"],
            highlightthickness=2,
            width=40,
            justify='center'
        )
        self.search_entry.pack(side=tk.LEFT, padx=(0, 20))

       
        self.search_entry.insert(0, "🔍 Search Products...")
        self.search_entry.config(fg="#AAAAAA") 
     
        def on_entry_click(event):
            if self.search_var.get() == "🔍 Search Products...":
                self.search_entry.delete(0, tk.END)
                self.search_entry.config(fg=self.colors["text"]) 
        def on_focusout(event):
            if self.search_var.get().strip() == "":
                self.search_entry.insert(0, "🔍 Search Products...")
                self.search_entry.config(fg="#AAAAAA")

        self.search_entry.bind("<FocusIn>", on_entry_click)
        self.search_entry.bind("<FocusOut>", on_focusout)
        self.search_entry.bind("<KeyRelease>", self.on_search_change)

     
        search_button = tk.Button(
            search_frame,
            text="Search",
            font=("Arial", 10, "bold"),
            bg=self.colors["button"],
            fg="white",
            width=10,
            command=self.perform_search
        )
        search_button.pack(side=tk.LEFT)

        clear_button = tk.Button(
            search_frame,
            text="Clear",
            font=("Arial", 10),
            bg=self.colors["white"],
            fg=self.colors["text"],
            width=8,
            command=self.clear_search
        )
        clear_button.pack(side=tk.LEFT, padx=(10, 0))
        
      
        self.products_frame = tk.Frame(self.root, bg=self.colors["bg"])
        self.products_frame.pack(pady=10)
        
        self.display_products(self.products)
        
        note_label = tk.Label(
            self.root,
            text="💡 Click 'View Details' to see product description\n🛒 Click 'Add +' to add product to cart",
            font=("Arial", 10),
            bg=self.colors["bg"],
            fg=self.colors["text"],
            justify=tk.CENTER
        )
        note_label.pack(pady=10)
    
    def display_products(self, products_list):
        for widget in self.products_frame.winfo_children():
            widget.destroy()
        
        if products_list:
            for name, price, emoji, color in products_list:
                self.create_product_card(self.products_frame, name, price, emoji, color)
        else:
            no_results = tk.Label(
                self.products_frame,
                text="No products found. Try a different search term.",
                font=("Arial", 12, "italic"),
                bg=self.colors["bg"],
                fg=self.colors["text"]
            )
            no_results.pack(pady=50)
    
    def create_product_card(self, parent, name, price, emoji, color):
        card = tk.Frame(
        parent,
        bg=self.colors["card"],
        relief=tk.FLAT,                   
        highlightbackground="#d89b8c",    
        highlightthickness=2,             
        width=140,                    
        height=280
        )
        card.pack(side=tk.LEFT, padx=15, pady=15)
        card.pack_propagate(False)

        img_path = self.product_images_paths.get(name)
        if img_path and os.path.exists(img_path):
            try:
                pil_image = Image.open(img_path)
                pil_image = pil_image.resize((100, 100), Image.LANCZOS)
                img = ImageTk.PhotoImage(pil_image)
                self.product_images[name] = img
                tk.Label(card, image=img, bg=self.colors["card"]).pack(pady=(10, 5))
            except Exception as e:
                print(f"خطأ في تحميل الصورة {name}: {e}")
                tk.Label(card, text="🖼️\nImage\nError", font=("Arial", 8), bg=self.colors["card"], fg="gray").pack(pady=(10, 5))
        else:
            tk.Label(card, text="🖼️\nNo\nImage", font=("Arial", 8), bg=self.colors["card"], fg="gray").pack(pady=(10, 5))
        
        tk.Label(
            card,
            text=f"{emoji} {name}",
            font=("Arial", 10, "bold"),
            bg=self.colors["card"],
            fg="#c5897a"
        ).pack(pady=8)
        
        tk.Label(
            card,
            text=price,
            font=("Arial", 12, "bold"),
            bg=self.colors["card"],
            fg="#e7a8a1"
        ).pack(pady=3)
        
        add_btn = tk.Button(
            card,
            text="Add +",
            font=("Arial", 9),
            bg=self.colors["pink"],
            width=10,
            command=lambda n=name, p=price: self.select_product(n, p)
        )
        add_btn.pack(pady=3)
        
        desc_btn = tk.Button(
            card,
            text="View Details",
            font=("Arial", 8),
            bg="#d89b8c",
            fg="white",
            width=10,
            command=lambda n=name: self.show_description(n)
        )
        desc_btn.pack(pady=3)
    
    def select_product(self, name, price):
        try:
            price_float = float(price.replace('$', ''))
        except ValueError:
            messagebox.showerror("Error", "Invalid price format.")
            return
        
        cart_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cart.json')
        try:
            with open(cart_file, 'r') as f:
                cart = json.load(f)
        except FileNotFoundError:
            cart = []
        
        cart.append({'name': name, 'price': price_float})
        
        with open(cart_file, 'w') as f:
            json.dump(cart, f, indent=4)
        
        messagebox.showinfo("Added to Cart", f"✅ {name}\n💰 Price: {price}")
    
    def show_description(self, product_name):
        description = self.product_descriptions.get(product_name, "No description available.")
        
        desc_window = tk.Toplevel(self.root)
        desc_window.title(f"{product_name} - Description")
        desc_window.geometry("400x250")
        desc_window.configure(bg=self.colors["bg"])
        desc_window.resizable(False, False)
        
        tk.Label(
            desc_window,
            text=f"📖 {product_name}",
            font=("Arial", 14, "bold"),
            bg=self.colors["bg"],
            fg=self.colors["text"]
        ).pack(pady=20)
        
        desc_text = tk.Text(
            desc_window,
            font=("Arial", 11),
            bg="white",
            fg=self.colors["text"],
            height=6,
            width=40,
            wrap=tk.WORD,
            relief=tk.FLAT
        )
        desc_text.pack(pady=10, padx=20)
        desc_text.insert(tk.END, description)
        desc_text.config(state=tk.DISABLED)
        
        tk.Button(
            desc_window,
            text="Close",
            font=("Arial", 10, "bold"),
            bg=self.colors["button"],
            fg="white",
            width=15,
            command=desc_window.destroy
        ).pack(pady=10)
    
    def on_search_change(self, event=None):
        search_term = self.search_var.get().lower().strip()
        if search_term and search_term != "🔍 search products...":
            filtered_products = [p for p in self.products if search_term in p[0].lower()]
            self.display_products(filtered_products)
        else:
            self.display_products(self.products)
    
    def perform_search(self):
        self.on_search_change()
    
    def clear_search(self):
        self.search_var.set("")
        self.display_products(self.products)
        self.search_entry.focus_set()
    
    def back_to_dashboard(self):
        self.root.destroy()
        self.dashboard.show_again()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = HairCarePage(root)
    root.mainloop()