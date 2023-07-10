import qrcode
import qrcode.image.svg

# create qr code, chose colors and size and type of image file ?


def create_qr(qr_infos=None, back_col="white", fill_col="black") -> None:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_infos)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_col, back_color=back_col)
    img.save("test_image.png")  # Chose where to save ?


if __name__ == "__main__":
    create_qr("https://youtu.be/dQw4w9WgXcQ")
