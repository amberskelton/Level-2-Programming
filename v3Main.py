"""Version 3 Menu Program
   ----------------------
   Menu program with a login, displays the cafe menu,
   allows users to add multiple items to the cart, and ability to pay"""
#imports different modules and their functions
import sys#sys.exit() to exit program
import v3Auth#functions containing authentication processes
import v3Menu#functions containing the menu, ordering and payment processes
#user interface using frames
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import *
from PIL import Image, ImageTk#images

root=tk.Tk()
root.title("BDSC Café Menu")
root.geometry("600x800")

#dictionary containing info on the current logged in user
user_info={
    "id":"",
    "password":""
}

#create frames
fr_welcome=tk.Frame(root,bg="#5b183a")
fr_login=tk.Frame(root,bg="#5b183a")
fr_register=tk.Frame(root,bg="#5b183a")
fr_menu=tk.Frame(root,bg="#5b183a")
fr_history=tk.Frame(root,bg="#5b183a")

#use for loop to bring forward frames
for frame in (fr_welcome,fr_login,fr_register,fr_menu,fr_history):
    frame.place(relwidth=1,relheight=1)

#function to show frame
def show_frame(frame):
    frame.tkraise()

#function for if login chosen
def login_chosen():
    student_id=login_id.get().strip()
    pswd=login_pswd.get().strip()
    if not student_id.isdigit() or len(student_id)!=5:
        messagebox.showerror(title="Error",message="Please enter your 5-number student ID.")
        return
    if pswd=="":
        messagebox.showerror(title="Error",message="Please enter your password.")
        return
    if v3Auth.user_login(student_id,pswd):
        user_info["id"]=student_id
        user_info["password"]=pswd
        messagebox.showinfo(title="Success",message="Login success!")
        login_id.delete(0, tk.END)#clears the entry box after button pressed
        login_pswd.delete(0, tk.END)
        show_frame(fr_menu)
    else:
        if v3Auth.find_acc(student_id):
            messagebox.showerror(title="Error",message="Incorrect password. Please try again.")
        else:
            messagebox.showerror(title="Error",message="This ID has not been registered.")

#function for if register chosen
def register_chosen():
    student_id=register_id.get().strip()
    pswd=register_pswd.get().strip()
    verify=verify_pswd.get().strip()
    if not student_id.isdigit() or len(student_id)!=5:
        messagebox.showerror(title="Error",message="Please enter your 5-number student ID.")
        return
    if pswd=="" or not pswd.isalnum():
        messagebox.showerror(title="Error",message="Please create your password containing only letters and numbers.")
        return
    if verify!=pswd:
        messagebox.showerror(title="Error",message="Passwords do not match.")
        return
    if v3Auth.user_register(student_id,pswd):
        user_info["id"]=student_id
        user_info["password"]=pswd
        messagebox.showinfo(title="Success",message=f'You have been registered.\nYour password is "{pswd}".')
        register_id.delete(0, tk.END)#clears the entry box after button pressed
        register_pswd.delete(0, tk.END)
        show_frame(fr_menu)
    else:
        messagebox.showerror(title="Error",message="This ID has already been registered.\n\nPlease register with another ID, or go back and log in.")

#function that enables/disables the quantity box depending on whether the checkbox is selected/unselected
def toggle_item(checkbox_state,entry):
    if checkbox_state.get():#if checkbox ticked is True, enables quantity box
        entry.config(state="normal")
    else:#if checkbox ticked is False, delete anything in it and disables the quantity box
        entry.delete(0,tk.END)
        entry.config(state="disabled")
        
#function for updating the cart when edited
def refresh_cart():
    lbl_id.config(text=f"ID: {user_info['id']}")#updates the id
    invoice,total=v3Menu.write_invoice(cart)
    show_invoice.delete(0,tk.END)
    for item in cart:
        eqn=item[1]*item[2]
        show_invoice.insert(tk.END,f"{item[0]} x{item[2]} - ${eqn:.2f}")
    lbl_tot.config(text=f"Total: ${total:.2f}")#updates the total

