from executor import Executor, PrepExecutor, DevExecutor, Logger
import json

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

    def run(self):
        for step in self.workflow['steps']:
            executor_class = EXECUTOR_MAP[step["type"]]
            result = executor_class(step)
            result.execute()
        print("Execution completed.")

if __name__ == "__main__":
    Task = Orchestrator("workflow.json")
    Task.run()

    with open("logs.txt", "w") as file:
        for i, log_entry in enumerate(Logger.get_log()):
            file.write(f"{i+1}: {log_entry}\n")