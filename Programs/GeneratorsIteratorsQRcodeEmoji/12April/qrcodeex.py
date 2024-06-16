import qrcode

# generating a QR code using the make() function
qr_img = qrcode.make("Dear Students Course Completed-Best of Luck")
#qr_img = qrcode.make("https://www.google.com/")
# saving the image file
qr_img.save("qrimage2.jpg")
print("QR Code generated--verify")