#function for adding to the cart
def select_items():
    #if ticked, get that quantity
    for product in products:
        if products[product].get():
            quantity=qty_boxes[product].get().strip()
            #check for invalid input
            if quantity == "":
                messagebox.showerror("Error",f"Please enter a quantity for {product}")
                return
            if not quantity.isdigit():
                messagebox.showerror("Error",f"Please enter a quantity for {product} in a number more than 0")
                return
            quantity=int(quantity)
            if quantity>10:
                messagebox.showerror("Error",f"You cannot order more than 10 {product}")
                return
            if quantity<=0:
                messagebox.showerror("Error",f"Please enter a quantity for {product} in a number more than 0")
                return
    for product in products:
        if products[product].get():
            quantity=int(qty_boxes[product].get().strip())
            found=False#base is item not in cart
            for item in cart:
                if item[0]==product:#if the product is in the cart
                    item[2]+=quantity#adjust the current quantity in the cart
                    found=True#item in cart
                    break
            if not found:#if not in cart, add the product,etc to the cart
                cart.append([product,prices[product],quantity])#adds a list of the menu item, its price and the quantity set by user into the cart
    refresh_cart()
    for product in products:
        products[product].set(False)#unticks every checkbox
        qty_boxes[product].delete(0,tk.END)#clears every quantity box
        qty_boxes[product].config(state="disabled")#user unable to type in quantity box since the checkbox is unticked

#function for removing from the cart
def remove_item():
    selected=show_invoice.curselection()
    if not selected:#if nothing in the invoice is selected
        messagebox.showerror("Error","Please select an item from the invoice")
        return
    item=cart[selected[0]]
    qty_remove=simpledialog.askinteger("Remove Quantity",f"How many {item[0]} would you like to remove?\n"f"There are currently {item[2]} in the cart")
    if qty_remove==None:#if cancel is presssed
        return
    if qty_remove<=0:
        messagebox.showerror("Error","Please enter a positive number.")
        return
    if qty_remove<item[2]:#removes the desired quantity from the quantity in the cart given it is less than what is in the cart
        item[2]-=qty_remove
    elif qty_remove==item[2]:#if the quantity they want to remove is equal to the amount in the cart, remove the item from the cart entirely
        cart.remove(item)
    else:
        messagebox.showerror("Error","You cannot remove more than what is in the cart.")
        return
    refresh_cart()

#function to clear cart
def clear_cart():
    if len(cart)==0:
        messagebox.showerror("Error","Your cart is already empty")
        return
    cart.clear()
    refresh_cart()
    messagebox.showinfo("Success","Cart cleared")

#function to pay
def pay():
    while True:
        if len(cart)==0:
            messagebox.showerror("Error","Your cart is empty")
            return
        password=simpledialog.askstring("Confirm Password","Please enter your password:",show="*")
        if password==None:#if cancel pressed
            return
        elif password=="":
            messagebox.showerror("Error","Please enter your password")
        elif password!=user_info["password"]:#if the password is incorrect
            messagebox.showerror("Error","Incorrect password, please try again")
        else:#if password correct, write invoice and clear the cart
            invoice,total=v3Menu.write_invoice(cart)
            v3Menu.save_order(user_info["id"],invoice,total)
            messagebox.showinfo("Success","Payment successful!\nPlease pick your order up at the cafe!")
            cart.clear()
            refresh_cart()
            return

#function to view order history
def see_hist():
    history=v3Menu.get_order_hist(user_info["id"])
    #updates the order history
    ord_hist.config(state="normal")
    ord_hist.delete("1.0",tk.END)
    ord_hist.insert("1.0",history)
    ord_hist.config(state="disabled")#user cannot edit the text box
    show_frame(fr_history)
    #if there is no history
    if history=="":
        messagebox.showinfo("Order History","No order history!")
        return

#when logout button is pressed, it clears the cart
def logout():
    cart.clear()
    show_frame(fr_welcome)

#welcome page
fr_title=tk.Frame(fr_welcome,bg="#5b183a")
fr_title.pack()

logo=Image.open("bdsc_logo.png")#image
logo=logo.resize((50,50))
bdsclogo=ImageTk.PhotoImage(logo)

tk.Label(fr_title,padx=20,pady=5,bg="#5b183a",fg="white",text="BDSC CAFÉ",font=("Helvetica Neue",50,"bold")).pack(side="right")
tk.Label(fr_title,pady=5,image=bdsclogo,bg="#5b183a").pack(side="left",pady=10)

foodimg=Image.open("food.png")#image
w,h=foodimg.size
foodimg=foodimg.crop((0,100,w,300))
foodimg=foodimg.resize((520,50))
foodpic=ImageTk.PhotoImage(foodimg)
tk.Label(fr_welcome,pady=5,image=foodpic,bg="#5b183a").pack()

tk.Label(fr_welcome,padx=20,pady=5,bg="#5b183a",fg="white",text="Do you have an existing account or would you like to register?",font=("Opulent",20)).pack()

