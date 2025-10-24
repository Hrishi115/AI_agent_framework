import json
from executor import Executor, PrepExecutor, DevExecutor, Logger
import time


EXECUTOR_MAP = {
    'none' : Executor,
    'preparation': PrepExecutor,
    'development': DevExecutor,
}

class Orchestrator: 
    def __init__ (self, workflow_path):
        with open(workflow_path) as f:
            workflow = json.load(f)
        self.workflow = workflow

    def _validate(self, workflow):
        required_keys = ["name", "type"]
        for step in self.workflow['steps']:
            for key in required_keys:
                if key not in step:
                    raise ValueError(f"Step missing required key: {key}")


    def run(self):
        self._validate(self.workflow)
        context = {}
        for step in self.workflow['steps']:
            start = time.time()
            try:
                executor_class = EXECUTOR_MAP[step["type"]]
                if executor_class is None:
                    raise KeyError(f"Unknown step type: {step.get("type")}")
                result = executor_class(step)
                result = result.execute(context)
                duration = time.time() - start

                Logger.append({
                    "step": step.get("name"),
                    "type": step.get("type"),
                    "status": result.get("status", "unknown"),
                    "duration": duration,
                    "timestamp": time.ctime(),
                    "error": result.get("error")
                })
            except Exception as e:
                print(f"Executor error for step {step['name']}: {e}")
                Logger.append({
                    "step": step.get("name"),
                    "type": step.get("type"),
                    "status": result.get("failed"),
                    "duration": duration,
                    "timestamp": time.ctime(),
                    "error": str(e)
                })
                break
        else:
            print("Execution completed.")

if __name__ == "__main__":
    Task = Orchestrator("workflow.json")
    Task.run()

    with open("logs.txt", "w") as file:
        for log_entry in (Logger.get_log()):
            file.write(f"{log_entry}\n")