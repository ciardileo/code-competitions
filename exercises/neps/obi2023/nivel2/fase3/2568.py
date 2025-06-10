"""
mecanicos devem estar organizado dos mais lentos para os mais rapidos
e os carros devem estar ao contrário

um mecanico lento sempre deve pegar um carro rapido
"""

def main():
    N, M = [int(x) for x in input().split()]  # carros e mecânicos
    
    carros = [int(x) for x in input().split()]
    carros.sort()
    
    mecanicos = [int(x) for x in input().split()]
    mecanicos.sort(reverse=True)
    
    
    
    

    

if __name__ == "__main__":
    main()