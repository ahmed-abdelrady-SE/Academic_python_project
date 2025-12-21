import tkinter as tk 
class MainDashboard:
    def __init__(self, username):
        self.window = tk.Tk()  
        self.window.title("SkinGlow Beauty")  
        self.window.geometry("1000x800")      
        self.window.resizable(True, True)  
        self.window.configure(bg='#f8f0f3')   
        self.center_window()  
        self.username = username  
        self.create_widgets()  
    def center_window(self):
        self.window.update_idletasks()  
        width = 1000    
        height = 800   
        screen_width = self.window.winfo_screenwidth()    
        screen_height = self.window.winfo_screenheight()  
        x = (screen_width // 2) - (width // 2)      
        y = (screen_height // 2) - (height // 2)    
        self.window.geometry(f'{width}x{height}+{x}+{y}')
    def create_widgets(self):
        # =========== (Header) ===========
        top_bar = tk.Frame(
            self.window,    
            bg='#c3a4b4',
            height=140     
        )
        top_bar.pack(fill='x')  
        # ننشئ إطار داخلي داخل الهيدر
        inner_rect = tk.Frame(
            top_bar,       
            bg='#fdf7f7',   
            height=80       
        )
        inner_rect.pack(expand=False, fill='x', padx=250, pady=30)
        title_frame = tk.Frame(inner_rect, bg='#fdf7f7')
        title_frame.pack(expand=True)  
        tk.Label(
            title_frame,                
            text="✨",               
            font=("Segoe UI", 28, "bold"),  
            bg='#fdf7f7',             
            fg='#FFD700'             
        ).pack(side='left')           
        
        tk.Label(
            title_frame,
            text=" SkinGlow Beauty ",  
            font=("Segoe UI", 28, "bold"),
            bg='#fdf7f7',
            fg='#01224f'               
        ).pack(side='left')

        tk.Label(
            title_frame,
            text="✨",
            font=("Segoe UI", 28, "bold"),
            bg='#fdf7f7',
            fg='#FFD700'
        ).pack(side='left')
        # ===========المحتوى ===========
        main_content = tk.Frame(self.window, bg='#f8f0f3')
        main_content.pack(fill='both', expand=True)
        # =========== رسائل الترحيب ===========
        welcome_frame = tk.Frame(main_content, bg='#f8f0f3')
        welcome_frame.pack(pady=35)  
        tk.Label(
            welcome_frame,
            text=f"🌸 Hello {self.username}! 🌸",  

            font=("Segoe UI", 16, "bold"),
            bg='#f8f0f3',
            fg='#e75480' 
        ).pack()
        tk.Label(
            welcome_frame,
            text="Welcome to your beauty dashboard 💖",
            font=("Segoe UI", 11),  # حجم أصغر
            bg='#f8f0f3',
            fg='#ff69b4'  # وردي فاتح
        ).pack(pady=(3, 0))  
        # =========== 4.  الأزرار الرئيسية ===========
        buttons_container = tk.Frame(main_content, bg='#f8f0f3')
        buttons_container.pack(
            expand=True,    
            fill='both',  
            padx=100,       
            pady=20      
        )
        # =========== 5. الصف الأول من الأزرار (4 أزرار) ===========
        row1_frame = tk.Frame(buttons_container, bg='#f8f0f3')
        row1_frame.pack(pady=(0, 40))  
        #  نعرف بيانات الأزرار في قائمة
        row1_buttons = [
            # (نص الزر, لون الزر, دالة الزر)
            ("🛍️ My Cart", "#f9e4b9", self.open_cart),        
            ("👩‍🦰 Hair Care", "#bf9392", self.open_hair_care),  
            ("🌸 Fragrances", "#ffaca6", self.open_fragrances), 
            ("📋 Order", "#ff8e96", self.open_order)         
        ]
        for text, color, command in row1_buttons:
            #     إطار صغير حول كل زر
            btn_frame = tk.Frame(row1_frame, bg='#f8f0f3')
            btn_frame.pack(
                side='left',    
                padx=15,        
                expand=True     
            )
            #  الزر نفسه
            btn = tk.Button(
                btn_frame,
                text=text,          
                command=command,    
                bg=color,           
                fg='#5a3828',       
                font=("Segoe UI", 13, "bold"),  
                width=14,          
                height=3,        
                relief='flat',     
                borderwidth=0,      
                cursor='heart',     # cursor='heart' يعني شكل الماوس يتحول لقلب لو الاولد مضايقين ممكن نشيله  ❤️
                justify='center',  
                activebackground='#e69fb1',  
                activeforeground='white'     # لون النص لما يكون الزر مضغوط
            )
            btn.pack()          # نعرض الزر في الإطار
            btn.bind("<Enter>", lambda e, b=btn: b.config(
                bg='#e69fb1',    
                fg='white'       
            ))
            btn.bind("<Leave>", lambda e, b=btn, c=color: b.config(
                bg=c,           
                fg='#5a3828'    
            ))
        # ===========. الصف الثاني من الأزرار (3 أزرار) ===========
        row2_frame = tk.Frame(buttons_container, bg='#f8f0f3')
        row2_frame.pack(pady=(0, 50))  
        
        row2_buttons = [
            ("🧔‍♂️ Men's Care", "#01224f", self.open_mens),     
            ("👩‍🦰 Women's Care", "#ffaca6", self.open_womens), 
            ("💄 Makeup", "#ffaca6", self.open_makeup)        
        ]
        for text, color, command in row2_buttons:
            btn_frame = tk.Frame(row2_frame, bg='#f8f0f3')
            btn_frame.pack(side='left', padx=25, expand=True)
            is_blue = (color == "#01224f")  # دى بتطلع True لو اللون أزرق
            btn = tk.Button(
                btn_frame,
                text=text,
                command=command,
                bg=color,
                fg='white' if is_blue else '#5a3828',  
          
                font=("Segoe UI", 13, "bold"),
                width=14,
                height=3,
                relief='flat',
                borderwidth=0,
                cursor='heart',
                justify='center',
                activebackground='#52535c' if is_blue else '#e69fb1',
                activeforeground='white'
            )
            btn.pack()
            if is_blue:  
                btn.bind("<Enter>", lambda e, b=btn: b.config(
                    bg='#52535c' 
                ))
                btn.bind("<Leave>", lambda e, b=btn: b.config(
                    bg='#01224f'  
                ))
            else:  
                btn.bind("<Enter>", lambda e, b=btn: b.config(
                    bg='#e69fb1', 
                    fg='white'    
                ))
                btn.bind("<Leave>", lambda e, b=btn, c=color: b.config(
                    bg=c,       
                    fg='#5a3828'  
                ))
        # ===========. خط فاصل ===========
        separator = tk.Frame(buttons_container, bg='#e69fb1', height=2)
        separator.pack(fill='x', pady=(20, 40))

        # ========== . زر الخروج ===========
        exit_frame = tk.Frame(buttons_container, bg='#f8f0f3')
        exit_frame.pack()
        
        exit_btn = tk.Button(
            exit_frame,
            text="🚪 Exit System ✨",
            command=self.window.quit,  # self.window.quit: يغلق النافذة
            bg='#8a6d5b',    
            fg='white',       
            font=("Segoe UI", 13, "bold"),
            width=22,         
            height=2,         
            relief='flat',
            borderwidth=0,
            cursor='heart',
            activebackground='#655555',   
            activeforeground='white'     
        )
        exit_btn.pack()
        exit_btn.bind("<Enter>", lambda e: exit_btn.config(
            bg='#655555',                   
            text="⛔ Exit System 💔"         
        ))
        exit_btn.bind("<Leave>", lambda e: exit_btn.config(
            bg='#8a6d5b',                    
            text="🚪 Exit System ✨"        
        ))
        # =========== . الفوتر  ===========
        footer = tk.Frame(
            self.window,
            bg='#c3a4b4',    
            height=100       
        )
        footer.pack(fill='x', side='bottom')  
        footer_content = tk.Frame(footer, bg='#c3a4b4')
        footer_content.pack(expand=True, fill='both', pady=25)
        
        tk.Label(
            footer_content,
            text="💖 SkinGlow Beauty © 2024 | Premium Beauty Solutions 💖",
            font=("Segoe UI", 12, "bold"),
            bg='#c3a4b4',
            fg='white' 
        ).pack(expand=True)
        
        tk.Label(
            footer_content,
            text="Elevating Beauty Standards Since 2024",
            font=("Segoe UI", 9, "italic"), 
            bg='#c3a4b4',
            fg='#fdf7f7'  
        ).pack(pady=(5, 0)) 

    def open_cart(self):
        self.window.withdraw()       
        from CartPage import CartPage    
        CartPage(self)                
    #  دالة فتح صفحة عناية الشعر 
    def open_hair_care(self):
        self.window.withdraw()
        from HairCare import HairCarePage  
        HairCarePage(self)                 
    #  دالة فتح صفحة العطور 
    def open_fragrances(self):
        self.window.withdraw()
        from Fragrancespage import open_fragrances_page 
        open_fragrances_page(self)                   
    #  دالة فتح صفحة الطلبات (Order)
    def open_order(self):
        self.window.withdraw()
        from OrderHistory import OrderHistory  
        OrderHistory(self)              
    #  دالة فتح صفحة عناية الرجال
    def open_mens(self):
        self.window.withdraw()
        from mens_skincare import MensSkincarePage
        MensSkincarePage(self)
    #  دالة فتح صفحة عناية النساء
    def open_womens(self):
        self.window.withdraw()
        from womens_skincare import WomensSkincarePage
        WomensSkincarePage(self)
    #  دالة فتح صفحة الماكياج
    def open_makeup(self):
        self.window.withdraw()
        from makeup import makeup
        makeup(self.window, self)
    #  دالة إعادة إظهار النافذة الرئيسية
    def show_again(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.create_widgets() 
        self.window.deiconify()
        self.window.mainloop()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = MainDashboard("Beautiful User")  
    app.run()