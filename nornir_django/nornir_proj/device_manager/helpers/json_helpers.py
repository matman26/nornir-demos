from nornir.core.task import Result, MultiResult, AggregatedResult

def nornir_result_to_dict(results):
  out_dict = dict()
  if isinstance(results, Result):
    out_dict['changed'] = results.changed
    out_dict['failed']  = results.failed
    out_dict['host']    = results.host.name or ''
    out_dict['result']  = results.result or ''
    return out_dict

  elif isinstance(results, AggregatedResult):
    for host, hostresults in results.items():
      if isinstance(hostresults, MultiResult):
        res_list = []
        for res in hostresults:
          res_list.append(nornir_result_to_dict(res))
        out_dict[host] = res_list
      elif isinstance(hostresults, Result):
        out_dict[host] = nornir_result_to_dict(hostresults)

  return out_dict
