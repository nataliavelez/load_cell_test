from time import sleep, clock
import datetime
import serial

### Set output filename ###
# Get condition label
# 1: Weak succeeds
# 2: Weak fails
# 3: Strong succeeds
# 4: Strong fails
# 5: DEBUG

condition_names = ["weakY", "weakN", "strongY", "strongN", "debug"]
condition_in = input("Welcome! What condition are you running?\n1 - Weak succeeds\n2 - Weak fails\n3 - Strong succeeds\n4 - Strong fails\n5 - Debug\n>> ")
try:
	condition_no = int(condition_in)
	condition = condition_names[condition_no - 1]
except ValueError:
	# If value is not an integer, use as a custom label
	condition = condition_in

ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
fname = "data/%s_%s.tsv" % (condition, ts)


### Read data from Arduino ###
port="/dev/tty.usbserial-AD02CRLB"
ser=serial.Serial(port,9600)
ser.baudrate=9600

print("Taring...")
ser.write(str.encode("x"))
sleep(2.)

print("Saving data to: %s" % fname)

try:
	with open(fname, "wb") as file:
		header="time\tforce\tcalibration\n"
		file.write(str.encode(header))
		read_ser = ser.readline() # Toss out first line
		while True:
			read_ser = ser.readline()
			file.write(read_ser)

except KeyboardInterrupt:
	print("Goodbye!")
