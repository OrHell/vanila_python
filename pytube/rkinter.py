from tkinter import *
root=Tk()
root.withdraw()
txt=Text()
txt.pack()

l=Toplevel()
l.geometry('+200+200')
l.overrideredirect(1)
Label(l,text='Программа запускается\n, терпение, только терпение').pack()


def start():
	root.deiconify()
	l.destroy()
	

root.after(2000,start)

root.mainloop()