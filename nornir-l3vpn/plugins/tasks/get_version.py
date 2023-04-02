from nornir.core.task import Task, Result

def show_version(task: Task, **kwargs) -> Result:
    """
        This task runs 'show version' on the target device and returns
        the output from the command.
    """

    # === Initializes a Netmiko (ssh) connection to the device
    connection = task.host.get_connection('netmiko', task.nornir.config)

    # === Sends show version command to device
    result_data = connection.send_command('show version', **kwargs)

    # === Returns execution results
    return Result(
        result=result_data,
        host=task.host,
        changed=False
    )
