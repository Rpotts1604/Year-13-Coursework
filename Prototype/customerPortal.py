from customtkinter import *
import customtkinter as ctk
from CTkMessagebox import *
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

    myBookingsButton = CTkButton(frame, text='My Bookings', command=customerBookingsMenu)
    myBookingsButton.grid(row=1, column=0, pady=(15, 15))

    accountDetailsButton = CTkButton(frame, text='My Account', command='')
    accountDetailsButton.grid(row=2, column=0, pady=(15, 15))

    
    frame.place(relx=.5, rely=.5, anchor='c')
    root.mainloop()

#Customers already placed bookings
def customerBookingsMenu():
    root = CTk()
    root.geometry('800x800')
    root.maxsize(1200, 1200)
    root.minsize(400, 400)
    root.title('Halo Leisure Customer Portal')

    frame = CTkScrollableFrame(root, height=500, width=500)

    def bookingsLabels(rowNum, type, date, time):
        CTkLabel(frame, text=f'{type}, {date}, {time}', font=('Arial', 20)).grid(row=rowNum, column=0, padx=(0, 15), pady=(10, 10))
        cancelButton = CTkButton(frame, text='Cancel', font=CTkFont('Arial', 20), command=lambda: cancelBooking(rowNum))
        cancelButton.grid(row=rowNum, column= 1, padx=(15, 0), pady=(10, 10))

    rowNum = 0
    f = open(f'Prototype/customerBookings/{name}.txt', 'r')
    for line in f:
        rowNum = rowNum + 1
        lineSplit = line.split(',')
        bookingsLabels((rowNum-1), str(lineSplit[0]), str(lineSplit[1]), str(lineSplit[2]))
    f.close()


    CTkLabel(root, text='Your Booking History', font=('Arial', 55)).place(relx=.5, rely=.1, anchor='c')

    frame.place(relx=.5, rely=.5, anchor='c')
    root.mainloop()

def cancelBooking(rowNum):
    f = open(f'Prototype/customerBookings/{name}.txt','r')
    oldFile = f.readlines()
    f.close()
    print(oldFile)
    print(len(oldFile))

    f = open(f'Prototype/customerBookings/{name}.txt', 'w')
    for i in range(len(oldFile)):
        if i != rowNum:
            f.write(oldFile[i])

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



    gymBookingButton = CTkButton(frame, text='Swimming', command=swimBookingTable.bookingTable)
    gymBookingButton.grid(row=0, column=0, pady=(15, 15))

    gymBookingButton = CTkButton(frame, text='Gym', command=gymBookingTable.bookingTable)
    gymBookingButton.grid(row=1, column=0, pady=(15, 15))

    frame.place(rely=.5, relx=.5, anchor='c')
    root.mainloop()

customerPortalWin()