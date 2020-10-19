## **Js Objects in Python**
---
## Made with :
* Literally only one class
* Basic Python Knowledge
* Recursion
* Dunder/magic methods to sharp some edges
---
### **How** can i use it ?
> In **Javascript**: 
```js
let obj = {
    price: 2000,
    audi: {
        engine: 100
    }
}
console.log(obj.price)
console.log(obj.audi)
console.log(obj.audi.price)
```
##### **We would get this**
```
>>> 2000
>>> {engine: 100}
>>> 100
```
> In **Python**:
```python
dict = {
    "price": 2000,
    "audi": {
        "engine": 100
    }
}
print(dict["price"])
print(dict["audi"])
print(dict["audi"]["price"])
```
##### **Obviously same output**
```
>>> 2000
>>> {engine: 100}
>>> 100
```

> So i made this javascript concept in python:
```python
from JsObject import JsObject
dict = {
    "price": 2000,
    "audi": {
        "engine": 100
    }
}
#with this u just need to pass the dictionary as a parameter to the 
#(for now only works with dictionaries)
#class JsObject as it follows -->

obj = JsObject(dict)
print(obj.price)
print(obj.audi)
print(obj.audi.price)
```
> Same output but with less effort:
```
>>> 2000
>>> {engine: 100}
>>> 100
```
---
## 

> **I'l be reading the suggestions and issues so make sure u give me headaches :D**


##### Anything more u can contact me via Discord (like programming partner or things like that) -> tiagooo#1547