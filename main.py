import pytesseract
from PIL import Image
from requests import get
from shutil import copyfileobj
import tkinter as tk


def image_to_text(file_name):
    image = Image.open(file_name)
    text = pytesseract.image_to_string(image)
    save_to_file(file_name, text)


def save_to_file(name, text):
    file_name = name.split('.')[0]
    save_path = file_name + '.txt'
    with open(save_path, 'w') as f:
        f.write(text)


def get_img(url):
    res = get(url, stream=True)
    file_name = url.split('/')[-1]
    if res.status_code == 200:
        download_path = file_name
        with open(download_path, 'wb') as f:
            copyfileobj(res.raw, f)
            image_to_text(download_path)


def main_tk():
    root = tk.Tk()
    root.title('Image to Text')
    root.geometry('200x200')
    label = tk.Label(root, text="Type the image name: ")
    label.pack()
    entry = tk.Entry(root)
    entry.pack()
    button = tk.Button(
        text="Convert",
        width=18,
        height=1,
        bg="blue",
        fg="white",
        command=lambda: image_to_text(entry.get())
    )
    button.pack()
    label2 = tk.Label(root, text="Or Type the image url: ")
    label2.pack()
    entry2 = tk.Entry(root)
    entry2.pack()
    button = tk.Button(
        text="Download and Convert",
        width=18,
        height=1,
        bg="blue",
        fg="white",
        command=lambda: get_img(entry2.get())
    )
    button.pack()
    root.mainloop()



if __name__ == "__main__":
    main_tk()

