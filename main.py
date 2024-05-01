import customtkinter
from pytube import YouTube
from tkinter import filedialog
import time
import pyautogui

def past():
    pyautogui.hotkey('ctrl', 'v')

def start_dow():
    try:
        yt_link = url_var.get()
        ytobj = YouTube(yt_link, on_progress_callback=on_progress)

        video = ytobj.streams.filter(res='720p').first()
        save_path = folder_path
        video.download(output_path=save_path)
    except Exception as e:
        fin.configure(text="YouTube URL is invalid.", text_color='red')
    else:
        fin.configure(text="Download complete", text_color='green')

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = bytes_downloaded / total_size * 100
    per = str(int(percent))
    progress.configure(text=per + '%')
    progressBar.set(percent)  # Update progress bar value

    # Calculate download speed
    global start_time, prev_bytes_downloaded
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time > 0:
        download_speed = (bytes_downloaded - prev_bytes_downloaded) / elapsed_time / 1024  # Convert bytes to KB
        speed_label.configure(text=f"Speed: {download_speed:.2f} KB/s")
    start_time = current_time
    prev_bytes_downloaded = bytes_downloaded

def browse_destination():
    global folder_path
    folder_path = filedialog.askdirectory()

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry('480x360')
app.title('Anuprash_Downloader')
app.iconbitmap('icon.ico')


title = customtkinter.CTkLabel(app, text='Enter Link')
title.pack(padx=10, pady=10)

url_var = customtkinter.StringVar()

link = customtkinter.CTkEntry(app, width=350, textvariable=url_var)
link.pack()

fin = customtkinter.CTkLabel(app, text="")
fin.pack()

progress = customtkinter.CTkLabel(app, text="0%")
progress.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

speed_label = customtkinter.CTkLabel(app, text="Speed: 0 KB/s")
speed_label.pack()

dow_button = customtkinter.CTkButton(app, text="Download 720p", command=start_dow)
dow_button.pack(padx=10, pady=10)

dow_button1 = customtkinter.CTkButton(app, text="Browse", command=browse_destination)
dow_button1.pack(padx=10, pady=10)

dow_button2 = customtkinter.CTkButton(app, text="paste", width=3, height=2, fg_color="red", command=past)
dow_button2.place(x=420, y=52.5)

start_time = time.time()
prev_bytes_downloaded = 0

app.mainloop()
