"""

"""

def main():
    resultados = []
    output = ""
    count = 1
    partidas = 1
    
    while True:
        partidas = int(input())
        
        if partidas == 0:
            break

        for _ in range(partidas):
            pro, contra = [int(x) for x in input().split()]
            resultados.append(pro-contra)
        
        max_ending_here = resultados[0]
        max_so_far = resultados[0]
        current_start = 0
        best_start = 0
        best_end = 0

        for i in range(1, partidas):
            if resultados[i] > max_ending_here + resultados[i]:
                max_ending_here = resultados[i]
                current_start = i
            else:
                max_ending_here += resultados[i]

            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
                best_start = current_start
                best_end = i
            elif max_ending_here == max_so_far:
                if i - current_start > best_end - best_start:
                    best_start = current_start
                    best_end = i
                    
        resultado = f"{best_start + 1} {best_end + 1}" if max_so_far >= 0 else "nenhum"
        
        if count >= 2:
            output += "\n\n"
            
        output += f"Teste {count}\n{resultado}"
                
        resultados.clear()    
        count += 1
    
    print(output)
    
    
if __name__ == "__main__":
    main()