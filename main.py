#importing
from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
#connecting to mysql server
mypass="MyNewSecret123!"
mydatabase="db"
con=pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur=con.cursor()

#designing the window
root=Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")
#adding the background image
same=True
n=1.6
background_image=Image.open('lib.jpeg')
[imageSizeWidth, imageSizeHeight]=background_image.size
newImageSizeWidth=int(imageSizeWidth*n)
if same:
    newImageSizeHeight=int(imageSizeHeight*n)
else:
    newImageSizeHeight=int(imageSizeHeight/n)
background_image=background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.Resampling.LANCZOS)
img=ImageTk.PhotoImage(background_image)
Canvas1=Canvas(root)
Canvas1.create_image(300,340,image=img)
Canvas1.config(bg="white",width=newImageSizeWidth,height=newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)
#setting up the upper frame
headingFrame1=Frame(root,bg='#ADD8E6',bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel=Label(headingFrame1, text="WELCOME TO LIBRARY!",bg="black",fg="white",font=("Arial Rounded MT Bold",15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
#adding the buttons
btn1=Button(root,text="Add Book Details",bg="black",fg="white",command=addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
btn2=Button(root,text="Delete Book",bg="black",fg="white",command=delete)
btn2.place(relx=0.28,rely=0.5,relwidth=0.45,relheight=0.1)
btn3=Button(root,text="View Book List",bg="black",fg="white",command=View)
btn3.place(relx=0.28,rely=0.6,relwidth=0.45,relheight=0.1)
btn4=Button(root,text="Issue Book to New Student",bg="black",fg="white",command=issueBook)
btn4.place(relx=0.28,rely=0.7,relwidth=0.45,relheight=0.1)
btn5=Button(root,text="Return Book",bg="black",fg="white",command=returnBook)
btn5.place(relx=0.28,rely=0.8,relwidth=0.45,relheight=0.1)

root.mainloop()