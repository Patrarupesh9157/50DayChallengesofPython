import qrcode
import random
import string
result_str = ''.join(random.choice(string.ascii_letters) for i in range(5))

data = input('Enter any Valuable things to make qr:')

qr_img = qrcode.make(data)
print(f'Your file name is: {result_str}.jpg')
qr_img.save(f"{result_str}.jpg") 