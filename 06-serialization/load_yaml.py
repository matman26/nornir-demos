import ruamel.yaml as yaml

with open("example.yaml", "r") as stream:
    try:
        data = yaml.safe_load(stream)
        print(data)
    except yaml.YAMLError as exc:
        print(exc)
        raise exc

choice = input("Insert router3? [y,N]")
if choice in ("y", "Y"):
    data['hosts'].append({'router3': {'managed': False, 'address': '10.0.2.3'}})

print(data)
with open("output.yaml", "w+") as stream:
    try:
        yaml.dump(data, stream)
    except yaml.YAMLError as exc:
        print(exc)
        raise exc