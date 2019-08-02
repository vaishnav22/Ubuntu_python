import qrcode
from PIL import Image

text = input("Enter your name : \n")
blood = input('Enter the Blood Group:\n')
img = qrcode.make(str(text)+str(blood))
img.save("/home/vaishnav/Desktop/pycharm/mile_stone_project!/all_QR_code/{}.png".format(text))

img.show("/home/vaishnav/Desktop/pycharm/mile_stone_project!/all_QR_code/{}.png".format(text))