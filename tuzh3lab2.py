import Tkinter
import pyfirmata
From time import sleep
def onStartButtonPress():
	startbutton.config(state=Tkinter.DISABLED)
	ledPin(1).write(1)
	ledPin(2).write(1)
	sleep(1)
	ledPin(1).write(0)
	ledPin(2).write(0)
	startbutton.config(state=Tkinter.ACTIVE)
port = ‘COM6’
board = pyfirmata.Arduino(port)
sleep(5)
ledPin1 = board.get_pin(‘d:11:o’)
ledPin2 = board.get_pin(‘d:10:o’)
top = Tkinter.Tk()
top.title(“Blink Led using button”)
top.minsize(300,30)
startButton = Tkinter.Button(top,
			     text=”Start”
			     command=onStartButtonPress)
startButton.pack()
top.mainloop()
