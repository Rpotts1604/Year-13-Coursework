from customtkinter import *
import customtkinter as ctk
import tkinter
from CTkScrollableDropdown import *
from random import randint
import bookingTables.swimBookingTable as swimBookingTable
import bookingTables.gymBookingTable as gymBookingTable
from CTkMessagebox import *

days = []
for i in range(1, 32):
    days.append(f'{i}')
months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
years = []
for i in range(1900, 2025):
    years.append(f'{i}')
accountTypes = ['non-member', 'halo active', 'halo active a2l', 'swimming lessons']

haloID = ''


#search the system for an existing customer
def searchCustomer(searchTerm, customerSelect, root):    
    numOfLines = 0
    lineCount = 0
    f = open('Prototype\customerDetails.txt', 'r')
    for line in f:
        numOfLines += 1
    f.close()

    f = open('Prototype\customerDetails.txt', 'r')
    for line in f:

        lineSplit = line.split(',')
        if lineSplit[len(lineSplit)-2] == searchTerm:
            customerSelect.set(f'{lineSplit[0]} {lineSplit[1]}')
            f = open('Prototype\currentLogin.txt', 'w')
            f.write(str(lineSplit[len(lineSplit)-2]))
            global currentLogin
            currentLogin = lineSplit[len(lineSplit)-2]
            f.close()
            print(customerSelect.get())
            return
        lineCount += 1
    f.close()
    if numOfLines == lineCount:
        CTkMessagebox(root, title='ERROR', message='User Does Not Exist')

#Main Admin portal home page
def adminPortalWin():
    root = CTk()
    root.geometry('800x800')
    root.maxsize(1200, 1200)
    root.minsize(400, 400)  
    root.title('Halo Leisure Admin Portal')

    customerSelect = StringVar(root, 'None Selected')
     
    frame = CTkFrame(root)
    searchFrame = CTkFrame(root)

    addCustomerButton = CTkButton(frame, text='Add Customer', command=addCustomer)
    addCustomerButton.grid(row=0, column=0, pady=(10, 10))

    bookCustomerButton = CTkButton(frame, text='Book Session', command=bookCustomer)
    bookCustomerButton.grid(row=1, column=0, pady=(10, 10))

    editCustomerButton = CTkButton(frame, text='Edit Details', command=lambda: customerAccountEdit(currentLogin))
    editCustomerButton.grid(row=2, column=0, pady=(10, 10))

    CTkLabel(frame, textvariable=customerSelect, bg_color='white', text_color='black', width=300).grid(row=3, column=0)

    searchCustomerEntry = CTkEntry(searchFrame)
    searchCustomerEntry.grid(row=0, column=0)

    searchButton = CTkButton(searchFrame, text='Search', command=lambda: searchCustomer(str(searchCustomerEntry.get()), customerSelect, root))
    searchButton.grid(row=0, column=1)

    frame.place(relx=.5, rely=.5, anchor='c')
    searchFrame.place(relx=.5, rely=.9, anchor='c')
    root.mainloop()

#add a customer to the system, detail inputs
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

    CTkLabel(frame, text='Password').grid(row=8, column=0)
    passwordInput = CTkEntry(frame)
    passwordInput.grid(row=8, column=1)

    #create unique halo ID
    loop = True
    while loop == True:
        newHaloID = (f'YSP{randint(11111,99999)}')
        f = open('Prototype/existingMembershipNum.txt', 'r')
        if newHaloID not in f:
            f.close()
            f = open('Prototype/existingMembershipNum', 'a')
            f.write(f'{newHaloID}, \n')
            loop = False
        f.close()
        

    addDetailsButton = CTkButton(root, text='Confirm Details', command=lambda: addDetails(str(fName.get()), str(lName.get()), str(daySelect.
    get()), str(monthSelect.get()), str(yearSelect.get()), str(postcode.get()), str(address.get()), str(phoneNo.get()), str(email.get()), str(accountTypeSelect.get()), newHaloID, passwordInput.get()))
    addDetailsButton.place(relx=.5, rely=.7, anchor='c')

    frame.place(rely=.5, relx=.5, anchor='c')
    root.mainloop()

#Booking menu for list of booking options
def bookCustomer():
    root = CTk()
    root.geometry('800x800')
    root.maxsize(1200, 1200)
    root.minsize(400, 400)
    root.title('Halo Leisure Customer Portal')

    frame = CTkFrame(root)

    CTkLabel(root, text='Book A Session', font=('Arial', 55)).place(relx=.5, rely=.1, anchor='c')

    swimBookingButton = CTkButton(frame, text='Swimming', command=swimBookingTable.bookingTable)
    swimBookingButton.grid(row=0, column=0, pady=(15, 15))

    gymBookingButton = CTkButton(frame, text='Gym', command=gymBookingTable.bookingTable)
    gymBookingButton.grid(row=1, column=0, pady=(15, 15))

    frame.place(rely=.5, relx=.5, anchor='c')
    root.mainloop()

