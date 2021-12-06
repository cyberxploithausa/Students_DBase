# FrontEnd
from tkinter import *
import tkinter.messagebox
import stdDataBase


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Database System")
        self.root.geometry("1350x3700+0+0")
        self.root.config(bg="cadet blue")

        stdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        # ===============================Functions=============================================

        def get_selected_tuple(event):
            global selected_tuple
            index = studentList.curselection()[0]
            selected_tuple = studentList.get(index)

            self.txtstdID.delete(0, END)
            self.txtstdID.insert(END, selected_tuple[1])

            self.txtFna.delete(0, END)
            self.txtFna.insert(END, selected_tuple[2])

            self.txtSna.delete(0, END)
            self.txtSna.insert(END, selected_tuple[3])

            self.txtDoB.delete(0, END)
            self.txtDoB.insert(END, selected_tuple[4])

            self.txtAge.delete(0, END)
            self.txtAge.insert(END, selected_tuple[5])

            self.txtGender.delete(0, END)
            self.txtGender.insert(END, selected_tuple[6])

            self.txtAdr.delete(0, END)
            self.txtAdr.insert(END, selected_tuple[7])

            self.txtMobile.delete(0, END)
            self.txtMobile.insert(END, selected_tuple[8])

        def iExit():
            iExit = tkinter.messagebox.askyesno(
                "Student Database Management System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def addData():
            if (len(stdID.get()) != 0):
                stdDataBase.addStdRec(stdID.get(), Firstname.get(), Surname.get(
                ), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())
                studentList.delete(0, END)
                studentList.insert(END, (stdID.get(), Firstname.get(), Surname.get(
                ), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()))
            write_file()

        #creating a backup file should in case anything happened...
        #This should be store in the c drive maybe inside {appdata -> Roamning}
        def write_file():
            file_bck = open("C:/Users/cyberxploit/AppData/Roaming/backup.txt", "a")

            backup = [self.txtstdID.get(), self.txtFna.get(), self.txtSna.get(), self.txtDoB.get(
            ), self.txtAge.get(), self.txtGender.get(), self.txtAdr.get(), self.txtMobile.get()]

            for i in backup:
                file_bck.write(f"{i} ")
                if i == self.txtMobile.get():
                    file_bck.write('\n')

        def displayData():
            studentList.delete(0, END)
            for row in stdDataBase.viewData():
                studentList.insert(END, row, str(""))

        def clearData():
            self.txtstdID.delete(0, END)
            self.txtFna.delete(0, END)
            self.txtSna.delete(0, END)
            self.txtDoB.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtAdr.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtMobile.delete(0, END)

        def deleteData():
            deleteData = tkinter.messagebox.askyesno(
                "Student Database Management System", "Confirm if you want to delete")
            if deleteData > 0:
                if (len(stdID.get())) != 0:
                    stdDataBase.deleteRec(selected_tuple[0])
                    clearData()
                    displayData()

        def searchData():
            studentList.delete(0, END)
            for row in stdDataBase.searchData(stdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()):
                studentList.insert(END, row, str(""))

        def updateData():
            if (len(stdID.get()) != 0):
                stdDataBase.deleteRec(selected_tuple[0])
            if (len(stdID.get()) != 0):
                stdDataBase.addStdRec(stdID.get(), Firstname.get(), Surname.get(
                ), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())
                studentList.delete(0, END)
                studentList.insert(END, stdID.get(), Firstname.get(), Surname.get(
                ), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())

        # ===============================Frames===============================================
        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8,
                         bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lbtTit = Label(TitFrame, font=("arial", 47, "bold"),
                            text="CyberXploit Hausa Training", bg="Ghost White", fg="red")
        self.lbtTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70,
                            padx=18, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400,
                          padx=20, pady=20, bg="cadet blue", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, bg="Ghost White", relief=RIDGE,
                                   font=("arial", 20, "bold"), text="Student Membership Info \n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, bg="Ghost White", relief=RIDGE,
                                    font=("arial", 20, "bold"), text="Book Details \n")
        DataFrameRIGHT.pack(side=RIGHT)

        # =================================Labels And Entry Widget==========================================
        self.lblstdID = Label(DataFrameLEFT, font=(
            "arial", 20, "bold"), text="Student ID :", padx=2, pady=2, bg="Ghost White")
        self.lblstdID.grid(row=0, column=0, sticky='W')
        self.txtstdID = Entry(DataFrameLEFT, font=(
            "arial", 20, "bold"), textvariable=stdID, width=39)
        self.txtstdID.grid(row=0, column=1)
        self.txtstdID.bind('<Enter>')

        self.lblFna = Label(DataFrameLEFT, font=(
            "arial", 20, "bold"), text="Firstname :", padx=2, pady=2, bg="Ghost White")
        self.lblFna.grid(row=1, column=0, sticky='W')
        self.txtFna = Entry(DataFrameLEFT, font=(
            "arial", 20, "bold"), textvariable=Firstname, width=39)
        self.txtFna.grid(row=1, column=1)

        self.lblSna = Label(DataFrameLEFT, font=(
            "arial", 20, "bold"), text="Surname :", padx=2, pady=2, bg="Ghost White")
        self.lblSna.grid(row=2, column=0, sticky='W')
        self.txtSna = Entry(DataFrameLEFT, font=(
            "arial", 20, "bold"), textvariable=Surname, width=39)
        self.txtSna.grid(row=2, column=1)

        self.lblDoB = Label(DataFrameLEFT, font=(
            "arial", 20, "bold"), text="Date of Birth :", padx=2, pady=3, bg="Ghost White")
        self.lblDoB.grid(row=3, column=0, sticky='W')
        self.txtDoB = Entry(DataFrameLEFT, font=(
            "arial", 20, "bold"), textvariable=DoB, width=39)
        self.txtDoB.grid(row=3, column=1)

        self.lblAge = Label(DataFrameLEFT, font=(
            "arial", 20, "bold"), text="Age :", padx=2, pady=3, bg="Ghost White")
        self.lblAge.grid(row=4, column=0, sticky='W')
        self.txtAge = Entry(DataFrameLEFT, font=(
            "arial", 20, "bold"), textvariable=Age, width=39)
        self.txtAge.grid(row=4, column=1)

        self.lblGender = Label(DataFrameLEFT, font=(
            "arial", 20, "bold"), text="Gender :", padx=2, pady=3, bg="Ghost White")
        self.lblGender.grid(row=5, column=0, sticky='W')
        self.txtGender = Entry(DataFrameLEFT, font=(
            "arial", 20, "bold"), textvariable=Gender, width=39)
        self.txtGender.grid(row=5, column=1)

        self.lblAdr = Label(DataFrameLEFT, font=(
            "arial", 20, "bold"), text="Address :", padx=2, pady=3, bg="Ghost White")
        self.lblAdr.grid(row=6, column=0, sticky='W')
        self.txtAdr = Entry(DataFrameLEFT, font=(
            "arial", 20, "bold"), textvariable=Address, width=39)
        self.txtAdr.grid(row=6, column=1)

        self.lblMobile = Label(DataFrameLEFT, font=(
            "arial", 20, "bold"), text="Mobile :", padx=2, pady=3, bg="Ghost White")
        self.lblMobile.grid(row=7, column=0, sticky='W')
        self.txtMobile = Entry(DataFrameLEFT, font=(
            "arial", 20, "bold"), textvariable=Mobile, width=39)
        self.txtMobile.grid(row=7, column=1)

        # =================================ListBox and Scrollbar Widget==========================================

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentList = Listbox(DataFrameRIGHT, width=41, height=16, font=(
            "arial", 12, "bold"), yscrollcommand=scrollbar.set)
        studentList.grid(row=0, column=0, padx=8)

        scrollbar.config(command=studentList.yview)
        studentList.bind("<<ListboxSelect>>", get_selected_tuple)

        # =================================Button Widget========================================================
        self.btnAddData = Button(ButtonFrame, text="Add New", font=(
            "arial", 20, "bold"), command=addData, height=1, width=10, bd=4)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplayData = Button(ButtonFrame, text="View All", font=(
            "arial", 20, "bold"), command=displayData, height=1, width=10, bd=4)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=(
            "arial", 20, "bold"), command=clearData, height=1, width=10, bd=4)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=(
            "arial", 20, "bold"), command=deleteData, fg="red", height=1, width=10, bd=4)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=(
            "arial", 20, "bold"), command=searchData, height=1, width=10, bd=4)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=(
            "arial", 20, "bold"), command=updateData, height=1, width=10, bd=4)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExitData = Button(ButtonFrame, text="Exit", font=(
            "arial", 20, "bold"), command=iExit, fg="red", height=1, width=10, bd=4)
        self.btnExitData.grid(row=0, column=6)


if __name__ == "__main__":
    root = Tk()
    application = Student(root)
    root.mainloop()
