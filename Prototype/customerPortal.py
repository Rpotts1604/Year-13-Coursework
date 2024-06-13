from customtkinter import *
import customtkinter as ctk
import bookingTables.swimBookingTable as swimBookingTable
import bookingTables.gymBookingTable as gymBookingTable

f = open('Prototype\currentLogin.txt', 'r')
name = f.read()
f.close()

#Main customer portal window home page
def customerPortalWin():
    root = CTk()
    root.geometry('800x800')
    root.maxsize(1200, 1200)
    root.minsize(400, 400)
    root.title('Halo Leisure Customer Portal')

    frame = CTkFrame(root)

    CTkLabel(root, text='Halo Leisure', font=('Arial', 55)).place(relx=.5, rely=.1, anchor='c')
    CTkLabel(root, text='Customer Portal', font=('Arial', 35)).place(relx=.5, rely=.2, anchor='c')
    CTkLabel(root, text=f'Hello, {name}', font=('Arial', 35)).place(relx=.5, rely=.3, anchor='c')

    bookingMenuButton = CTkButton(frame, text='Make a booking', command=bookingMenu)
    bookingMenuButton.grid(row=0, column=0, pady=(15, 15))

    myBookingsButton = CTkButton(frame, text='My Bookings', command=customerBookings)
    myBookingsButton.grid(row=1, column=0, pady=(15, 15))

    accountDetailsButton = CTkButton(frame, text='My Account', command='')
    accountDetailsButton.grid(row=2, column=0, pady=(15, 15))

    
    frame.place(relx=.5, rely=.5, anchor='c')
    root.mainloop()

#Customers already placed bookings
def customerBookings():
    return

#Booking menu for list of booking options
def bookingMenu():
    root = CTk()
    root.geometry('800x800')
    root.maxsize(1200, 1200)
    root.minsize(400, 400)
    root.title('Halo Leisure Customer Portal')

    frame = CTkFrame(root)

    CTkLabel(root, text='Book A Session', font=('Arial', 55)).place(relx=.5, rely=.1, anchor='c')

    gymBookingButton = CTkButton(frame, text='Swimming', command=swimBookingTable.bookingTable)
    gymBookingButton.grid(row=0, column=0, pady=(15, 15))

    gymBookingButton = CTkButton(frame, text='Gym', command=gymBookingTable.bookingTable)
    gymBookingButton.grid(row=1, column=0, pady=(15, 15))

    frame.place(rely=.5, relx=.5, anchor='c')
    root.mainloop()