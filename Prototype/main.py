from customtkinter import *
import customtkinter as ctk
import adminPortal
import customerPortal
from time import sleep
from CTkMessagebox import *


#Customer login screen
def customerLogin():
    customerLoginScreen = CTk()
    customerLoginScreen.geometry('300x300')
    customerLoginScreen.title('Customer Login')
    
    frame = CTkFrame(customerLoginScreen)
    
    CTkLabel(frame, text='Halo ID').grid(row=0, column=0, pady=(0, 10), padx=(0, 10))
    usernameEntry = CTkEntry(frame)
    usernameEntry.grid(row=0, column=1, pady=(0, 10))
    
    CTkLabel(frame, text='Password').grid(row=1, column=0, pady=(10, 0), padx=(0, 10))
    passwordEntry = CTkEntry(frame)
    passwordEntry.grid(row=1, column=1, pady=(10, 0))
    
    loginButton = CTkButton(customerLoginScreen, text='Login', command=lambda: customerLoginCheck(usernameEntry.get(), passwordEntry.get(), customerLoginScreen))
    loginButton.place(relx=.5, rely=.8, anchor='c')
    
    frame.place(relx=.5, rely=.5, anchor='c')
    
    customerLoginScreen.mainloop()

#Admin login screen
def adminLogin():
    adminLoginScreen = CTk()
    adminLoginScreen.geometry('300x300')
    adminLoginScreen.title('Administrator Login')
    
    frame = CTkFrame(adminLoginScreen)
    
    CTkLabel(frame, text='Username  ').grid(row=0, column=0, pady=(0, 10))
    usernameEntry = CTkEntry(frame)
    usernameEntry.grid(row=0, column=1, pady=(0, 10))
    
    CTkLabel(frame, text='Password  ').grid(row=1, column=0, pady=(10, 0))
    passwordEntry = CTkEntry(frame)
    passwordEntry.grid(row=1, column=1, pady=(10, 0))
    
    loginButton = CTkButton(adminLoginScreen, text='Login', command=lambda: adminLoginCheck(usernameEntry.get(), passwordEntry.get(), adminLoginScreen))
    loginButton.place(relx=.5, rely=.8, anchor='c')
    
    frame.place(relx=.5, rely=.5, anchor='c')
    
    adminLoginScreen.mainloop()

#Customer username and password validation check
def customerLoginCheck(username, password, customerLoginScreen):
    f = open('Prototype\customerlogins.txt', 'r')
    for line in f:
        splitLine = line.split(',')
        if splitLine[0] == username and splitLine[1] == password:
            customerLoginScreen.withdraw()
            root.withdraw()
            customerPortal.customerPortalWin(username)
            return
    CTkMessagebox(customerLoginScreen, title='ERROR', message='Login not found')
        
#Admin username and password validation check
def adminLoginCheck(username, password, adminLoginScreen):

    f = open('Prototype/adminlogins.txt', 'r')
    for line in f:
        splitLine = line.split(',')
        if splitLine[0] == username and splitLine[1] == password:
            adminLoginScreen.withdraw()
            root.withdraw()
            adminPortal.adminPortalWin()  
            return
    CTkMessagebox(adminLoginScreen, title='ERROR', message='Login not found')
        
#Main login home page
root = CTk()
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')
root.geometry('800x800')
root.maxsize(1200, 1200)
root.minsize(400, 400)
root.title('Halo Leisure Login Portal')

CTkLabel(root, text='Halo Leisure', font=('Arial', 55)).place(relx=.5, rely=.1, anchor='c')

customerLoginButton = CTkButton(root, text='Customer\nLogin', command=customerLogin, font=('Arial', 25))
customerLoginButton.place(relx=.33, rely=.5, anchor='c')

adminLoginButton = CTkButton(root, text='Administrator\nLogin', command=adminLogin, font=('Arial', 25))
adminLoginButton.place(relx=.66, rely=.5, anchor='c')


root.mainloop()
