from tkinter import *
import calendar

def showCalender():
    gui = Tk()
    gui.config(background='grey')
    gui.title("Calender for the year")
    gui.geometry("550x600")
    year = int(year_field.get())
    gui_content=  calendar.calendar(year)
    calYear = Label(gui, text= gui_content, font= "Consolas 10 bold")
    calYear.grid(row=5, column=1,padx=20)
    gui.mainloop()

if __name__=='__main__':
    new = Tk()
    new.config(background='yellow')
    new.title("Calender")
    new.geometry("250x140")
    cal = Label(new, text="Calender",bg='yellow',font=("times", 28, "bold"))
    year = Label(new, text="Enter year", bg='blue')
    year_field=Entry(new)
    button = Button(new, text='Show Calender', fg='Black',bg='blue',command=showCalender)
    Exit = Button(new, text='Exit', fg='Black', bg='blue', command=exit)
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    Exit.grid(row=6, column=1)
    new.mainloop()