fr_welc_btns=tk.Frame(fr_welcome,bg="#5b183a")
fr_welc_btns.pack()
tk.Button(fr_welc_btns,text="Login",highlightbackground="#5b183a",font=("Opulent",15,"bold"),command=lambda:show_frame(fr_login)).pack(side="left",pady=5)
tk.Button(fr_welc_btns,text="Register",highlightbackground="#5b183a",font=("Opulent",15,"bold"),command=lambda:show_frame(fr_register)).pack(side="right")

#login page
fr_title2=tk.Frame(fr_login,bg="#5b183a")
fr_title2.pack()

tk.Label(fr_title2,padx=20,pady=5,bg="#5b183a",fg="white",text="BDSC CAFÉ",font=("Helvetica Neue",50,"bold")).pack(side="right")
tk.Label(fr_title2,pady=5,image=bdsclogo,bg="#5b183a").pack(side="left",pady=10)
tk.Label(fr_login,padx=20,pady=5,bg="#5b183a",fg="white",text="LOGIN",font=("Helvetica Neue",30,"bold")).pack()
tk.Label(fr_login,padx=20,pady=5,bg="#5b183a",fg="white",text="Student ID:",font=("Opulent",20)).pack()
login_id=tk.Entry(fr_login,highlightbackground="#5b183a",font=("Opulent",15,"bold"))
login_id.pack()
tk.Label(fr_login,padx=20,pady=5,bg="#5b183a",fg="white",text="Password:",font=("Opulent",20)).pack()
login_pswd=tk.Entry(fr_login,highlightbackground="#5b183a",font=("Opulent",15,"bold"),show="*")
login_pswd.pack()

tk.Button(fr_login,text="Login",highlightbackground="#5b183a",font=("Opulent",15,"bold"),command=login_chosen).pack()
tk.Button(fr_login,text="Back",highlightbackground="#5b183a",font=("Opulent",15,"bold"),command=lambda:show_frame(fr_welcome)).pack()

#register page
fr_title3=tk.Frame(fr_register,bg="#5b183a")
fr_title3.pack()

tk.Label(fr_title3,padx=20,pady=5,bg="#5b183a",fg="white",text="BDSC CAFÉ",font=("Helvetica Neue",50,"bold")).pack(side="right")
tk.Label(fr_title3,pady=5,image=bdsclogo,bg="#5b183a").pack(side="left",pady=10)
tk.Label(fr_register,padx=20,pady=5,bg="#5b183a",fg="white",text="REGISTER",font=("Helvetica Neue",30,"bold")).pack()
tk.Label(fr_register,padx=20,pady=5,bg="#5b183a",fg="white",text="Student ID:",font=("Opulent",20)).pack()
register_id=tk.Entry(fr_register,highlightbackground="#5b183a",font=("Opulent",15,"bold"))
register_id.pack()
tk.Label(fr_register,padx=20,pady=5,bg="#5b183a",fg="white",text="Create password:",font=("Opulent",20)).pack()
register_pswd=tk.Entry(fr_register,highlightbackground="#5b183a",font=("Opulent",15,"bold"),show="*")
register_pswd.pack()
tk.Label(fr_register,padx=20,pady=5,bg="#5b183a",fg="white",text="Verify password:",font=("Opulent",20)).pack()
verify_pswd=tk.Entry(fr_register,highlightbackground="#5b183a",font=("Opulent",15,"bold"),show="*")
verify_pswd.pack()

tk.Button(fr_register,text="Register",highlightbackground="#5b183a",font=("Opulent",15,"bold"),command=register_chosen).pack()
tk.Button(fr_register,text="Back",highlightbackground="#5b183a",font=("Opulent",15,"bold"),command=lambda:show_frame(fr_welcome)).pack()

#menu page
menu=v3Menu.dict_menu()
#empty cart and dictionaries for when user starts ordering
cart=[]
products={}
qty_boxes={}
prices={}

fr_title4=tk.Frame(fr_menu,bg="#5b183a")
fr_title4.pack()

