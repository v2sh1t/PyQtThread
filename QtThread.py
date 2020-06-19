from time import time

from PySide2.QtCore import QThread, Signal


class WorkThread(QThread):
    trigger = Signal(str)

    def __init__(self):
        super(WorkThread, self).__init__()

    def run(self):
        time.sleep(1800)
        # time.sleep(60)
        self.trigger.emit('enable')