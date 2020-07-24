import serial
Import pyfirmata
From time import sleep
	    Pin= 13
	    Port = ‘dev/ttyACM0’
	    Board = pyfirmata.Arduino(port)
	    Board.digital[pin].write(1)
	    Sleep(1)
	    Board = pyfirmata.Arduino(port)
	    Sleep(0)
            Board = pyfirmata.Arduino(port)
	    Board.digital[pin].write(1)
	    Sleep(1)
	    Board = pyfirmata.Arduino(port)
	    Sleep(0)
            Board = pyfirmata.Arduino(port)
	    Board.digital[pin].write(1)
	    Sleep(1)
	    Board = pyfirmata.Arduino(port)
	    Sleep(0)
