from customtkinter import *
import customtkinter as ctk
import tkinter


def searchCustomer(searchTerm):
    f = open('Prototype\customerDetails.txt', 'r')
    for line in f:
        lineSplit = line.split(',')
        if lineSplit[6] == searchTerm:
            customerSelect.set(f'{lineSplit[0]} {lineSplit[1]}')
            print(customerSelect)

#Main Admin portal home page
def adminPortalWin():

    root = CTk()
    root.geometry('800x800')
    root.maxsize(1200, 1200)
    root.minsize(400, 400)  
    root.title('Halo Leisure Admin Portal')

    global customerSelect
    customerSelect = StringVar()
    print(customerSelect)
     
    frame = CTkFrame(root)
    searchFrame = CTkFrame(root)

    addCustomerButton = CTkButton(frame, text='Add Customer', command='')
    addCustomerButton.grid(row=0, column=0)

    bookCustomerButton = CTkButton(frame, text='Book Session')
    bookCustomerButton.grid(row=1, column=0)

    customerSelect.set('none')
    CTkLabel(frame, textvariable=customerSelect).grid(row=2, column=0)

    searchCustomerEntry = CTkEntry(searchFrame)
    searchCustomerEntry.grid(row=0, column=0)

    searchButton = CTkButton(searchFrame, text='Search', command=lambda: searchCustomer(str(searchCustomerEntry.get())))
    searchButton.grid(row=0, column=1)

    frame.place(relx=.5, rely=.5, anchor='c')
    searchFrame.place(relx=.5, rely=.9, anchor='c')
    root.mainloop()