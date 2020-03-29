import tkinter
import random

def click_btn():
    label["text"]=random.choice(["大吉です!!^_^", "中吉です^_^", "小吉です!", "凶です(涙)"])
    label.update()

root = tkinter.Tk()
root.title("誰でもおみくじソフト")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="fortune_image.png")
canvas.create_image(400, 300, image=gazou)
label = tkinter.Label(root, text="何がでる？", font=("Times New Roman", 80), bg="white")
label.place(x=190, y=150)
button = tkinter.Button(root, text="おみくじを引く", font=("Times New Roman", 60), command=click_btn, fg="skyblue")
button.place(x=165, y=370)
root.mainloop()
