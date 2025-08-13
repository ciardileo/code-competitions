"""

"""

def divmod2(a, b):
    if a >= 0 and b >= 0:
        return divmod(a, b)
    
    return -(abs(a) // abs(b)), a % b
        
    

def main():
    a, b = [int(x) for x in input().split()]  # números
    
    quociente, resto = divmod2(a, b)
    print(f"{quociente} {resto}")
    
    
if __name__ == "__main__":
    main()