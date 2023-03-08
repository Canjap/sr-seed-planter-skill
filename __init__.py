from mycroft import MycroftSkill, intent_file_handler


class SrSeedPlanter(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('planter.seed.sr.intent')
    def handle_planter_seed_sr(self, message):
        numseeds = message.data.get('numseeds')

        self.speak_dialog('planter.seed.sr', data={
            'numseeds': numseeds
        })


def create_skill():
    return SrSeedPlanter()

