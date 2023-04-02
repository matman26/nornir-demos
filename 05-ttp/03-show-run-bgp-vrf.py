#!/usr/bin/python3
from ttp import ttp
from pprint import pprint

data = """
router bgp 65213
 vrf 3G_RANSHARING
  rd 65213:1234
  label mode per-ce
  address-family ipv4 unicast
  !
  neighbor 10.5.6.2
   password abc12345
   remote-as 12345
   shutdown
   description 3G_DATA
   address-family ipv4 unicast
    send-community-ebgp
    route-policy DROP-ALL in
    route-policy DROP-ALL out
    remove-private-AS
    soft-reconfiguration inbound
   !
  !
  neighbor 10.2.3.1
   remote-as 12345
   shutdown
   description 3G_VOICE
   address-family ipv4 unicast
    send-community-ebgp
    route-policy DROP-ALL in
    route-policy DROP-ALL out
    remove-private-AS
    soft-reconfiguration inbound
   !
  !
 !
!
"""

ttp_template = """
<macro>
def todash(input_string):
  return input_string.replace(' ','-')
</macro>
<group name='config'>
 <group name='neighbor'>
  <group name='{{neighbor}}'>
  neighbor {{neighbor | IP}}
   password {{password | WORD}}
   <group name='address-family'>
    <group name='{{address-family}}'>
   address-family {{address-family | ORPHRASE | macro('todash')}}
    route-policy {{route-policy-in}} in
    route-policy {{route-policy-out}} out
    soft-reconfiguration {{soft-reconfiguration | ORPHRASE}}
    {{_end_}}
    </group>
   </group>
  </group>
 </group>
</group>
"""

parser = ttp(data=data,template=ttp_template)
parser.parse()
results = parser.result(format='json')[0]
print(results)
