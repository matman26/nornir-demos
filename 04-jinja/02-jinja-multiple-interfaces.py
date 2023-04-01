from jinja2 import Template

template = Template("""
{% for interface in interfaces %}
interface {{ interface.name }}
  description {{ interface.description }}
{% endfor %}
""")

interfaces = [
  {
   'name': 'Ethernet 0/0',
   'description': 'Test Interface'
  },
  {
   'name': 'Loopback 10',
   'description': 'Loopback Interface'
  },
  {
   'name': 'Loopback 300',
   'description': 'Loopback Interface'
  },

]

print(template.render({'interfaces': interfaces}))
