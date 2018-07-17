import json
with open('123.json') as f:
    person = json.load(f)
    print(person)
    print(json.dumps(person, indent=4))