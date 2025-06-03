
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

# list1 = input("Enter the first list of elements separated by spaces: ").split()
# list2 = input("Enter the second list of elements separated by spaces: ").split()
# common_elements = list(set(list1) & set(list2))

# print("Common elements:", common_elements)

# def pattern(n):
#     length =2*n-1
#     for i in range(length):
#         print(" ".join(str(n-min(i,j,length-1-i,length-1-j)) for j in range(length)))

# pattern(int(input("enter number : ")))

# def isPrime(n):
#     flag = True
#     for i in range(2,n):
#         if (n%i==0):
#             flag = False
#     return flag

# def primeRange(m,n):
#     lst = []
#     for i in range(m,n):
#         if(isPrime(i)):
#             lst.append(i)
#     return lst

# # print(primeRange(10,20))

# def foo(bar: float) -> float:
#     if not isinstance(bar, float):
#         raise TypeError("learned something i guess") #that python can not be use as typed language
#     return bar
# print(foo(10))

# def createDict():
#     dict1 = {}
#     n = int(input("Enter the number of elements: "))
#     for i in range(n):
#         key = input("Enter the key: ")
#         value = input("Enter the value: ")
#         dict1[key] = value
#     return dict1

# d = createDict()
# print(d)

# def pattern(n):
#     count = 1
#     for i in range(1,n+1):
#         for j in range(i):
#             if i%2!=0:
#                 print(count,end=" ")
#                 count+=1
#             else:
#                 print(chr(96+count),end=" ")
#                 count+=1
#         print()

# pattern(int(input("enter number : ")))


l1 = [1,2,3,4,3,2,1]
def foo(l):
    maxV = max(l)
    flag = True;
    for i in range(0,maxV-1):
        if l[i]<l[i+1]:
            continue
        else:
            print("first",i)
            flag = False
            break

    t = l.index(maxV)

    for i in range(t,len(l)-1):
        if l[i]>l[i+1]:
            continue
        else:
            print(i)
            flag = False
            break
    return flag

print(foo(l1))