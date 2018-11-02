from tkinter import *
import tkinter.messagebox as tm
import pymysql

mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="DISASTER_MANAGEMENT_SYSTEM"
)
db = pymysql.connect("localhost", "root", "password", "DISASTER_MANAGEMENT_SYSTEM")
cursor = db.cursor()

def insert(cur, user_id, first_name, last_name, username, password, email, zip_code, role):
        sql = "INSERT INTO `DISASTER_MANAGEMENT_SYSTEM`.`ACCOUNTS` (" \
            "`AccountID`, `FirstName`, `LastName`, `EmailAddress`," \
            " `Password`, `Role`, `UserName`, `Zipcode`)" \
            " VALUES ('{}', '{}', '{}', '{}', '{}'," \
            " '{}', '{}', '{}')".format(
            user_id, first_name, last_name, email,
            password, role, username, zip_code)
        # cursor.execute(sql)
        try:
            # execute sql
            cursor.execute(sql)
            db.commit()
        except pymysql.err.IntegrityError as e:
            print(e.args)
            # roll back if any error occur
            db.rollback()

class CreateAccountFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_firstName = Label(self, text="FirstName")
        self.label_lastName = Label(self, text="LastName")
        self.label_emailAddress = Label(self, text="EmailAddress")
        self.label_zipcode = Label(self, text="ZipCode")
        self.label_role = Label(self, text="Role")
        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_firstName = Entry(self)
        self.entry_lastName = Entry(self)
        self.entry_emailAddress = Entry(self)
        self.entry_zipcode = Entry(self)
        self.entry_role = Entry(self)
        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_firstName.grid(row=0, sticky=E)
        self.label_lastName.grid(row=1, sticky=E)
        self.label_emailAddress.grid(row=2, sticky=E)
        self.label_zipcode.grid(row=3, sticky=E)
        self.label_role.grid(row=4, sticky=E)
        self.label_username.grid(row=5, sticky=E)
        self.label_password.grid(row=6, sticky=E)

        self.entry_firstName.grid(row=0, column=1)
        self.entry_lastName.grid(row=1, column=1)
        self.entry_emailAddress.grid(row=2, column=1)
        self.entry_zipcode.grid(row=3, column=1)
        self.entry_role.grid(row=4, column=1)
        self.entry_username.grid(row=5, column=1)
        self.entry_password.grid(row=6, column=1)

        self.logbtn = Button(self, text="CreateAccount", command=self._create_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _create_btn_clicked(self):
        # print("Clicked")
        firstName = self.entry_firstName.get()
        lastName = self.entry_lastName.get()
        emailAddress = self.entry_emailAddress.get()
        zipcode = self.entry_zipcode.get()
        role = self.entry_role.get()
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print(firstName, emailAddress)
        insert(cursor, 2, firstName, lastName, username, password, emailAddress, zipcode, role)


# insert(cursor, '2', 'Matt', 'Barry', 'mbarry', 'mbarry', 'mbarry@email.com', '52245', 'V', 'apple, clothes, $5')

root = Tk()
lf = CreateAccountFrame(root)
root.mainloop()