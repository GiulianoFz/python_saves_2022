def hello():
    print("hellO wOrld")

hello() #esto invoca a la funcion

print("--------------------------------")

def hello(name):
    print("hello " + name)

hello("Julian")

print("--------------------------------")


def hello(name="Person"): #queda eso en caso de no tener ningun dato de nombre
    print("hello " + name)
hello() #recordá esto, si no te agarra el codigo es porq falta la funcion