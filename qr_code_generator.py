import qrcode


class QRCodeGenerator:
    def __init__(self, data):
        self.data = data

    def generate(self):
        qr_code = qrcode.QRCode(version=1, box_size=10, border=5)
        qr_code.add_data(self.data)
        qr_code.make(fit=True)
        qr_code.print_ascii()
        img = qr_code.make_image(fill='black', back_color='white')
        img.save('output/qrcode.png')
