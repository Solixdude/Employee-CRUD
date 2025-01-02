from tkinter import *
import mysql.connector
from tkinter import messagebox
import os

# Funcție pentru inserare
def insertData():
    global myDB
    id = enterId.get()
    name = enterName.get()
    dept = enterDept.get()

    if id == "" or name == "" or dept == "":
        messagebox.showwarning("Cannot insert.", "All fields are required!")
    else:
        try:
            myDB = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd=os.getenv('DB_PASSWORD', 'Imsexyandiknow1'),
                database="employee_database"
            )
            myCur = myDB.cursor()

            query = "INSERT INTO empDetails (empID, empName, empDept) VALUES (%s, %s, %s)"
            values = (id, name, dept)
            myCur.execute(query, values)
            myDB.commit()

            enterId.delete(0, 'end')
            enterName.delete(0, 'end')
            enterDept.delete(0, 'end')

            messagebox.showinfo("Insert Status", "Data Inserted Successfully")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            myDB.close()

# Funcție pentru actualizare
def updateData():
    global myDB
    id = enterId.get()
    name = enterName.get()
    dept = enterDept.get()

    if id == "" or name == "" or dept == "":
        messagebox.showwarning("Cannot update.", "All fields are required!")
    else:
        try:
            myDB = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd=os.getenv('DB_PASSWORD', 'Imsexyandiknow1'),
                database="employee_database"
            )
            myCur = myDB.cursor()

            query = "UPDATE empDetails SET empName = %s, empDept = %s WHERE empID = %s"
            values = (name, dept, id)
            myCur.execute(query, values)
            myDB.commit()

            enterId.delete(0, 'end')
            enterName.delete(0, 'end')
            enterDept.delete(0, 'end')

            messagebox.showinfo("Update Status", "Data Updated Successfully")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            myDB.close()

# Funcție pentru obținerea datelor
def getData():
    global myDB
    id = enterId.get()

    if id == "":
        messagebox.showwarning("Fetch Status", "Please provide the Emp ID to fetch the data")
    else:
        try:
            myDB = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd=os.getenv('DB_PASSWORD', 'Imsexyandiknow1'),
                database="employee_database"
            )
            myCur = myDB.cursor()

            query = "SELECT * FROM empDetails WHERE empID = %s"
            myCur.execute(query, (id,))
            rows = myCur.fetchall()

            if not rows:
                messagebox.showwarning("Fetch Status", "No data found for the given Employee ID")
            else:
                enterName.delete(0, 'end')
                enterDept.delete(0, 'end')
                for row in rows:
                    enterName.insert(0, row[1])
                    enterDept.insert(0, row[2])
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            myDB.close()

# Funcție pentru ștergere
def deleteData():
    global myDB
    id = enterId.get()

    if id == "":
        messagebox.showwarning("Delete Status", "Employee ID is required!")
    else:
        try:
            myDB = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd=os.getenv('DB_PASSWORD', 'Imsexyandiknow1'),
                database="employee_database"
            )
            myCur = myDB.cursor()

            query = "DELETE FROM empDetails WHERE empID = %s"
            myCur.execute(query, (id,))
            myDB.commit()

            enterId.delete(0, 'end')
            enterName.delete(0, 'end')
            enterDept.delete(0, 'end')

            messagebox.showinfo("Delete Status", "Employee deleted successfully")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            myDB.close()

def show():
    myDB = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd=os.getenv('DB_PASSWORD', 'Imsexyandiknow1'),
        database="employee_database"
    )
    myCur = myDB.cursor()
    myCur.execute("select * from empDetails")
    rows = myCur.fetchall()
    showData.delete(0, showData.size())

    for row in rows:
        addData = str(row[0] + ' ' + row[1] + ' ' + row[2])
        showData.insert(showData.size() + 1, addData)

        myDB.close()

# Funcție pentru resetarea câmpurilor
def resetFields():
    enterId.delete(0, 'end')
    enterName.delete(0, 'end')
    enterDept.delete(0, 'end')

    messagebox.showinfo("Reset Status", "Database reset successfully!")

# Interfața grafică (Tkinter)
window = Tk()
window.geometry("600x270")
window.title("Employee CRUD App")

empId = Label(window, text="Employee ID", font=("Serif", 12))
empId.place(x=20, y=30)

empName = Label(window, text="Employee Name", font=("Serif", 12))
empName.place(x=20, y=60)

empDep = Label(window, text="Employee Dept", font=("Serif", 12))
empDep.place(x=20, y=90)

enterId = Entry(window)
enterId.place(x=170, y=30)

enterName = Entry(window)
enterName.place(x=170, y=60)

enterDept = Entry(window)
enterDept.place(x=170, y=90)

insertBtn = Button(window, text="Insert", font=("Sans", 12), bg='white', command=insertData)
insertBtn.place(x=20, y=160)

updateBtn = Button(window, text="Update", font=("Sans", 12), bg='white', command=updateData)
updateBtn.place(x=80, y=160)

getBtn = Button(window, text="Fetch", font=("Sans", 12), bg='white', command=getData)
getBtn.place(x=150, y=160)

deleteBtn = Button(window, text="Delete", font=("Sans", 12), bg='white', command=deleteData)
deleteBtn.place(x=210, y=160)

resetBtn = Button(window, text="Reset", font=("Sans", 12), bg="white", command=resetFields)
resetBtn.place(x=20, y=210)

showData = Listbox(window)
showData.place(x=330, y=30)

window.mainloop()




