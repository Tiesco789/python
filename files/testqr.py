import qrcode

texto = input("Digite o texto para gerar o QR Code: ")

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(texto)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")
