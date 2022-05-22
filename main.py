import tkinter as tk
from tkinter import ttk
import pyautogui
import os


def make_video():
    print("Make video")
    images = [img for img in os.listdir(os.getcwd()) if img.endswith(".png")]
    os.system("ffmpeg -f image2 -r " + str(tk.fps_input.get()) + " -i Frame%d.png -vcodec libx264 -crf 25 -pix_fmt yuv420p output.mp4")
    #delete the screenshots
    for i in range(0, 100):
        os.remove("Frame" + str(i) + ".png")

def start_recording():
    print("Start recording")
    tk.status_label.config(text="Status: Recording")
    for i in range(0, 100):
        #take a screenshot
        pyautogui.screenshot("Frame" + str(i) + ".png")
        i += 1
    make_video()
    

def stop_recording():
    print("Stop recording")
    tk.status_label.config(text="Status: Not recording")
    tk.window.destroy()

def create_window():
    tk.window = tk.Tk()
    tk.window.title("Python Screen Recorder")
    tk.window.geometry("400x400")
    tk.window.resizable(False, False)
    tk.window.configure(background="black")

    tk.label = tk.Label(tk.window, text="Python Screen Recorder", font=("Helvetica", 16), fg="white", bg="black")
    tk.label.pack()
    tk.fps_label = tk.Label(tk.window, text="Speed:", font=("Helvetica", 12), fg="white", bg="black")
    tk.fps_label.pack()
    tk.fps_input = tk.Entry(tk.window, width=5, font=("Helvetica", 12), fg="white", bg="black")
    tk.fps_input.pack()
    #add a start button and a stop button
    tk.start_button = tk.Button(tk.window, text="Start", font=("Helvetica", 12), fg="white", bg="black", command=start_recording)
    tk.start_button.pack()
    tk.stop_button = tk.Button(tk.window, text="Stop", font=("Helvetica", 12), fg="white", bg="black", command=stop_recording)
    tk.stop_button.pack()
    tk.status_label = tk.Label(tk.window, text="Status:", font=("Helvetica", 12), fg="white", bg="black")
    tk.status_label.pack()
    #show the window
    tk.window.mainloop()

create_window()