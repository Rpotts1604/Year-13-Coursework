from customtkinter import *
import customtkinter as ctk
from CTkMessagebox import *
from CTkScrollableDropdown import *
import bookingTables.swimBookingTable as swimBookingTable
import bookingTables.gymBookingTable as gymBookingTable

days = []
for i in range(1, 32):
    days.append(f'{i}')
months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
years = []
for i in range(1900, 2025):
    years.append(f'{i}')


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

    accountDetailsButton = CTkButton(frame, text='My Account', command=lambda: customerAccountEdit(username))
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