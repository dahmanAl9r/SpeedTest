from speedtest import Speedtest
from tkinter import *
from tkinter import ttk
import threading
import time

root = Tk()

root.title("Internet speed test")
root.resizable(False,False)
root.geometry("450x300")
root.config(bg='white')

def DownloadSpeed():
	while True:
		try:
			global d_ko
			internet = Speedtest()

			d_mb = round(internet.download()/(1024*1024),2)
			Download.Speed_mb.config(text=d_mb)

			d_ko = float(d_mb*125)
			Download.Speed_ko.config(text=d_ko)

			d_mo = int(d_ko/1000)

			d_o = int(d_ko*1000)

			if d_ko >= 1000:
				Download.Speed_mo_o.config(text=d_mo)
				Download.Mo.config(text='Mo/s')

			if d_ko < 1000:
				Download.Speed_mo_o.config(text=d_o)
				Download.Mo.config(text='Octets/s')
			time.sleep(0.01)
		except:
			pass

def DoDownloadSpeed():
	try:
		threading.Thread(target=DownloadSpeed).start()
	except threading.ThreadError:
		pass

def UploadSpeed():
	while True:
		try:
			time.sleep(0.01)
			internet = Speedtest()

			u_mb = round(internet.upload()/(1024*1024),2)
			Upload.Speed_mb.config(text=u_mb)

			u_ko = int(u_mb*125)
			Upload.Speed_ko.config(text=u_ko)

			u_mo = int(u_ko/1000)

			u_o = int(u_ko*1000)

			if u_ko > 1000:
				Upload.Speed_mo.config(text=u_mo)
				Upload.Mo.config(text='Mo/s')

			if u_ko < 1000:
				Upload.Speed_mo.config(text=u_o)
				Upload.Mo.config(text='Octets/s')
		except:
			pass

def DoUploadSpeed():
	try:
		threading.Thread(target=UploadSpeed).start()
	except threading.ThreadError:
		pass

def Pings():
	while True:
		try:
			time.sleep(0.1)
			internet = Speedtest()

			internet.get_servers()
			best_server = internet.get_best_server()

			ping = internet.results.ping
			# print(p)

			Ping.ping.config(text=f"{ping:.2f}")
		except:
			pass

def DoPings():
	try:
		threading.Thread(target=Pings).start()
	except threading.ThreadError:
		pass


notebook = ttk.Notebook(root)

downloadspeed = Frame(notebook)
uploadspeed = Frame(notebook)
pingspeed = Frame(notebook)

notebook.add(downloadspeed,text='DownloadSpeed')
notebook.add(uploadspeed,text='UploadSpeed')
notebook.add(pingspeed,text='PingSpeed')


class Download():
	DownloadTitle = Label(downloadspeed,text='DownloadSpeed',fg='white',bg='#333',height=1,font=("Calibri",15))
	DownloadTitle.pack(fill=X)

	Space1 = Frame(downloadspeed,bg='whitesmoke',relief=SOLID,bd=1)
	Space1.place(x=10,y=40,width=430,height=225)

	Speed_mb = Label(Space1,fg='black',text="0.00",bg='whitesmoke',height=1,font=("Calibri",18))
	Speed_mb.place(x=150,y=10)
	Mpbs = Label(Space1,fg='black',text="MBPS",bg='whitesmoke',height=1,font=("Calibri",18))
	Mpbs.place(x=400-180,y=10)

	dahman = False

	Speed_ko = Label(Space1,fg='black',text="00",bg='whitesmoke',height=1,font=("Calibri",18))
	Speed_ko.place(x=150,y=50)
	Ko = Label(Space1,fg='black',text="Ko/s",bg='whitesmoke',height=1,font=("Calibri",18))
	Ko.place(x=420-180,y=50)

	Speed_mo_o = Label(Space1,fg='black',text="00",bg='whitesmoke',height=1,font=("Calibri",18))
	Speed_mo_o.place(x=150,y=90)
	Mo = Label(Space1,fg='black',text="Octets/s",bg='whitesmoke',height=1,font=("Calibri",18))
	Mo.place(x=440-180,y=90)
	
	GetDownloadSpeed = Button(Space1,text='Start',fg='white',bg='#333',relief=SOLID,bd=1,font=("Calibri",15),cursor="hand2",command=DoDownloadSpeed)
	GetDownloadSpeed.place(x=10,y=145,width=410,height=70)

class Upload():
	UploadTitle = Label(uploadspeed,text='UploadSpeed',fg='white',bg='#537188',height=1,font=("Calibri",15))
	UploadTitle.pack(fill=X)

	Space2 = Frame(uploadspeed,bg='whitesmoke',relief=SOLID,bd=1)
	Space2.place(x=10,y=40,width=430,height=225)

	Speed_mb = Label(Space2,fg='black',text="0.00",bg='whitesmoke',height=1,font=("Calibri",18))
	Speed_mb.place(x=150,y=10)
	Mpbs = Label(Space2,fg='black',text="MBPS",bg='whitesmoke',height=1,font=("Calibri",18))
	Mpbs.place(x=400-180,y=10)

	Speed_ko = Label(Space2,fg='black',text="00",bg='whitesmoke',height=1,font=("Calibri",18))
	Speed_ko.place(x=150,y=50)
	Ko = Label(Space2,fg='black',text="Ko/s",bg='whitesmoke',height=1,font=("Calibri",18))
	Ko.place(x=420-180,y=50)

	Speed_mo = Label(Space2,fg='black',text="00",bg='whitesmoke',height=1,font=("Calibri",18))
	Speed_mo.place(x=150,y=90)
	Mo = Label(Space2,fg='black',text="Mo/s",bg='whitesmoke',height=1,font=("Calibri",18))
	Mo.place(x=440-180,y=90)

	GetUploadSpeed = Button(Space2,text='Start',fg='white',bg='#537188',relief=SOLID,bd=1,font=("Calibri",15),cursor="hand2",command=DoUploadSpeed)
	GetUploadSpeed.place(x=10,y=145,width=410,height=70)

class Ping():
	PingTitle = Label(pingspeed,text='PingSpeed',fg='white',bg='#4C4C6D',height=1,font=("Calibri",15))
	PingTitle.pack(fill=X)

	Space3 = Frame(pingspeed,bg='whitesmoke',relief=SOLID,bd=1)
	Space3.place(x=10,y=40,width=430,height=225)

	ping = Label(Space3,fg='black',text="00",bg='whitesmoke',height=1,font=("Calibri",18))
	ping.place(x=150,y=65)

	Ms = Label(Space3,fg='black',text="Ms",bg='whitesmoke',height=1,font=("Calibri",18))
	Ms.place(x=420-180,y=65)

	GetPing = Button(Space3,text='Start',fg='white',bg='#4C4C6D',relief=SOLID,bd=1,font=("Calibri",15),cursor="hand2",command=DoPings)
	GetPing.place(x=10,y=145,width=410,height=70)
notebook.pack(expand=True,fill="both")

root.mainloop()