import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"rate":"$120K", "model": "BMW 230", "mpg": 27.5},
    {"rate":"$100K", "model": "Ford Edge", "mpg": 24.1}
  ]
}
print(x)

print(json.dumps(x, indent=4, separators=(", ", " = "),sort_keys=True))