from nornir.core.task import Task, Result
from ttp import ttp

cdp_entry_template = """
<group name="{{neighbor_name}}">
Device ID: {{ neighbor_name }}
  IP address: {{ neighbor_address }}
Platform: {{ platform_string | ORPHRASE }},  Capabilities: {{ device_capabilities | ORPHRASE }}
</group>
"""

def map_neighbors(task: Task, *args, **kwargs) -> Result:
    """Uses CDP to grab neighbor data and return result as dictionary."""
    net_connect = task.host.get_connection('netmiko', task.nornir.config)
    result_data = net_connect.send_command('show cdp neighbors detail', **kwargs)
    parser = ttp(data=result_data,template=cdp_entry_template)
    parser.parse()
    results = parser.result(format='raw')[0][0]

    return Result(
        result=results,
        changed=False,
        host=task.host)
