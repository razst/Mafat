# import the necessary packages
from imutils.video import VideoStream
import imagezmq
import time

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5555

# initialize the ImageSender object with the socket address of the
# server
sender = imagezmq.ImageSender(connect_to="tcp://{}:{}".format(SERVER_IP,SERVER_PORT),REQ_REP=False)

vs = VideoStream(src=0).start()
time.sleep(2.0)
 
for i in range(1000):
# while True:
	# read the frame from the camera and send it to the server
	frame = vs.read()
	print("about to send")
	sender.send_image_pubsub("client 1", frame)
	print("sent")
sender.close()