tk.Label(fr_title4,padx=20,pady=5,bg="#5b183a",fg="white",text="BDSC CAFÉ",font=("Helvetica Neue",50,"bold")).pack(side="right")
tk.Label(fr_title4,pady=5,image=bdsclogo,bg="#5b183a").pack(side="left",pady=10)
tk.Label(fr_menu,bg="#5b183a",padx=20,text="Please select the checkboxes and enter the quantity of the item you would like to order!",fg="white",font=("Opulent",15)).pack()
for category,items in menu.items():
    fr_category=tk.Frame(fr_menu,bg="#5b183a")
    fr_category.pack()
    tk.Label(fr_category,bg="#5b183a",fg="white",padx=5,pady=5,text=f"{category}",font=("Opulent",30,"bold")).pack(side="left")
    if category=="Food":
        blueimg=Image.open("blue.png")#image
        blueimg=blueimg.resize((240,2))
        blueline=ImageTk.PhotoImage(blueimg)
        tk.Label(fr_category,pady=5,image=blueline,bg="#5b183a").pack(side="right",pady=10)
    elif category=="Drinks":
        blueimg=blueimg.resize((205,2))
        tk.Label(fr_category,pady=5,image=blueline,bg="#5b183a").pack(side="right",pady=10)
    for product,price in items.items():
        fr_products=tk.Frame(fr_menu,bg="#5b183a")
        fr_products.pack()
        selected=tk.BooleanVar()#changes checkbox to boolean variable for ticked/unticked
        qty_entry=tk.Entry(fr_products,width=5,state="disabled",disabledbackground="#7d3c5d",highlightthickness=0)
        #creates a checkbox for each menu item, calls toggle_item() when ticked/unticked
        tk.Checkbutton(fr_products,bg="#5b183a",text=f"{product}",variable=selected,width=25,anchor="w",font=("Opulent",15,"bold"),fg="white",command=lambda checkbox_state=selected,entry=qty_entry:toggle_item(checkbox_state,entry)).pack(side="left")
        tk.Label(fr_products,bg="#5b183a",fg="white",text=f"${price:.2f}").pack(side="left")
        qty_entry.pack(side="right")
        #obtaining the checkboix, quantity box and price from dictionaries for each product
        products[product]=selected
        qty_boxes[product]=qty_entry
        prices[product]=price

tk.Button(fr_menu,text="Add To Cart",bg="#5b183a",highlightbackground="#5b183a",font=("Opulent",15,"bold"),command=select_items).pack(pady=10)

tk.Label(fr_menu,text=f"Invoice",bg="#5b183a",fg="white",font=("Opulent",30,"bold")).pack()

lbl_id=tk.Label(fr_menu,text=f"ID: {user_info['id']}",bg="#5b183a",fg="white",font=("Opulent",15,"bold"))
lbl_id.pack()

show_invoice=tk.Listbox(fr_menu,width=30,height=5)
show_invoice.pack()

lbl_tot=tk.Label(fr_menu,text="Total: $0.00",bg="#5b183a",fg="white",font=("Opulent",15,"bold"))
lbl_tot.pack()
line_break=tk.Label(fr_menu,text="",bg="#5b183a",fg="white")
line_break.pack()

fr_buttons=tk.Frame(fr_menu,bg="#5b183a")
fr_buttons.pack()
fr_buttons2=tk.Frame(fr_menu,bg="#5b183a")
fr_buttons2.pack()

#order history
fr_title5=tk.Frame(fr_history,bg="#5b183a")
fr_title5.pack()

tk.Label(fr_title5,padx=20,pady=5,bg="#5b183a",fg="white",text="BDSC CAFÉ",font=("Helvetica Neue",50,"bold")).pack(side="right")
tk.Label(fr_title5,pady=5,image=bdsclogo,bg="#5b183a").pack(side="left",pady=10)

tk.Label(fr_history,text="ORDER HISTORY",bg="#5b183a",fg="white",font=("Helvetica Neue",30,"bold")).pack()
ord_hist=tk.Text(fr_history,width=60,height=20)
ord_hist.pack()
tk.Button(fr_history,text="Back",highlightbackground="#5b183a",font=("Opulent",15,"bold"),command=lambda: show_frame(fr_menu)).pack()

tk.Button(fr_buttons,text="Remove Item",highlightbackground="#5b183a",font=("Opulent",15,"bold"),command=remove_item).pack(side="left")
tk.Button(fr_buttons,text="Clear Cart",highlightbackground="#5b183a",font=("Opulent",15,"bold"),command=clear_cart).pack(side="left")
tk.Button(fr_buttons2,text="Pay",highlightbackground="#5b183a",font=("Opulent",15,"bold"),command=pay).pack(side="left")
tk.Button(fr_buttons2,text="Order History",highlightbackground="#5b183a",font=("Opulent",15,"bold"),command=see_hist).pack(side="left")
tk.Button(fr_buttons2,text="Logout",highlightbackground="#5b183a",font=("Opulent",15,"bold"),command=logout).pack(side="left")

#runs the program starting with the welcome frame
show_frame(fr_welcome)
root.mainloop()
