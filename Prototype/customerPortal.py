from customtkinter import *
import customtkinter as ctk
import Prototype.bookingTables.swimBookingTable as swimBookingTable

def customerPortalWin():
    root = CTk()
    root.geometry('800x800')
    root.maxsize(1200, 1200)
    root.minsize(400, 400)
    root.title('Halo Leisure Customer Portal')

    frame = CTkFrame(root)

    CTkLabel(root, text='Halo Leisure', font=('Arial', 55)).place(relx=.5, rely=.1, anchor='c')
    CTkLabel(root, text='Customer Portal', font=('Arial', 35)).place(relx=.5, rely=.2, anchor='c')

    bookingMenuButton = CTkButton(frame, text='Make a booking', command=bookingMenu)
    bookingMenuButton.grid(row=0, column=0, pady=(15, 15))

    bookingMenuButton = CTkButton(frame, text='My Bookings', command=customerBookings)
    bookingMenuButton.grid(row=1, column=0, pady=(15, 15))

    accountDetailsButton = CTkButton(frame, text='My Account', command='')
    accountDetailsButton.grid(row=2, column=0, pady=(15, 15))

    
    frame.place(relx=.5, rely=.5, anchor='c')
    root.mainloop()

def customerBookings():
    return

def bookingMenu():
    root = CTk()
    root.geometry('800x800')
    root.maxsize(1200, 1200)
    root.minsize(400, 400)
    root.title('Halo Leisure Customer Portal')

    frame = CTkFrame(root)

    gymBookingButton = CTkButton(frame, text='Gym', command=)

    

    frame.place(rely=.5, relx=.5, anchor='c')
    root.mainloop()

customerPortalWin()