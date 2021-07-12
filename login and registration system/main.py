from tkinter import*
import json
from tkinter import messagebox
import smtplib
import random
from tkinter.simpledialog import*
root=Tk()
data_of_passwords_boi=StringVar()
data_of_username_boi=StringVar()
data_of_username_boi.set('')
data_of_passwords_boi.set('')
iasdoisdufdd=IntVar()
iasdoisdufdd1=IntVar()
def show_pass1(s):
	if iasdoisdufdd1.get()==0:
		input_of_password1.config(show='')
	if iasdoisdufdd1.get()!=0:
		input_of_password1.config(show='*')
def show_pass(s):
	if iasdoisdufdd.get()==0:
		input_of_password.config(show='')
	if iasdoisdufdd.get()!=0:
		input_of_password.config(show='*')
def register_1():
	if input_of_password1.get()=='':
		messagebox.showinfo('Info','Please Set A Password')
	if input_of_user_name1.get()=='':
		messagebox.showinfo('Info','Please Set A User Name')
	if input_of_password1.get()!='' and input_of_user_name1.get()!='':
		data=json.dumps({"user name": input_of_user_name1.get(), "password": input_of_password1.get()}, sort_keys=True,indent=True)
		a=open('data.json','w')
		a.write(data)
		messagebox.showinfo('Info','Registered.')
		root.deiconify()
		root_12.destroy()
def register_boii():
	root.iconify()
	global input_of_password1,input_of_user_name1,root_12
	root_12=Toplevel()
	root_12.title('Register')
	root_12.minsize(500,225)
	input_of_user_name1=Entry(root_12,width=14,font=('Arial',20,'bold'),textvariable=data_of_username_boi)
	input_of_user_name1.place(x=175,y=16)
	user_name_lab=Label(root_12,text='User Name:',font=('Arial',20,'bold')).place(x=1,y=15)
	input_of_password1=Entry(root_12,width=14,font=('Arial',20,'bold'),show='*',textvariable=data_of_passwords_boi)
	input_of_password1.place(x=175,y=71)
	passoword_lab1=Label(root_12,text='Password:',font=('Arial',23,'bold')).place(x=1,y=70)
	Register1=Button(root_12,text='Register',borderwidth=5,background='purple1',fg='white',font=('Arial Rounded MT bold',12,'bold'),command=register_1)
	Register1.place(x=220,y=115)
	show_password=Checkbutton(root_12,text='Show Password',variable=iasdoisdufdd1)
	show_password.place(x=390,y=80)
	show_password.bind('<Button-1>',show_pass1)
	input_of_password1.delete(0,END)
	input_of_user_name1.delete(0,END)
def login1():
	with open('data.json','r') as data_infinte:
		real_data=json.load(data_infinte)
	if real_data['user name']==input_of_user_name.get() and real_data['password']==input_of_password.get():
		messagebox.showinfo('Login','Successfully Log on')
		print('BYEEEE.... (:')
		exit()
	else:
		messagebox.showerror('Info','The Password Or User Name Is Not Correct!!')
def login_boii():
	root.iconify()
	global hide_pass1,show_password
	global input_of_password
	global input_of_user_name,root_1
	root_1=Toplevel()
	root_1.title('Login')
	root_1.maxsize(500,225)
	root_1.minsize(500,225)
	input_of_user_name=Entry(root_1,width=14,font=('Arial',20,'bold'))
	input_of_user_name.place(x=175,y=16)
	user_name_lab=Label(root_1,text='User Name:',font=('Arial',20,'bold')).place(x=1,y=15)
	input_of_password=Entry(root_1,width=14,font=('Arial',20,'bold'),show='*')#ide for low end machine.
	input_of_password.place(x=175,y=71)
	passoword_lab=Label(root_1,text='Password:',font=('Arial',23,'bold'),).place(x=1,y=70)
	LOGin=Button(root_1,text='Login',borderwidth=5,background='purple1',fg='white',font=('Arial Rounded MT bold',12,'bold'),command=login1)
	LOGin.place(x=220,y=115)
	show_password=Checkbutton(root_1,text='Show Password',variable=iasdoisdufdd)
	show_password.place(x=390,y=80)
	show_password.bind('<Button-1>',show_pass)
	iasdoisdufdd.set(0)
root.title('LOGin AnD Registeration SySTEM.'.title())
root.minsize(100,200)
register=Button(root,text='Register',width=13,command=register_boii,borderwidth=5,background='purple1',fg='white',font=('Arial Rounded MT bold',15,'bold'))
register.place(y=50,x=1)
LOGin=Button(root,text='Login',width=13,command=login_boii,borderwidth=5,background='purple1',fg='white',font=('Arial Rounded MT bold',15,'bold'))
OR=Label(root,text='Or',font=('Arial Rounded MT bold',20,'bold')).place(x=80,y=100)
LOGin.place(y=150,x=1)
root.mainloop()