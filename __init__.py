from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.parse import extract_number
import socket

class SrSeedPlanter(MycroftSkill):
	def __init__(self):
		MycroftSkill.__init__(self)

	def initialize(self):
		self.log.exception("Something went wrong")

	@intent_file_handler('planter.seed.sr.intent')
	def handle_planter_seed_sr(self, message):
		numseeds = int(extract_number(message.data.get('numseeds')))
		numseeds = str(numseeds)
		numseeds = numseeds.encode(encoding='utf-8')
		HOST = "192.168.1.204"
		PORT = 8181

		try:
			toMotorPi = socket.socket(
			socket.AF_INET, socket.SOCK_STREAM
			)
			toMotorPi.connect((HOST, PORT))
			toMotorPi.send(numseeds)
			ifRecieved = toMotorPi.recv(1024)
			print("the Motor Pi recieved the message: {}".format(ifRecieved))
			numseeds = numseeds.decode('utf-8')
		except:
			self.log.exception("Something went wrong")
		else:
			self.speak_dialog('planter.seed.sr', data={
			'numseeds' : numseeds
			})

def create_skill():
    return SrSeedPlanter()
