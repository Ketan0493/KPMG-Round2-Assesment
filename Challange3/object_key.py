def get_value(Object, Key):
  for i in Key.split('/'):
    if type(Object) is dict:
      value = Object.get(i)
      Object = value
  return value

Object = {"x":{"y":{"z":"a"}}}
Key = 'x/y/z'
print("Value is ---> ", get_value(Object, Key))