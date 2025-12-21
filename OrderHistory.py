from tkinter import *
import json

class OrderHistory:
    def __init__(self, parent):
        self.parent = parent
        self.window = Tk()  
        self.window.title("Order History")  
        self.window.geometry("1000x800")      
        self.window.resizable(True, True)     
        self.window.configure(bg='#f8f0f3')     
        self.history = self.load_history()
        self.create_widgets()  
    
    def load_history(self):
        try:
            with open('order_history.json', 'r') as f:
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
            text="Order History 📋",
            font=("Segoe UI", 28, "bold"),
            bg='#fdf7f7',
            fg='#bf9392' 
        ).pack(side='left')
        main_content = Frame(
            self.window,
            bg="#f8f0f3"
        )
        main_content.pack(fill='both', expand=True)
        
        # Frame for history items inside main_content
        items_frame = Frame(main_content, bg="#f8f0f3")
        items_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Display order history
        if self.history:
            for order in self.history:
                order_frame = Frame(items_frame, bg="#ffffff", relief="ridge", borderwidth=2)
                order_frame.pack(fill='x', pady=10, padx=10)
                
                timestamp_label = Label(order_frame, text=f"Order Date: {order['timestamp']}", font=("Arial", 12, "bold"), bg="#ffffff")
                timestamp_label.pack(anchor='w', padx=10, pady=5)
                
                total_label = Label(order_frame, text=f"Total: ${order['total']:.2f}", font=("Arial", 12), bg="#ffffff")
                total_label.pack(anchor='w', padx=10, pady=5)
                
                items_text = "\n".join([f"{item['name']} - ${item['price']:.2f}" for item in order['items']])
                items_label = Label(order_frame, text=f"Items:\n{items_text}", font=("Arial", 10), bg="#ffffff", justify='left')
                items_label.pack(anchor='w', padx=10, pady=5)
        else:
            no_history_label = Label(items_frame, text="No order history found.", font=("Arial", 14), bg="#f8f0f3")
            no_history_label.pack(pady=50)

        self.back_button()
    
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

if __name__ == "__main__":   
    root = Tk()
    root.withdraw()
    app = OrderHistory(None)
    app.run()