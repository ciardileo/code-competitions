def main():
    N = int(input())
    
    count = 1
    while True:
        multiplo = str(N * count)
        s = {x for x in multiplo}
        
        if len(s) == 1:
            if "1" in s:
                print(multiplo)
                break
        elif len(s) == 2:
            if "1" in s and "0" in s:
                print(multiplo)
                break
            
        count += 1
                

if __name__ == "__main__":
    main()