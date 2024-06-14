import customtkinter as ctk
from customtkinter import *
from tkcalendar import Calendar
from CTkMessagebox import *

#Main booking tables for dates and times
def bookingTable():

    f = open('Prototype\currentLogin.txt', 'r')
    customerName = f.read()
    f.close()
    root = CTk()
    root.geometry('600x600')
    root.maxsize(600, 600)
    root.minsize(600, 600)
    root.title('Halo Leisure Gym Booking Sheet')

    frame = CTkFrame(root)

    #select date
    dateSelect = Calendar(frame, selectmode='day',  year = 2024, month=6, day=1, font=('Arial', (10)))
    dateSelect.grid(row=0, column=0, padx=(0, 15))

    #select time
    timeSelect = CTkComboBox(frame, values=(
        '6', '6:30', '7', '7:30', '8', '8:30', '9', '9:30', '10', '10:30', '11', '11:30', '12', '12:30', '13', '13:30', '14', '14:30', '15', '15:30', '16', '16:30', '17', '17:30', '18', '18:30', '19', '19:30', '20', '20:30', '21', '21:30', '22', '22:30'
    ))
    timeSelect.grid(row=0, column=1, padx=(15, 0))

    bookButton = CTkButton(root, text='Book Session', command=lambda: bookSession(str(dateSelect.get_date()), str(timeSelect.get()), customerName, root))
    bookButton.place(relx=.5, rely=.7, anchor='c')

    frame.place(rely=.5, relx=.5, anchor='c')
    root.mainloop()

#input booking details into customers file
def bookSession(date, time, customerName, root):
    f = open(f'Prototype\customerBookings\{customerName}.txt', 'a')
    f.close()
    f = open(f'Prototype\customerBookings\{customerName}.txt', 'r')
    for line in f:
        lineSplit = line.split(',')
        if lineSplit[0] == 'gym' and lineSplit[1] == date and lineSplit[2] == time:
            CTkMessagebox(root, title='ERROR', message='Session Already Booked')
            return
    f.close()
        
    f = open(f'Prototype\customerBookings\{customerName}.txt', 'a')
    f.write(f'gym,{date},{time}, \n')
    f.close()
        



