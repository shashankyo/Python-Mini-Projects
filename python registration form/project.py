from tkinter import *
root  = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

#Heading
Label(root, text="Python Registration Form", font="arial 15 bold").grid(row=0, column=3)

#Field name
name=Label(root, text="Name")
phone=Label(root, text="Phone")
gender=Label(root, text="Gender")
emergency=Label(root, text="Emergency")
paymentmode=Label(root, text="Payment Mode")

#Packing Fields
name.grid(row=1, column=1)
phone.grid(row=2, column=1)
gender.grid(row=3, column=1)
emergency.grid(row=4, column=1)
paymentmode.grid(row=5, column=1)

#Variable for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentmodevalue = StringVar
checkvalue = IntVar

#Creating entry field
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)

#Packing entry field
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

#Creating checkbox
checkbtn = Checkbutton(text="remember me?", variable=checkvalue)
checkbtn.grid(row=6, column=3)

#Submit button
Button(text ="Submit", command = getvals).grid(row=7, column=3)
root.mainloop()
