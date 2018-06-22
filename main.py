__author__ = "Абельханов Р.Р."
__copyright__ = "Copyright 2018, Rihan_Zer0"
__email__ = "rinat-sonic@mail.ru"

from tkinter import *
import numpy as np


def main():
    root = Tk()
    top = SLAU(root)
    root.mainloop()

class SLAU:
    z = 5

    def Reset(self):
        self.A1.delete(0, END)
        self.A2.delete(0, END)
        self.A3.delete(0, END)
        self.A4.delete(0, END)
        self.A5.delete(0, END)
        self.B1.delete(0, END)
        self.B2.delete(0, END)
        self.B3.delete(0, END)
        self.B4.delete(0, END)
        self.B5.delete(0, END)
        self.C1.delete(0, END)
        self.C2.delete(0, END)
        self.C3.delete(0, END)
        self.C4.delete(0, END)
        self.C5.delete(0, END)
        self.D1.delete(0, END)
        self.D2.delete(0, END)
        self.D3.delete(0, END)
        self.D4.delete(0, END)
        self.D5.delete(0, END)
        self.E1.delete(0, END)
        self.E2.delete(0, END)
        self.E3.delete(0, END)
        self.E4.delete(0, END)
        self.E5.delete(0, END)
        self.R1.delete(0, END)
        self.R2.delete(0, END)
        self.R3.delete(0, END)
        self.R4.delete(0, END)
        self.R5.delete(0, END)
        self.X1.delete(0, END)
        self.X2.delete(0, END)
        self.X3.delete(0, END)
        self.X4.delete(0, END)
        self.X5.delete(0, END)
        return

    def calc(self):
        global z
        self.X1.delete(0, END)
        self.X2.delete(0, END)
        self.X3.delete(0, END)
        self.X4.delete(0, END)
        self.X5.delete(0, END)
        if z == 5:
            M1 = np.array([[float(self.A1.get()), float(self.B1.get()), float(self.C1.get()), float(self.D1.get()), float(self.E1.get())],
                           [float(self.A2.get()), float(self.B2.get()), float(self.C2.get()), float(self.D2.get()), float(self.E2.get())],
                           [float(self.A3.get()), float(self.B3.get()), float(self.C3.get()), float(self.D3.get()), float(self.E3.get())],
                           [float(self.A4.get()), float(self.B4.get()), float(self.C4.get()), float(self.D4.get()), float(self.E4.get())],
                           [float(self.A5.get()), float(self.B5.get()), float(self.C5.get()), float(self.D5.get()), float(self.E5.get())]])
            M2 = np.linalg.inv(M1)
            M3 = np.array([float(self.R1.get()), float(self.R2.get()), float(self.R3.get()), float(self.R4.get()), float(self.R5.get())])
            RES = np.round(M2.dot(M3), decimals=10)
            self.X1.insert(0, RES[0])
            self.X2.insert(0, RES[1])
            self.X3.insert(0, RES[2])
            self.X4.insert(0, RES[3])
            self.X5.insert(0, RES[4])
        elif z == 1:
            M1 = np.array([[float(self.A1.get())]])
            M2 = np.linalg.inv(M1)
            M3 = np.array([float(self.R1.get())])
            RES = np.round(M2.dot(M3), decimals=10)
            self.X1.insert(0, RES[0])
        elif z == 2:
            M1 = np.array([[float(self.A1.get()), float(self.B1.get())],
                           [float(self.A2.get()), float(self.B2.get())]])
            M2 = np.linalg.inv(M1)
            M3 = np.array([float(self.R1.get()), float(self.R2.get())])
            RES = np.round(M2.dot(M3), decimals=10)
            self.X1.insert(0, RES[0])
            self.X2.insert(0, RES[1])
        elif z == 3:
            M1 = np.array([[float(self.A1.get()), float(self.B1.get()), float(self.C1.get())],
                           [float(self.A2.get()), float(self.B2.get()), float(self.C2.get())],
                           [float(self.A3.get()), float(self.B3.get()), float(self.C3.get())]])
            M2 = np.linalg.inv(M1)
            M3 = np.array([float(self.R1.get()), float(self.R2.get()), float(self.R3.get())])
            RES = np.round(M2.dot(M3), decimals=10)
            self.X1.insert(0, RES[0])
            self.X2.insert(0, RES[1])
            self.X3.insert(0, RES[2])
        elif z == 4:
            M1 = np.array([[float(self.A1.get()), float(self.B1.get()), float(self.C1.get()), float(self.D1.get())],
                           [float(self.A2.get()), float(self.B2.get()), float(self.C2.get()), float(self.D2.get())],
                           [float(self.A3.get()), float(self.B3.get()), float(self.C3.get()), float(self.D3.get())],
                           [float(self.A4.get()), float(self.B4.get()), float(self.C4.get()), float(self.D4.get())]])
            M2 = np.linalg.inv(M1)
            M3 = np.array([float(self.R1.get()), float(self.R2.get()), float(self.R3.get()), float(self.R4.get())])
            RES = np.round(M2.dot(M3), decimals=10)
            self.X1.insert(0, RES[0])
            self.X2.insert(0, RES[1])
            self.X3.insert(0, RES[2])
            self.X4.insert(0, RES[3])
        return

    def make_1(self):
        global z
        z = 1
        self.A2.configure(state='disabled')
        self.A3.configure(state='disabled')
        self.A4.configure(state='disabled')
        self.A5.configure(state='disabled')
        self.B1.configure(state='disabled')
        self.B2.configure(state='disabled')
        self.B3.configure(state='disabled')
        self.B4.configure(state='disabled')
        self.B5.configure(state='disabled')
        self.C1.configure(state='disabled')
        self.C2.configure(state='disabled')
        self.C3.configure(state='disabled')
        self.C4.configure(state='disabled')
        self.C5.configure(state='disabled')
        self.D1.configure(state='disabled')
        self.D2.configure(state='disabled')
        self.D3.configure(state='disabled')
        self.D4.configure(state='disabled')
        self.D5.configure(state='disabled')
        self.E1.configure(state='disabled')
        self.E2.configure(state='disabled')
        self.E3.configure(state='disabled')
        self.E4.configure(state='disabled')
        self.E5.configure(state='disabled')
        self.R2.configure(state='disabled')
        self.R3.configure(state='disabled')
        self.R4.configure(state='disabled')
        self.R5.configure(state='disabled')
        self.X2.configure(state='disabled')
        self.X3.configure(state='disabled')
        self.X4.configure(state='disabled')
        self.X5.configure(state='disabled')

    def make_2(self):
        global z
        z = 2
        self.A2.configure(state='normal')
        self.A3.configure(state='disabled')
        self.A4.configure(state='disabled')
        self.A5.configure(state='disabled')
        self.B1.configure(state='normal')
        self.B2.configure(state='normal')
        self.B3.configure(state='disabled')
        self.B4.configure(state='disabled')
        self.B5.configure(state='disabled')
        self.C1.configure(state='disabled')
        self.C2.configure(state='disabled')
        self.C3.configure(state='disabled')
        self.C4.configure(state='disabled')
        self.C5.configure(state='disabled')
        self.D1.configure(state='disabled')
        self.D2.configure(state='disabled')
        self.D3.configure(state='disabled')
        self.D4.configure(state='disabled')
        self.D5.configure(state='disabled')
        self.E1.configure(state='disabled')
        self.E2.configure(state='disabled')
        self.E3.configure(state='disabled')
        self.E4.configure(state='disabled')
        self.E5.configure(state='disabled')
        self.R2.configure(state='normal')
        self.R3.configure(state='disabled')
        self.R4.configure(state='disabled')
        self.R5.configure(state='disabled')
        self.X2.configure(state='normal')
        self.X3.configure(state='disabled')
        self.X4.configure(state='disabled')
        self.X5.configure(state='disabled')

    def make_3(self):
        global z
        z = 3
        self.A2.configure(state='normal')
        self.A3.configure(state='normal')
        self.A4.configure(state='disabled')
        self.A5.configure(state='disabled')
        self.B1.configure(state='normal')
        self.B2.configure(state='normal')
        self.B3.configure(state='normal')
        self.B4.configure(state='disabled')
        self.B5.configure(state='disabled')
        self.C1.configure(state='normal')
        self.C2.configure(state='normal')
        self.C3.configure(state='normal')
        self.C4.configure(state='disabled')
        self.C5.configure(state='disabled')
        self.D1.configure(state='disabled')
        self.D2.configure(state='disabled')
        self.D3.configure(state='disabled')
        self.D4.configure(state='disabled')
        self.D5.configure(state='disabled')
        self.E1.configure(state='disabled')
        self.E2.configure(state='disabled')
        self.E3.configure(state='disabled')
        self.E4.configure(state='disabled')
        self.E5.configure(state='disabled')
        self.R2.configure(state='normal')
        self.R3.configure(state='normal')
        self.R4.configure(state='disabled')
        self.R5.configure(state='disabled')
        self.X2.configure(state='normal')
        self.X3.configure(state='normal')
        self.X4.configure(state='disabled')
        self.X5.configure(state='disabled')

    def make_4(self):
        global z
        z = 4
        self.A2.configure(state='normal')
        self.A3.configure(state='normal')
        self.A4.configure(state='normal')
        self.A5.configure(state='disabled')
        self.B1.configure(state='normal')
        self.B2.configure(state='normal')
        self.B3.configure(state='normal')
        self.B4.configure(state='normal')
        self.B5.configure(state='disabled')
        self.C1.configure(state='normal')
        self.C2.configure(state='normal')
        self.C3.configure(state='normal')
        self.C4.configure(state='normal')
        self.C5.configure(state='disabled')
        self.D1.configure(state='normal')
        self.D2.configure(state='normal')
        self.D3.configure(state='normal')
        self.D4.configure(state='normal')
        self.D5.configure(state='disabled')
        self.E1.configure(state='disabled')
        self.E2.configure(state='disabled')
        self.E3.configure(state='disabled')
        self.E4.configure(state='disabled')
        self.E5.configure(state='disabled')
        self.R2.configure(state='normal')
        self.R3.configure(state='normal')
        self.R4.configure(state='normal')
        self.R5.configure(state='disabled')
        self.X2.configure(state='normal')
        self.X3.configure(state='normal')
        self.X4.configure(state='normal')
        self.X5.configure(state='disabled')

    def make_5(self):
        global z
        z = 5
        self.A2.configure(state='normal')
        self.A3.configure(state='normal')
        self.A4.configure(state='normal')
        self.A5.configure(state='normal')
        self.B1.configure(state='normal')
        self.B2.configure(state='normal')
        self.B3.configure(state='normal')
        self.B4.configure(state='normal')
        self.B5.configure(state='normal')
        self.C1.configure(state='normal')
        self.C2.configure(state='normal')
        self.C3.configure(state='normal')
        self.C4.configure(state='normal')
        self.C5.configure(state='normal')
        self.D1.configure(state='normal')
        self.D2.configure(state='normal')
        self.D3.configure(state='normal')
        self.D4.configure(state='normal')
        self.D5.configure(state='normal')
        self.E1.configure(state='normal')
        self.E2.configure(state='normal')
        self.E3.configure(state='normal')
        self.E4.configure(state='normal')
        self.E5.configure(state='normal')
        self.R2.configure(state='normal')
        self.R3.configure(state='normal')
        self.R4.configure(state='normal')
        self.R5.configure(state='normal')
        self.X2.configure(state='normal')
        self.X3.configure(state='normal')
        self.X4.configure(state='normal')
        self.X5.configure(state='normal')

    def __init__(self, top=None):
        font7 = "-family {Comic Sans MS} -size 13 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        top.geometry("800x500+494+404")
        top.title("СЛАУ")

        self.A1 = Entry(top)
        self.A1.place(relx=0.06, rely=0.1,height=30, relwidth=0.07)
        self.A1.configure(font=font7, justify=CENTER)

        self.A2 = Entry(top)
        self.A2.place(relx=0.06, rely=0.22,height=30, relwidth=0.07)
        self.A2.configure(font=font7, justify=CENTER)

        self.A3 = Entry(top)
        self.A3.place(relx=0.06, rely=0.34,height=30, relwidth=0.07)
        self.A3.configure(font=font7, justify=CENTER)

        self.A4 = Entry(top)
        self.A4.place(relx=0.06, rely=0.46,height=30, relwidth=0.07)
        self.A4.configure(font=font7, justify=CENTER)

        self.A5 = Entry(top)
        self.A5.place(relx=0.06, rely=0.58,height=30, relwidth=0.07)
        self.A5.configure(font=font7, justify=CENTER)

        self.B1 = Entry(top)
        self.B1.place(relx=0.16, rely=0.1,height=30, relwidth=0.07)
        self.B1.configure(font=font7, justify=CENTER)

        self.B2 = Entry(top)
        self.B2.place(relx=0.16, rely=0.22,height=30, relwidth=0.07)
        self.B2.configure(font=font7, justify=CENTER)

        self.B3 = Entry(top)
        self.B3.place(relx=0.16, rely=0.34,height=30, relwidth=0.07)
        self.B3.configure(font=font7, justify=CENTER)

        self.B4 = Entry(top)
        self.B4.place(relx=0.16, rely=0.46,height=30, relwidth=0.07)
        self.B4.configure(font=font7, justify=CENTER)

        self.B5 = Entry(top)
        self.B5.place(relx=0.16, rely=0.58,height=30, relwidth=0.07)
        self.B5.configure(font=font7, justify=CENTER)

        self.C1 = Entry(top)
        self.C1.place(relx=0.26, rely=0.1,height=30, relwidth=0.07)
        self.C1.configure(font=font7, justify=CENTER)

        self.C2 = Entry(top)
        self.C2.place(relx=0.26, rely=0.22,height=30, relwidth=0.07)
        self.C2.configure(font=font7, justify=CENTER)

        self.C3 = Entry(top)
        self.C3.place(relx=0.26, rely=0.34,height=30, relwidth=0.07)
        self.C3.configure(font=font7, justify=CENTER)

        self.C4 = Entry(top)
        self.C4.place(relx=0.26, rely=0.46,height=30, relwidth=0.07)
        self.C4.configure(font=font7, justify=CENTER)

        self.C5 = Entry(top)
        self.C5.place(relx=0.26, rely=0.58,height=30, relwidth=0.07)
        self.C5.configure(font=font7, justify=CENTER)

        self.D1 = Entry(top)
        self.D1.place(relx=0.36, rely=0.1,height=30, relwidth=0.07)
        self.D1.configure(font=font7, justify=CENTER)

        self.D2 = Entry(top)
        self.D2.place(relx=0.36, rely=0.22,height=30, relwidth=0.07)
        self.D2.configure(font=font7, justify=CENTER)

        self.D3 = Entry(top)
        self.D3.place(relx=0.36, rely=0.34,height=30, relwidth=0.07)
        self.D3.configure(font=font7, justify=CENTER)

        self.D4 = Entry(top)
        self.D4.place(relx=0.36, rely=0.46,height=30, relwidth=0.07)
        self.D4.configure(font=font7, justify=CENTER)

        self.D5 = Entry(top)
        self.D5.place(relx=0.36, rely=0.58,height=30, relwidth=0.07)
        self.D5.configure(font=font7, justify=CENTER)

        self.E1 = Entry(top)
        self.E1.place(relx=0.46, rely=0.1,height=30, relwidth=0.07)
        self.E1.configure(font=font7, justify=CENTER)

        self.E2 = Entry(top)
        self.E2.place(relx=0.46, rely=0.22,height=30, relwidth=0.07)
        self.E2.configure(font=font7, justify=CENTER)

        self.E3 = Entry(top)
        self.E3.place(relx=0.46, rely=0.34,height=30, relwidth=0.07)
        self.E3.configure(font=font7, justify=CENTER)

        self.E4 = Entry(top)
        self.E4.place(relx=0.46, rely=0.46,height=30, relwidth=0.07)
        self.E4.configure(font=font7, justify=CENTER)

        self.E5 = Entry(top)
        self.E5.place(relx=0.46, rely=0.58,height=30, relwidth=0.07)
        self.E5.configure(font=font7, justify=CENTER)

        self.R1 = Entry(top)
        self.R1.place(relx=0.63, rely=0.1,height=30, relwidth=0.07)
        self.R1.configure(font=font7, justify=CENTER)

        self.R2 = Entry(top)
        self.R2.place(relx=0.63, rely=0.22,height=30, relwidth=0.07)
        self.R2.configure(font=font7, justify=CENTER)

        self.R3 = Entry(top)
        self.R3.place(relx=0.63, rely=0.34,height=30, relwidth=0.07)
        self.R3.configure(font=font7, justify=CENTER)

        self.R4 = Entry(top)
        self.R4.place(relx=0.63, rely=0.46,height=30, relwidth=0.07)
        self.R4.configure(font=font7, justify=CENTER)

        self.R5 = Entry(top)
        self.R5.place(relx=0.63, rely=0.58,height=30, relwidth=0.07)
        self.R5.configure(font=font7, justify=CENTER)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.06, rely=0.86, height=34, width=57)
        self.Button1.configure(font=font7)
        self.Button1.configure(text='''1''', command=self.make_1)

        self.Button2 = Button(top)
        self.Button2.place(relx=0.16, rely=0.86, height=34, width=57)
        self.Button2.configure(font=font7)
        self.Button2.configure(text='''2''', command=self.make_2)

        self.Button3 = Button(top)
        self.Button3.place(relx=0.26, rely=0.86, height=34, width=57)
        self.Button3.configure(font=font7)
        self.Button3.configure(text='''3''', command=self.make_3)

        self.Button4 = Button(top)
        self.Button4.place(relx=0.36, rely=0.86, height=34, width=57)
        self.Button4.configure(font=font7)
        self.Button4.configure(text='''4''', command=self.make_4)

        self.Button5 = Button(top)
        self.Button5.place(relx=0.46, rely=0.86, height=34, width=57)
        self.Button5.configure(font=font7)
        self.Button5.configure(text='''5''', command=self.make_5)

        self.size = Message(top)
        self.size.place(relx=0.08, rely=0.76, relheight=0.07, relwidth=0.45)
        self.size.configure(font=font7)
        self.size.configure(text='''Размер Матрицы''')
        self.size.configure(width=360)

        self.ButtonR = Button(top)
        self.ButtonR.place(relx=0.78, rely=0.74, height=34, width=137)
        self.ButtonR.configure(font=font7)
        self.ButtonR.configure(text='''Сбросить''', command=self.Reset)

        self.ButtonE = Button(top)
        self.ButtonE.place(relx=0.78, rely=0.86, height=34, width=137)
        self.ButtonE.configure(font=font7)
        self.ButtonE.configure(text='''Решить''', command=self.calc)

        self.MessagE = Message(top)
        self.MessagE.place(relx=0.54, rely=0.1, relheight=0.07, relwidth=0.08)
        self.MessagE.configure(font=font7)
        self.MessagE.configure(text='''=''')
        self.MessagE.configure(width=60)

        self.MessagE_22 = Message(top)
        self.MessagE_22.place(relx=0.54, rely=0.22, relheight=0.07, relwidth=0.08)
        self.MessagE_22.configure(font=font7)
        self.MessagE_22.configure(text='''=''')
        self.MessagE_22.configure(width=60)

        self.MessagE_23 = Message(top)
        self.MessagE_23.place(relx=0.54, rely=0.34, relheight=0.07, relwidth=0.08)
        self.MessagE_23.configure(font=font7)
        self.MessagE_23.configure(text='''=''')
        self.MessagE_23.configure(width=60)

        self.MessagE_24 = Message(top)
        self.MessagE_24.place(relx=0.54, rely=0.46, relheight=0.07, relwidth=0.08)
        self.MessagE_24.configure(font=font7)
        self.MessagE_24.configure(text='''=''')
        self.MessagE_24.configure(width=60)

        self.MessagE_25 = Message(top)
        self.MessagE_25.place(relx=0.54, rely=0.58, relheight=0.07, relwidth=0.08)
        self.MessagE_25.configure(font=font7)
        self.MessagE_25.configure(text='''=''')
        self.MessagE_25.configure(width=60)

        self.MessagX1 = Message(top)
        self.MessagX1.place(relx=0.81, rely=0.1, relheight=0.07, relwidth=0.08)
        self.MessagX1.configure(font=font7)
        self.MessagX1.configure(text='''X1=''')
        self.MessagX1.configure(width=60)

        self.MessagX2 = Message(top)
        self.MessagX2.place(relx=0.81, rely=0.22, relheight=0.07, relwidth=0.08)
        self.MessagX2.configure(font=font7)
        self.MessagX2.configure(text='''X2=''')
        self.MessagX2.configure(width=60)

        self.MessagX3 = Message(top)
        self.MessagX3.place(relx=0.81, rely=0.34, relheight=0.07, relwidth=0.08)
        self.MessagX3.configure(font=font7)
        self.MessagX3.configure(text='''X3=''')
        self.MessagX3.configure(width=60)

        self.MessagX4 = Message(top)
        self.MessagX4.place(relx=0.81, rely=0.46, relheight=0.07, relwidth=0.08)
        self.MessagX4.configure(font=font7)
        self.MessagX4.configure(text='''X4=''')
        self.MessagX4.configure(width=60)

        self.MessagX5 = Message(top)
        self.MessagX5.place(relx=0.81, rely=0.58, relheight=0.07, relwidth=0.08)
        self.MessagX5.configure(font=font7)
        self.MessagX5.configure(text='''X5=''')
        self.MessagX5.configure(width=60)

        self.X1 = Entry(top)
        self.X1.place(relx=0.89, rely=0.1,height=30, relwidth=0.07)
        self.X1.configure(font=font7, justify=CENTER)

        self.X2 = Entry(top)
        self.X2.place(relx=0.89, rely=0.22,height=30, relwidth=0.07)
        self.X2.configure(font=font7, justify=CENTER)

        self.X3 = Entry(top)
        self.X3.place(relx=0.89, rely=0.34,height=30, relwidth=0.07)
        self.X3.configure(font=font7, justify=CENTER)

        self.X4 = Entry(top)
        self.X4.place(relx=0.89, rely=0.46,height=30, relwidth=0.07)
        self.X4.configure(font=font7, justify=CENTER)

        self.X5 = Entry(top)
        self.X5.place(relx=0.89, rely=0.58,height=30, relwidth=0.07)
        self.X5.configure(font=font7, justify=CENTER)


if __name__ == '__main__':
    main()