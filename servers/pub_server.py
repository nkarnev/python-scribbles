import zmq
import random
import sys
import time

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)
while True:
    topic = "TEST_TOPIC"  # random.randrange(9999,10005)
    messagedata = random.randrange(1, 215)
    print("{} : {}".format(topic, messagedata))
    socket.send_string("%s %d" % (topic, messagedata))
    time.sleep(1)
