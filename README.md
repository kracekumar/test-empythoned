README
----
Testing empythoned library - https://github.com/replit/empythoned. Empythoned
helps to run python code in browser using emscripten which converts CPython
to JS. As a result you need to hit server to evaluate python code.

To start server
----

`$ sudo pip install flask`
`$ python app.py`

Visit `http://0.0.0.0:5000`

Examples
----

```
name = "Python"

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    

if __name__ == "__main__":
    p = Person("kracekumar", 23)
    print p.__dict__

```

Exceptions
----

```
import urllib
response = urllib.urlopen("http://python.org/")
print response.headers
```