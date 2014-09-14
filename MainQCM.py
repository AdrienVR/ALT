
class MainQCM():
    def __init__(self,  conteneur=None):
        self.conteneur = conteneur
        self.answerButton = {"A":self.conteneur.pushButtonRep1,
                             "B":self.conteneur.pushButtonRep2,
                             "C":self.conteneur.pushButtonRep3,
                             "D":self.conteneur.pushButtonRep4}

    def normaliseSentence(self, text):
        text=text.strip()
        return text

    def setQCM(qcm):
        self.conteneur.labelQuestion = qcm.question

        for a in "ABCD":
            self.answerButton[a].setText(a+" : "+qcm.getAnswer(a))