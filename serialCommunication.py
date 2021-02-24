import serial, time
arduinoCom = serial.Serial('COM9', 115200, timeout=.1)
time.sleep(1) #give the connection a second to settle
while True:
	val=input('Enter a value: ')
	if val=='1':
		print('LED is on')
	elif val=='2':
		print("Fan is on")
	elif val=='0':
		print("Fan is off")
	else:
		print("LED is off")
	print(str.encode(val))
	arduinoCom.write(str.encode(val))