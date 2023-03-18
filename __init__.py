from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.parse import extract_number
import socket

class SrSeedPlanter(MycroftSkill):
	def __init__(self):
		MycroftSkill.__init__(self)

	@intent_file_handler('planter.seed.sr.intent')
	def handle_planter_seed_sr(self, message):
		numseeds = int(extract_number(message.data.get('numseeds')))

		HOST = "192.168.1.204"
		PORT = 8181

		try:
			toMotorPi = socket.socket(
			socket.AF_INET, socket.SOCK_STREAM
			)
			toMotorPi.connect((HOST, PORT))
			toMotorPi.send(message)
			ifRecieved = toMotorPi.recv(1024)
			print("the Motor Pi recieved the message: {}".format(ifRecieved))
		except Exception as e:
			print(e)
		else:
			self.speak_dialog('planter.seed.sr', data={
			'numseeds' : numseeds
			})

def create_skill():
    return SrSeedPlanter()
