import random
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk,Image
from tkcalendar import Calendar,DateEntry

class Bill:
    def __init__(self):
        self.sa=Tk()
        self.sa.title('Billing')
        self.sa.geometry('1920x1080')

        self.myfont=Font(self.sa,family='monospace',size=30,weight='bold',slant='italic')
        self.l1=Label(self.sa,text='Food Billing System',bg='light green',fg='black',font=self.myfont,height='2')
        self.l1.pack(fill=X)

        self.f1=Frame(self.sa,width='378',height='1050',bg='deep sky blue',border=1,highlightbackground='navy',highlightthickness=1.5)
        self.f1.pack(side=LEFT)
        self.f01=Frame(self.f1,width='378',height='35',bg='deep pink',highlightbackground='navy',highlightthickness=2)
        self.f01.place(x=-2,y=0)
        self.myfont1 = Font(self.sa, family='monospace', size=15, weight='bold', slant='italic')
        self.menu=Label(self.f01,text='Menu',bg='deep pink',fg='white',font=self.myfont1)
        self.menu.place(x=150,y=0)

        self.img = ImageTk.PhotoImage(Image.open('blob.jpeg'))
        self.i1 = Label(self.sa, image=self.img, height=94, width=200)
        self.i1.place(x=0, y=0)

        self.img1 = ImageTk.PhotoImage(Image.open('briyani.jpeg'))
        self.i2 = Label(self.sa, image=self.img1, height=94, width=200)
        self.i2.place(x=1160, y=0)

        self.myfont3 = Font(self.sa, family='monospace', size=12, slant='italic', weight='bold')

        self.ml0 = Label(self.f1, text='Idli\t\tRs:',font=self.myfont3,bg='deep sky blue',fg='blue')
        self.ml0.place(x=55, y=45)
        self.ml1 = Label(self.f1, text='Dosa \t\tRs: ',font=self.myfont3,bg='deep sky blue',fg='blue')
        self.ml1.place(x=55, y=80)
        self.ml2 = Label(self.f1, text='Poori \t\tRs:',font=self.myfont3,bg='deep sky blue',fg='blue')
        self.ml2.place(x=55, y=115)
        self.ml3 = Label(self.f1, text='Chicken Briyani \tRs:',font=self.myfont3,bg='deep sky blue',fg='blue')
        self.ml3.place(x=55, y=150)
        self.ml4 = Label(self.f1, text='Motton Briyani \tRs:',font=self.myfont3,bg='deep sky blue',fg='blue')
        self.ml4.place(x=55, y=185)
        self.ml5 = Label(self.f1, text='Moshrom Briyani \tRs:',font=self.myfont3,bg='deep sky blue',fg='blue')
        self.ml5.place(x=55, y=220)
        self.ml6 = Label(self.f1, text='Grill \t\tRs:',font=self.myfont3,bg='deep sky blue',fg='blue')
        self.ml6.place(x=55, y=255)
        self.ml7 = Label(self.f1, text='Dhanthuri \tRs:',font=self.myfont3,bg='deep sky blue',fg='blue')
        self.ml7.place(x=55, y=290)
        self.ml8 = Label(self.f1, text='Chicken Rice \tRs:',font=self.myfont3,bg='deep sky blue',fg='blue')
        self.ml8.place(x=55, y=325)
        self.ml9 = Label(self.f1, text='Egg Rice \t\tRs:',font=self.myfont3,bg='deep sky blue',fg='blue')
        self.ml9.place(x=55, y=360)
        self.ml10 = Label(self.f1, text='Juice \t\tRs:',font=self.myfont3,bg='deep sky blue',fg='blue')
        self.ml10.place(x=55, y=395)
        self.ml11= Label(self.f1, text='Meals \t\tRs:',font=self.myfont3,bg='deep sky blue',fg='blue')
        self.ml11.place(x=55, y=430)
        self.ml12 = Label(self.f1, text='Baratta \t\tRs: ',font=self.myfont3,bg='deep sky blue',fg='blue')
        self.ml12.place(x=55, y=465)
        self.ml13 = Label(self.f1, text='Coffee \t\tRs:',font=self.myfont3,bg='deep sky blue',fg='blue')
        self.ml13.place(x=55, y=500)
        self.ml14 = Label(self.f1, text='Tea \t\tRs:',font=self.myfont3,bg='deep sky blue',fg='blue')
        self.ml14.place(x=55, y=535)
        self.ml15 = Label(self.f1, text='Samosa \t\tRs:',font=self.myfont3,bg='deep sky blue',fg='blue')
        self.ml15.place(x=55, y=570)

        self.rl0 = Label(self.f1, text='10.00', font=self.myfont3, bg='deep sky blue',fg='dark orange')
        self.rl0.place(x=250, y=45)
        self.rl1 = Label(self.f1, text='20.00', font=self.myfont3, bg='deep sky blue',fg='dark orange')
        self.rl1.place(x=250, y=80)
        self.rl2 = Label(self.f1, text='15.00', font=self.myfont3, bg='deep sky blue',fg='dark orange')
        self.rl2.place(x=250, y=115)
        self.rl3 = Label(self.f1, text='170.00', font=self.myfont3, bg='deep sky blue',fg='dark orange')
        self.rl3.place(x=250, y=150)
        self.rl4 = Label(self.f1, text='200.00', font=self.myfont3, bg='deep sky blue',fg='dark orange')
        self.rl4.place(x=250, y=185)
        self.rl5 = Label(self.f1, text='150.00', font=self.myfont3, bg='deep sky blue',fg='dark orange')
        self.rl5.place(x=250, y=220)
        self.rl6 = Label(self.f1, text='250.00', font=self.myfont3, bg='deep sky blue',fg='dark orange')
        self.rl6.place(x=250, y=255)
        self.rl7 = Label(self.f1, text='180.00', font=self.myfont3, bg='deep sky blue',fg='dark orange')
        self.rl7.place(x=250, y=290)
        self.rl8 = Label(self.f1, text='80.00', font=self.myfont3, bg='deep sky blue',fg='dark orange')
        self.rl8.place(x=250, y=325)
        self.rl9 = Label(self.f1, text='60.00', font=self.myfont3, bg='deep sky blue',fg='dark orange')
        self.rl9.place(x=250, y=360)
        self.rl10 = Label(self.f1, text='30.00', font=self.myfont3, bg='deep sky blue',fg='dark orange')
        self.rl10.place(x=250, y=395)
        self.rl11 = Label(self.f1, text='100.00', font=self.myfont3, bg='deep sky blue',fg='dark orange')
        self.rl11.place(x=250, y=430)
        self.rl12 = Label(self.f1, text='15.00', font=self.myfont3, bg='deep sky blue',fg='dark orange')
        self.rl12.place(x=250, y=465)
        self.rl13 = Label(self.f1, text='12.00', font=self.myfont3, bg='deep sky blue',fg='dark orange')
        self.rl13.place(x=250, y=500)
        self.rl14 = Label(self.f1, text='8.00', font=self.myfont3, bg='deep sky blue',fg='dark orange')
        self.rl14.place(x=250, y=535)
        self.rl15 = Label(self.f1, text='5.00', font=self.myfont3, bg='deep sky blue',fg='dark orange')
        self.rl15.place(x=250, y=570)

        self.f2=Frame(self.sa,width='418',height='1050',bg='deep sky blue',border=1,highlightbackground='navy',highlightthickness=1.5)
        self.f2.pack(side=LEFT)
        self.f02=Frame(self.f2,width='418',height='35',bg='deep pink',highlightbackground='navy',highlightthickness=2)
        self.f02.place(x=-2,y=0)
        self.f002 = Frame(self.f2, width='418', height='50', bg='deep pink',highlightbackground='navy',highlightthickness=2)
        self.f002.place(x=-2, y=565)

        self.items=Label(self.f02,text='Ordered Items',bg='deep Pink',fg='white',font=self.myfont1)
        self.items.place(x=110,y=0)

        self.c1 = Label(self.f2, text='Idly \t\t:', font=self.myfont3, bg='deep sky blue',fg='blue')
        self.c1.place(x=35, y=45)
        self.c2 = Label(self.f2, text='Dosa \t\t:', font=self.myfont3, bg='deep sky blue',fg='blue')
        self.c2.place(x=35, y=77)
        self.c3 = Label(self.f2, text='Poori \t\t:', font=self.myfont3, bg='deep sky blue',fg='blue')
        self.c3.place(x=35, y=109)
        self.c4 = Label(self.f2, text='Chicken Briyani \t:', font=self.myfont3, bg='deep sky blue',fg='blue')
        self.c4.place(x=35, y=141)
        self.c5 = Label(self.f2, text='Motton Briyani  \t:', font=self.myfont3, bg='deep sky blue',fg='blue')
        self.c5.place(x=35, y=173)
        self.c6 = Label(self.f2, text='Moshrom Briyani  \t:', font=self.myfont3, bg='deep sky blue',fg='blue')
        self.c6.place(x=35, y=205)
        self.c7 = Label(self.f2, text='Grill \t\t:', font=self.myfont3, bg='deep sky blue',fg='blue')
        self.c7.place(x=35, y=237)
        self.c8 = Label(self.f2, text='Dhanthuri \t:', font=self.myfont3, bg='deep sky blue',fg='blue')
        self.c8.place(x=35, y=269)
        self.c9 = Label(self.f2, text='Chicken Rice \t:', font=self.myfont3, bg='deep sky blue',fg='blue')
        self.c9.place(x=35, y=301)
        self.c10 = Label(self.f2, text='Egg Rice \t\t:', font=self.myfont3, bg='deep sky blue',fg='blue')
        self.c10.place(x=35, y=333)
        self.c11 = Label(self.f2, text='Juice \t\t:', font=self.myfont3, bg='deep sky blue',fg='blue')
        self.c11.place(x=35, y=365)
        self.c12 = Label(self.f2, text='Meals \t\t:', font=self.myfont3, bg='deep sky blue',fg='blue')
        self.c12.place(x=35, y=397)
        self.c13 = Label(self.f2, text='Barotta \t\t:', font=self.myfont3, bg='deep sky blue',fg='blue')
        self.c13.place(x=35, y=429)
        self.c14 = Label(self.f2, text='Coffee \t\t:', font=self.myfont3, bg='deep sky blue',fg='blue')
        self.c14.place(x=35, y=461)
        self.c15 = Label(self.f2, text='Tea  \t\t:', font=self.myfont3, bg='deep sky blue',fg='blue')
        self.c15.place(x=35, y=493)
        self.c16 = Label(self.f2, text='Samosa \t\t:', font=self.myfont3, bg='deep sky blue',fg='blue')
        self.c16.place(x=35, y=525)

        self.e1 = Entry(self.f2, width=20,border=2)
        self.e1.place(x=235, y=47)
        self.e2 = Entry(self.f2, width=20,border=2)
        self.e2.place(x=235, y=79)
        self.e3 = Entry(self.f2, width=20,border=2)
        self.e3.place(x=235, y=111)
        self.e4 = Entry(self.f2, width=20,border=2)
        self.e4.place(x=235, y=143)
        self.e5 = Entry(self.f2, width=20,border=2)
        self.e5.place(x=235, y=175)
        self.e6 = Entry(self.f2, width=20,border=2)
        self.e6.place(x=235, y=207)
        self.e7 = Entry(self.f2, width=20,border=2)
        self.e7.place(x=235, y=239)
        self.e8 = Entry(self.f2, width=20,border=2)
        self.e8.place(x=235, y=271)
        self.e9 = Entry(self.f2, width=20,border=2)
        self.e9.place(x=235, y=303)
        self.e10 = Entry(self.f2, width=20,border=2)
        self.e10.place(x=235, y=335)
        self.e11 = Entry(self.f2, width=20,border=2)
        self.e11.place(x=235, y=367)
        self.e12 = Entry(self.f2, width=20,border=2)
        self.e12.place(x=235, y=399)
        self.e13 = Entry(self.f2, width=20,border=2)
        self.e13.place(x=235, y=431)
        self.e14 = Entry(self.f2, width=20,border=2)
        self.e14.place(x=235, y=463)
        self.e15 = Entry(self.f2, width=20,border=2)
        self.e15.place(x=235, y=495)
        self.e16 = Entry(self.f2, width=20,border=2)
        self.e16.place(x=235, y=527)

        self.e1.insert(0,'0')
        self.e2.insert(0,'0')
        self.e3.insert(0,'0')
        self.e4.insert(0,'0')
        self.e5.insert(0,'0')
        self.e6.insert(0,'0')
        self.e7.insert(0,'0')
        self.e8.insert(0,'0')
        self.e9.insert(0,'0')
        self.e10.insert(0,'0')
        self.e11.insert(0,'0')
        self.e12.insert(0,'0')
        self.e13.insert(0,'0')
        self.e14.insert(0,'0')
        self.e15.insert(0,'0')
        self.e16.insert(0,'0')

        self.f3=Frame(self.sa,width='794',height='300',bg='deep sky blue',border=1,highlightbackground='navy',highlightthickness=1.5)
        self.f3.pack(side=TOP)
        self.f03=Frame(self.f3,width='794',height='35',bg='deep pink',highlightbackground='navy',highlightthickness=2)
        self.f03.place(x=0,y=0)
        self.Bmenu = Label(self.f03, text='Bill Area', bg='deep pink', fg='white', font=self.myfont1)
        self.Bmenu.place(x=220, y=0)
        self.Tprice = Label(self.f3, text='Total Price\t:', bg='deep sky blue', font=self.myfont3, fg='blue')
        self.Tprice.place(x=80, y=65)
        self.Tax = Label(self.f3, text='TAX\t18%\t:', bg='deep sky blue', font=self.myfont3, fg='blue')
        self.Tax.place(x=80, y=110)
        self.cgst = Label(self.f3, text='C GST\t\t:', bg='deep sky blue', font=self.myfont3, fg='blue')
        self.cgst.place(x=80, y=150)
        self.sgst = Label(self.f3, text='S GST\t\t:', bg='deep sky blue', font=self.myfont3, fg='blue')
        self.sgst.place(x=80, y=190)
        self.nrate = Label(self.f3, text='Net Rate\t\t:', bg='deep sky blue', font=self.myfont3, fg='blue')
        self.nrate.place(x=80, y=230)

        self.etp = Entry(self.f3, width=30, border=2)
        self.etp.place(x=260, y=67)
        self.et = Entry(self.f3, width=30, border=2)
        self.et.place(x=260, y=109)
        self.ecg = Entry(self.f3, width=30, border=2)
        self.ecg.place(x=260, y=151)
        self.esg = Entry(self.f3, width=30, border=2)
        self.esg.place(x=260, y=193)
        self.enr = Entry(self.f3, width=30, border=2)
        self.enr.place(x=260, y=235)

        self.ysb = Scrollbar(self.sa, orient=VERTICAL)
        self.ysb.pack(side=RIGHT, fill=Y)

        self.txt = Text(self.sa, width='794', height='400', bg='dark gray', highlightbackground='navy',
                        highlightthickness=1.5, yscrollcommand=self.ysb.set)
        self.txt.pack(side=TOP)

        self.ysb.config(command=self.txt.yview)

        self.b1 = Button(self.f2, text='Total', bg='deep pink', padx=10, command=self.total)
        self.b1.place(x=30, y=580)
        self.b2 = Button(self.f2, text='Bill', bg='deep pink', padx=15, command=self.bill)
        self.b2.place(x=130, y=580)
        self.b3 = Button(self.f2, text='Clear', bg='deep pink', padx=10, command=self.clear)
        self.b3.place(x=230, y=580)
        self.b4 = Button(self.f2, text='Exit', bg='deep pink', padx=15, command=self.sa.quit)
        self.b4.place(x=330, y=580)

        self.sa.mainloop()

    def clear(self):

        self.e1.delete(0, END)
        self.e1.insert(0, '0')
        self.e2.delete(0, END)
        self.e2.insert(0, '0')
        self.e3.delete(0, END)
        self.e3.insert(0, '0')
        self.e4.delete(0, END)
        self.e4.insert(0, '0')
        self.e5.delete(0, END)
        self.e5.insert(0, '0')
        self.e6.delete(0, END)
        self.e6.insert(0, '0')
        self.e7.delete(0, END)
        self.e7.insert(0, '0')
        self.e8.delete(0, END)
        self.e8.insert(0, '0')
        self.e9.delete(0, END)
        self.e9.insert(0, '0')
        self.e10.delete(0, END)
        self.e10.insert(0, '0')
        self.e11.delete(0, END)
        self.e11.insert(0, '0')
        self.e12.delete(0, END)
        self.e12.insert(0, '0')
        self.e13.delete(0, END)
        self.e13.insert(0, '0')
        self.e14.delete(0, END)
        self.e14.insert(0, '0')
        self.e15.delete(0, END)
        self.e15.insert(0, '0')
        self.e16.delete(0, END)
        self.e16.insert(0, '0')

        self.etp.delete(0, END)
        self.et.delete(0, END)
        self.esg.delete(0, END)
        self.ecg.delete(0, END)
        self.enr.delete(0, END)

        self.txt.delete('1.0', END)

    def total(self):
        self.s1 = float(self.e1.get())
        self.y1 = float(self.rl0.cget('text'))
        self.sy1 = self.s1 * self.y1

        self.s2 = float(self.e2.get())
        self.y2 = float(self.rl1.cget('text'))
        self.sy2 = self.s2 * self.y2

        self.s3 = float(self.e3.get())
        self.y3 = float(self.rl2.cget('text'))
        self.sy3 = self.s3 * self.y3

        self.s4 = float(self.e4.get())
        self.y4 = float(self.rl3.cget('text'))
        self.sy4 = self.s4 * self.y4

        self.s5 = float(self.e5.get())
        self.y5 = float(self.rl4.cget('text'))
        self.sy5 = self.s5 * self.y5

        self.s6 = float(self.e6.get())
        self.y6 = float(self.rl5.cget('text'))
        self.sy6 = self.s6 * self.y6

        self.s7 = float(self.e7.get())
        self.y7 = float(self.rl6.cget('text'))
        self.sy7 = self.s7 * self.y7

        self.s8 = float(self.e8.get())
        self.y8 = float(self.rl7.cget('text'))
        self.sy8 = self.s8 * self.y8

        self.s9 = float(self.e9.get())
        self.y9 = float(self.rl8.cget('text'))
        self.sy9 = self.s9 * self.y9

        self.s10 = float(self.e10.get())
        self.y10 = float(self.rl9.cget('text'))
        self.sy10 = self.s10 * self.y10

        self.s11 = float(self.e11.get())
        self.y11 = float(self.rl10.cget('text'))
        self.sy11 = self.s11 * self.y11

        self.s12 = float(self.e12.get())
        self.y12 = float(self.rl11.cget('text'))
        self.sy12 = self.s12 * self.y12

        self.s13 = float(self.e13.get())
        self.y13 = float(self.rl12.cget('text'))
        self.sy13 = self.s13 * self.y13

        self.s14 = float(self.e14.get())
        self.y14 = float(self.rl13.cget('text'))
        self.sy14 = self.s14 * self.y14

        self.s15 = float(self.e15.get())
        self.y15 = float(self.rl14.cget('text'))
        self.sy15 = self.s15 * self.y15

        self.s16 = float(self.e16.get())
        self.y16 = float(self.rl15.cget('text'))
        self.sy16 = self.s16 * self.y16

        self.ToTal = self.sy1 + self.sy2 + self.sy3 + self.sy4 + self.sy5 + self.sy6 + self.sy7 + self.sy8 + self.sy9 + self.sy10 + self.sy11 + self.sy12 + self.sy13 + self.sy14 + self.sy15 + self.sy16

        self.etp.delete(0, END)
        self.etp.insert(0, self.ToTal)

        self.et.delete(0, END)
        self.tax = self.ToTal * 18 / 100
        self.et.insert(0, self.tax)

        self.cgst = self.tax / 2
        self.ecg.delete(0, END)
        self.ecg.insert(0, self.cgst)

        self.sgst = self.tax / 2
        self.esg.delete(0, END)
        self.esg.insert(0, self.sgst)

        self.net = self.tax + self.cgst + self.sgst + self.ToTal
        self.enr.delete(0, END)
        self.enr.insert(0, self.net)

    def bill(self):

        self.txt.delete('1.0', END)
        self.txt.insert(END, '\n\t\t\t  HOTEL 20 20')
        self.txt.insert(END, '\n--------------------------------------------------------------------')
        self.txt.insert(END, '\nBill No\t:\t' + str(random.randint(1000, 100000)))
        self.txt.insert(END, '\nDate\t:'+str(tkcalendar.Calendar))
        self.txt.insert(END, '\n--------------------------------------------------------------------')
        self.txt.insert(END, '\n\tProducts\t\t\tQuantity\t\t\tPrice\t')
        self.txt.insert(END, '\n--------------------------------------------------------------------')

        if self.s1 != 0:
            self.txt.insert(END, '\n\tItali' + '\t\t\t' + str(self.s1) + '\t\t\t' + str(self.sy1))

        if self.s2 != 0:
            self.txt.insert(END, '\n\tD0sa' + '\t\t\t' + str(self.s2) + '\t\t\t' + str(self.sy2))

        if self.s3 != 0:
            self.txt.insert(END, '\n\tPoori' + '\t\t\t' + str(self.s3) + '\t\t\t' + str(self.sy3))

        if self.s4 != 0:
            self.txt.insert(END, '\n\tChicken briyani' + '\t\t\t' + str(self.s4) + '\t\t\t' + str(self.sy4))

        if self.s5 != 0:
            self.txt.insert(END, '\n\tMotton Briyani' + '\t\t\t' + str(self.s5) + '\t\t\t' + str(self.sy5))

        if self.s6 != 0:
            self.txt.insert(END, '\n\tMoshrom Briyani' + '\t\t\t' + str(self.s6) + '\t\t\t' + str(self.sy6))

        if self.s7 != 0:
            self.txt.insert(END, '\n\tGrill' + '\t\t\t' + str(self.s7) + '\t\t\t' + str(self.sy7))

        if self.s8 != 0:
            self.txt.insert(END, '\n\tDhanthur' + '\t\t\t' + str(self.s8) + '\t\t\t' + str(self.sy8))

        if self.s9 != 0:
            self.txt.insert(END, '\n\tChicken Rice' + '\t\t\t' + str(self.s9) + '\t\t\t' + str(self.sy9))

        if self.s10 != 0:
            self.txt.insert(END, '\n\tEgg Rice' + '\t\t\t' + str(self.s10) + '\t\t\t' + str(self.sy10))

        if self.s11 != 0:
            self.txt.insert(END, '\n\tJuice' + '\t\t\t' + str(self.s11) + '\t\t\t' + str(self.sy11))

        if self.s12 != 0:
            self.txt.insert(END, '\n\tMeals' + '\t\t\t' + str(self.s12) + '\t\t\t' + str(self.sy12))

        if self.s13 != 0:
            self.txt.insert(END, '\n\tBarotta' + '\t\t\t' + str(self.s13) + '\t\t\t' + str(self.sy13))

        if self.s14 != 0:
            self.txt.insert(END, '\n\tCoffee' + '\t\t\t' + str(self.s14) + '\t\t\t' + str(self.sy14))

        if self.s15 != 0:
            self.txt.insert(END, '\n\tTea' + '\t\t\t' + str(self.s15) + '\t\t\t' + str(self.sy15))

        if self.s16 != 0:
            self.txt.insert(END, '\n\tSamosa' + '\t\t\t' + str(self.s16) + '\t\t\t' + str(self.sy16))

        self.txt.insert(END, '\n--------------------------------------------------------------------')
        self.txt.insert(END, '\n\t\t\t\tTAX\t18%\t:' + '\t' + str(self.tax))
        self.txt.insert(END, '\n\t\t\t\tC GST\t\t:' + '\t' + str(self.cgst))
        self.txt.insert(END, '\n\t\t\t\tS GST\t\t:' + '\t' + str(self.sgst))
        self.txt.insert(END, '\n--------------------------------------------------------------------')
        self.txt.insert(END, '\n\t\t\t\tTotal Price\t\t:' + '\t' + str(self.net))
        self.txt.insert(END, '\n--------------------------------------------------------------------')
        self.txt.insert(END, '\n\t\t\t!!  Thank Q  !!')

z = Bill()