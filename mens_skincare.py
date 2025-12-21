import json
import tkinter as tk
from tkinter import messagebox
import os

class MensSkincarePage:
    def __init__(self, dashboard):
        self.dashboard = dashboard
        self.root = tk.Toplevel()
        self.root.title("men's Skincare")
        self.root.geometry("1200x700")
        
        self.colors = {
            "bg": "#d2f1fe",
            "card": "#FFFFFF",
            "blue": "#B6E5FF",
            "gray": "#696A6A",
            "light_gray": "#A0A0A0",
            "text": "#333333",
            "button": "#1735CA",
            "search_bg": "#FFFFFF",
            "search_border": "#7D8181",
        }
        
        self.product_descriptions = {
            "Face Cream": "Hydrating moisturizer with SPF 30 for all-day protection",
            "Serum": "Vitamin C serum for brightening and anti-aging benefits",
            "Sunscreen": "Broad spectrum SPF 50+ for maximum sun protection",
            "Cleanser": "Gentle foaming cleanser that removes makeup and impurities",
            "Shaving Foam": "Rich protective foam that delivers a clean, comfortable shave",
            "Eye Cream": "Anti-aging cream to reduce dark circles and puffiness",
            "Mask": "Clay mask for deep cleansing and pore refinement",
            "Beard Oil": "Light nourishing oil that softens beard hair and moisturizes skin beneath"
        }
        
        self.products = [
            ("Face Cream", "$24", "🧴", self.colors["blue"]),
            ("Serum", "$36", "💧", self.colors["gray"]),
            ("Sunscreen", "$20", "☀️", self.colors["light_gray"]),
            ("Cleanser", "$16", "✨", self.colors["blue"]),
            ("Shaving Foam", "$18", "💦", self.colors["gray"]),
            ("Eye Cream", "$28", "👁️", self.colors["light_gray"]),
            ("Mask", "$14", "🎭", self.colors["blue"]),
            ("Beard Oil", "$10", "✨", self.colors["gray"])
        ]

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.product_images_paths = {
            "Face Cream": os.path.join(BASE_DIR, "images", "cream.png"),
            "Serum": os.path.join(BASE_DIR, "images", "serum2.png"),
            "Sunscreen": os.path.join(BASE_DIR, "images", "sunscreen2.png"),
            "Cleanser": os.path.join(BASE_DIR, "images", "Cleanser.png"),
            "Shaving Foam": os.path.join(BASE_DIR, "images", "Shaving Foam.png"),
            "Eye Cream": os.path.join(BASE_DIR, "images", "eyecream.png"),
            "Mask": os.path.join(BASE_DIR, "images", "mask2.png"),
            "Beard Oil": os.path.join(BASE_DIR, "images", "Beard Oil.png")
        }

        self.product_images = {}

        
        self.root.configure(bg=self.colors["bg"])
        self.show_main_page()
    
    def show_main_page(self):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Back button
        back_button = tk.Button(
            self.root,
            text="← Back",
            font=("Arial", 10, "bold"),
            bg="#494448",
            fg="white",
            width=10,
            height=1,
            command=self.back_to_dashboard
        )
        back_button.pack(anchor=tk.NW, padx=20, pady=10)
        
        # Header
        header = tk.Label(
            self.root,
            text="✨Hello Beautiful User!✨\nWelcome to men's care section ♡",
            font=("Arial", 16, "bold"),
            bg=self.colors["bg"],
            fg=self.colors["text"],
            justify=tk.CENTER
        )
        header.pack(pady=(10, 20))
        
        # Search frame
        search_frame = tk.Frame(self.root, bg=self.colors["bg"])
        search_frame.pack(pady=(0, 20))
        
        # Search label
        search_label = tk.Label(
            search_frame,
            text="🔍 Search Products:",
            font=("Arial", 11, "bold"),
            bg=self.colors["bg"],
            fg=self.colors["text"]
        )
        search_label.pack(side=tk.LEFT, padx=(0, 10))
        
        # Search entry
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
        
        # Search button
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
        
        # Clear search button
        clear_button = tk.Button(
            search_frame,
            text="Clear",
            font=("Arial", 10),
            bg=self.colors["gray"],
            fg=self.colors["text"],
            width=8,
            command=self.clear_search
        )
        clear_button.pack(side=tk.LEFT, padx=(10, 0))
        
        # Products container frame
        self.products_frame = tk.Frame(self.root, bg=self.colors["bg"])
        self.products_frame.pack(pady=10)
        
        # Display all products initially
        self.display_products(self.products)
        
        # Note label
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
        # Clear existing products
        for widget in self.products_frame.winfo_children():
            widget.destroy()
        
        # Display products
        if products_list:
            for name, price, emoji, color in products_list:
                self.create_product_card(self.products_frame, name, price, emoji, color)
        else:
            # Show message when no products found
            no_results = tk.Label(
                self.products_frame,
                text="No products found. Try a different search term.",
                font=("Arial", 12, "italic"),
                bg=self.colors["bg"],
                fg=self.colors["text"]
            )
            no_results.pack(pady=50)
    
    def create_product_card(self, parent, name, price, emoji, color):
        # Create product card frame
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
        
        # Product name with emoji
        tk.Label(
            card,
            text=f"{emoji} {name}",
            font=("Arial", 10, "bold"),
            bg=self.colors["card"]
        ).pack(pady=8)
        
        # Price
        tk.Label(
            card,
            text=price,
            font=("Arial", 12, "bold"),
            bg=self.colors["card"],
            fg="#012FB9"
        ).pack(pady=3)
        
        # Add to cart button
        add_btn = tk.Button(
            card,
            text="Add +",
            font=("Arial", 9),
            bg=color,
            width=10,
            command=lambda n=name, p=price: self.select_product(n, p)
        )
        add_btn.pack(pady=3)
        
        # View details button
        desc_btn = tk.Button(
            card,
            text="View Details",
            font=("Arial", 8),
            bg="#012FB9",
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
        """Filter products as user types"""
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
        """Perform search when search button is clicked"""
        self.on_search_change()
    
    def clear_search(self):
        """Clear search field and show all products"""
        self.search_var.set("")
        self.display_products(self.products)
        self.search_entry.focus_set()
    
    def back_to_dashboard(self):
        self.root.destroy()
        self.dashboard.show_again()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = MensSkincarePage(root)
    root.mainloop()
