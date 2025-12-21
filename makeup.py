import json
import tkinter as tk
from tkinter import messagebox
import os

class makeup:
    def __init__(self, root, parent=None):
        self.parent = parent
        self.root = tk.Toplevel()
        self.root.title("Women's Makeup")
        self.root.geometry("1200x600")
        
        self.colors = {
            "bg": "#f8f0f3",
            "card": "#FFFFFF",
            "pink": "#FFB6C1",
            "purple": "#D8BFD8",
            "coral": "#FFDAB9",
            "text": "#333333",
            "button": "#9D4D6E",
            "search_bg": "#FFFFFF",
            "search_border": "#FFB6C1",
        }
        
        self.product_descriptions = {
            "Matte Lipstick": "Long-lasting matte lipstick in classic red shade",
            "Foundation": "Full coverage foundation for all skin types",
            "Mascara": "Volumizing mascara for dramatic lashes",
            "Blush": "Soft pink blush for a natural glow",
            "Eyeshadow Palette": "Neutral eyeshadow palette with 12 shades",
            "Eyeliner": "Liquid eyeliner with precise application",
            "Setting Powder": "Translucent setting powder for shine control",
            "Lip Gloss": "Shiny lip gloss with plumping effect"
        }
        
        self.products = [
            ("Matte Lipstick", "$22", "💋", self.colors["pink"]),
            ("Foundation", "$35", "🎨", self.colors["purple"]),
            ("Mascara", "$18", "👁️", self.colors["coral"]),
            ("Blush", "$24", "🌸", self.colors["pink"]),
            ("Eyeshadow Palette", "$32", "🌈", self.colors["purple"]),
            ("Eyeliner", "$16", "✏️", self.colors["coral"]),
            ("Setting Powder", "$26", "🌫️", self.colors["pink"]),
            ("Lip Gloss", "$14", "👄", self.colors["purple"])
        ]
        
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.product_images_paths = {
            "Matte Lipstick": os.path.join(BASE_DIR, "images", "Matte.png"),
            "Foundation": os.path.join(BASE_DIR, "images", "Foundation.png"),
            "Mascara": os.path.join(BASE_DIR, "images", "Mascara.png"),
            "Blush": os.path.join(BASE_DIR, "images", "Blush.png"),
            "Eyeshadow Palette": os.path.join(BASE_DIR, "images", "Eyeshadow.png"),
            "Eyeliner": os.path.join(BASE_DIR, "images", "Eyeliner.png"),
            "Setting Powder": os.path.join(BASE_DIR, "images", "Powder.png"),
            "Lip Gloss": os.path.join(BASE_DIR, "images", "Gloss.png")
        }

        self.product_images = {}
        
        self.root.configure(bg=self.colors["bg"])
        self.show_main_page()
    
    def show_main_page(self):
        """عرض الصفحة الرئيسية"""
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        
        back_button = tk.Button(
            self.root,
            text="← Back",
            font=("Arial", 10, "bold"),
            bg="#3D2D3F",
            fg="white",
            width=10,
            height=1,
            command=self.go_to_main_menu
        )
        back_button.pack(anchor=tk.NW, padx=20, pady=10)
        
        header = tk.Label(
            self.root,
            text="💄 Makeup Section 💄\nFind Your Perfect Look",
            font=("Arial", 16, "bold"),
            bg=self.colors["bg"],
            fg=self.colors["text"],
            justify=tk.CENTER
        )
        header.pack(pady=20)
        
        
        search_frame = tk.Frame(self.root, bg=self.colors["bg"])
        search_frame.pack(pady=(0, 20))
        
        
        search_label = tk.Label(
            search_frame,
            text="🔍 Search Products:",
            font=("Arial", 11, "bold"),
            bg=self.colors["bg"],
            fg=self.colors["text"]
        )
        search_label.pack(side=tk.LEFT, padx=(0, 10))
        
    
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=("Arial", 11),
            bg=self.colors["search_bg"],
            fg=self.colors["text"],
            relief=tk.SOLID,
            borderwidth=2,
            width=30
        )
        self.search_entry.pack(side=tk.LEFT, padx=(0, 10))
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
            bg="#D8BFD8",
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
        """Display products in the products frame"""
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
            relief=tk.RIDGE,
            borderwidth=2,
            width=140,
            height=280
        )
        card.pack(side=tk.LEFT, padx=6, pady=5)
        card.pack_propagate(False)

        #Product image
        img_path = self.product_images_paths.get(name)
        if img_path:
            img = tk.PhotoImage(file=img_path)
            img = img.subsample(5, 5)
            self.product_images[name] = img

            tk.Label(
                card,
                image=img,
                bg=self.colors["card"]
            ).pack(pady=(5, 2))
        
        
        tk.Label(
            card,
            text=f"{emoji} {name}",
            font=("Arial", 10, "bold"),
            bg=self.colors["card"]
        ).pack(pady=8)
        
        
        tk.Label(
            card,
            text=price,
            font=("Arial", 12, "bold"),
            bg=self.colors["card"],
            fg="#FF1493"
        ).pack(pady=3)
        

        add_btn = tk.Button(
            card,
            text="Add +",
            font=("Arial", 9),
            bg=color,
            width=10,
            command=lambda n=name, p=price: self.select_product(n, p)
        )
        add_btn.pack(pady=3)
        
        
        desc_btn = tk.Button(
            card,
            text="View Details",
            font=("Arial", 8),
            bg="#B8486B",
            fg="white",
            width=10,
            command=lambda n=name: self.show_description(n)
        )
        desc_btn.pack(pady=3)
    
    def select_product(self, name, price):
        # Parse price (remove '$' and convert to float)
        try:
            price_float = float(price.replace('$', ''))
        except ValueError:
            messagebox.showerror("Error", "Invalid price format.")
            return
        
        # Load existing cart
        cart_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cart.json')
        try:
            with open(cart_file, 'r') as f:
                cart = json.load(f)
        except FileNotFoundError:
            cart = []
        
        # Add new item
        cart.append({'name': name, 'price': price_float})
        
        # Save back to file
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
        desc_text.config(state=tk.DISABLED)  # جعل النص للقراءة فقط
        
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
        if search_term:
            filtered_products = []
            for name, price, emoji, color in self.products:
                if search_term in name.lower():
                    filtered_products.append((name, price, emoji, color))
            self.display_products(filtered_products)
        else:
            self.display_products(self.products)
    
    def perform_search(self):
    
        self.on_search_change()
    
    def clear_search(self):

        self.search_var.set("")
        self.display_products(self.products)
        self.search_entry.focus_set()
    
    def go_to_main_menu(self):
        self.root.destroy()
        self.parent.show_again()
    
if __name__ == "__main__":
    root = tk.Tk()
    app = makeup(root)
    root.mainloop()