import qrcode

item = input('input item: ')
img = qrcode.make(item)

img.save('your_own_qrcode.png')