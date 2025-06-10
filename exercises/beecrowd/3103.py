def mover0(num):
    for i in range(len(num)):
        if num[i] != "0":
            num[0], num[i] = num[i], num[0]
            break
        
    return num
    
def main():
    n = int(input())
    resultados = []
    
    for _ in range(n):
        num = sorted(input().strip())
        
        if num[0] == "0":
            num = mover0(num)
        
        resultados.append("".join(num))
    
    print(*resultados, sep="\n")
    
    
if __name__ == "__main__":
    main()