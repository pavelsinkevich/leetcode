'''You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. 
Return the destination city, that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
'''
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
start_cities = set()
finish_cities = set()
for city_pair in paths:
    start_cities.add(city_pair[0])
    finish_cities.add(city_pair[1])
res = finish_cities.difference(start_cities).pop()    
print(res)