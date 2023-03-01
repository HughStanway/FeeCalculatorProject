#Import the required libraries
from tkinter import *

#Create an instance of tkinter frame and set geometry of the frame
win= Tk()
win.geometry("600x300")
win.title("Fee Calculator")

#Create a frame
frame = Frame(win)
frame.pack(side="top", expand=True, fill="both")

#Inital page - welcome message and currency selction
def start_page():
    for widgets in frame.winfo_children():
        widgets.destroy() 

    def pound():
        print("POUND") 
        for widgets in frame.winfo_children():
           widgets.destroy()
        
        def ebay_function():
            print("EBAY")
            for widgets in frame.winfo_children():
               widgets.destroy()
    
            def display_text(): 
               nonlocal entry_ebay
               string_price = entry_ebay.get() 
               print(string_price)
    
               nonlocal entry_shipping 
               string_shipping = entry_shipping.get()
               print(string_shipping)
    
               payment = int(string_price)
               shipping =int(string_shipping)
    
               payout = round((((0.872 * payment)-0.3) - shipping), 2)
               print(payout)
               message = '£', payout
               Label(frame, text = "Your final payout will be: \n").pack() 
               Label(frame, text = message).pack() 
    
            #Ebay Selcetion Code
            Button(frame, text="Back", command = pound).place(x=0,y=0)
            Label(frame, text= "Ebays current fees are 12.8% plus 30p of the final value of the order \n").pack() 
            Label(frame, text = "PLease enter your final sale price: \n").pack()
            entry_ebay = Entry(frame)
            entry_ebay.focus_set() 
            entry_ebay.pack() 
    
            Label(frame, text = "Please Enter your shipping cost: ").pack()
            entry_shipping = Entry(frame)
            entry_shipping.pack() 
    
            Button(frame, text = "Enter", command = display_text).pack() 
    
            Label(frame, text = "").pack()  
        
        def depop_function():
            print("DEPOP")
            for widgets in frame.winfo_children():
               widgets.destroy()
    
            def display_text():
                nonlocal entry_depop
                string_price = entry_depop.get() 
                print(string_price)
    
                nonlocal entry_shipping
                string_shipping = entry_shipping.get()
                print(string_shipping)
     
                payment = int(string_price)
                shipping =int(string_shipping)
    
                payout = round(((0.8651 * payment) - shipping), 2)
                print(payout)
                message = '£', payout
                Label(frame, text = "Your final payout will be: \n").pack() 
                Label(frame, text = message).pack() 
    
    
    
            #Ebay Selcetion Code
            Button(frame, text="Back", command=pound).place(x=0,y=0) 
            Label(frame, text= "Depop and Paypal fees currently total 13.49% \n").pack() 
            Label(frame, text = "PLease enter your final sale price: \n").pack()
            entry_depop = Entry(frame)
            entry_depop.focus_set() 
            entry_depop.pack() 
    
            Label(frame, text = "Please Enter your shipping cost: ").pack()
            entry_shipping = Entry(frame)
            entry_shipping.pack() 
    
            Button(frame, text = "Enter", command = display_text).pack() 
    
            Label(frame, text = "").pack() 
            
        #Back button 1
        Button(frame, text="Back", command=start_page).place(x=0,y=0) 
        #Button Selection message 
        Label(frame, text="You have selected GBP£ as your currency.").pack() 
        Label(frame, text = "Please Select your chosen e-commerce site from the list: \n").pack() 
    
        #Create select Ebay Button
        Button(frame, text="Ebay", command= ebay_function).pack()
    
        #Create select Depop Button
        Button(frame, text="Depop", command= depop_function).pack()
    
    def dollar():
        print("DOLLAR") 
        for widgets in frame.winfo_children():
           widgets.destroy()
        
        def ebay_function():
            print("EBAY")
            for widgets in frame.winfo_children():
               widgets.destroy()
    
            def display_text(): 
               nonlocal entry_ebay
               string_price = entry_ebay.get() 
               print(string_price)
    
               nonlocal entry_shipping 
               string_shipping = entry_shipping.get()
               print(string_shipping)
    
               payment = int(string_price)
               shipping =int(string_shipping)
    
               payout = round((((0.872 * payment)-0.3) - shipping), 2)
               print(payout)
               message_dollar = payout, '$'
               Label(frame, text = "Your final payout will be: \n").pack() 
               Label(frame, text = message_dollar).pack() 
    
            #Ebay Selcetion Code
            Button(frame, text="Back", command = dollar).place(x=0,y=0)
            Label(frame, text= "Ebays current fees are 12.8% plus 30p of the final value of the order \n").pack() 
            Label(frame, text = "PLease enter your final sale price: \n").pack()
            entry_ebay = Entry(frame)
            entry_ebay.focus_set() 
            entry_ebay.pack() 
    
            Label(frame, text = "Please Enter your shipping cost: ").pack()
            entry_shipping = Entry(frame)
            entry_shipping.pack() 
    
            Button(frame, text = "Enter", command = display_text).pack() 
    
            Label(frame, text = "").pack()  
        
        def depop_function():
            print("DEPOP")
            for widgets in frame.winfo_children():
               widgets.destroy()
    
            def display_text():
                nonlocal entry_depop
                string_price = entry_depop.get() 
                print(string_price)
    
                nonlocal entry_shipping
                string_shipping = entry_shipping.get()
                print(string_shipping)
     
                payment = int(string_price)
                shipping =int(string_shipping)
    
                payout = round(((0.8651 * payment) - shipping), 2)
                print(payout)
                message_dollar = payout, '$'
                Label(frame, text = "Your final payout will be: \n").pack() 
                Label(frame, text = message_dollar).pack() 
    
    
    
            #Ebay Selcetion Code
            Button(frame, text="Back", command=dollar).place(x=0,y=0) 
            Label(frame, text= "Depop and Paypal fees currently total 13.49% \n").pack() 
            Label(frame, text = "PLease enter your final sale price: \n").pack()
            entry_depop = Entry(frame)
            entry_depop.focus_set() 
            entry_depop.pack() 
    
            Label(frame, text = "Please Enter your shipping cost: ").pack()
            entry_shipping = Entry(frame)
            entry_shipping.pack() 
    
            Button(frame, text = "Enter", command = display_text).pack() 
    
            Label(frame, text = "").pack() 
            
        #Back button 1
        Button(frame, text="Back", command=start_page).place(x=0,y=0) 
        #Button Selection message 
        Label(frame, text="You have selceted USD$ as your currency.").pack() 
        Label(frame, text = "Please Select your chosen e-commerce site from the list: \n").pack() 
    
        #Create select Ebay Button
        Button(frame, text="Ebay", command= ebay_function).pack()
    
        #Create select Depop Button
        Button(frame, text="Depop", command= depop_function).pack()
            
    
    #Create welcome message using text label 
    Label(frame,text="This programme calculates final payout for sales on e-commerce websites. Such as: \n -Ebay \n -Depop \n").pack()
    Label(frame, text="First, Please select desired currency: \n").pack() 
    
    Button(frame, text="£", command= pound).pack()
    Button(frame, text="$", command= dollar).pack() 

start_page()

win.mainloop()
