import time
from globals import Log 

class Executor: 
    def __init__ (self, step):
        self.step = step

    def execute(self, context):
        print(f"Executing: {self.step['name']}")
        start = time.time()
        try:
            # Logging the starting of the process
            Log.append({
                'status': 'started',
                'step': self.step['name'], 
                'timestamp': time.ctime()
                })
            
            #simulating process
            time.sleep(2)

            # update shared data
            context[self.step["name"]] = {"done": True}

        # Exception Handling
        except Exception as e:
            return {"status": "failed", "error":str(e)} 
        
        # Logging the final endpoint of the function
        else:
            Log.append({
                'status': 'completed',
                'step': self.step['name'], 
                'timestamp': time.ctime(),
                'duration': time.time() - start
            })
            return {"status": "success", "output": None}

class PrepExecutor():
    def __init__(self, step):
        self.step = step

    def execute(self, context):
        print(f"Preparing: {self.step['name']}")
        start = time.time()
        try:
            # Logging the starting of the process
            Log.append({
                'status': 'preparation started', 
                'step': self.step['name'], 
                'timestamp': time.ctime()
                })
            
            #simulating process
            time.sleep(2)

            # update shared data
            context[self.step["name"]] = {"done": True}
            
        # Exception handling
        except Exception as e:
            return {"status": "failed", "error": str(e)}
        
        # Logging the final endpoint of the function
        else:
            Log.append({
                'status': 'preparation completed', 
                'step': self.step['name'], 
                'timestamp': time.ctime(), 
                'duration': time.time() - start
            })
            return {"status": "success", "output": None}
            
class DevExecutor():
    def __init__(self, step):
        self.step = step

    def execute(self, context):
        print(f"Developing: {self.step['endgoal']}")
        start = time.time()
        try:
            # Logging the start of the program
            Log.append({
                'status': 'development started', 
                'step': self.step['name'], 
                'timestamp': time.ctime()
                })
            
            # simlating process
            time.sleep(2)
            
            # update shared data
            context[self.step["name"]] = {"done": True}
            
        except Exception as e:
            return {"status": "failed", "error": str(e)}
        else:
            Log.append({
                'status': 'development completed', 
                'step': self.step['name'], 
                'timestamp': time.ctime(),
                'duration': time.time() - start
            })
            return {"status": "success", "output": None}

class Logger:
    @staticmethod
    def get_log():
        return Log
    
    @staticmethod
    def append(entry):
        Log.append(entry)