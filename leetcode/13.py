"""
Ex 13 - easy
Roman numbers to integer
"""

def roman_to_integer(number: str):
    number = number.upper()
    
    symbols = {
        'I': [1,],
        'V': [5,],
        'X': [10,],
        'L': [50,],
        'C': [100,],
        'D': [500,],
        'M': [1000,],
        'IV': [4,],
        'IX': [9,],
        'XL': [40,],
        'XC': [90,],
        'CD': [400,],
        'CM': [900,],
    }
    
    for key in symbols.keys():
        symbols[key] += [number.count(key) if number.count(key) != -1 else 0]
        
    symbols["I"][1] -=symbols['IV'][1] + symbols['IX'][1]
    symbols["V"][1] -= symbols['IV'][1]
    symbols["X"][1] -= symbols['IX'][1] + symbols['XL'][1] + symbols['XC'][1]
    symbols["L"][1] -= symbols['XL'][1]
    symbols["C"][1] -= symbols['XC'][1] + symbols['CD'][1] + symbols['CM'][1]
    symbols["D"][1] -= symbols['CD'][1]
    symbols["M"][1] -= symbols['CM'][1]
    
    soma = [x * y for x, y in symbols.values()]
        
    return sum(soma)
    
    

roman = input()

print(roman_to_integer(roman))