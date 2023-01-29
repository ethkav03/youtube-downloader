from pytube import YouTube
from PIL import Image, ImageTk
import tkinter as tk

def Download(link):
    try:
        video = YouTube(link)
        print("Attempting to download YouTube video title: {}".format(video.title))
        stream = video.streams.get_highest_resolution()
        video = stream.download()
        print("YouTube Video Successfully Downloaded!")
    except:
        print("Failed to download YouTube video.")

def main():
    window = tk.Tk()
    window.title("YouTube Video Downloader")

    canvas = tk.Canvas(height=600, width=800)
    canvas.grid(columnspan=3, rowspan=4)

    # youtube downloader logo
    logo = Image.open("images/ytlogo.png")
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(window, image=logo)
    logo_label.image = logo
    logo_label.grid(column=1, row=0)

    # link input
    text = tk.Label(window, text="Insert YouTube video link:")
    text.grid(column=1, row=1)
    input_box = tk.Entry(window, width=50)
    input_box.grid(column=1, row=2)

    # download button
    download = tk.Button(
        window,
        text="Download",
        width=20, height=3,
        bg="red", fg="white",
        command=lambda:Download(input_box.get())
    )
    download.grid(column=1, row=3)

    window.mainloop()


if __name__ == "__main__":
    main()