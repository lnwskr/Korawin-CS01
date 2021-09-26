from tkinter import *


expression = ""


def press(num):

    global expression


    expression = expression + str(num)

    equation.set(expression)


def equalpress():

    try:

        global expression


        total = str(eval(expression))

        equation.set(total)

        expression = ""

    except:

        equation.set(" error ")
        expression = ""



def clear():
    global expression
    expression = ""
    equation.set("")



if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="white")
    gui.title("Simple Calculator")
    gui.geometry("150x500")
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=10)
    button1 = Button(gui, text=' 1 ', fg='blue', bg='grey',
                    command=lambda: press(1), height=4, width=3)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='blue', bg='grey',
                    command=lambda: press(2), height=4, width=3)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='blue', bg='grey',
                    command=lambda: press(3), height=4, width=3)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='blue', bg='grey',
                    command=lambda: press(4), height=4, width=3)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='blue', bg='grey',
                    command=lambda: press(5), height=4, width=3)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='blue', bg='grey',
                    command=lambda: press(6), height=4, width=3)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='blue', bg='grey',
                    command=lambda: press(7), height=4, width=3)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='blue', bg='grey',
                    command=lambda: press(8), height=4, width=3)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='blue', bg='grey',
                    command=lambda: press(9), height=4, width=3)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='blue', bg='grey',
                    command=lambda: press(0), height=4, width=3)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='blue', bg='grey',
                command=lambda: press("+"), height=4, width=3)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='blue', bg='grey',
                command=lambda: press("-"), height=4, width=3)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='blue', bg='grey',
                    command=lambda: press("*"), height=4, width=3)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='blue', bg='grey',
                    command=lambda: press("/"), height=4, width=3)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='blue', bg='grey',
                command=equalpress, height=4, width=3)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='blue', bg='grey',
                command=clear, height=4, width=3)
    clear.grid(row=5, column='1')

    Decimal= Button(gui, text='.', fg='blue', bg='grey',
                    command=lambda: press('.'), height=4, width=3)
    Decimal.grid(row=6, column=0)
    gui.mainloop()