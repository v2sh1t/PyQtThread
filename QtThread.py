from time import time

from PySide2.QtCore import QThread, Signal


class WorkThread(QThread):
    trigger = Signal(str)

    def __init__(self, sec: int = None):
        super(WorkThread, self).__init__()
        self.sec = sec

    def run(self):
        time.sleep(self.sec)
        # time.sleep(60)
        self.trigger.emit('enable')
