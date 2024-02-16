def cipher(pt, key):
    ct=[]

    for char in pt:
        ct.append(chr(ord(char) + key))

    return "".join(ct)

pt = input("Enter plain text: ")
key = int(input("Enter key: "))
ct = cipher(pt, key)
print(ct)

def decipher(ct, key):
    pt=[]

    for char in ct:
        ct.append(chr(ord(char) - key))

    return "".join(pt)