
# -*- coding: utf-8 -*-

class Stats():
    """met a jour toutes les stats"""
    staticSynonymes=None
    def __init__(self, pb1, pb2, pb3, pb4):
            self.dictProgressBars = {"toeic":pb1,
                                     "qcm":pb2,
                                      "traduction":pb3,
                                     "toeic2":pb4}

    def initPb(self, string, max):
        self.dictProgressBars[string].setMaximum(max)

    def update(self, string, taux):
        self.dictProgressBars[string].setValue(taux)
        self.dictProgressBars[string].update()
