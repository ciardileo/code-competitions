"""
calculate the maximum number of cakes you can produce with the ingredients
"""

def cakes(recipe: dict, stock: dict):
    maximum_number = 0
    count = 0
    for name, qtd in recipe.items():
        if name not in stock.keys():
            return 0
        
        qtd_stock = stock[name]
        
        # print(f'{name}: {qtd_stock} / {qtd} = {qtd_stock // qtd}')
        if count == 0:
            maximum_number = qtd_stock // qtd
        else:
            maximum_number = (qtd_stock // qtd) if (qtd_stock // qtd) < maximum_number else maximum_number
            
        # print(maximum_number)
            
            
        count += 1
        
    return maximum_number

# alternativa B

def cakes(recipe: dict, stock: dict):
    return min(stock.get(ingrediente, 0) // qtd for ingrediente, qtd in recipe.items())
    

# recipe = {'cream': 200, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}

# stock = {'sugar': 1700, 'flour': 20000, 'milk': 20000, 'oil': 30000, 'cream': 5000}

# print(cakes(recipe, stock))

