import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

gpio.setup(17,gpio.OUT)
gpio.setup(22,gpio.IN)

while True:
	if gpio.input(22) == False:
		gpio.output(17,gpio.HIGH)
		print(":)")
	else:
		gpio.output(17,gpio.LOW)
		print(":(")