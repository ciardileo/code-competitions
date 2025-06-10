# declaration (sets have unique values)
numbers = {2, 3, 4, 6, 10, 10}
numbers2 = set([2, 4, 5, 10, 10])

# functions
numbers.add(3)
# numbers.clear()
numbers.pop()  # removes last
numbers.update(numbers2)  # updates with a new set

# sets functions
numbers3 = numbers + numbers2  # numbers.union(numbers2)
numbers3 = numbers - numbers2 # numbers.difference(numbers2)
numbers3 = numbers.intersection