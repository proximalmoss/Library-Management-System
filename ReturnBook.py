from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

# Database Connection
mypass = "MyNewSecret123!"  # Change this to your actual MySQL password
mydatabase = "db"

try:
    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()
except pymysql.Error as err:
    messagebox.showerror("Database Error", f"Error: {err}")
    exit()

# Table Names
issueTable = "books_issued"
bookTable = "books"

def returnn():
    global bookInfo1, root

    bid = bookInfo1.get().strip()  # Get user input and remove extra spaces
    if not bid:
        messagebox.showwarning("Warning", "Please enter a Book ID!")
        return

    allBid = []  # Store all issued book IDs

    try:
        # Fetch all issued book IDs from books_issued table
        cur.execute(f"SELECT bid FROM {issueTable} WHERE bid IS NOT NULL")
        allBid = [str(row[0]) for row in cur.fetchall()]  # Convert to string

        print("Fetched Book IDs:", allBid)  # Debugging Output

        if bid not in allBid:
            messagebox.showinfo("Error", "Book ID not found in issued books")
            return

        # Check the book status in books table
        cur.execute(f"SELECT status FROM {bookTable} WHERE bid = %s", (bid,))
        result = cur.fetchone()

        if result:
            check = result[0]  # Fetch status
            print(f"Book ID {bid} Status:", check)  # Debugging Output

            if check.lower() == "issued":
                # Delete from books_issued table
                cur.execute(f"DELETE FROM {issueTable} WHERE bid = %s", (bid,))
                con.commit()

                # Update status in books table
                cur.execute(f"UPDATE {bookTable} SET status = 'avail' WHERE bid = %s", (bid,))
                con.commit()

                messagebox.showinfo("Success", f"Book ID {bid} returned successfully!")
            else:
                messagebox.showinfo("Message", "This book is already available!")
        else:
            messagebox.showinfo("Error", "Book ID not found in books table")
    except pymysql.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    finally:
        root.destroy()

def returnBook():
    global bookInfo1, root

    root = Tk()
    root.title("Library Management System")
    root.geometry("600x500")
    root.config(bg="#006B38")

    headingFrame = Frame(root, bg="#FFBB00", bd=5)
    headingFrame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame, text="Return Book", bg='black', fg='white', font=("Arial Rounded MT Bold",15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.3)

    lb1 = Label(labelFrame, text="Book ID:", bg='black', fg='white', font=('Courier', 12))
    lb1.place(relx=0.05, rely=0.3)

    bookInfo1 = Entry(labelFrame, font=('Courier', 12))
    bookInfo1.place(relx=0.3, rely=0.3, relwidth=0.6)

    SubmitBtn = Button(root, text="Return", bg='#d1ccc0', fg='black', command=returnn)
    SubmitBtn.place(relx=0.28, rely=0.7, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.7, relwidth=0.18, relheight=0.08)

    root.mainloop()