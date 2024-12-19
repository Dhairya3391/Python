
# person = {'name': 'Alice', 'age': 30}
# for key in person:
#     print(key, person[key])

# for key, value in person.items():
#     print(key, value)

# for value in person.values():
#     print(value)

# colors = ['red', 'green', 'blue']
# for i, color in enumerate(colors):
#     print(i, color)

# i = enumerate(["spme","shiehf","sadhiueh"])
# print(list(i))

# num = int(input("enter number"))
# for i in range(0,6):
#     print("*"*i*2)








def pattern(n):
    length =2*n-1
    for i in range(length):
        print(" ".join(str(n-min(i,j,length-1-i,length-1-j)) for j in range(length)))

pattern(int(input("enter number : ")))
