from customtkinter import *
import customtkinter as ctk

def customerLogin():
    customerLoginScreen = CTk()
    customerLoginScreen.geometry('300x300')
    customerLoginScreen.title('Customer Login')
    
    frame = CTkFrame(customerLoginScreen)
    
    CTkLabel(frame, text='Username  ').grid(row=0, column=0, pady=(0, 10))
    usernameEntry = CTkEntry(frame)
    usernameEntry.grid(row=0, column=1, pady=(0, 10))
    
    CTkLabel(frame, text='Password  ').grid(row=1, column=0, pady=(10, 0))
    passwordEntry = CTkEntry(frame)
    passwordEntry.grid(row=1, column=1, pady=(10, 0))
    
    loginButton = CTkButton(customerLoginScreen, text='Login', command=lambda: customerLoginCheck(usernameEntry.get(), passwordEntry.get(), customerLoginScreen))
    loginButton.place(relx=.5, rely=.8, anchor='c')
    
    frame.place(relx=.5, rely=.5, anchor='c')
    
    customerLoginScreen.mainloop()

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


def customerLoginCheck(username, password, customerLoginScreen):
    f = open('customerlogins.txt', 'r')
    for line in f:
        splitLine = line.split(',')
        if splitLine[0] == username and splitLine[1] == password:
            customerLoginScreen.withdraw()
            root.withdraw()
            customerPortal()
        
    
    
def adminLoginCheck(username, password, adminLoginScreen):
    f = open('adminlogins.txt', 'r')
    for line in f:
        splitLine = line.split(',')
        if splitLine[0] == username and splitLine[1] == password:
            adminLoginScreen.withdraw()
            root.withdraw()
            adminPortal()   
        
        
def adminPortal():
    root = CTk()
    root.geometry('800x800')
    root.maxsize(1200, 1200)
    root.minsize(400, 400)  
    root.title('Halo Leisure Admin Portal')
    
    root.mainloop()
    
def customerPortal():
    root = CTk()
    root.geometry('800x800')
    root.maxsize(1200, 1200)
    root.minsize(400, 400)
    root.title('Halo Leisure Customer Portal')
    
    root.mainloop()

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
