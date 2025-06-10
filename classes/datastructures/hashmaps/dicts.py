hash = dict({"Idade": 15})
hash.update({"Nome": "Leo"})

if "Leo" in hash.values():
    print("Tem leo")
    
if "Nome" in hash.keys():
    print("Tem nome")
    
print(hash)