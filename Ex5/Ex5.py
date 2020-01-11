name = "SunvoDz"
age = 22

print(" My name is {0} \n I'm {1} year old ".format(name,age))

print(" My name is {names} \n I'm {ages} year old ".format(names=name,ages=age))

print(" My name is {name} \n I'm {age} year old ".format(**locals()))
