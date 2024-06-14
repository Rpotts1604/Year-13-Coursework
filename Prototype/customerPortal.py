from customtkinter import *
import customtkinter as ctk
from CTkMessagebox import *
import bookingTables.swimBookingTable as swimBookingTable
import bookingTables.gymBookingTable as gymBookingTable


#Main customer portal window home page
def customerPortalWin(username):
    f = open('Prototype\currentLogin.txt', 'w')
    f.write(username)
    f.close()
    
    root = CTk()
    root.geometry('800x800')
    root.maxsize(1200, 1200)
    root.minsize(400, 400)
    root.title('Halo Leisure Customer Portal')

    frame = CTkFrame(root)

    CTkLabel(root, text='Halo Leisure', font=('Arial', 55)).place(relx=.5, rely=.1, anchor='c')
    CTkLabel(root, text='Customer Portal', font=('Arial', 35)).place(relx=.5, rely=.2, anchor='c')
    CTkLabel(root, text=f'Hello, {username}', font=('Arial', 35)).place(relx=.5, rely=.3, anchor='c')

    bookingMenuButton = CTkButton(frame, text='Make a booking', command=bookingMenu)
    bookingMenuButton.grid(row=0, column=0, pady=(15, 15))

    myBookingsButton = CTkButton(frame, text='My Bookings', command=lambda: customerBookingsMenu(username))
    myBookingsButton.grid(row=1, column=0, pady=(15, 15))

    accountDetailsButton = CTkButton(frame, text='My Account', command='')
    accountDetailsButton.grid(row=2, column=0, pady=(15, 15))

    
    frame.place(relx=.5, rely=.5, anchor='c')
    root.mainloop()

#reload the window to update bookings (BROKEN)
def updateWin(bookingsLabels, username, frame):
    rowNum = 0
    f = open(f'Prototype/customerBookings/{username}.txt', 'r')
    for line in f:
        rowNum = rowNum + 1
        lineSplit = line.split(',')
        bookingsLabels((rowNum-1), str(lineSplit[0]), str(lineSplit[1]), str(lineSplit[2]), frame, username)
    f.close()

#show customers previous bookings on the window
def bookingsLabels(rowNum, type, date, time, frame, username):
    CTkLabel(frame, text=f'{type}, {date}, {time}', font=('Arial', 20)).grid(row=rowNum, column=0, padx=(0, 15), pady=(10, 10))
    cancelButton = CTkButton(frame, text='Cancel', font=CTkFont('Arial', 20), command=lambda: cancelBooking(rowNum, username, frame))
    cancelButton.grid(row=rowNum, column= 1, padx=(15, 0), pady=(10, 10))

#Customers already placed bookings
def customerBookingsMenu(username):
    root = CTk()
    root.geometry('800x800')
    root.maxsize(1200, 1200)
    root.minsize(400, 400)
    root.title('Halo Leisure Customer Portal')

    frame = CTkScrollableFrame(root, height=500, width=500)

    updateWin(bookingsLabels, username, frame)

    CTkLabel(root, text='Your Booking History', font=('Arial', 55)).place(relx=.5, rely=.1, anchor='c')

    frame.place(relx=.5, rely=.5, anchor='c')
    root.mainloop()

def cancelBooking(rowNum, username, frame):
    f = open(f'Prototype/customerBookings/{username}.txt','r')
    oldFile = f.readlines()
    f.close()
    print(oldFile)
    print(len(oldFile))

    f = open(f'Prototype/customerBookings/{username}.txt', 'w')
    for i in range(len(oldFile)):
        if i != rowNum:
            f.write(oldFile[i])

    updateWin(bookingsLabels, username, frame)

    CTkMessagebox(title='Cancel Confirmed', message='Session Successfully Cancelled')


#Booking menu for list of booking options
def bookingMenu():
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