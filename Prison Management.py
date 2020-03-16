from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
from PIL import ImageTk,Image
import sqlite3

conn=sqlite3.connect('Prison.db')
c=conn.cursor()


def main():
    root=Tk()
    app=PrisonLogin(root)
    if __name__ == '__main__':
        root.mainloop()
#==================LOGIN PAGE===========================================================================================
class PrisonLogin:
    def __init__(self,master):
        self.master=master
        self.master.title("Prison Login")
        self.master.geometry("1400x1080")
        self.master.config(bg='black')
        self.frame=Frame(self.master, width=50,height=50,bg='black')
        self.frame.pack()
        self.Username=StringVar()
        self.Password = StringVar()
        self.lb1Title=Label(self.frame,text="Prison Management System",font=('arial',50,'bold'),bg='black',fg='red')
        self.lb1Title.grid(row=0,column=0,columnspan=2,pady=20)
        self.photo2 = PhotoImage(file='Prisoner1.png')
        self.photo = Label(self.frame, image=self.photo2, bg='white')
        self.photo.grid(row=1,column=0)

    #===================================================================================================================
        self.LoginFrame1=LabelFrame(self.frame,width=50,height=50,text="Login",font=('arial',20,'bold'),relief='ridge',bg='black',bd=0,fg='red')
        self.LoginFrame1.grid(row=1,column=1)
        self.LoginFrame2 = LabelFrame(self.frame, width=50, height=50,font=('arial', 20, 'bold'), relief='ridge',
                                      bg='black', bd=0,fg='red')
        self.LoginFrame2.grid(row=2, column=1)
    #===================================================================================================================
        self.lblUsername=Label(self.LoginFrame1,text="Username",font=('arial',20,'bold'),bd=15,bg='black',fg='red')
        self.lblUsername.grid(row=0,column=0)

        self.txtUsername=Entry(self.LoginFrame1,font=('arial',10,'bold'),bd=0,textvariable=self.Username,width=33)
        self.txtUsername.grid(row=0,column=1,padx=10)

        self.lblPassword=Label(self.LoginFrame1,text="Password",font=('arial',20,'bold'),bd=15,bg='black',fg='red')
        self.lblPassword.grid(row=1,column=0)

        self.txtPassword=Entry(self.LoginFrame1,font=('arial',10,'bold'),show='*',bd=0,textvariable=self.Password,width=33)
        self.txtPassword.grid(row=1,column=1,columnspan=2,pady=5)
    #===================================================================================================================
        self.btnLogin=Button(self.LoginFrame2,text="Login",width=10,font=('arial',14,'bold'),bg='black',fg='red',command=self.Login_System)
        self.btnLogin.grid(row=2,column=0,pady=5,padx=5)

        self.btnReset = Button(self.LoginFrame2, text="Reset", width=10, font=('arial', 14, 'bold'), bg='black',
                               fg='red',command=self.iReset)
        self.btnReset.grid(row=2, column=1, pady=5, padx=5)

        self.btnExit = Button(self.LoginFrame2, text="Exit", width=10, font=('arial', 14, 'bold'), bg='black',
                               fg='red',command=self.iExit)
        self.btnExit.grid(row=2, column=2, pady=5, padx=5)

    def Login_System(self):
        user=(self.Username.get())
        pas=(self.Password.get())
        if(user==str('Jailor') and pas==str('Jailor@prison')):
           self.Login_Window()
        else:
           tkinter.messagebox.askyesno("Prison Login","Invalid Login Details")
           self.Username.set("")
           self.Password.set("")

    def iReset(self):
        self.Username.set("")
        self.Password.set("")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Prison Login System","Confirm if you want to exit")
        if self.iExit>0:
          self.master.destroy()
          return

    def Login_Window(self):
        self.PrisonWindow=Toplevel(self.master)
        self.app=PrisonManagement(self.PrisonWindow)
#========================END OF LOGIN PAGE==============================================================================
#========================MENU OF PRISON STARTS==========================================================================
class PrisonManagement:
    def __init__(self,master):
        self.master=master
        self.master.title("Prison Login")
        self.master.geometry("1400x1080")
        self.master.config(bg='Black')
        self.frame = Frame(self.master, width=50, height=50, bg='black')
        self.frame.pack()
        self.lb1Title = Label(self.frame, text="Welcome to Shawshank Prison", font=('arial', 50, 'bold'), bg='black',
                              fg='red')
        self.lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        self.photo2 = PhotoImage(file='Prison Main1.png')
        self.photo = Label(self.frame, image=self.photo2, bg='white').grid(row=1,column=0)

        self.LoginFrame1 = LabelFrame(self.frame, width=50, height=50, font=('arial', 20, 'bold'),
                                      relief='ridge', bg='black', bd=0, fg='red')
        self.LoginFrame1.grid(row=2, column=0)
        self.btnLogin = Button(self.LoginFrame1, text="Prisoner", width=10, font=('arial', 25, 'bold'), bg='black',
                               fg='red',command=self.ThePrisoner)
        self.btnLogin.grid(row=0, column=0, pady=5, padx=4)
        self.btnstaff = Button(self.LoginFrame1, text="Staff", width=10, font=('arial', 25, 'bold'), bg='black',
                               fg='red',command=self.Staff)
        self.btnstaff.grid(row=0, column=1, pady=5, padx=5)
        self.btnEdcatin = Button(self.LoginFrame1, text="Education", width=10, font=('arial', 25, 'bold'), bg='black',
                               fg='red',command=self.Edu)
        self.btnEdcatin.grid(row=0, column=2, pady=5, padx=5)
        self.btnRemand = Button(self.LoginFrame1, text="Remand Case", width=15, font=('arial',25, 'bold'), bg='black',
                               fg='red',command=self.Remand)
        self.btnRemand.grid(row=0, column=3, pady=5, padx=5)
        self.btnCase = Button(self.LoginFrame1, text="Cases", width=10, font=('arial', 25, 'bold'), bg='black',
                               fg='red',command=self.Crime)
        self.btnCase.grid(row=0, column=4, pady=5, padx=5)
        self.btnBack = Button(self.frame, text="Exit", width=10, font=('arial', 20, 'bold'), bg='black',
                               fg='red',command=self.exit)
        self.btnBack.grid(row=25, column=0, pady=5, padx=5)
    ###################################################################################################################
    def ThePrisoner(self):
        self.PrisonWindow1 = Toplevel(self.master)
        self.app = Prisoner(self.PrisonWindow1)


    def Staff(self):
        self.Prisonstaff=Toplevel(self.master)
        self.app=PrisonStaff(self.Prisonstaff)

    def Remand(self):
        self.remand=Toplevel(self.master)
        self.app=PrisonRemand(self.remand)

    def Edu(self):
        self.edu=Toplevel(self.master)
        self.app=PrisonEdu(self.edu)

    def Crime(self):
        self.crime = Toplevel(self.master)
        self.app = PrisonerCases(self.crime)
    def exit(self):
        self.master.destroy()

#========================END OF MENU PAGE===============================================================================

#========================START OF PRISONER PAGE=========================================================================
class Prisoner:
    def __init__(self, master):
        self.p=master
        self.p.title("Prisoner")
        self.p.geometry("1400x1080")
        self.p.config(bg='Black')
        self.frame = Frame(self.p, width=50, height=50, bg='black')
        self.frame.pack()
        #===============================================================================================================
        self.lb1Title = Label(self.frame, text="Prisoner Details", font=('arial', 50, 'bold'), bg='black',
                              fg='red')
        self.lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        self.photo2 = PhotoImage(file='Male Prisoner.png')
        self.photo = Label(self.frame, image=self.photo2, bg='white').grid(row=1, column=0)
        #===============================================================================================================
        self.LoginFrame1 = LabelFrame(self.frame, width=50, height=50, font=('arial', 20, 'bold'),
                                      relief='ridge', bg='black', bd=0, fg='red')
        self.LoginFrame1.grid(row=2, column=0)
        self.btnPrisoner = Button(self.LoginFrame1, text="Add Prisoner", width=10, font=('arial', 20, 'bold'), bg='black',
                               fg='red',command=self.FillForm)
        self.btnPrisoner.grid(row=0, column=0, pady=5, padx=5)
        self.btnDelete = Button(self.LoginFrame1, text="Delete Prisoner", width=15, font=('arial', 20, 'bold'), bg='black',
                               fg='red',command=self.delete)
        self.btnDelete.grid(row=0, column=1, pady=5, padx=5)
        self.UP=Button(self.LoginFrame1, text="Update Prisoner Record",width=20, font=('arial', 20, 'bold'), bg='black',
                               fg='red',command=self.up)
        self.UP.grid(row=0,column=2,pady=5,padx=10)
        self.btnView = Button(self.LoginFrame1, text="View Prisoners", width=12, font=('arial', 20, 'bold'),
                                bg='black',fg='red',command=self.Show)
        self.btnView.grid(row=0, column=3, pady=5, padx=5)
        self.btnBack = Button(self.frame, text="Back", width=10, font=('arial', 20, 'bold'), bg='black',
                              fg='red',command=self.iExit)
        self.btnBack.grid(row=25, column=0, pady=5, padx=5)


    def FillForm(self):
        self.Form = Toplevel(self.p)
        self.app = DetailsForm(self.Form)
    def delete(self):
        self.d = Toplevel(self.p)
        self.app = Delete(self.d)
    def Show(self):
        self.show=Toplevel(self.p)
        self.app=ShowR(self.show)
    def up(self):
        self.PUP = Toplevel(self.p)
        self.app = UpdateP(self.PUP)
    def iExit(self):
        self.p.destroy()


