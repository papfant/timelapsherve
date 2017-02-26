from picamera import PiCamera
from time import sleep
from time import time
from time import localtime
from time import strftime
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-a", "--shut", dest = "shut", help = "if a = 1, shutdown a fter picture")
(options, args) = parser.parse_args()


def shutdownpi():
    command = "/usr/bin/sudo /sbin/shutdown -h 1"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output
sleep(60)
if localtime()[3] == 12:
	with PiCamera() as camera:
		camera.resolution = (2592,1944)
		camera.framerate = 15
		sleep(5)
		print('Ready to capture')
		camera.capture('/home/pi/TimeLapseHerve/image' + strftime('%Y-%m-%d_%H%M%S') + '.jpg')
else:
	print('Wait ... Thats not the good time now ...')
	with PiCamera() as camera:
		camera.resolution = (2592,1944)
		camera.framerate = 15
		sleep(5)
		print('Ready to capture')
		camera.capture('/home/pi/TimeLapseHerve/image' + strftime('%Y-%m-%d_%H%M%S') + '.jpg')
	#sleep(294)	
if options.shut:
	sleep(60)
	shutdownpi()
	print('Ive send the signal to nap')
