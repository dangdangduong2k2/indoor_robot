from tkinter import *
from time import sleep
from PIL import ImageTk, Image
from time import sleep
import serial
import pyfirmata


def main():
	root =Tk()
	run = window(root)
class window:
	def __init__(self, root):

		#set bg

		self.root = root
		self.root.title('duong')
		self.root.geometry("%dx%d+%d+%d" % (500,750,(self.root.winfo_screenwidth())/2-(500/2),(self.root.winfo_screenheight())/2-(750/2)-40))
		self.root.resizable(False,False)
		self.imga= Image.open("D:\\mappp.png") 
		self.resize_imga= self.imga.resize((500,750),Image.ANTIALIAS) 
		self.imgb= ImageTk.PhotoImage(self.resize_imga)
		self.bg = Label(self.root, image=self.imgb).place(x=0,y=-32, relwidth=1,relheight=1)

		#set radiobt1

		self.r= IntVar()
		self.rdbt0= Radiobutton(master=self.root, text='0',variable=self.r,value=0,command=self.status).place(x=-100,y=-100)
		self.rdbt1= Radiobutton(master=self.root, text='1',variable=self.r,value=1,command=self.status).place(x=15,y=590)
		self.rdbt2= Radiobutton(master=self.root, text='2',variable=self.r,value=2,command=self.status).place(x=15,y=620)
		self.rdbt3= Radiobutton(master=self.root, text='3',variable=self.r,value=3,command=self.status).place(x=15,y=650)
		self.rdbt4= Radiobutton(master=self.root, text='4',variable=self.r,value=4,command=self.status	).place(x=15,y=680)

		#set radiobt2
		self.s= IntVar()
		self.rdbt00= Radiobutton(master=self.root, text='0',variable=self.s,value=0).place(x=-100,y=720)
		self.rdbt11= Radiobutton(master=self.root, text='1',variable=self.s,value=1).place(x=100,y=720)
		self.rdbt22= Radiobutton(master=self.root, text='2',variable=self.s,value=2).place(x=210,y=720)
		self.rdbt33= Radiobutton(master=self.root, text='3',variable=self.s,value=3).place(x=310,y=720)
		self.rdbt44= Radiobutton(master=self.root, text='4',variable=self.s,value=4).place(x=410,y=720)

		#set bt

		self.bt=Button(master=self.root, text='confirm',command=self.click).place(x=300,y=640)
		

		#set label

		self.Label=Label(self.root, text='Status',bg='white').place(x=20,y=720)

		# set sensor 

		self.board = pyfirmata.Arduino('COM5')
		self.it = pyfirmata.util.Iterator(self.board)
		self.it.start()
		self.inp1 = self.board.get_pin('d:8:i')
		self.inp2 = self.board.get_pin('d:9:i')
		self.inp3 = self.board.get_pin('d:10:i')
		self.inp4 = self.board.get_pin('d:11:i')

		self.com ="COM8"
		self.a=[1,2,3,4]
		self.buadrate = 9600
		self.robot =serial.Serial(self.com,self.buadrate)
	
		self.root.mainloop()

		
	def status(self):
		
		while True:
			self.signal1 = self.inp1.read()
			self.signal2 = self.inp2.read()
			self.signal3 = self.inp3.read()
			self.signal4 = self.inp4.read()
			if self.signal1 is False:
				self.s.set('1')
				break
			if self.signal2 is False:
				self.s.set('2')
				break
			if self.signal3 is False:
				self.s.set('3')
				break
			if self.signal4 is False:
				self.s.set('4')
				break
			else: 
				self.s.set('0')
				break

	def click(self):
		while True:
			self.signal1 = self.inp1.read()
			self.signal2 = self.inp2.read()
			self.signal3 = self.inp3.read()
			self.signal4 = self.inp4.read()
			if int(self.r.get()) in self.a :
				self.robot.write(b'n')
			if int(self.r.get()==1) and self.signal1 is False:
				self.r.set('1')
				self.robot.write(b's')
				break
			if int(self.r.get()==2) and self.signal2 is False:
				self.r.set('2')
				self.robot.write(b's')
				break
			if int(self.r.get()==3) and self.signal3 is False:
				self.r.set('3')
				self.robot.write(b's')
				break
			if int(self.r.get()==4) and self.signal4 is False:
				self.r.set('4')
				self.robot.write(b's')
				break
					

					
main()
		

