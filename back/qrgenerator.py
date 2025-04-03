import qrcode
from qrcode.image.styledpil import StyledPilImage

import io

def generateqr(data: str):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(data)
    return qr

def createImage(qr, embeded_image = None) -> io.BytesIO:
    qrBytes = io.BytesIO()

    if(embeded_image is None):
        qr.make().save(qrBytes, format="PNG")
    else:
        qr.make_image(image_factory=StyledPilImage, embeded_image_path=embeded_image).save(qrBytes, format="PNG")

    return qrBytes