#========================DETAILS IN PRISONER============================================================================
class DetailsForm:
    def __init__(self, master):
        def aaa():
            self.conne = sqlite3.connect('Prison.db')
            cca = self.conne.cursor()
            cca.execute(
                "INSERT INTO Prisoner VALUES(:id, :First_name, :Last_name, :Age,  :Height, :Cellno, :Gender, :Duration)",
                {
                    'id': self.id.get(),
                    'First_name': self.firstname.get(),
                    'Last_name': self.lastname.get(),

                    'Age': self.age.get(),
                    'Height': self.height.get(),
                    'Cellno': self.cellno.get(),
                    'Gender': self.gender.get(),
                    'Duration': self.duration.get()
                })
            self.conne.commit()

            self.conne.close()


            self.id.set("")
            self.firstname.set("")
            self.lastname.set("")

            self.age.set("")
            self.height.set("")
            self.cellno.set("")
            self.gender.set("")
            self.duration.set("")

        def sub():
            self.conn = sqlite3.connect('Prison.db')
            self.cc = self.conn.cursor()
            self.conn.close()
            try:
                conn.create_function("aa",0,aaa())
                self.cc.execute("select aa()")
            except:
                pass

        self.f=master
        self.f.title("Prisoner Details")
        self.f.geometry("1400x1080")
        self.f.config(bg='Black')
        self.frame = Frame(self.f, width=50, height=50, bg='black')
        self.frame.pack()
        self.id = IntVar()
        self.firstname = StringVar()
        self.lastname=StringVar()
        self.age=IntVar()
        self.gender=StringVar()
        self.cellno=IntVar()
        self.height=StringVar()
        self.duration=StringVar()
        self.lb1Title = Label(self.frame, text="Enter Priosner Details", font=('arial', 40, 'bold'), bg='black',
                              fg='red')
        self.lb1Title.grid(row=0, column=0, columnspan=2, pady=20)

        self.ID = Label(self.frame, text="Prisoner ID", font=('arial', 20, 'bold'), bd=15, bg='black',
                                 fg='red')
        self.ID.grid(row=1, column=0)

        self.pid = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.id,
                                 width=33)
        self.pid.grid(row=1, column=1, padx=10)

        self.Firstname = Label(self.frame, text="First Name", font=('arial', 20, 'bold'), bd=15, bg='black',
                        fg='red')
        self.Firstname.grid(row=2, column=0)

        self.Fname = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.firstname,
                         width=33)
        self.Fname.grid(row=2, column=1, padx=5)
        self.Lastname = Label(self.frame, text="Last Name", font=('arial', 20, 'bold'), bd=15, bg='black',
                               fg='red')
        self.Lastname.grid(row=2, column=2)

        self.Lname = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.lastname,
                           width=33)
        self.Lname.grid(row=2, column=3, padx=5)

        self.Ag = Label(self.frame, text="Age", font=('arial', 20, 'bold'), bd=15, bg='black',
                        fg='red')
        self.Ag.grid(row=3, column=0)

        self.Age = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.age,
                         width=33)
        self.Age.grid(row=3, column=1, padx=10)

        self.Hei = Label(self.frame, text="Height", font=('arial', 20, 'bold'), bd=15, bg='black',
                        fg='red')
        self.Hei.grid(row=4, column=0)

        self.Height = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.height,
                         width=33)
        self.Height.grid(row=4, column=1, padx=10)

        self.Cell = Label(self.frame, text="Cell Number", font=('arial', 20, 'bold'), bd=15, bg='black',
                        fg='red')
        self.Cell.grid(row=5, column=0)

        self.Cellno = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.cellno,
                         width=33)
        self.Cellno.grid(row=5, column=1, padx=10)
        self.Gend = Label(self.frame, text="Gender", font=('arial', 20, 'bold'), bd=15, bg='black',
                          fg='red')
        self.Gend.grid(row=6, column=0)

        self.Gender = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.gender,
                         width=33)
        self.Gender.grid(row=6, column=1, padx=10)

        self.Dura = Label(self.frame, text="Duration", font=('arial', 20, 'bold'), bd=15, bg='black',
                        fg='red')
        self.Dura.grid(row=7, column=0)

        self.Duration = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.duration,width=33)
        self.Duration.grid(row=7, column=1, padx=10)

        self.btnSubmit = Button(self.frame, text="Submit", width=10, font=('arial', 15, 'bold'),
                                bg='black',fg='red',command=sub)
        self.btnSubmit.grid(row=8, column=0, pady=5, padx=5)
        self.btnClear = Button(self.frame, text="Reset", width=10, font=('arial', 15, 'bold'),
                              bg='black',
                              fg='red')
        self.btnClear.grid(row=8, column=2, pady=5, padx=5)
        self.btnBack = Button(self.frame, text="Exit", width=10, font=('arial', 15, 'bold'), bg='black',
                              fg='red',command=self.iexit)
        self.btnBack.grid(row=8, column=3, pady=5, padx=5)

    # def sub(self):
    #
    #     self.conn = sqlite3.connect('Prison.db')
    #     self.c = self.conn.cursor()
    #     self.c.execute("INSERT INTO Prisoner VALUES(:id, :First_name, :Last_name, :Age,  :Height, :Cellno, :Gender, :Duration)",
    #               {
    #                   'id': self.id.get(),
    #                   'First_name': self.firstname.get(),
    #                   'Last_name':self.lastname.get(),
    #
    #                   'Age': self.age.get(),
    #                   'Height': self.height.get(),
    #                   'Cellno': self.cellno.get(),
    #                   'Gender': self.gender.get(),
    #                   'Duration':self.duration.get()
    #               })
    #     self.conn.commit()
    #     self.conn.close()
    #
    #     self.id.set("")
    #     self.firstname.set("")
    #     self.lastname.set("")
    #
    #     self.age.set("")
    #     self.height.set("")
    #     self.cellno.set("")
    #     self.gender.set("")
    #     self.duration.set("")


    def iexit(self):
        self.f.destroy()

#========================END OF DETAILS IN PRISONER=====================================================================
#========================START OF DELETE IN PRISONER====================================================================
class Delete:

     def __init__(self, master):
          self.d = master
          self.d.title("Prisoner Details")
          self.d.geometry("1400x1080")
          self.d.config(bg='Black')
          self.frame = Frame(self.d, width=50, height=50, bg='black')
          self.frame.pack()
          self.id = StringVar()
          self.lb1Title = Label(self.frame, text="Delete Prisoner Record", font=('arial', 40, 'bold'), bg='black', fg='red')
          self.lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
          self.ID = Label(self.frame, text="Enter Prisoner ID", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
          self.ID.grid(row=1, column=0)
          self.pid = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.id, width=33)
          self.pid.grid(row=1, column=1, padx=10)
          self.btndelete = Button(self.frame, text="Delete", width=10, font=('arial', 15, 'bold'),bg='black', fg='red', command=self.dell)
          self.btndelete.grid(row=2, column=0, pady=5, padx=5)
          self.btnBack = Button(self.frame, text="Exit", width=10, font=('arial', 15, 'bold'), bg='black', fg='red', command=self.Exit)
          self.btnBack.grid(row=2, column=3, pady=5, padx=5)
     def dell(self):
         self.him=StringVar()
         self.him=self.id.get()
         conn = sqlite3.connect("Prison.db")
         c = conn.cursor()
         c.execute("DELETE FROM Prisoner WHERE ID="+self.him)
         conn.commit()
         c.execute("DELETE FROM RemandCase WHERE oid=" + self.him)
         conn.commit()
         c.execute("DELETE FROM Education WHERE oid=" + self.him)
         conn.commit()

         conn.close()
     def Exit(self):
         self.d.destroy()

