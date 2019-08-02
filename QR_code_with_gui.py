from tkinter import *
import qrcode
from PIL import Image,ImageFont,ImageDraw



win = Tk()
win.title('ID Card Generator')
win.geometry("300x200")

############ get user information##############


def userData():
    global Name
    Name = nameEntry.get()

    global Blood
    Blood = bloodEntry.get()

    global Number
    Number = numberEntry.get()

    global Email
    Email = emailEntry.get()

    img = qrcode.make(str(Name)+'\n'+ str(Blood)+'\n'+Number+'\n'+str(Email))
    img.save("/home/vaishnav/Desktop/pycharm/mile_stone_project!/all_QR_code/ID_card_name/{}.png".format(Name))      #### QR generator Code
    img.show("/home/vaishnav/Desktop/pycharm/mile_stone_project!/all_QR_code/ID_card_name/{}.png".format(Name))

    # font = ImageFont.truetype('Roboto-Bold.ttf', size=45)
    # (x, y) = (50, 50)
    # message = Name
    # color = 'rgb(0, 0, 0)'
    # image1 = Image.new('RGBA', (300, 400), 'white')
    # draw = ImageDraw.Draw(image1)
    # image1 = draw.text((x, y), message, fill=color, font=font)
    # image1.show()

###############################################


################## GUI Inputs for window ########

name = Label(win, text = 'Name')
name.grid(row=0)

blood = Label(win, text= 'Bloog Group')
blood.grid(row =1)


number = Label(win,text='Number')
number.grid(row=2)


email = Label(win,text = 'Email')
email.grid(row=3)


nameEntry =  Entry(win)
nameEntry.grid(row=0,column=1)

bloodEntry = Entry(win)
bloodEntry.grid(row=1,column=1)

numberEntry = Entry(win)
numberEntry.grid(row=2,column=1)

emailEntry = Entry(win)
emailEntry.grid(row=3,column=1)

button_1 = Button(win,text = 'Submit',command=userData)
button_1.grid(columnspan=2)

##button_2 = Button(win,text = 'Generate ID card',command=generateId)
##button_2.grid(columnspan=2)


win.mainloop()