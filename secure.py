import Tkinter as Tk
import os, datetime


root = Tk.Tk()
root.title("Enter pattern")
w,h= 300,300
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
pattern_list = []
times =0
day = datetime.datetime.today().weekday()
def secure():
	root.destroy()
	quit()
def unsecure() :
	global times
	for _ in range(len(pattern_list)):
		pattern_list.pop()
	times+=1
	if times>2:
		os.system("sudo su")
		os.system("poweroff")
	os.system("gnome-screensaver-command -l")
def check() :
	if day == 0 :
		if pattern_list == [2,1] :
			secure()
	elif day == 1 :
		if pattern_list == [2,1,2] :
			secure()
	elif day == 2 :
		if pattern_list == [2,1,2,6] :
			secure()
	elif day == 3 :
		if pattern_list == [2,1,2,6,8] :
			secure()
	elif day == 4 :
		if pattern_list == [2,1,2,6,8,7] :
			secure()
	elif day == 5 :
		if pattern_list == [2,1,2,6,8,7,4] :
			secure()
	elif day == 6 :
		if pattern_list == [2,1,2,6,8,7,4,5] :
			secure()
	if len(pattern_list)>10 :
		unsecure()



def bf1():
	pattern_list.append(1)
	check()
def bf2():
	pattern_list.append(2)
	check()
def bf3():
	pattern_list.append(3)
	check()
def bf4():
	pattern_list.append(4)
	check()
def bf5():
	pattern_list.append(5)
	check()
def bf6():
	pattern_list.append(6)
	check()
def bf7():
	pattern_list.append(7)
	check()
def bf8():
	pattern_list.append(8)
	check()
def bf9():
	pattern_list.append(9)
	check()

b1 = Tk.Button(root, justify =Tk.LEFT,command = bf1)
b1.config(width="100",height="100", activebackground = "SlateGray1")
b1.place(x=0,y=0)

b2 = Tk.Button(root, justify =Tk.LEFT,command = bf2)
b2.config(width="100",height="100", activebackground = "SlateGray1")
b2.place(x=100,y=0)

b3 = Tk.Button(root, justify =Tk.LEFT,command = bf3)
b3.config(width="100",height="100", activebackground = "SlateGray1")
b3.place(x=200,y=0)

b4 = Tk.Button(root, justify =Tk.LEFT,command = bf4)
b4.config(width="100",height="100", activebackground = "SlateGray1")
b4.place(x=0,y=100)

b5 = Tk.Button(root, justify =Tk.LEFT,command = bf5)
b5.config(width="100",height="100", activebackground = "SlateGray1")
b5.place(x=100,y=100)

b6 = Tk.Button(root, justify =Tk.LEFT,command = bf6)
b6.config(width="100",height="100", activebackground = "SlateGray1")
b6.place(x=200,y=100)

b7 = Tk.Button(root, justify =Tk.LEFT,command = bf7)
b7.config(width="100",height="100", activebackground = "SlateGray1")
b7.place(x=0,y=200)

b8 = Tk.Button(root, justify =Tk.LEFT,command = bf8)
b8.config(width="100",height="100", activebackground = "SlateGray1")
b8.place(x=100,y=200)

b9 = Tk.Button(root, justify =Tk.LEFT,command = bf9)
b9.config(width="100",height="100", activebackground = "SlateGray1")
b9.place(x=200,y=200)

root.mainloop()
