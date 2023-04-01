from jinja2 import Template

template = Template("""
interface {{ interface }}
  description {{ description }}
""")

data = {
  'interface': 'Ethernet 0/0',
  'description': 'Test Interface'
}

print(template.render(data))
