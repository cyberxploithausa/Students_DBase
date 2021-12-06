# BackEnd
import sqlite3


def studentData():
    conn = sqlite3.connect("C:/Users/cyberxploit/AppData/Roaming/student.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, stdID text, \
        Firstname text, Surname text, DoB text, Age text, Gender text, Address text, Mobile text)")
    conn.commit()
    conn.close()


def addStdRec(stdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile):
    conn = sqlite3.connect("C:/Users/cyberxploit/AppData/Roaming/student.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO student VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", (stdID, Firstname,
                                                                              Surname, DoB, Age, Gender, Address, Mobile))
    conn.commit()
    conn.close()


def viewData():
    conn = sqlite3.connect("C:/Users/cyberxploit/AppData/Roaming/student.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    row = cur.fetchall()
    conn.close()
    return row


def deleteRec(id):
    conn = sqlite3.connect("C:/Users/cyberxploit/AppData/Roaming/student.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    conn.commit()
    conn.close()


def searchData(stdID="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    conn = sqlite3.connect("C:/Users/cyberxploit/AppData/Roaming/student.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student WHERE stdID=? OR Firstname=? OR Surname=? OR DoB=? OR Age=? OR \
        Gender=? OR Address=? OR Mobile=?", (stdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
    row = cur.fetchall()
    conn.close()
    return row


def dataUpdate(id, stdID="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    conn = sqlite3.connect("C:/Users/cyberxploit/AppData/Roaming/student.db")
    cur = conn.cursor()
    cur.execute("UPDATE student  SET stdID=?, Firstname=?, Surname=?, DoB= ?, Age=?, Gender=?, Address=?, \
        Mobile=? WHERE id=?", (stdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile, id))
    conn.commit()
    conn.close()


studentData()
