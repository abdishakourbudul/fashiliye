from tkinter import Tk, Label, Button, filedialog
import cv2
from PIL import Image, ImageTk


def qr_code_read(image_path):
    image = cv2.imread(image_path)
    if image is None:
        result_label.config(text="no image found")
        return
    detector = cv2.QRCodeDetector()
    data, point, _ = detector.detectAndDecode(image)

    if data:
        result_label.config(text="your data is : " + data)
    else:
        result_label.config(text="no data ")


def select_file():
    file_path = filedialog.askopenfilename(
        title="select file",
        filetypes=[("image_file", "*.png; *.jpeg; *.jpg")])

    if file_path:
        img = Image.open(file_path)
        img = img.resize((150, 150))
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo

        qr_code_read(file_path)


window = Tk()
window.title("fashiliye")
window.geometry("300x250")

label = Label(window, text="scan every qr code",
              font=("Arial, 14"), ).pack(pady=20)
button = Button(window, text="scan", bg="blue",
                fg="white",  command=select_file)
button.pack(padx=20)

result_label = Label(window, text="", font=("Arial, 9"))
result_label.pack(pady=10)

image_label = Label(window)
image_label.pack(pady=10)

window.mainloop()
