from typing import Any, List, Type
from concurrent.futures import ThreadPoolExecutor, as_completed
from nornir.plugins.runners import ThreadedRunner, SerialRunner
from nornir.core.task import Task, AggregatedResult
from nornir.core.inventory import Host
from tqdm import tqdm

class SerialProgressBarRunner(SerialRunner):
    """
    SerialProgressBarRunner runs the task over each host sequentially.
    Prints a cute progress bar.
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
        # Optional arguments are passed to tqdm
        self.args = args
        self.kwargs = kwargs
        self.desc = kwargs.pop('desc', False)

    def run(self, task: Task, hosts: List[Host]) -> AggregatedResult:
        result = AggregatedResult(task.name)
        for host in tqdm(hosts,*self.args,**self.kwargs):
            result[host.name] = task.copy().start(host)
        return result

class ThreadedProgressBarRunner(ThreadedRunner):
    """
    ThreadedProgressBarRunner runs the task over each host using threads.
    Prints a cute progress bar.
    Arguments:
        num_workers: number of threads to use
    """
    def __init__(self, num_workers: int = 20, **kwargs):
        super().__init__(num_workers)
        # Optional arguments are passed to tqdm
        self.kwargs = kwargs
        self.desc = kwargs.pop('desc', False)

    def run(self, task: Task, hosts: List[Host]) -> AggregatedResult:
        result = AggregatedResult(task.name)
        futures = []
        description = task.name if not self.desc else self.desc

        with ThreadPoolExecutor(self.num_workers) as pool:
            for host in hosts:
                future = pool.submit(task.copy().start, host)
                futures.append(future)

            for future in tqdm(as_completed(futures),
                               total=len(hosts),
                               desc=description, **self.kwargs):
                worker_result = future.result()
                result[worker_result.host.name] = worker_result

        return result
