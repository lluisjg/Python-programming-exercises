def buildDictionary(n):
    d=dict()

    for i in range(n):
        d[i]=i*i

    return d

print("Give me a number:")
z=int(input())

dicto=buildDictionary(z)

print(dicto)


""" l'interesant d'aquest exercici es l'us de la funcio nativa dict() 

https://docs.python.org/3/library/functions.html#func-dict

"""