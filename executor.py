import time

Log = []

class Executor: 
    def __init__ (self, step):
        self.step = step

    def execute(self):
        print(f"Executing: {self.step['name']}")
        Log.append({'step': self.step['name'], 'status': 'started'})
        time.sleep(2)
        Log.append({'step': self.step['name'], 'status': 'completed'})

class PrepExecutor():
    def __init__(self, step):
        self.step = step

    def execute(self):
        print(f"Preparing: {self.step['name']}")
        Log.append({'step': self.step['name'], 'status': 'preparation started'})
        time.sleep(2)
        Log.append({'step': self.step['name'], 'status': 'preparation completed'})
        
class DevExecutor():
    def __init__(self, step):
        self.step = step

    def execute(self):
        print(f"Developing: {self.step['endgoal']}")
        Log.append({'step': self.step['name'], 'status': 'development started'})
        time.sleep(2)
        Log.append({'step': self.step['name'], 'status': 'development completed'})

class Logger:
    @staticmethod
    def get_log():
        return Log