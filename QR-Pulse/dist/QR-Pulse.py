import qrcode
import os
import pathlib
from shutil import move

def generate_qr_code(url, output_file):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    image.save(output_file)
print("""

█▀▀▀▀▀█ ▄█ ▄▄ ▀█▀ █▀▀▀▀▀█
█ ███ █ ▄█▀█  ██  █ ███ █
█ ▀▀▀ █ ▄ █ ▀▄▀▄  █ ▀▀▀ █
▀▀▀▀▀▀▀ ▀ ▀ █ ▀ ▀ ▀▀▀▀▀▀▀
▀██▀█▄▀███▀ ▀█ ▀██ █ █ █ 
 ▄▀█▀▄▀ ██▄█▀ ███▀██ ▀▀██
▄▄  ▀ ▀▀ ▀▄▀█ █▀▄▀▀█▀█▀▀▀
█ ▄▀██▀██▀▀▄▀  ▀▀▄▄█▀ ▀██
▀ ▀▀  ▀ ▄▄ ██▀█▀█▀▀▀███▀▄
█▀▀▀▀▀█ ▀▀█   █ █ ▀ █▄ ▀▀
█ ███ █ █  ▄▀█▀▀▀██▀██▀▄▄
█ ▀▀▀ █ █ ▀▄▄ ▀██▄   ▀  █
▀▀▀▀▀▀▀ ▀▀▀  ▀▀   ▀▀ ▀▀▀▀

""")
# URL
urlx = input("Entrez l'url à convertir : ")
url = [urlx]

# Chemin de sortie sur le bureau
output_file_prefix = "QRcode"
output_dir = os.path.join(pathlib.Path.home(), "Desktop")
current_version = 1

while os.path.exists(os.path.join(output_dir, f"{output_file_prefix}{current_version}.png")):
    current_version += 1

output_file = os.path.join(output_dir, f"{output_file_prefix}{current_version}.png")

generate_qr_code(url, output_file)
print(f"QR code généré avec succès. Chemin de sortie : {output_file}.")
input("Appuyez sur la touche Entrée pour quitter le script. ")
exit()