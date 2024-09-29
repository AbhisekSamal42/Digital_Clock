import tkinter
import time
def updateTime():
    currentTime = time.strftime("%H:%M:%S")
    clock_label.config(text = currentTime)
    clock_label.after(1000,updateTime)
root = tkinter.Tk()
root.title("Digital Clock")
clock_label = tkinter.Label(root,font = ('calibri',40,'bold'),background ='green',foreground='blue')
clock_label.pack(anchor='center')
updateTime()
root.mainloop()
