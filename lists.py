demo_list = [1, "hello", 1.34, True, [1, 2, 3]]
colors = ["red", "green", "blue"]

numbers_list = list((1, 2, 3))
#print(type(numbers_list))

r = list(range(1, 101))
#print(r)
print(len(demo_list))
print(colors[0]) #colors es la variable

#print(colors)
#colors[1] = "yellow"
print(colors)

colors.sort()
print(colors)

colors.sort(reverse=True)
print(colors)