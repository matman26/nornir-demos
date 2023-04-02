from nornir.core.task import Task, Result, AggregatedResult, MultiResult
from device_manager.helpers.json_helpers import nornir_result_to_dict
from task_manager.models import ExecutionResults
from task_manager.models import ExecutionEvents
from nornir.core.processor import Processor
from nornir.core.inventory import Host
import json

class DjangoEventProcessor(Processor):
    def task_started(self, task: Task) -> None:
        """
        This method is called right before starting the task
        """
        print(f"EventProcessor: Right before starting task {task.name}")

    def task_completed(self, task: Task, result: AggregatedResult) -> None:
        """
        This method is called when all the hosts have completed executing their respective task
        """
        print(f"EventProcessor: Finished task on host {task.name}")

    def task_instance_started(self, task: Task, host: Host) -> None:
        """
        This method is called before a host starts executing its instance of the task
        """
        pass

    def task_instance_completed(
        self, task: Task, host: Host, result: MultiResult
    ) -> None:
        """
        This method is called when a host completes its instance of a task
        """
        pass

    def subtask_instance_started(self, task: Task, host: Host) -> None:
        """
        This method is called before a host starts executing a subtask
        """
        pass

    def subtask_instance_completed(
        self, task: Task, host: Host, result: MultiResult
    ) -> None:
        """
        This method is called when a host completes executing a subtask
        """
        pass

class DjangoResultProcessor(Processor):
    def task_started(self, task: Task) -> None:
        """
        This method is called right before starting the task
        """
        pass

    def task_completed(self, task: Task, result: AggregatedResult) -> None:
        """
        This method is called when all the hosts have completed executing their respective task
        """
        print(f"ResultProcessor: Finished task {task.name}")
        results_dict = nornir_result_to_dict(result)
        print(f"ResultProcessor: Recording execution results {results_dict}")
        res = ExecutionResults(
            name=task.name,
            hosts=','.join(results_dict.keys()),
            results=json.dumps(results_dict),
        )
        res.save()
        print(f"ResultProcessor: Recorded execution results")

    def task_instance_started(self, task: Task, host: Host) -> None:
        """
        This method is called before a host starts executing its instance of the task
        """
        pass

    def task_instance_completed(
        self, task: Task, host: Host, result: MultiResult
    ) -> None:
        """
        This method is called when a host completes its instance of a task
        """
        pass

    def subtask_instance_started(self, task: Task, host: Host) -> None:
        """
        This method is called before a host starts executing a subtask
        """
        pass

    def subtask_instance_completed(
        self, task: Task, host: Host, result: MultiResult
    ) -> None:
        """
        This method is called when a host completes executing a subtask
        """
        pass
