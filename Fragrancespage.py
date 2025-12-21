import os
from tkinter import *
from tkinter import messagebox
from main_dashboard import *
import json
def open_fragrances_page(root_app ):
 def go_back():
        
        window1.destroy()
       
        root_app.show_again()


 

 def add_to_json(product_name, price):
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
    cart.append({'name': product_name, 'price': price_float})
        
        # Save back to file
    with open(cart_file, 'w') as f:
      json.dump(cart, f, indent=4)      

 window1 = Toplevel(root_app.window)

 icon=PhotoImage(file='images/pharmacy.png')
 window1.iconphoto(True,icon)

 window1.geometry("1100x900")

 window1.title("fragrances")

 label=Label(window1,
            text="💗fragrances💗" ,
            font=('Arail','35','bold') ,
            fg="#fdf7f7",
            bg="#875b35",
            relief=RAISED,
           )
 label.pack()
 
 # 1111111111

 card_frame = Frame(window1, 
                      padx=10, 
                      pady=5, 
                      bg="#f9e4b9", 
                      highlightbackground="#e69fb1", 
                      highlightthickness=2) 
 card_frame.pack(side="left", padx=20, pady=10)
 image1=PhotoImage(file="images/botel1.png")
 lb1=Label(card_frame,image=image1)
 lb1.pack() 
 card_frame.image1 = image1
 lb2=Label(card_frame,text="chanel",font=('arail','10','bold'),bg="#f9e4b9",fg="#01224f")
 lb2.pack()

 lbn=Label(card_frame,text="Woody",font=('arail','10','bold'),bg="#f9e4b9",fg="#01224f")
 lbn.pack(pady=5)

 lb3=Label(card_frame,text="price =50$",bg="#f9e4b9",fg="#01224f")
 lb3.pack(pady=5)
 but=Button(card_frame,text="Add to cart",bg="#8a6d5b", fg="#5a3828",cursor="heart",command=lambda: add_to_json("Chanel", "50$"))
 but.pack(pady=7)

 #2222222
 card_frame2 = Frame(window1, 
                      padx=10, 
                      pady=5, 
                      bg="#f9e4b9", 
                      highlightbackground="#e69fb1", 
                      highlightthickness=2) 
 card_frame2.pack(side="left", padx=30, pady=10)
 image2=PhotoImage(file="images/botel2.png")
 lb4=Label(card_frame2,image=image2)
 lb4.pack(padx=15)
 card_frame2.image2 = image2

 lb5=Label(card_frame2,text="Doir",font=('arail','10','bold'),bg="#f9e4b9",fg="#01224f")
 lb5.pack()

 lbn=Label(card_frame2,text="Warm",font=('arail','10','bold'),bg="#f9e4b9",fg="#01224f")
 lbn.pack(pady=5)

 lb6=Label(card_frame2,text="price =60$",bg="#f9e4b9",fg="#01224f")
 lb6.pack(pady=5)

 but=Button(card_frame2,text="Add to cart",bg="#8a6d5b", fg="#5a3828",cursor="heart",command=lambda: add_to_json("Dior", "60$"))
 but.pack(pady=7)

 #333333333
 card_frame3 = Frame(window1, 
                      padx=10, 
                      pady=5, 
                      bg="#f9e4b9", 
                      highlightbackground="#e69fb1", 
                      highlightthickness=2)
 card_frame3.pack(side="left", padx=30, pady=10)
 image3=PhotoImage(file="images/botel3.png")
 lb7=Label(card_frame3,image=image3)
 lb7.pack()
 card_frame3.image3 = image3

 lb8=Label(card_frame3,text=" Burberry",font=('arail','10','bold'),bg="#f9e4b9",fg="#01224f")
 lb8.pack()

 lbn=Label(card_frame3,text="Fresh/Citrus",font=('arail','10','bold'),bg="#f9e4b9",fg="#01224f")
 lbn.pack(pady=5)

 lb9=Label(card_frame3,text="price =40$",bg="#f9e4b9",fg="#01224f")
 lb9.pack(pady=5)

 but=Button(card_frame3,text="Add to cart",bg="#8a6d5b", fg="#5a3828",cursor="heart",command=lambda: add_to_json("Burberry", "40$"))
 but.pack(pady=7)


 #44444444444444
 card_frame4 = Frame(window1, 
                      padx=10, 
                      pady=5, 
                      bg="#f9e4b9",  
                      highlightbackground="#e69fb1", 
                      highlightthickness=2) 
 card_frame4.pack(side="left", padx=30, pady=10)
 image4=PhotoImage(file="images/botel4.png")
 lb10=Label(card_frame4,image=image4)
 lb10.pack()
 card_frame4.image4 = image4

 lb11=Label(card_frame4,text="Creed",font=('arail','10','bold'),bg="#f9e4b9",fg="#01224f")
 lb11.pack()

 lbn=Label(card_frame4,text="Oriental",font=('arail','10','bold'),bg="#f9e4b9",fg="#01224f")
 lbn.pack(pady=5)

 lb12=Label(card_frame4,text="price =77$",bg="#f9e4b9",fg="#01224f")
 lb12.pack(pady=5)
 but=Button(card_frame4,text="Add to cart",bg="#8a6d5b", fg="#5a3828",cursor="heart",command=lambda: add_to_json("Creed", "77$"))
 but.pack(pady=7)

   #55555555555
 card_frame5 = Frame(window1, 
                      padx=10, 
                      pady=5, 
                      bg="#f9e4b9",  
                      highlightbackground="#e69fb1", 
                      highlightthickness=2) 
 card_frame5.pack(side="left", padx=30, pady=10)
 image5=PhotoImage(file="images/botel5.png")
 lb13=Label(card_frame5,image=image5)
 lb13.pack()
 card_frame5.image5 = image5

 lb14=Label(card_frame5,text="Lancome",font=('arail','10','bold'),bg="#f9e4b9",fg="#01224f")
 lb14.pack()

 lbn=Label(card_frame5,text="Floral",font=('arail','10','bold'),bg="#f9e4b9",fg="#01224f")
 lbn.pack(pady=5)

 lb15=Label(card_frame5,text="price =44$",bg="#f9e4b9",fg="#01224f")
 lb15.pack(pady=5)
 but=Button(card_frame5,text="Add to cart",bg="#8a6d5b", fg="#5a3828",cursor="heart",command=lambda: add_to_json("Lancome", "44$"))
 but.pack(pady=7)

  #66666666666
 card_frame6 = Frame(window1, 
                      padx=10, 
                      pady=5, 
                      bg="#f9e4b9",  
                      highlightbackground="#e69fb1", 
                      highlightthickness=2) 
 card_frame6.pack(side="left", padx=30, pady=10)
 image6=PhotoImage(file="images/botel6.png")
 lb16=Label(card_frame6,image=image6)
 lb16.pack()
 card_frame6.image6 = image6

 lb17=Label(card_frame6,text="Bloom",font=('arail','10','bold'),bg="#f9e4b9",fg="#01224f")
 lb17.pack()

 lbn=Label(card_frame6,text="Oriental",font=('arail','10','bold'),bg="#f9e4b9",fg="#01224f")
 lbn.pack(pady=5)

 lb18=Label(card_frame6,text="price =59$",bg="#f9e4b9",fg="#01224f")
 lb18.pack(pady=5)

 but=Button(card_frame6,text="Add to cart",bg="#8a6d5b", fg="#5a3828",cursor="heart",command=lambda: add_to_json("Bloom", "59$"))
 but.pack(pady=7)

 #7777777777
 card_frame7 = Frame(window1, 
                      padx=10, 
                      pady=5, 
                      bg="#f9e4b9",  
                      highlightbackground="#e69fb1", 
                      highlightthickness=2) 
 card_frame7.pack(side="left", padx=30, pady=10)
 image7=PhotoImage(file="images/botel7.png")
 lb19=Label(card_frame7,image=image7)
 lb19.pack()
 card_frame6.image7 = image7

 lb20=Label(card_frame7,text="Sauvage",font=('arail','10','bold'),bg="#f9e4b9",fg="#01224f")
 lb20.pack()

 lbn=Label(card_frame7,text="Floral",font=('arail','10','bold'),bg="#f9e4b9",fg="#01224f")
 lbn.pack(pady=5)

 lb21=Label(card_frame7,text="price =80$",bg="#f9e4b9",fg="#01224f")
 lb21.pack(pady=5)

 but=Button(card_frame7,text="Add to cart",bg="#8a6d5b", fg="#5a3828",cursor="heart",command=lambda: add_to_json("Sauvage", "80$"))
 but.pack(pady=7)

 #==============================================================================================

 ##---------------------------------------------------------------------------------------------
 
 button=Button(window1,text=" ☜(ﾟヮﾟ☜)Back",
 bg="#82400d",
 font=('arail','20','bold'),
 cursor="heart",
 command=go_back,
 activebackground="#B85B6C"
 )
 button.place(x=0,y=1)
 ##========================================================================================
 window1.config(background="#F4E2CB")
