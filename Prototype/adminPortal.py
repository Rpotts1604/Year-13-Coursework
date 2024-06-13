from customtkinter import *
import customtkinter as ctk
import tkinter
from CTkScrollableDropdown import *
from random import randint

days = []
for i in range(1, 32):
    days.append(f'{i}')
months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
years = []
for i in range(1900, 2025):
    years.append(f'{i}')
accountTypes = ['non-member', 'halo active', 'halo active a2l', 'swimming lessons']

def searchCustomer(searchTerm, customerSelect):
    f = open('Prototype\customerDetails.txt', 'r')
    for line in f:
        lineSplit = line.split(',')
        if lineSplit[6] == searchTerm:
            customerSelect.set(f'{lineSplit[0]} {lineSplit[1]}')
            print(customerSelect.get())

#Main Admin portal home page
def adminPortalWin():

    root = CTk()
    root.geometry('800x800')
    root.maxsize(1200, 1200)
    root.minsize(400, 400)  
    root.title('Halo Leisure Admin Portal')

    customerSelect = StringVar(root, 'None')
     
    frame = CTkFrame(root)
    searchFrame = CTkFrame(root)

    addCustomerButton = CTkButton(frame, text='Add Customer', command=addCustomer)
    addCustomerButton.grid(row=0, column=0)

    bookCustomerButton = CTkButton(frame, text='Book Session')
    bookCustomerButton.grid(row=1, column=0)

    CTkLabel(frame, textvariable=customerSelect).grid(row=2, column=0)

    searchCustomerEntry = CTkEntry(searchFrame)
    searchCustomerEntry.grid(row=0, column=0)

    searchButton = CTkButton(searchFrame, text='Search', command=lambda: searchCustomer(str(searchCustomerEntry.get()), customerSelect))
    searchButton.grid(row=0, column=1)

    frame.place(relx=.5, rely=.5, anchor='c')
    searchFrame.place(relx=.5, rely=.9, anchor='c')
    root.mainloop()

def addCustomer():
    root = CTk()
    root.geometry('800x800')
    root.maxsize(1200, 1200)
    root.minsize(400, 400)  
    root.title('Halo Leisure Admin Portal')
    frame = CTkFrame(root)

    CTkLabel(frame, text='First Name').grid(row=0, column=0)
    fName = CTkEntry(frame)
    fName.grid(row=0, column=1)

    CTkLabel(frame, text='Last Name').grid(row=1, column=0)
    lName = CTkEntry(frame)
    lName.grid(row=1, column=1)

    CTkLabel(frame, text='Date Of Birth').grid(row=2, column=0)

    daySelect = CTkComboBox(frame, values='D')
    daySelect.grid(row=2, column=1)
    CTkScrollableDropdown(daySelect, values=days)

    monthSelect = CTkComboBox(frame, values='M')
    monthSelect.grid(row=2, column=2)
    CTkScrollableDropdown(monthSelect, values=months)

    yearSelect = CTkComboBox(frame, values='Y')
    yearSelect.grid(row=2, column=3)
    CTkScrollableDropdown(yearSelect, values=years)

    CTkLabel(frame, text='Postcode').grid(row=3, column=0)
    postcode = CTkEntry(frame)
    postcode.grid(row=3, column=1)

    CTkLabel(frame, text='Address').grid(row=4, column=0)
    address = CTkEntry(frame)
    address.grid(row=4, column=1)

    CTkLabel(frame, text='Phone Number').grid(row=5, column=0)
    phoneNo = CTkEntry(frame)
    phoneNo.grid(row=5, column=1)

    CTkLabel(frame, text='Email').grid(row=6, column=0)
    email = CTkEntry(frame)
    email.grid(row=6, column=1)

    CTkLabel(frame, text='Account Type').grid(row=7, column=0)
    accountTypeSelect = CTkComboBox(frame, values=' ')
    accountTypeSelect.grid(row=7, column=1)
    CTkScrollableDropdown(accountTypeSelect, values=accountTypes, width=200)

    #fix plzzzz
    numOfLines = 0
    count = 0
    f = open('Prototype/existingMembershipNum.txt', 'r')
    for line in f:
        numOfLines = numOfLines + 1
    f.close()

    f = open('Prototype/existingMembershipNum.txt', 'r')
    for line in f:
        count = count + 1
        haloIdCreate = randint(11111, 99999)
        print(haloIdCreate, count, numOfLines)
        lineSplit = line.split(',')
        if lineSplit[0] != haloIdCreate and count == numOfLines:
            print('valid')
            break
    f.close()


    addDetailsButton = CTkButton(root, text='Confirm Details', command=lambda: addDetails(str(fName.get()), str(lName.get()), str(daySelect.
    get()), str(monthSelect.get()), str(yearSelect.get()), str(postcode.get()), str(address.get()), str(phoneNo.get()), str(email.get())))
    addDetailsButton.place(relx=.5, rely=.7, anchor='c')

    frame.place(rely=.5, relx=.5, anchor='c')
    root.mainloop()

def addDetails(fName, lName, day, month, year, postcode, address, phoneNo, email):
    f = open('Prototype/customerDetails.txt', 'a')
    f.write(f'{fName}, {lName}, {day}/{month}/{year}, {postcode}, {address}, {phoneNo}, {email}, \n')
    f.close()

adminPortalWin()