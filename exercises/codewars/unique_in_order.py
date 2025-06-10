"""
return a list without repetitions and in order
"""

# def unique_in_order(sequence):
#     result = sorted([item for item in sequence], key=lambda x: x.lower())
#     result += '.'
    
#     result2 = [result[i] for i in range(len(result) - 1) if result[i] != result[i + 1]]
#     return result2
    
def unique_in_order(sequence):
    result = [sequence[i] for i in range(len(sequence)) if sequence[i] != (sequence[i + 1] if (i + 1) < len(sequence) else False)]
    return result
    
# print(unique_in_order("ASKDFOKCSMBAAABOORLfdfd3aaa"))