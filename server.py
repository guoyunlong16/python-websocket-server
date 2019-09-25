import time
from websocket_server import WebsocketServer

# Called for every client connecting (after handshake)
def new_client(client, server):
	print("New client connected and was given id %d" % client['id'])
	#server.send_message_to_all("Hey all, a new client has joined us")
        short_message = ""
        middle_message = ""
        long_message = ""
        with open("hamlet.txt") as f:
            short_message=f.read()
        with open("xiangcunjiaoshi_liucixin.txt") as f:
            middle_message=f.read()
        with open("theLongestDayInChangAn.txt") as f:
           long_message=f.read() 
        send_message(client, server, short_message)
        send_message(client, server, middle_message)
        send_message(client, server, long_message)

def send_message(client, server, message):
        t_end = time.time() + 10
        count = 1
        while time.time() < t_end:
	    server.send_message(client, message)
            count += 1
            time.sleep(5)
    
# Called for every client disconnecting
def client_left(client, server):
        print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
	if len(message) > 200:
		message = message[:200]+'..'
	print("Client(%d) said: %s" % (client['id'], message))


PORT=80
HOST='0.0.0.0'
server = WebsocketServer(PORT, host=HOST)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
