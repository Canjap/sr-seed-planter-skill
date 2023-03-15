from mycroft import MycroftSkill, intent_file_handler

class SrSeedPlanter(MycroftSkill):
	def __init__(self):
		MycroftSkill.__init__(self)
		HOST = "192.168.1.203"
		PORT = 65329

	@intent_file_handler('planter.seed.sr.intent')
	def handle_planter_seed_sr(self, message):
		global numseeds
		numseeds = message.data.get('numseeds')
		self.speak_dialog('planter.seed.sr', data={
		'numseeds': numseeds
		})

	message = int(numseeds)
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


def create_skill():
    return SrSeedPlanter()

