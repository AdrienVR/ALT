
class Questionnaire():
    def __init__(self):
        self.question = ""
        self.answers = {}

    def getAnswer(self, a):
        return self.answers[a]