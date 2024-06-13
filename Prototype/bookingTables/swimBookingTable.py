table = [
    [ #monday
        #6
        #6 30
        #7
        #7 30
        #8
        #8 30
        #9
        #9 30
        #10
        #10 30
        #11
        #11 30
        #12
    ], 
    [ #tuesday
        #6
        #6 30
        #7
        #7 30
        #8
        #8 30
        #9
        #9 30
        #10
        #10 30
        #11
        #11 30
        #12
    ], 
    [ #wednesday
        #6
        #6 30
        #7
        #7 30
        #8
        #8 30
        #9
        #9 30
        #10
        #10 30
        #11
        #11 30
        #12
    ], 
    [ #thursday
        #6
        #6 30
        #7
        #7 30
        #8
        #8 30
        #9
        #9 30
        #10
        #10 30
        #11
        #11 30
        #12
    ]
    , 
    [ #friday
        #6
        #6 30
        #7
        #7 30
        #8
        #8 30
        #9
        #9 30
        #10
        #10 30
        #11
        #11 30
        #12
    ], 
    [ #saturday
        #6
        #6 30
        #7
        #7 30
        #8
        #8 30
        #9
        #9 30
        #10
        #10 30
        #11
        #11 30
        #12
    ], 
]

import customtkinter as ctk
from customtkinter import *

#Booking table display for dates and times
def bookingTable():
    root = CTk()
    root.geometry('800x800')
    root.maxsize(800, 800)
    root.minsize(800, 800)
    root.title('Halo Leisure Booking Sheet')

    root.mainloop()