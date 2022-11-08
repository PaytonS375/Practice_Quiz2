# Identify and update the code below to accomplish the following tasks:

# 1) Rearrange the widgets in the window so that it looks like the picture provided and add any necessary widgets. 
#    Fix the frame size
# 2) Change the title of the dialog box from 'Quiz II' to 'Breakfast Diner Delivery App Order'
# 3) Change the default option for the radio button to Pancakes (when the programs starts up)
# 4) Fix the buttons (not currently working)
# 5) Add a label and input box (to the top frame) where the user can enter in the address of the delivery
# 6) The review order button should then display the address, total cost of the food, 
#    as well as a random delivery time between 20 and 100 minutes



import tkinter
import tkinter.messagebox
import random

class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.geometry('300x300') # 1 - change size of window
        self.main_window.title("Breakfast Diner Delivery App Order") # 2 - change title


        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #address - # 5
        self.address_label = tkinter.Label(self.top_frame, text="Delivery Address: ") 
        self.address_entry = tkinter.Entry(self.top_frame)

        self.address_label.pack(side='left')
        self.address_entry.pack()
        
        
        #entrees - # 4
        self.var = tkinter.IntVar()
     
        self.entree_label = tkinter.Label(self.mid_frame,text='Select an entree', font=('',15))

        self.entree1 = tkinter.Radiobutton(self.mid_frame,text='Pancakes ($8)',variable=self.var,value=8) # 3 - change value attribute for default options
        self.entree2 = tkinter.Radiobutton(self.mid_frame,text='Waffle ($9)',variable=self.var,value=9)
        self.entree3 = tkinter.Radiobutton(self.mid_frame,text='English Breakfast ($5)',variable=self.var,value=5)

        self.var.set(8) # set the IntVar to the value of the default Radiobutton - # 3

        self.entree_label.pack()
        self.entree1.pack()
        self.entree2.pack()
        self.entree3.pack()
        

        #sides - # 4
        self.side_label = tkinter.Label(self.mid_frame,text='Select your sides',font=('',15))

        self.sidevar1 = tkinter.IntVar() # check for IntVar with Radio and Checkbuttons
        self.sidevar2 = tkinter.IntVar()
        self.sidevar3 = tkinter.IntVar()

        self.side1 = tkinter.Checkbutton(self.mid_frame,text='Hashbrowns ($1.50)',variable=self.sidevar1)
        self.side2 = tkinter.Checkbutton(self.mid_frame,text='Sausage ($2.20)',variable=self.sidevar2)
        self.side3 = tkinter.Checkbutton(self.mid_frame,text='Bacon ($2.25)',variable=self.sidevar3)

        self.side_label.pack()
        self.side1.pack()
        self.side2.pack()
        self.side3.pack()


        #buttons - # 4 and # 6 (command)
        self.ok_button = tkinter.Button(self.bottom_frame,text='Review Order', command=self.calculate)
        self.quit_button = tkinter.Button(self.bottom_frame,text='Quit',command=self.main_window.destroy)

        
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='right')

        
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        
       
        tkinter.mainloop()

    #function - # 6
    def calculate(self):
            # 6) The review order button should then display the address, total cost of the food, 
            #    as well as a random delivery time between 20 and 100 minutes
            delivery_time = random.randrange(20, 100)
            customer_address = self.address_entry.get() # grabbing the entry box contents as a string

            # change the value of the radiobutton to the cost of the item - Pizza is $5, change the value atrribute to 5 (value cannot be the same as another radiobutton)

            # Radiobuttons
            entree_total = float(round(self.var.get(), 2)) # grab the IntVar, not the Radiobutton value

            # Checkbuttons
            sides_total = 0

            if self.sidevar1.get() == 1: # grab the IntVar, not the Checkbutton value
                sides_total += 1.50
            if self.sidevar2.get() == 1:
                sides_total += 2.20
            if self.sidevar3.get() == 1:
                sides_total += 2.25

            

            tkinter.messagebox.showinfo('Pizza time woooo', f'Delivery time: {delivery_time} minutes\nOrder Total: {entree_total + sides_total}\nDelivery Address: {customer_address}')


my_gui = MyGUI()