#add a customers details to the system
def addDetails(fName, lName, day, month, year, postcode, address, phoneNo, email, accountType, haloID, password):
    f = open('Prototype/customerDetails.txt', 'a')
    f.write(f'{fName},{lName},{day}/{month}/{year},{postcode},{address},{phoneNo},{email},{accountType},{haloID},\n')
    f.close()
    
    f = open('Prototype/customerlogins.txt', 'a')
    f.write(f'{haloID},{password}')

#edit customer account details
def customerAccountEdit(username):
    root = CTk()
    root.geometry('800x800')
    root.maxsize(1200, 1200)
    root.minsize(400, 400)
    root.title('Halo Leisure Customer Portal')

    frame = CTkFrame(root)

    f = open('Prototype/customerDetails.txt', 'r')
    for line in f:
        lineSplit = line.split(',')
        if lineSplit[len(lineSplit) - 2] == username:
            fName = StringVar(root, lineSplit[0])
            lName = StringVar(root, lineSplit[1])
            dob = StringVar(root, lineSplit[2])
            dobSplit = (dob.get()).split('/')
            day = dobSplit[0]
            month = dobSplit[1]
            year = dobSplit[2]
            postcode = StringVar(root, lineSplit[3])
            address = StringVar(root, lineSplit[4])
            phoneNo = StringVar(root, lineSplit[5])
            email = StringVar(root, lineSplit[6])
    f.close()

    CTkLabel(frame, text='First Name').grid(row=0, column=0)
    fNameEdit = CTkEntry(frame, textvariable=fName)
    fNameEdit.grid(row=0, column=1)

    CTkLabel(frame, text='Last Name').grid(row=1, column=0)
    lNameEdit = CTkEntry(frame, textvariable=lName)
    lNameEdit.grid(row=1, column=1)

    CTkLabel(frame, text='Date Of Birth').grid(row=2, column=0)
    daySelect = CTkComboBox(frame, values=day)
    daySelect.grid(row=2, column=1)
    CTkScrollableDropdown(daySelect, values=days)

    monthSelect = CTkComboBox(frame, values=month)
    monthSelect.grid(row=2, column=2)
    CTkScrollableDropdown(monthSelect, values=months)

    yearSelect = CTkComboBox(frame, values=year)
    yearSelect.grid(row=2, column=3)
    CTkScrollableDropdown(yearSelect, values=years)

    CTkLabel(frame, text='').grid(row=3, column=0)
    postCodeEdit = CTkEntry(frame, textvariable=postcode)
    postCodeEdit.grid(row=3, column=1)

    CTkLabel(frame, text='').grid(row=4, column=0)
    addressEdit = CTkEntry(frame, textvariable=address)
    addressEdit.grid(row=4, column=1)


    CTkLabel(frame, text='').grid(row=5, column=0)
    phoneNoEdit = CTkEntry(frame, textvariable=phoneNo)
    phoneNoEdit.grid(row=5, column=1)

    CTkLabel(frame, text='').grid(row=6, column=0)
    emailEdit = CTkEntry(frame, textvariable=email)
    emailEdit.grid(row=6, column=1)

    saveButton = CTkButton(root, text='Save', command=lambda: saveChanges(fNameEdit.get(), lNameEdit.get(), (f'{daySelect.get()}/{monthSelect.get()}/{yearSelect.get()}'), postCodeEdit.get(),addressEdit.get(), phoneNoEdit.get(), emailEdit.get()))
    saveButton.place(relx=.5, rely=.8, anchor='c')
    
    frame.place(relx=.5, rely=.5, anchor='c')
    root.mainloop()

def saveChanges(fNameSave, lNameSave, dobSave, postCodeSave,addressSave, phoneNoSave, emailSave):
    currentLoginFile = open('Prototype/currentLogin.txt', 'r')
    currentLoginArray = currentLoginFile.readlines()
    currentLogin = currentLoginArray[0]
    currentLoginFile.close()
    f = open('Prototype/customerDetails.txt', 'r')
    tempFile = open('Prototype/customerDetailsTemp.txt', 'w')
    for line in f:
        lineSplit = line.split(',')
        accountType = lineSplit[7]
        tempFile.write(line)
    f.close()
    tempFile.close()

    f = open('Prototype/customerDetails.txt', 'w')
    tempFile = open('Prototype/customerDetailsTemp.txt', 'r')
    for line in tempFile:
        lineSplit = line.split(',')
        if lineSplit[8] != currentLogin:
            f.write(line)
    print(f'{fNameSave},{lNameSave},{dobSave},{postCodeSave},{addressSave},{phoneNoSave},{emailSave},{accountType},{currentLogin},\n')
    f.write(f'{fNameSave},{lNameSave},{dobSave},{postCodeSave},{addressSave},{phoneNoSave},{emailSave},{accountType},{currentLogin},\n')
    f.close()
    tempFile.close()