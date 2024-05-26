from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def handle_login():
   email=email_input.get()
   password=pass_input.get()

   if email=='ashikagupta1503@gmail.com' and password=='flipkart.123':
        messagebox.showinfo('yayy','Login successfull')
   else: 
        messagebox.showerror('Error','Login failed')
    




root=Tk()

root.title('Login to Flipkart') #To change the title of window
# root.iconbitmap() #To change the icon of the window
root.configure(background='#0096DC')
root.geometry('350x500')

img=Image.open(r"C:\Users\ashik\100 Days Of Python\Tkinter\flipkart-logo.png")
resized_img=img.resize((90,90))
img=ImageTk.PhotoImage(resized_img)

img_label = Label(root, image=img)
img_label.pack(pady=(10,10))

text_label=Label(root,text="Flipkart",background="#0096DC" ,foreground="white")
text_label.pack(pady=2)
text_label.config(font=('verdana' ,15))


email_label=Label(root,text='Enter your email:',bg='#0096DC',fg='white')
email_label.pack(pady=5)
email_label.config(font=('verdana' ,16))

email_input=Entry(root,width=30)
email_input.pack(padx=5 ,pady=5)

pass_label=Label(root,text='Enter your password:',bg='#0096DC',fg='white')
pass_label.pack()
pass_label.config(font=('verdana' ,16))

pass_input=Entry(root,width=30)
pass_input.pack(padx=10 ,pady=5)

button=Button(root,text='Login',bg='white',fg='black',width=10,command=handle_login)
button.pack(padx=10,pady=10)

root.mainloop()