class UpdateP:
    def __init__(self, master):
        self.u=master
        self.u.title("Prisoner Details")
        self.u.geometry("1400x1080")
        self.u.config(bg='Black')
        frame = Frame(self.u, width=50, height=50, bg='black')
        frame.pack()
        global Uid
        global UFname
        global ULname
        global UAge
        global UHeight
        global UCellno
        global UGender
        global UDuration
        self.UID=StringVar()
        lb1Title = Label(frame, text="Update Prisoner Record", font=('arial', 40, 'bold'), bg='black',fg='red')
        lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        uid = Label(frame, text="Enter Prisoner ID", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        uid.grid(row=1, column=0)
        upid = Entry(frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.UID, width=33)
        upid.grid(row=1, column=1, padx=10)
        update = Button(frame, text="Update", width=10, font=('arial', 15, 'bold'),bg='black', fg='red', command=self.UP)
        update.grid(row=2, column=3, pady=5, padx=5)
        Firstname = Label(frame, text="First Name", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Firstname.grid(row=3, column=0)
        UFname = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        UFname.grid(row=3, column=1, padx=5)
        Lastname = Label(frame, text="Last Name", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Lastname.grid(row=3, column=2)
        ULname = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        ULname.grid(row=3, column=3, padx=5)
        Ag = Label(frame, text="Age", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Ag.grid(row=4, column=0)
        UAge = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        UAge.grid(row=4, column=1, padx=10)
        Hei = Label(frame, text="Height", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Hei.grid(row=4, column=2)
        UHeight = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        UHeight.grid(row=4, column=3, padx=10)
        Cell = Label(frame, text="Cell Number", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Cell.grid(row=5, column=0)
        UCellno = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        UCellno.grid(row=5, column=1, padx=10)
        Gend = Label(frame, text="Gender", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Gend.grid(row=5, column=2)
        UGender = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        UGender.grid(row=5, column=3, padx=10)
        Dura = Label(frame, text="Duration", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Dura.grid(row=6, column=0)
        UDuration = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        UDuration.grid(row=6, column=1, padx=10)
        btnSubmit = Button(frame, text="Save Record", width=10, font=('arial', 15, 'bold'),bg='black', fg='red', command=self.Usub)
        btnSubmit.grid(row=7, column=0, pady=5, padx=5)
        btnex=Button(frame, text="Exit", width=10, font=('arial', 15, 'bold'),bg='black', fg='red', command=self.Uex).grid(row=7,column=2,pady=5,padx=5)
    def UP(self):
        conn = sqlite3.connect("Prison.db")
        c = conn.cursor()
        self.record_id=self.UID.get()
        c.execute("SELECT * FROM Prisoner WHERE ID=?",(self.record_id,))
        records=c.fetchall()
        for record in records:
            UFname.insert(0, record[1])
            ULname.insert(0, record[2])
            UAge.insert(0, record[3])
            UHeight.insert(0, record[4])
            UCellno.insert(0, record[5])
            UGender.insert(0, record[6])
            UDuration.insert(0, record[7])
    def Usub(self):
        conn = sqlite3.connect("Prison.db")
        c = conn.cursor()
        c.execute("UPDATE Prisoner SET  FirstName= :first, LastName= :last, Age= :ag, Height= :hei, Cellno= :cell, Gender= :gend, Duration= :dura  WHERE ID= :id",
                  {
                      'id':self.UID.get(),
                      'first':  UFname.get(),
                      'last': ULname.get(),
                      'ag': UAge.get(),
                      'hei':UHeight.get(),
                      'cell':UCellno.get(),
                      'gend':UGender.get(),
                      'dura':UDuration.get()
                  })
        conn.commit()
        conn.close()
    def Uex(self):
        self.u.destroy()





#========================END OF DELETE IN PRISONER======================================================================
#============================PRINT PRISONER RECORD======================================================================
class ShowR:
    def __init__(self, master):
        self.d=master
        self.d.title("Show Records")
        self.d.geometry("1400x1080")
        self.d.config(bg='Black')
        self.frame = Frame(self.d, width=50, height=50, bg='black')
        self.frame.pack()
        self.lb1Title = Label(self.frame, text="Prisoners Records", font=('arial', 40, 'bold'), bg='black',fg='red')
        self.lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        self.LoginFrame1 = LabelFrame(self.frame, width=50, height=50, font=('arial', 30, 'bold'),relief='ridge', bg='black', bd=0, fg='red')
        self.LoginFrame1.grid(row=1, column=0)
        self.lab1=Label(self.LoginFrame1,text="ID",font=('arial',25, 'bold'),bg='black',fg='red').grid(row=0,column=0)
        self.lab2 = Label(self.LoginFrame1, text="First Name", font=('arial', 25, 'bold'), bg='black', fg='red').grid(row=0,column=1)
        self.lab3 = Label(self.LoginFrame1, text="Last Name", font=('arial', 25, 'bold'), bg='black', fg='red').grid(row=0,column=2)
        self.lab4 = Label(self.LoginFrame1, text="Age", font=('arial', 25, 'bold'), bg='black', fg='red').grid(row=0,column=3)
        self.lab5 = Label(self.LoginFrame1, text="Height", font=('arial', 25, 'bold'), bg='black', fg='red').grid(row=0,column=4)
        self.lab6 = Label(self.LoginFrame1, text="Cell Number", font=('arial', 25, 'bold'), bg='black', fg='red').grid(row=0, column=5)
        self.lab7 = Label(self.LoginFrame1, text="Gender", font=('arial', 25, 'bold'), bg='black', fg='red').grid(row=0,column=6)
        self.lab8 = Label(self.LoginFrame1, text="Duration", font=('arial',20, 'bold'), bg='black', fg='red').grid(row=0,column=7)
        row_no=0
        self.conn = sqlite3.connect('Prison.db')
        self.c = self.conn.cursor()
        values=self.c.execute("select * from Prisoner order by ID ")
        self.records=self.c.fetchall()
        for self.record in self.records:
            id_no=self.record[0]
            f_name=self.record[1]
            l_name=self.record[2]
            age=self.record[3]
            hei_ght=self.record[4]
            cell_num=self.record[5]
            gend_er=self.record[6]
            dur_ation=self.record[7]
            row_no=row_no+1
            self.Label=Label(self.LoginFrame1, text=id_no, width=7, font=('times', 20, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=0, padx=(0, 2))
            self.Labe2 = Label(self.LoginFrame1, text=f_name, width=15, font=('times', 20, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=1, padx=(0, 2))
            self.Labe3 = Label(self.LoginFrame1, text=l_name, width=15, font=('times', 20, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=2, padx=(0, 2))
            self.Labe4 = Label(self.LoginFrame1, text=age, width=7, font=('times', 20, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=3, padx=(0, 2))
            self.Labe5 = Label(self.LoginFrame1, text=hei_ght, width=9, font=('times', 20, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=4, padx=(0, 2))
            self.Labe6 = Label(self.LoginFrame1, text=cell_num, width=13, font=('times', 20, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=5, padx=(0, 2))
            self.Labe7 = Label(self.LoginFrame1, text=gend_er, width=13, font=('times', 20, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=6, padx=(0, 2))
            self.Labe8 = Label(self.LoginFrame1, text=dur_ation, width=5, font=('times', 20, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=7, padx=(0, 2))
        row_no=row_no+6
        self.btnBack = Button(self.frame, text="Exit", width=10, font=('arial', 15, 'bold'), bg='black',fg='red', command=self.iexit)
        self.btnBack.grid(row=row_no, column=0, pady=5, padx=5)
        self.conn.commit()
        self.conn.close()
    def iexit(self):
        self.d.destroy()
#========================END OF PRINT IN PRISONER ======================================================================
#========================END OF PRISONER TABLE==========================================================================
#======================STAFF TABLE======================================================================================
class PrisonStaff:
    def __init__(self, master):
        self.s=master
        self.s.title("Prisoner Staff")
        self.s.geometry("1400x1080")
        self.s.config(bg='Black')
        self.frame = Frame(self.s, width=50, height=50, bg='black')
        self.frame.pack()

        self.lb1Title = Label(self.frame, text="Staff Details", font=('arial', 50, 'bold'), bg='black',
                              fg='red')
        self.lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        self.photo2 = PhotoImage(file='Staff.png')
        self.photo = Label(self.frame, image=self.photo2, bg='white').grid(row=1, column=0)
        self.LoginFrame1 = LabelFrame(self.frame, width=50, height=50, font=('arial', 20, 'bold'),
                                      relief='ridge', bg='black', bd=0, fg='red')
        self.LoginFrame1.grid(row=2, column=0)
        self.btnPrisoner = Button(self.LoginFrame1, text="Add Staff", width=10, font=('arial', 25, 'bold'),
                                  bg='black',fg='red',command=self.add)
        self.btnPrisoner.grid(row=0, column=0, pady=5, padx=5)
        self.btnDelete = Button(self.LoginFrame1, text="Delete Staff", width=10, font=('arial', 25, 'bold'),
                                bg='black',
                                fg='red',command=self.delete)
        self.btnDelete.grid(row=0, column=1, pady=5, padx=5)
        self.btnView = Button(self.LoginFrame1, text="View Staff", width=10, font=('arial', 25, 'bold'),
                              bg='black',fg='red',command=self.shows)
        self.btnView.grid(row=0, column=2, pady=5, padx=5)
        self.btnup=Button(self.LoginFrame1, text="Update Staff Record", width=18, font=('arial', 25, 'bold'),
                              bg='black',fg='red',command=self.up).grid(row=0,column=3,pady=5,padx=5)

        self.btnBack = Button(self.frame, text="Back", width=10, font=('arial', 20, 'bold'), bg='black',
                              fg='red',command=self.iexit)
        self.btnBack.grid(row=25, column=0, pady=5, padx=5)
    def add(self):
        self.Add = Toplevel(self.s)
        self.app = DetailsStaff(self.Add)
    def delete(self):
        self.d = Toplevel(self.s)
        self.app = DeleteStaff(self.d)
    def shows(self):
        self.v = Toplevel(self.s)
        self.app = ViewStaff(self.v)
    def up(self):
        self.u = Toplevel(self.s)
        self.app = UpdateStaff(self.u)
    def iexit(self):
        self.s.destroy()
#========================DETAILS IN STAFF TABLE=========================================================================
class DetailsStaff:
    def __init__(self, master):
        self.f=master
        self.f.title("Staff Details")
        self.f.geometry("1400x1080")
        self.f.config(bg='Black')
        self.frame = Frame(self.f, width=50, height=50, bg='black')
        self.frame.pack()
        self.staffid = IntVar()
        self.stafffirstname = StringVar()
        self.stafflastname=StringVar()
        self.staffage=IntVar()
        self.staffgender=StringVar()
        self.staffdoj=StringVar()
        self.staffrank=StringVar()
        self.lb1Title = Label(self.frame, text="Enter Staff Details", font=('arial', 40, 'bold'), bg='black',fg='red')
        self.lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        self.ID = Label(self.frame, text="Staff ID", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.ID.grid(row=1, column=0)
        self.pid = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.staffid,width=33)
        self.pid.grid(row=1, column=1, padx=10)
        self.Firstname = Label(self.frame, text="First Name", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.Firstname.grid(row=2, column=0)
        self.Fname = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.stafffirstname,width=33)
        self.Fname.grid(row=2, column=1, padx=5)
        self.Lastname = Label(self.frame, text="Last Name", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.Lastname.grid(row=2, column=2)
        self.Lname = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.stafflastname,width=33)
        self.Lname.grid(row=2, column=3, padx=5)
        self.Ag = Label(self.frame, text="Age", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.Ag.grid(row=3, column=0)
        self.Age = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.staffage,width=33)
        self.Age.grid(row=3, column=1, padx=10)
        self.Hei = Label(self.frame, text="Gender", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.Hei.grid(row=4, column=0)
        self.Height = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.staffgender,width=33)
        self.Height.grid(row=4, column=1, padx=10)
        self.Cell = Label(self.frame, text="Date Of Joining", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.Cell.grid(row=5, column=0)
        self.Cellno = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.staffdoj,width=33)
        self.Cellno.grid(row=5, column=1, padx=10)
        self.Gend = Label(self.frame, text="Rank Of Staff", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.Gend.grid(row=6, column=0)
        self.Gender = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.staffrank,width=33)
        self.Gender.grid(row=6, column=1, padx=10)
        self.btnSubmit = Button(self.frame, text="Submit", width=10, font=('arial', 15, 'bold'), bg='black',fg='red',command=self.submit)
        self.btnSubmit.grid(row=8, column=0, pady=5, padx=5)
        self.btnClear = Button(self.frame, text="Reset", width=10, font=('arial', 15, 'bold'),bg='black',fg='red')
        self.btnClear.grid(row=8, column=2, pady=5, padx=5)
        self.btnBack = Button(self.frame, text="Exit", width=10, font=('arial', 15, 'bold'), bg='black',fg='red',command=self.Exit)
        self.btnBack.grid(row=8, column=3, pady=5, padx=5)
    def submit(self):
        self.conn = sqlite3.connect('Prison.db')
        self.c = self.conn.cursor()
        self.c.execute(
            "INSERT INTO Staff VALUES(:id, :First_name, :Last_name, :Age,  :Gender, :DOJ, :Rank)",
            {
                'id': self.staffid.get(),
                'First_name': self.stafffirstname.get(),
                'Last_name': self.stafflastname.get(),
                'Age': self.staffage.get(),
                'Gender': self.staffgender.get(),
                'DOJ': self.staffdoj.get(),
                'Rank': self.staffrank.get()
             })
        self.conn.commit()
        self.conn.close()
        self.staffid.set("")
        self.stafffirstname.set("")
        self.stafflastname.set("")
        self.staffage.set("")
        self.staffgender.set("")
        self.staffdoj.set("")
        self.staffrank.set("")
    def Exit(self):
        self.f.destroy()
#========================END OF DETAILS IN STAFF TABLE==================================================================
#========================DELETE IN STAFF TABLE =========================================================================
class DeleteStaff:
    def __init__(self, master):
        self.id = StringVar()
        self.d = master
        self.d.title("Staff Details")
        self.d.geometry("1400x1080")
        self.d.config(bg='Black')
        self.frame = Frame(self.d, width=50, height=50, bg='black')
        self.frame.pack()
        self.sid=StringVar()
        self.lb1Title = Label(self.frame, text="Delete Staff Record", font=('arial', 40, 'bold'), bg='black',fg='red')
        self.lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        self.ID = Label(self.frame, text="Enter Staff ID", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.ID.grid(row=1, column=0)
        self.pid = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.sid, width=33)
        self.pid.grid(row=1, column=1, padx=10)
        self.btndelete = Button(self.frame, text="Delete", width=10, font=('arial', 15, 'bold'),bg='black', fg='red', command=self.dell)
        self.btndelete.grid(row=2, column=0, pady=5, padx=5)
        self.btnBack = Button(self.frame, text="Exit", width=10, font=('arial', 15, 'bold'), bg='black',fg='red', command=self.Exit)
        self.btnBack.grid(row=2, column=3, pady=5, padx=5)
    def dell(self):
        self.him = self.sid.get()
        conn = sqlite3.connect("Prison.db")
        c = conn.cursor()
        c.execute("DELETE FROM Staff WHERE oid=" + self.him)
        conn.commit()
        conn.close()
    def Exit(self):
        self.d.destroy()
class ViewStaff:
    def __init__(self, master):
        self.id = StringVar()
        self.d = master
        self.d.title("View Staff Details")
        self.d.geometry("1400x1080")
        self.d.config(bg='Black')
        self.frame = Frame(self.d, width=50, height=50, bg='black')
        self.frame.pack()
        self.lb1Title = Label(self.frame, text="Staff Records", font=('arial', 40, 'bold'), bg='black',fg='red')
        self.lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        self.LoginFrame1 = LabelFrame(self.frame, width=50, height=50, font=('arial', 30, 'bold'),relief='ridge', bg='black', bd=0, fg='red')
        self.LoginFrame1.grid(row=1, column=0)
        self.lab1 = Label(self.LoginFrame1, text="ID", font=('arial', 20, 'bold'), bg='black', fg='red').grid(row=0,column=0)
        self.lab2 = Label(self.LoginFrame1, text="First Name", font=('arial', 20, 'bold'), bg='black', fg='red').grid(row=0, column=1)
        self.lab3 = Label(self.LoginFrame1, text="Last Name", font=('arial', 20, 'bold'), bg='black', fg='red').grid(row=0, column=2)
        self.lab4 = Label(self.LoginFrame1, text="Age", font=('arial', 20, 'bold'), bg='black', fg='red').grid(row=0,column=3)
        self.lab5 = Label(self.LoginFrame1, text="Gender", font=('arial', 20, 'bold'), bg='black', fg='red').grid(row=0,column=4)
        self.lab6 = Label(self.LoginFrame1, text="Date of Joining", font=('arial', 20, 'bold'), bg='black', fg='red').grid(row=0,column=5)
        self.lab7 = Label(self.LoginFrame1, text="Rank", font=('arial', 20, 'bold'), bg='black', fg='red').grid(row=0,column=6)
        row_no = 0;
        self.conn = sqlite3.connect('Prison.db')
        self.c = self.conn.cursor()
        values = self.c.execute("select * from Staff order by ID ")
        self.records = self.c.fetchall()
        for self.record in self.records:
            id_no = self.record[0]
            f_name = self.record[1]
            l_name = self.record[2]
            age = self.record[3]
            gend_er = self.record[4]
            doj = self.record[5]
            rank = self.record[6]
            row_no = row_no + 1
            self.Label = Label(self.LoginFrame1, text=id_no, width=7, font=('times', 17, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=0, padx=(0, 2))
            self.Labe2 = Label(self.LoginFrame1, text=f_name, width=15, font=('times', 17, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=1, padx=(0, 2))
            self.Labe3 = Label(self.LoginFrame1, text=l_name, width=15, font=('times', 17, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=2, padx=(0, 2))
            self.Labe4 = Label(self.LoginFrame1, text=age, width=7, font=('times', 17, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=3, padx=(0, 2))
            self.Labe5 = Label(self.LoginFrame1, text=gend_er, width=9, font=('times', 17, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=4, padx=(0, 2))
            self.Labe6 = Label(self.LoginFrame1, text=doj, width=13, font=('times', 17, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=5, padx=(0, 2))
            self.Labe7 = Label(self.LoginFrame1, text=rank, width=19, font=('times', 17, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=6, padx=(0, 2))
        row_no = row_no + 6
        self.btnBack = Button(self.frame, text="Exit", width=10, font=('arial', 15, 'bold'), bg='black',fg='red', command=self.iexit)
        self.btnBack.grid(row=row_no, column=0, pady=5, padx=5)
        self.conn.commit()
        self.conn.close()
    def iexit(self):
        self.d.destroy()

class UpdateStaff:
    def __init__(self, master):
        self.u = master
        self.u.title("Staff Update")
        self.u.geometry("1400x1080")
        self.u.config(bg='Black')
        frame = Frame(self.u, width=50, height=50, bg='black')
        frame.pack()
        global SFname
        global SLname
        global SAge
        global Sgender
        global SDOJ
        global SRank
        global sid
        self.Sid = StringVar()
        lb1Title = Label(frame, text="Update Prisoner Record", font=('arial', 40, 'bold'), bg='black',fg='red')
        lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        uid = Label(frame, text="Enter Staff ID", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        uid.grid(row=1, column=0)
        sid = Entry(frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.Sid, width=33)
        sid.grid(row=1, column=1, padx=10)
        update = Button(frame, text="Update", width=10, font=('arial', 15, 'bold'),bg='black', fg='red', command=self.up)
        update.grid(row=2, column=3, pady=5, padx=5)
        Firstname = Label(frame, text="First Name", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Firstname.grid(row=3, column=0)
        SFname = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        SFname.grid(row=3, column=1, padx=5)
        Lastname = Label(frame, text="Last Name", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Lastname.grid(row=3, column=2)
        SLname = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        SLname.grid(row=3, column=3, padx=5)
        Ag = Label(frame, text="Age", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Ag.grid(row=4, column=0)
        SAge = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        SAge.grid(row=4, column=1, padx=10)
        Hei = Label(frame, text="Gender", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Hei.grid(row=4, column=2)
        Sgender = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        Sgender.grid(row=4, column=3, padx=10)
        Cell = Label(frame, text="Date of Joining", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Cell.grid(row=5, column=0)
        SDOJ = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        SDOJ.grid(row=5, column=1, padx=10)
        Gend = Label(frame, text="Rank", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Gend.grid(row=5, column=2)
        SRank = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        SRank.grid(row=5, column=3, padx=10)
        btnSubmit = Button(frame, text="Save Record", width=10, font=('arial', 15, 'bold'), bg='black', fg='red', command=self.usub)
        btnSubmit.grid(row=7, column=0, pady=5, padx=5)
        self.btnBack = Button(frame, text="Exit", width=10, font=('arial', 15, 'bold'), bg='black',fg='red', command=self.Exit)
        self.btnBack.grid(row=7, column=2, pady=5, padx=5)
    def up(self):
        conn = sqlite3.connect("Prison.db")
        c = conn.cursor()
        self.record_id = self.Sid.get()
        c.execute("SELECT * FROM Staff WHERE ID=?", (self.record_id,))
        records = c.fetchall()
        for record in records:
            SFname.insert(0, record[1])
            SLname.insert(0, record[2])
            SAge.insert(0, record[3])
            Sgender.insert(0, record[4])
            SDOJ.insert(0, record[5])
            SRank.insert(0, record[6])
    def usub(self):
        conn = sqlite3.connect("Prison.db")
        c = conn.cursor()
        c.execute(
            "UPDATE Staff SET  FirstName= :first, LastName= :last, Age= :ag,Gender= :gend,  DOJ= :doj, Rank= :rank  WHERE ID= :id",
            {
                'id': self.Sid.get(),
                'first': SFname.get(),
                'last': SLname.get(),
                'ag': SAge.get(),
                'gend': Sgender.get(),
                'doj': SDOJ.get(),
                'rank': SRank.get()
            })
        conn.commit()
        conn.close()

    def Exit(self):
        self.u.destroy()

#========================END OF DELETE IN STAFF TABLE===================================================================
#===========================REMAND CASE TABLE===========================================================================
class PrisonRemand:
    def __init__(self, master):
        self.r=master
        self.r.title("Prisoner Remand Cases")
        self.r.geometry("1400x1080")
        self.r.config(bg='Black')
        self.frame = Frame(self.r, width=50, height=50, bg='black')
        self.frame.pack()
        self.lb1Title = Label(self.frame, text="Remand Cases", font=('arial', 50, 'bold'), bg='black',fg='red')
        self.lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        self.photo2 = PhotoImage(file='Remand.png')
        self.photo = Label(self.frame, image=self.photo2, bg='white').grid(row=1, column=0)
        self.LoginFrame1 = LabelFrame(self.frame, width=50, height=50, font=('arial', 20, 'bold'),relief='ridge', bg='black', bd=0, fg='red')
        self.LoginFrame1.grid(row=2, column=0)
        self.btnAdd = Button(self.LoginFrame1, text="Add Remand Case", width=17, font=('arial', 20, 'bold'),bg='Black',fg='red',command=self.Addr)
        self.btnAdd.grid(row=0, column=0, pady=5, padx=5)
        self.btnDelete = Button(self.LoginFrame1, text="Remove Remand Case", width=19, font=('arial', 20, 'bold'),bg='black',fg='red',command=self.delete)
        self.btnDelete.grid(row=0, column=1, pady=5, padx=5)
        self.btnView = Button(self.LoginFrame1, text="View Remand Cases", width=19, font=('arial', 20, 'bold'),bg='black',fg='red',command=self.rview)
        self.btnView.grid(row=0, column=2, pady=5, padx=5)
        self.btnUP = Button(self.LoginFrame1, text="Update Remand Cases", width=20, font=('arial', 20, 'bold'),bg='black',fg='red', command=self.ru)
        self.btnUP.grid(row=0, column=3, pady=5, padx=5)
        self.btnBack = Button(self.frame, text="Back", width=10, font=('arial', 25, 'bold'), bg='black',fg='red',command=self.iexit)
        self.btnBack.grid(row=25, column=0, pady=5, padx=5)
    def Addr(self):
        self.Add = Toplevel(self.r)
        self.app = DetailsR(self.Add)
    def delete(self):
        self.d = Toplevel(self.r)
        self.app = DeleteRem(self.d)
    def ru(self):
        self.Ru=Toplevel(self.r)
        self.app=UpdateRem(self.Ru)
    def rview(self):
        self.rv = Toplevel(self.r)
        self.app = ViewRem(self.rv)
    def iexit(self):
        self.r.destroy()
#========================DETAILS IN REMAND CASE TABLE===================================================================
class  DetailsR:
    def __init__(self, master):
        self.f = master
        self.f.title("RemandCase Details")
        self.f.geometry("1400x1080")
        self.f.config(bg='Black')
        self.frame = Frame(self.f, width=50, height=50, bg='black')
        self.frame.pack()
        self.rid = IntVar()
        self.rfirstname = StringVar()
        self.rlastname = StringVar()
        self.rage = StringVar()
        self.rgender = StringVar()
        self.rcellno = IntVar()
        self.rheight = StringVar()
        self.rduration = StringVar()
        self.ronremand=StringVar()
        self.rnext=StringVar()
        self.rcasetype=StringVar()
        self.lb1Title = Label(self.frame, text="Enter Remand Cases Details", font=('arial', 40, 'bold'), bg='black',fg='red')
        self.lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        self.ID = Label(self.frame, text="Prisoner ID", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.ID.grid(row=1, column=0)
        self.pid = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.rid,width=33)
        self.pid.grid(row=1, column=1, padx=10)
        self.Firstname = Label(self.frame, text="First Name", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.Firstname.grid(row=2, column=0)
        self.Fname = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.rfirstname,width=33)
        self.Fname.grid(row=2, column=1, padx=5)
        self.Lastname = Label(self.frame, text="Last Name", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.Lastname.grid(row=2, column=2)
        self.Lname = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.rlastname,width=33)
        self.Lname.grid(row=2, column=3, padx=5)
        self.Ag = Label(self.frame, text="Age", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.Ag.grid(row=3, column=0)
        self.Age = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.rage,width=33)
        self.Age.grid(row=3, column=1, padx=10)
        self.Hei = Label(self.frame, text="Height", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.Hei.grid(row=3, column=2)
        self.Height = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.rheight,width=33)
        self.Height.grid(row=3, column=3, padx=10)
        self.Cell = Label(self.frame, text="Cell Number", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.Cell.grid(row=4, column=0)
        self.Cellno = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.rcellno,width=33)
        self.Cellno.grid(row=4, column=1, padx=10)
        self.Gend = Label(self.frame, text="Gender", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.Gend.grid(row=5, column=0)
        self.Gender = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.rgender,width=33)
        self.Gender.grid(row=5, column=1, padx=10)
        self.D = Label(self.frame, text="Duration", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.D.grid(row=5, column=2)
        self.Duration = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.rduration,width=33)
        self.Duration.grid(row=5, column=3, padx=10)
        self.ON = Label(self.frame, text="On Remand Until", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.ON.grid(row=6, column=0)
        self.Onr = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.ronremand,width=33)
        self.Onr.grid(row=6, column=1, padx=10)
        self.next = Label(self.frame, text="Next Hearing", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.next.grid(row=6, column=2)
        self.Nexth = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.rnext, width=33)
        self.Nexth.grid(row=6, column=3, padx=10)
        self.C = Label(self.frame, text="Case Type", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.C.grid(row=7, column=0)
        self.caset = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.rcasetype,width=33)
        self.caset.grid(row=7, column=1, padx=10)
        self.btnSubmit = Button(self.frame, text="Submit", width=10, font=('arial', 15, 'bold'),bg='black', fg='red',command=self.submit)
        self.btnSubmit.grid(row=8, column=0, pady=5, padx=5)
        self.btnClear = Button(self.frame, text="Reset", width=10, font=('arial', 15, 'bold'),bg='black',fg='red')
        self.btnClear.grid(row=8, column=2, pady=5, padx=5)
        self.btnBack = Button(self.frame, text="Exit", width=10, font=('arial', 15, 'bold'), bg='black',fg='red', command=self.Exit)
        self.btnBack.grid(row=8, column=3, pady=5, padx=5)
    def Exit(self):
        self.f.destroy()
    def submit(self):
        self.conn = sqlite3.connect('Prison.db')
        self.c = self.conn.cursor()
        self.c.execute("INSERT INTO RemandCase VALUES(:id, :First_name, :Last_name, :Age,  :Height, :Cellno, :Gender, :Duration, :Onremand, :NextHearing, :CaseType)",
         {
                'id': self.rid.get(),
                'First_name': self.rfirstname.get(),
                'Last_name': self.rlastname.get(),

                'Age': self.rage.get(),
                'Height': self.rheight.get(),
                'Cellno': self.rcellno.get(),
                'Gender': self.rgender.get(),
                'Duration': self.rduration.get(),
                'Onremand': self.ronremand.get(),
                'NextHearing':self.rnext.get(),
                'CaseType':self.rcasetype.get()

             })

        self.conn.commit()
        self.conn.close()
        self.rid.set("")
        self.rfirstname.set("")
        self.rlastname.set("")
        self.rage.set("")
        self.rheight.set("")
        self.rcellno.set("")
        self.rgender.set("")
        self.rduration.set("")
        self.ronremand.set("")
        self.rnext.set("")
        self.rcasetype.set("")
#========================END OF DETAILS IN REMAND CASE==================================================================
#========================DELETE IN REMAND CASE==========================================================================
class DeleteRem:
    def __init__(self, master):
        self.id = StringVar()
        self.d = master
        self.d.title("Staff Details")
        self.d.geometry("1400x1080")
        self.d.config(bg='Black')
        self.frame = Frame(self.d, width=50, height=50, bg='black')
        self.frame.pack()
        self.rid=StringVar()
        self.lb1Title = Label(self.frame, text="Delete RemandCase Record", font=('arial', 40, 'bold'), bg='black',fg='red')
        self.lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        self.ID = Label(self.frame, text="Enter Prisoner ID", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.ID.grid(row=1, column=0)
        self.pid = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.rid, width=33)
        self.pid.grid(row=1, column=1, padx=10)
        self.btndelete = Button(self.frame, text="Delete", width=10, font=('arial', 15, 'bold'),bg='black', fg='red', command=self.dell)
        self.btndelete.grid(row=2, column=0, pady=5, padx=5)
        self.btnBack = Button(self.frame, text="Exit", width=10, font=('arial', 15, 'bold'), bg='black',fg='red', command=self.Exit)
        self.btnBack.grid(row=2, column=3, pady=5, padx=5)

    def dell(self):
        self.him = self.rid.get()
        conn = sqlite3.connect("Prison.db")
        c = conn.cursor()
        c.execute("DELETE FROM RemandCase WHERE oid=" + self.him)
        conn.commit()
        c.execute('DELETE FROM Prisoner WHERE oid=' + self.him)
        conn.commit()
        conn.close()
    def Exit(self):
        self.d.destroy()
class ViewRem:
    def __init__(self, master):
        self.d=master
        self.d.title("Show Records")
        self.d.geometry("1400x1080")
        self.d.config(bg='Black')
        self.frame = Frame(self.d, width=50, height=50, bg='black')
        self.frame.pack()
        self.lb1Title = Label(self.frame, text="Remand Case Records", font=('arial', 40, 'bold'), bg='black',fg='red')
        self.lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        self.LoginFrame1 = LabelFrame(self.frame, width=50, height=50, font=('arial', 30, 'bold'),relief='ridge', bg='black', bd=0, fg='red')
        self.LoginFrame1.grid(row=1, column=0)
        self.lab1=Label(self.LoginFrame1,text="ID",font=('arial',15, 'bold'),bg='black',fg='red').grid(row=0,column=0)
        self.lab2 = Label(self.LoginFrame1, text="First Name", font=('arial', 15, 'bold'), bg='black', fg='red').grid(row=0,column=1)
        self.lab3 = Label(self.LoginFrame1, text="Last Name", font=('arial', 15, 'bold'), bg='black', fg='red').grid(row=0,column=2)
        self.lab4 = Label(self.LoginFrame1, text="Age", font=('arial', 15, 'bold'), bg='black', fg='red').grid(row=0,column=3)
        self.lab5 = Label(self.LoginFrame1, text="Height", font=('arial', 15, 'bold'), bg='black', fg='red').grid(row=0,column=4)
        self.lab6 = Label(self.LoginFrame1, text="Cellno", font=('arial', 15, 'bold'), bg='black', fg='red').grid(row=0,column=5)
        self.lab7 = Label(self.LoginFrame1, text="Gender", font=('arial', 15, 'bold'), bg='black', fg='red').grid(row=0,column=6)
        self.lab8 = Label(self.LoginFrame1, text="Duration", font=('arial',15, 'bold'), bg='black', fg='red').grid(row=0,column=7)
        self.lab9 = Label(self.LoginFrame1, text="Onremand", font=('arial', 15, 'bold'), bg='black', fg='red').grid(row=0,column=8)
        self.lab10 = Label(self.LoginFrame1, text="Next Hearing", font=('arial', 15, 'bold'), bg='black', fg='red').grid(row=0,column=9)
        self.lab11 = Label(self.LoginFrame1, text="Case Type", font=('arial', 15, 'bold'), bg='black', fg='red').grid(row=0,column=10)
        row_no=0;
        self.conn = sqlite3.connect('Prison.db')
        self.c = self.conn.cursor()
        values=self.c.execute("select * from RemandCase order by ID ")
        self.records=self.c.fetchall()
        for self.record in self.records:
            id_no=self.record[0]
            f_name=self.record[1]
            l_name=self.record[2]
            age=self.record[3]
            hei_ght=self.record[4]
            cell_num=self.record[5]
            gend_er=self.record[6]
            dur_ation=self.record[7]
            on_r=self.record[8]
            next_h=self.record[9]
            c_type=self.record[10]
            row_no=row_no+1
            self.Label=Label(self.LoginFrame1, text=id_no, width=7, font=('times', 17, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=0, padx=(0, 2))
            self.Labe2 = Label(self.LoginFrame1, text=f_name, width=11, font=('times', 17, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=1, padx=(0, 2))
            self.Labe3 = Label(self.LoginFrame1, text=l_name, width=11, font=('times', 17, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=2, padx=(0, 2))
            self.Labe4 = Label(self.LoginFrame1, text=age, width=7, font=('times', 17, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=3, padx=(0, 2))
            self.Labe5 = Label(self.LoginFrame1, text=hei_ght, width=9, font=('times', 17, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=4, padx=(0, 2))
            self.Labe6 = Label(self.LoginFrame1, text=cell_num, width=5, font=('times', 17, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=5, padx=(0, 2))
            self.Labe7 = Label(self.LoginFrame1, text=gend_er, width=8, font=('times', 17, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=6, padx=(0, 2))
            self.Labe8 = Label(self.LoginFrame1, text=dur_ation, width=9, font=('times', 17, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=7, padx=(0, 2))
            self.Labe9 = Label(self.LoginFrame1, text=on_r, width=9, font=('times', 17, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=8, padx=(0, 2))
            self.Labe10 = Label(self.LoginFrame1, text=next_h, width=9, font=('times', 17, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=9, padx=(0, 2))
            self.Labe11 = Label(self.LoginFrame1, text=c_type, width=11, font=('times', 17, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=10, padx=(0, 2))
        row_no=row_no+6
        self.btnBack = Button(self.frame, text="Exit", width=10, font=('arial', 15, 'bold'), bg='black',fg='red', command=self.iexit)
        self.btnBack.grid(row=row_no, column=0, pady=5, padx=5)
        self.conn.commit()
        self.conn.close()

    def iexit(self):
        self.d.destroy()
class UpdateRem:
    def __init__(self, master):
        self.u=master
        self.u.title("Prisoner Details")
        self.u.geometry("1400x1080")
        self.u.config(bg='Black')
        frame = Frame(self.u, width=50, height=50, bg='black')
        frame.pack()
        global Rid
        global RFname
        global RLname
        global RAge
        global RHeight
        global RCellno
        global RGender
        global RDuration
        global ROnr
        global RNH
        global RCT
        global upid
        self.RID=StringVar()
        lb1Title = Label(frame, text="Update Remand Cases Record", font=('arial', 40, 'bold'), bg='black',fg='red')
        lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        uid = Label(frame, text="Enter Prisoner ID", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        uid.grid(row=1, column=0)
        upid = Entry(frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.RID, width=33)
        upid.grid(row=1, column=1, padx=10)
        update = Button(frame, text="Update", width=10, font=('arial', 15, 'bold'),bg='black', fg='red', command=self.UP)
        update.grid(row=2, column=3, pady=5, padx=5)
        Firstname = Label(frame, text="First Name", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Firstname.grid(row=3, column=0)
        RFname = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        RFname.grid(row=3, column=1, padx=5)
        Lastname = Label(frame, text="Last Name", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Lastname.grid(row=3, column=2)
        RLname = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        RLname.grid(row=3, column=3, padx=5)
        Ag = Label(frame, text="Age", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Ag.grid(row=4, column=0)
        RAge = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        RAge.grid(row=4, column=1, padx=10)
        Hei = Label(frame, text="Height", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Hei.grid(row=4, column=2)
        RHeight = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        RHeight.grid(row=4, column=3, padx=10)
        Cell = Label(frame, text="Cell Number", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Cell.grid(row=5, column=0)
        RCellno = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        RCellno.grid(row=5, column=1, padx=10)
        Gend = Label(frame, text="Gender", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Gend.grid(row=5, column=2)
        RGender = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        RGender.grid(row=5, column=3, padx=10)
        Dura = Label(frame, text="Duration", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red').grid(row=6,column=0)
        RDuration = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        RDuration.grid(row=6, column=1, padx=10)
        onr = Label(frame, text="On Remand", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        onr.grid(row=7, column=0)
        ROnr = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        ROnr.grid(row=7, column=1, padx=10)
        NextH = Label(frame, text="Next Hearing", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        NextH.grid(row=7, column=2)
        RNH = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        RNH.grid(row=7, column=3, padx=10)
        CaseT= Label(frame, text="Case Type", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        CaseT.grid(row=8, column=0)
        RCT= Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        RCT.grid(row=8, column=1, padx=10)
        btnSubmit = Button(frame, text="Save Record", width=10, font=('arial', 15, 'bold'),bg='black', fg='red', command=self.Usub)
        btnSubmit.grid(row=9, column=0, pady=5, padx=5)
        btnex=Button(frame, text="Exit", width=10, font=('arial', 15, 'bold'),bg='black', fg='red', command=self.Uex).grid(row=9,column=2,pady=5,padx=5)
    def UP(self):
        conn = sqlite3.connect("Prison.db")
        c = conn.cursor()
        self.record_id=self.RID.get()
        c.execute("SELECT * FROM RemandCase WHERE ID=?",(self.record_id,))
        records=c.fetchall()
        for record in records:
            RFname.insert(0, record[1])
            RLname.insert(0, record[2])
            RAge.insert(0, record[3])
            RHeight.insert(0, record[4])
            RCellno.insert(0, record[5])
            RGender.insert(0, record[6])
            RDuration.insert(0, record[7])
            ROnr.insert(0, record[8])
            RNH.insert(0, record[9])
            RCT.insert(0, record[10])
    def Usub(self):
        conn = sqlite3.connect("Prison.db")
        c = conn.cursor()
        c.execute("UPDATE RemandCase SET  FirstName= :first, LastName= :last, Age= :ag, Height= :hei, Cellno= :cell, Gender= :gend, Duration= :dura,Onremand= :onr,NextHearing= :next,CaseType= :caset  WHERE ID= :id",
                  {
                      'id':self.RID.get(),
                      'first':  RFname.get(),
                      'last': RLname.get(),
                      'ag': RAge.get(),
                      'hei':RHeight.get(),
                      'cell':RCellno.get(),
                      'gend':RGender.get(),
                      'dura':RDuration.get(),
                      'onr': ROnr.get(),
                      'next': RNH.get(),
                      'caset':RCT.get()
                  })
        conn.commit()
        conn.close()
    def Uex(self):
        self.u.destroy()

#========================END OF DELETE IN REMAND CASE===================================================================
#========================PRISONER EDUCATION TABLE=======================================================================
class PrisonEdu:
    def __init__(self, master):
        self.e = master
        self.e.title("Prisoners Education")
        self.e.geometry("1400x1080")
        self.e.config(bg='Black')
        self.frame = Frame(self.e, width=50, height=50, bg='black')
        self.frame.pack()

        self.lb1Title = Label(self.frame, text="Prisoners Education", font=('arial', 50, 'bold'), bg='black',
                          fg='red')
        self.lb1Title.grid(row=0, column=0, columnspan=2, pady=20)

        self.photo2 = PhotoImage(file='Prisoner-education.png')
        self.photo = Label(self.frame, image=self.photo2, bg='white').grid(row=1, column=0)
        self.LoginFrame1 = LabelFrame(self.frame, width=50, height=50, font=('arial', 20, 'bold'),
                                  relief='ridge', bg='black', bd=0, fg='red')
        self.LoginFrame1.grid(row=2, column=0)

        self.btnAdd = Button(self.LoginFrame1, text="Add Education", width=12, font=('arial', 20, 'bold'), bg='Black',
                         fg='red',command=self.Edu)
        self.btnAdd.grid(row=0, column=0, pady=5, padx=5)
        self.btnDelete = Button(self.LoginFrame1, text="Remove Education Details", width=20, font=('arial', 20, 'bold'),
                            bg='black',fg='red',command=self.delete)
        self.btnDelete.grid(row=0, column=1, pady=5, padx=5)
        self.btnView = Button(self.LoginFrame1, text="View Education Details", width=19, font=('arial', 20, 'bold'),
                          bg='black',fg='red',command=self.eshow)
        self.btnView.grid(row=0, column=2, pady=5, padx=5)
        self.btnu=Button(self.LoginFrame1, text="Update Education Details", width=19, font=('arial', 20, 'bold'),
                          bg='black',fg='red',command=self.uedu).grid(row=0,column=3,pady=5,padx=5)
        self.btnBack = Button(self.frame, text="Back", width=10, font=('arial', 20, 'bold'), bg='black',
                          fg='red',command=self.iexit)
        self.btnBack.grid(row=25, column=0, pady=5, padx=5)
    def Edu(self):
        self.edu = Toplevel(self.e)
        self.app = DetailsE(self.edu)
    def delete(self):
        self.d = Toplevel(self.e)
        self.app = DeleteEdu(self.d)
    def eshow(self):
        self.Eshow = Toplevel(self.e)
        self.app = ViewEdu(self.Eshow)
    def uedu(self):
        self.Uedu = Toplevel(self.e)
        self.app = UpdateEdu(self.Uedu)
    def iexit(self):
        self.e.destroy()
#========================DETAILS IN PRISONER EDUCATION==================================================================
class DetailsE:
    def __init__(self, master):
        self.e = master
        self.e.title("Prisoners Education")
        self.e.geometry("1400x1080")
        self.e.config(bg='Black')
        self.frame = Frame(self.e, width=50, height=50, bg='black')
        self.frame.pack()
        self.cid = IntVar()
        self.cfirstname = StringVar()
        self.clastname = StringVar()
        self.courid = IntVar()
        self.cname = StringVar()
        self.cduration = StringVar()
        self.intime = StringVar()
        self.outime = StringVar()
        self.lb1Title = Label(self.frame, text="Enter Prisoners Education", font=('arial', 50, 'bold'), bg='black',fg='red')
        self.lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        self.ID = Label(self.frame, text="Prisoner ID", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.ID.grid(row=1, column=0)
        self.pid = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.cid,width=33)
        self.pid.grid(row=1, column=1, padx=10)
        self.Firstname = Label(self.frame, text="First Name", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.Firstname.grid(row=2, column=0)
        self.Fname = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.cfirstname,width=33)
        self.Fname.grid(row=2, column=1, padx=5)
        self.Lastname = Label(self.frame, text="Last Name", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.Lastname.grid(row=2, column=2)
        self.Lname = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.clastname,width=33)
        self.Lname.grid(row=2, column=3, padx=5)
        self.Ag = Label(self.frame, text="Course ID", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.Ag.grid(row=3, column=0)
        self.Age = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.courid,width=33)
        self.Age.grid(row=3, column=1, padx=10)
        self.Hei = Label(self.frame, text="Course Name", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.Hei.grid(row=3, column=2)
        self.Height = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.cname,width=33)
        self.Height.grid(row=3, column=3, padx=10)
        self.Cell = Label(self.frame, text="Course Duration", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.Cell.grid(row=4, column=0)
        self.Cellno = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.cduration,width=33)
        self.Cellno.grid(row=4, column=1, padx=10)
        self.Gend = Label(self.frame, text="In Time", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.Gend.grid(row=5, column=0)
        self.Gender = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.intime,width=33)
        self.Gender.grid(row=5, column=1, padx=10)
        self.D = Label(self.frame, text="Out Time", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.D.grid(row=5, column=2)
        self.Duration = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.outime,width=33)
        self.Duration.grid(row=5, column=3, padx=10)
        self.btnSubmit = Button(self.frame, text="Submit", width=10, font=('arial', 15, 'bold'),bg='black', fg='red', command=self.submit)
        self.btnSubmit.grid(row=6, column=0, pady=5, padx=5)
        self.btnClear = Button(self.frame, text="Reset", width=10, font=('arial', 15, 'bold'),bg='black',fg='red')
        self.btnClear.grid(row=6, column=2, pady=5, padx=5)
        self.btnBack = Button(self.frame, text="Exit", width=10, font=('arial', 15, 'bold'), bg='black',fg='red', command=self.Exit)
        self.btnBack.grid(row=6, column=3, pady=5, padx=5)
    def submit(self):
        self.conn = sqlite3.connect('Prison.db')
        self.c = self.conn.cursor()
        self.c.execute(
            "INSERT INTO Education VALUES(:id, :First_name, :Last_name, :CourseID,  :CourseName, :CourseD, :Intime, :Outime)",
            {
                'id': self.cid.get(),
                'First_name': self.cfirstname.get(),
                'Last_name': self.clastname.get(),
                'CourseID': self.courid.get(),
                'CourseName': self.cname.get(),
                'CourseD': self.cduration.get(),
                'Intime': self.intime.get(),
                'Outime':self.outime.get()
            })
        self.conn.commit()
        self.conn.close()
        self.cid.set("")
        self.cfirstname.set("")
        self.clastname.set("")
        self.courid.set("")
        self.cname.set("")
        self.cduration.set("")
        self.intime.set("")
        self.outime.set("")
    def Exit(self):
        self.e.destroy()

#========================END OF DETAILS IN PRISONER EDUCATION ==========================================================
#========================DELETE IN PRISONER EDUCATION===================================================================
class DeleteEdu:
    def __init__(self, master):
        self.id = StringVar()
        self.d = master
        self.d.title("Education Details")
        self.d.geometry("1400x1080")
        self.d.config(bg='Black')
        self.frame = Frame(self.d, width=50, height=50, bg='black')
        self.frame.pack()
        self.eid=StringVar()
        self.lb1Title = Label(self.frame, text="Delete Education Record", font=('arial', 40, 'bold'), bg='black',fg='red')
        self.lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        self.ID = Label(self.frame, text="Enter Prisoner ID", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.ID.grid(row=1, column=0)
        self.pid = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.eid, width=33)
        self.pid.grid(row=1, column=1, padx=10)
        self.btndelete = Button(self.frame, text="Delete", width=10, font=('arial', 15, 'bold'),bg='black', fg='red', command=self.dell)
        self.btndelete.grid(row=2, column=0, pady=5, padx=5)
        self.btnBack = Button(self.frame, text="Exit", width=10, font=('arial', 15, 'bold'), bg='black',fg='red', command=self.Exit)
        self.btnBack.grid(row=2, column=3, pady=5, padx=5)
    def dell(self):
        self.him = self.eid.get()
        conn = sqlite3.connect("Prison.db")
        c = conn.cursor()
        c.execute("DELETE FROM Education WHERE oid=" + self.him)
        conn.commit()
        conn.close()
    def Exit(self):
        self.d.destroy()
class ViewEdu:
    def __init__(self, master):
        self.e = master
        self.e.title("Prisoners Education")
        self.e.geometry("1400x1080")
        self.e.config(bg='Black')
        self.frame = Frame(self.e, width=50, height=50, bg='black')
        self.frame.pack()
        self.lb1Title = Label(self.frame, text="Education Records", font=('arial', 40, 'bold'), bg='black',fg='red')
        self.lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        self.LoginFrame1 = LabelFrame(self.frame, width=50, height=50, font=('arial', 30, 'bold'),relief='ridge', bg='black', bd=0, fg='red')
        self.LoginFrame1.grid(row=1, column=0)
        self.lab1 = Label(self.LoginFrame1, text="ID", font=('arial', 25, 'bold'), bg='black', fg='red').grid(row=0,column=0)
        self.lab2 = Label(self.LoginFrame1, text="First Name", font=('arial', 25, 'bold'), bg='black', fg='red').grid(row=0, column=1)
        self.lab3 = Label(self.LoginFrame1, text="Last Name", font=('arial', 25, 'bold'), bg='black', fg='red').grid(row=0, column=2)
        self.lab4 = Label(self.LoginFrame1, text="CID", font=('arial', 25, 'bold'), bg='black', fg='red').grid(row=0,column=3)
        self.lab5 = Label(self.LoginFrame1, text="CName", font=('arial', 25, 'bold'), bg='black', fg='red').grid(row=0,column=4)
        self.lab6 = Label(self.LoginFrame1, text="C Duration", font=('arial', 25, 'bold'), bg='black',fg='red').grid(row=0,column=5)
        self.lab7 = Label(self.LoginFrame1, text="Intime", font=('arial', 25, 'bold'), bg='black', fg='red').grid(row=0,column=6)
        self.lab8 = Label(self.LoginFrame1, text="Outime", font=('arial', 25, 'bold'), bg='black', fg='red').grid(row=0,column=7)
        row_no = 0;
        self.conn = sqlite3.connect('Prison.db')
        self.c = self.conn.cursor()
        values = self.c.execute("select * from Education order by ID ")
        self.records = self.c.fetchall()
        for self.record in self.records:
            id_no = self.record[0]
            f_name = self.record[1]
            l_name = self.record[2]
            c_id = self.record[3]
            C_name = self.record[4]
            C_duration = self.record[5]
            in_time = self.record[6]
            out_time=self.record[7]
            row_no = row_no + 1
            self.Label = Label(self.LoginFrame1, text=id_no, width=7, font=('times', 20, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=0, padx=(0, 2))
            self.Labe2 = Label(self.LoginFrame1, text=f_name, width=13, font=('times', 20, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=1, padx=(0, 2))
            self.Labe3 = Label(self.LoginFrame1, text=l_name, width=13, font=('times', 20, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=2, padx=(0, 2))
            self.Labe4 = Label(self.LoginFrame1, text=c_id, width=7, font=('times', 20, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=3, padx=(0, 2))
            self.Labe5 = Label(self.LoginFrame1, text=C_name, width=11, font=('times', 20, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=4, padx=(0, 2))
            self.Labe6 = Label(self.LoginFrame1, text=C_duration, width=10, font=('times', 20, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=5, padx=(0, 2))
            self.Labe7 = Label(self.LoginFrame1, text=in_time, width=10, font=('times', 20, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=6, padx=(0, 2))
            self.Labe8 = Label(self.LoginFrame1, text=out_time, width=10, font=('times', 20, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=7, padx=(0, 2))
        row_no = row_no + 6
        self.btnBack = Button(self.frame, text="Exit", width=10, font=('arial', 15, 'bold'), bg='black',fg='red', command=self.iexit)
        self.btnBack.grid(row=row_no, column=0, pady=5, padx=5)
        self.conn.commit()
        self.conn.close()

    def iexit(self):
        self.e.destroy()
class UpdateEdu:
    def __init__(self, master):
        self.u=master
        self.u.title("Prisoner Details")
        self.u.geometry("1400x1080")
        self.u.config(bg='Black')
        frame = Frame(self.u, width=50, height=50, bg='black')
        frame.pack()
        global Eid
        global EFname
        global ELname
        global ECID
        global ECN
        global ECD
        global EIN
        global EOUT
        self.EID=StringVar()
        lb1Title = Label(frame, text="Update Education Record", font=('arial', 40, 'bold'), bg='black',fg='red')
        lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        uid = Label(frame, text="Enter Prisoner ID", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        uid.grid(row=1, column=0)
        upid = Entry(frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.EID, width=33)
        upid.grid(row=1, column=1, padx=10)
        update = Button(frame, text="Update", width=10, font=('arial', 15, 'bold'),bg='black', fg='red', command=self.UP)
        update.grid(row=2, column=3, pady=5, padx=5)
        Firstname = Label(frame, text="First Name", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Firstname.grid(row=3, column=0)
        EFname = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        EFname.grid(row=3, column=1, padx=5)
        Lastname = Label(frame, text="Last Name", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Lastname.grid(row=3, column=2)
        ELname = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        ELname.grid(row=3, column=3, padx=5)
        Ag = Label(frame, text="Course ID", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Ag.grid(row=4, column=0)
        ECID = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        ECID.grid(row=4, column=1, padx=10)
        Hei = Label(frame, text="Course Name", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Hei.grid(row=4, column=2)
        ECN = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        ECN.grid(row=4, column=3, padx=10)
        Cell = Label(frame, text="Course Duration", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Cell.grid(row=5, column=0)
        ECD = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        ECD.grid(row=5, column=1, padx=10)
        Gend = Label(frame, text="In Time", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Gend.grid(row=5, column=2)
        EIN= Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        EIN.grid(row=5, column=3, padx=10)
        Dura = Label(frame, text="Out Time", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red').grid(row=6,column=0)
        EOUT = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        EOUT.grid(row=6, column=1, padx=10)
        btnSubmit = Button(frame, text="Save Record", width=10, font=('arial', 15, 'bold'),bg='black', fg='red', command=self.Usub)
        btnSubmit.grid(row=7, column=0, pady=5, padx=5)
        btnex=Button(frame, text="Exit", width=10, font=('arial', 15, 'bold'),bg='black', fg='red', command=self.Uex).grid(row=9,column=2,pady=5,padx=5)
    def UP(self):
        conn = sqlite3.connect("Prison.db")
        c = conn.cursor()
        self.record_id=self.EID.get()
        c.execute("SELECT * FROM Education WHERE ID=?",(self.record_id,))
        records=c.fetchall()
        for record in records:
            EFname.insert(0, record[1])
            ELname.insert(0, record[2])
            ECID.insert(0, record[3])
            ECN.insert(0, record[4])
            ECD.insert(0, record[5])
            EIN.insert(0, record[6])
            EOUT.insert(0, record[7])
    def Usub(self):
        conn = sqlite3.connect("Prison.db")
        c = conn.cursor()
        c.execute("UPDATE Education SET  FirstName= :first, LastName= :last, CourseID= :ag, CourseName= :hei, CourseD= :cell, Intime= :gend, Outime= :dura  WHERE ID= :id",
                  {
                      'id':self.EID.get(),
                      'first':  EFname.get(),
                      'last': ELname.get(),
                      'ag': ECID.get(),
                      'hei':ECN.get(),
                      'cell':ECD.get(),
                      'gend':EIN.get(),
                      'dura':EOUT.get()

                  })
        conn.commit()
        conn.close()
    def Uex(self):
        self.u.destroy()

#========================END OF DELETE IN PRISONER EDUCATION============================================================
#========================END OF PRISONER EDUCATION======================================================================
#========================PRISONER CASES=================================================================================
class PrisonerCases:
    def __init__(self, master):
        self.c = master
        self.c.title("Prisoners cases")
        self.c.geometry("1400x1080")
        self.c.config(bg='Black')
        self.frame = Frame(self.c, width=50, height=50, bg='black')
        self.frame.pack()
        self.lb1Title = Label(self.frame, text="Prisoners cases", font=('arial', 50, 'bold'), bg='black',fg='red')
        self.lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        self.photo2 = ImageTk.PhotoImage(file='Edu.jpg')
        self.photo = Label(self.frame, image=self.photo2, bg='white').grid(row=1, column=0)
        self.LoginFrame1 = LabelFrame(self.frame, width=50, height=50, font=('arial', 20, 'bold'),relief='ridge', bg='black', bd=0, fg='red')
        self.LoginFrame1.grid(row=2, column=0)
        self.btnAdd= Button(self.LoginFrame1, text="Add Prisoner Case", width=15, font=('arial', 20, 'bold'),bg='black', fg='red',command=self.Addc)
        self.btnAdd.grid(row=0, column=1, pady=5, padx=5)
        self.UP=Button(self.LoginFrame1, text="Update Prisoner Detail", width=19, font=('arial', 20, 'bold'),bg='black', fg='red',command=self.uc).grid(row=0,column=2)
        self.btnView = Button(self.LoginFrame1, text="View Prisoners Cases", width=17, font=('arial', 20, 'bold'),bg='black', fg='red',command=self.cview)
        self.btnView.grid(row=0, column=3, pady=5, padx=5)
        self.btnd=Button(self.LoginFrame1, text="Delete Prisoner Case", width=17, font=('arial', 20, 'bold'),bg='black', fg='red',command=self.dc)
        self.btnd.grid(row=0, column=4, pady=5, padx=5)
        self.btnBack = Button(self.frame, text="Back", width=10, font=('arial', 20, 'bold'), bg='black',fg='red',command=self.iexit)
        self.btnBack.grid(row=25, column=0, pady=5, padx=5)
    def Addc(self):
         self.Case = Toplevel(self.c)
         self.app = DetailsCase(self.Case)
    def cview(self):
        self.view = Toplevel(self.c)
        self.app = ViewCase(self.view)
    def uc(self):
        self.Upc=Toplevel(self.c)
        self.app=UpdateCase(self.Upc)
    def dc(self):
        self.Delc = Toplevel(self.c)
        self.app = DeleteCase(self.Delc)
    def iexit(self):
        self.c.destroy()
#========================DETAILS IN PRISONER CASES======================================================================
class DetailsCase:
    def __init__(self, master):
        self.c = master
        self.c.title("Prisoners cases")
        self.c.geometry("1400x1080")
        self.c.config(bg='Black')
        self.frame = Frame(self.c, width=50, height=50, bg='black')
        self.frame.pack()
        self.Pid = IntVar()
        self.caseid = IntVar()
        self.Pfirstname= StringVar()
        self.CT=StringVar()
        self.lb1Title = Label(self.frame, text="Enter Prisoners Cases", font=('arial', 50, 'bold'), bg='black',fg='red')
        self.lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        self.ID = Label(self.frame, text="Prisoner ID", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.ID.grid(row=1, column=0)
        self.pid = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.Pid,width=33)
        self.pid.grid(row=1, column=1, padx=10)
        self.Firstname = Label(self.frame, text="First Name", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.Firstname.grid(row=2, column=0)
        self.Fname = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.Pfirstname,width=33)
        self.Fname.grid(row=2, column=1, padx=5)
        self.CID = Label(self.frame, text="Case ID", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.CID.grid(row=3, column=0)
        self.CaseID = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.caseid,width=33)
        self.CaseID.grid(row=3, column=1, padx=10)
        self.Ctype = Label(self.frame, text="Case Type", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.Ctype.grid(row=4, column=0)
        self.Casetype = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.CT,width=33)
        self.Casetype.grid(row=4, column=1, padx=10)
        self.btnSubmit = Button(self.frame, text="Submit", width=10, font=('arial', 15, 'bold'),bg='black', fg='red', command=self.submit)
        self.btnSubmit.grid(row=5, column=0, pady=5, padx=5)
        self.btnClear = Button(self.frame, text="Reset", width=10, font=('arial', 15, 'bold'),bg='black',fg='red')
        self.btnClear.grid(row=5, column=2, pady=5, padx=5)
        self.btnBack = Button(self.frame, text="Exit", width=10, font=('arial', 15, 'bold'), bg='black',fg='red', command=self.Exit)
        self.btnBack.grid(row=5, column=3, pady=5, padx=5)
    def Exit(self):
        self.c.destroy()
    def submit(self):
        conn = sqlite3.connect('Prison.db')
        c = conn.cursor()
        c.execute( 'INSERT INTO "Case" VALUES(?,?,?,?)',(self.Pid.get(),self.Pfirstname.get(),self.caseid.get(),self.CT.get()))
        conn.commit()
        conn.close()
        self.Pid.set("")
        self.caseid.set("")
        self.Pfirstname.set("")
        self.CT.set("")
class ViewCase:
    def __init__(self, master):
        self.id = StringVar()
        self.d = master
        self.d.title("View Staff Details")
        self.d.geometry("1400x1080")
        self.d.config(bg='Black')
        self.frame = Frame(self.d, width=50, height=50, bg='black')
        self.frame.pack()
        self.lb1Title = Label(self.frame, text="Case Records", font=('arial', 40, 'bold'), bg='black',fg='red')
        self.lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        self.LoginFrame1 = LabelFrame(self.frame, width=50, height=50, font=('arial', 30, 'bold'),relief='ridge', bg='black', bd=0, fg='red')
        self.LoginFrame1.grid(row=1, column=0)
        self.lab1 = Label(self.LoginFrame1, text="ID", font=('arial', 20, 'bold'), bg='black', fg='red').grid(row=0,column=0)
        self.lab2 = Label(self.LoginFrame1, text="First Name", font=('arial', 20, 'bold'), bg='black', fg='red').grid(row=0, column=1)
        self.lab3 = Label(self.LoginFrame1, text="Case ID", font=('arial', 20, 'bold'), bg='black', fg='red').grid(row=0, column=2)
        self.lab4 = Label(self.LoginFrame1, text="Case Type", font=('arial', 20, 'bold'), bg='black', fg='red').grid(row=0,column=3)
        row_no = 0;
        self.conn = sqlite3.connect('Prison.db')
        self.c = self.conn.cursor()
        values = self.c.execute('select * from "Case" order by Pid ')
        self.records = self.c.fetchall()
        for self.record in self.records:
            id_no = self.record[0]
            f_name = self.record[1]
            c_id = self.record[2]
            c_type = self.record[3]
            row_no = row_no + 1
            self.Label = Label(self.LoginFrame1, text=id_no, width=7, font=('times', 20, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=0, padx=(0, 2))
            self.Labe2 = Label(self.LoginFrame1, text=f_name, width=15, font=('times', 20, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=1, padx=(0, 2))
            self.Labe3 = Label(self.LoginFrame1, text=c_id, width=15, font=('times', 20, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=2, padx=(0, 2))
            self.Labe4 = Label(self.LoginFrame1, text=c_type, width=30, font=('times', 20, 'italic'), fg='red', bd=1,bg='black', relief='ridge').grid(row=row_no, column=3, padx=(0, 2))
        row_no = row_no + 6
        self.btnBack = Button(self.frame, text="Exit", width=10, font=('arial', 15, 'bold'), bg='black',fg='red', command=self.iexit)
        self.btnBack.grid(row=row_no, column=0, pady=5, padx=5)
        self.conn.commit()
        self.conn.close()
    def iexit(self):
        self.d.destroy()
class UpdateCase:
    def __init__(self, master):
        self.u=master
        self.u.title("Prisoner Details")
        self.u.geometry("1400x1080")
        self.u.config(bg='Black')
        frame = Frame(self.u, width=50, height=50, bg='black')
        frame.pack()
        global CFname
        global CCaseid
        global CCT
        global upid
        lb1Title = Label(frame, text="Update Remand Cases Record", font=('arial', 40, 'bold'), bg='black',fg='red')
        lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        uid = Label(frame, text="Enter Prisoner ID", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        uid.grid(row=1, column=0)
        upid = Entry(frame, font=('arial', 10, 'bold'), bd=0, width=33)
        upid.grid(row=1, column=1, padx=10)
        update = Button(frame, text="Update", width=10, font=('arial', 15, 'bold'),bg='black', fg='red', command=self.UP)
        update.grid(row=2, column=3, pady=5, padx=5)
        Firstname = Label(frame, text="First Name", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Firstname.grid(row=3, column=0)
        CFname = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        CFname.grid(row=3, column=1, padx=5)
        Caseid = Label(frame, text="Case ID", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Caseid.grid(row=3, column=2)
        CCaseid = Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        CCaseid.grid(row=3, column=3, padx=5)
        Casetype = Label(frame, text="Case Type", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        Casetype.grid(row=4, column=0)
        CCT= Entry(frame, font=('arial', 10, 'bold'), bd=0,width=33)
        CCT.grid(row=4, column=1, padx=10)
        btnSubmit = Button(frame, text="Save Record", width=10, font=('arial', 15, 'bold'),bg='black', fg='red', command=self.Usub)
        btnSubmit.grid(row=5, column=0, pady=5, padx=5)
        btnex=Button(frame, text="Exit", width=10, font=('arial', 15, 'bold'),bg='black', fg='red', command=self.Uex).grid(row=5,column=2,pady=5,padx=5)
    def UP(self):
        conn = sqlite3.connect("Prison.db")
        c = conn.cursor()
        self.record_id=upid.get()
        c.execute('SELECT * FROM "Case" WHERE Pid=?',(self.record_id,))
        records=c.fetchall()
        for record in records:
            CFname.insert(0, record[1])
            CCaseid.insert(0, record[2])
            CCT.insert(0, record[3])
    def Usub(self):
        conn = sqlite3.connect("Prison.db")
        c = conn.cursor()
        c.execute('UPDATE "Case" SET  Pfirstname= :first, Pcaseid= :last, Casetype= :ag  WHERE Pid= :id',
                  {
                      'id':upid.get(),
                      'first':  CFname.get(),
                      'last': CCaseid.get(),
                      'ag': CCT.get()
                  })
        conn.commit()
        conn.close()
    def Uex(self):
        self.u.destroy()
class DeleteCase:
    def __init__(self, master):
        self.id = StringVar()
        self.d = master
        self.d.title("Staff Details")
        self.d.geometry("1400x1080")
        self.d.config(bg='Black')
        self.frame = Frame(self.d, width=50, height=50, bg='black')
        self.frame.pack()
        self.rid=StringVar()
        self.lb1Title = Label(self.frame, text="Delete Case Record", font=('arial', 40, 'bold'), bg='black',fg='red')
        self.lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        self.ID = Label(self.frame, text="Enter Prisoner ID", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.ID.grid(row=1, column=0)
        self.pid = Entry(self.frame, font=('arial', 10, 'bold'), bd=0, textvariable=self.rid, width=33)
        self.pid.grid(row=1, column=1, padx=10)
        self.btndelete = Button(self.frame, text="Delete", width=10, font=('arial', 15, 'bold'),bg='black', fg='red', command=self.dell)
        self.btndelete.grid(row=2, column=0, pady=5, padx=5)
        self.btnBack = Button(self.frame, text="Exit", width=10, font=('arial', 15, 'bold'), bg='black',fg='red', command=self.Exit)
        self.btnBack.grid(row=2, column=3, pady=5, padx=5)
    def dell(self):
        self.him = self.rid.get()
        conn = sqlite3.connect("Prison.db")
        c = conn.cursor()
        c.execute('DELETE FROM "Case" WHERE Pid=' + self.him)
        conn.commit()

        conn.close()
    def Exit(self):
        self.d.destroy()
#========================END  OF PRISONER CASES TABLE===================================================================
if __name__=='__main__':
    main()