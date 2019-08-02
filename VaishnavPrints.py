import qrcode
from PIL import Image

text = ('VAISHNAV PRINTS')
email = ('Email : sathya7227@gmail.com')
address = ('Address : #973,Swaghat Sankeerthana,2nd main road,M C Layout,Vijayanagar,Bangalore-560040')
pno = ('Mobile phno :9845615177/8310487294')
img = qrcode.make(str(text)+'\n'+str(email)+'\n'+str(address)+'\n'+str(pno))
img.save("/home/vaishnav/Desktop/pycharm/mile_stone_project!/all_QR_code/{}.png".format(text))

img.show("/home/vaishnav/Desktop/pycharm/mile_stone_project!/all_QR_code/{}.png".format(text))