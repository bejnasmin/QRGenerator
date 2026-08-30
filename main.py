import pyqrcode 

url = input("enter url to generate qr code: ")

qr_code = pyqrcode.create(url)
qr_code.svg('qrcode.svg',scale = 5) #scale burda boyut Yani burada create() QR kodu oluşturuyor, svg() ise oluşturulan QR kodu bir görsel dosyasına kaydediyor.

