from tkinter import *
import json
from datetime import datetime

class CartPage:
    def __init__(self, parent):
        self.parent = parent
        self.window = Tk()  
        self.window.title("cart")  
        self.window.geometry("1000x800")      
        self.window.resizable(True, True)     
        self.window.configure(bg='#f8f0f3')     
        self.cart = self.load_cart()
        self.create_widgets()  
    
    def load_cart(self):
        try:
            with open('cart.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
     
    def create_widgets(self):
        top_bar = Frame(
            self.window,
            bg="#efe1e6",
            height=140 
        )
        top_bar.pack(fill='x')  
        inner_rect = Frame(
            top_bar,
            bg="#efe1e6",
            height=40    
        )
        inner_rect.pack(expand=False, fill='x', padx=250, pady=30)
        title_frame = Frame(inner_rect, bg="#bf9392")
        title_frame.pack(expand=True)  
        Label(
            title_frame,
            text="Shopping cart 🛒",
            font=("Segoe UI", 28, "bold"),
            bg='#fdf7f7',
            fg='#bf9392' 
        ).pack(side='left')
        main_content = Frame(
            self.window,
            bg="#f8f0f3"
        )
        main_content.pack(fill='both', expand=True)

        items_frame = Frame(main_content, bg="#f8f0f3")
        items_frame.pack(expand=True, fill='both', padx=20, pady=20)

        total = 0
        for item in self.cart:
            item_label = Label(items_frame, text=f"{item['name']} - ${item['price']:.2f}", font=("Arial", 14), bg="#f8f0f3", anchor='w')
            item_label.pack(fill='x', pady=5)
            total += item['price']
        
        total_label = Label(items_frame, text=f"Total: ${total:.2f}", font=("Arial", 16, "bold"), bg="#f8f0f3")
        total_label.pack(pady=20)

        self.back_button()
        self.submit_order()

    def back_button(self):
        back_button = Button(
            self.window,
            text="back",
            font=("italic", 15, "bold"),
            bg="#bf9392",
            fg="white",
            cursor="heart",
            activebackground="white",
            activeforeground="#bf9392",
            command=self.close_window,
            pady=10,
            padx=10)
        back_button.place(x=10, y=25)
    
    def close_window(self):
        self.window.destroy()
        self.parent.show_again()
    
    def run(self):
        self.window.mainloop()

    def submit_order(self):
        back_button = Button(
            self.window,
            text="Buy",
            font=("italic", 15, "bold"),
            bg="#bf9392",
            fg="white",
            cursor="heart",
            activebackground="white",
            activeforeground="#bf9392",
            pady=10,
            padx=10)
        back_button.place(x=750, y=500)

    def submit_order(self):
        buy_button = Button(
            self.window,
            text="Buy",
            font=("italic", 15, "bold"),
            bg="#bf9392",
            fg="white",
            cursor="heart",
            activebackground="white",
            activeforeground="#bf9392",
            command=self.submit_To_orders_history,
            pady=10,
            padx=10)
        buy_button.place(x=750, y=500)
    
    def submit_To_orders_history(self):
        try:
            with open('order_history.json', 'r') as f:
                history = json.load(f)
        except FileNotFoundError:
            history = []

        order = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'items': self.cart.copy(),
            'total': sum(item['price'] for item in self.cart)
        }

        history.append(order)

        with open('order_history.json', 'w') as f:
            json.dump(history, f, indent=4)

        self.cart = []
        with open('cart.json', 'w') as f:
            json.dump(self.cart, f)
        
        from tkinter import messagebox
        messagebox.showinfo("Order Submitted", "Your order has been placed and recorded!")

if __name__ == "__main__":   
    root = Tk()
    root.withdraw()
    app = CartPage(None)
    app.run()