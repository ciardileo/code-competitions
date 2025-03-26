def main():
    t1 = int(input())
    t2 = int(input())
    t3 = int(input())

    if t1 < t2 and t1 < t3:
        print(1)
        if t2 < t3:
            print(2)
            print(3)
        else:
            print(3)
            print(2)
    elif t2 < t1 and t2 < t3:
        print(2)
        if t1 < t3:
            print(1)
            print(3)
        else:
            print(3)
            print(1)
    else:
        print(3)
        if t2 < t1:
            print(2)
            print(1)
        else:
            print(1)
            print(2)
            
    

if __name__ == "__main__":
    main()
