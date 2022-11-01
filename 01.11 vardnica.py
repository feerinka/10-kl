d = {}
print("Nospiediet stop,lai pārtraukt!")
while True:
        a=input("Key: ")
        if a=="stop":
            b=a
            d[a]=b
            del d["stop"]
            print(d)
            break
        else:
            b=input("Value: ")
            d[a]=b
            print(d)
