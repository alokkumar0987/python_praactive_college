# how to read data in single line ---->>> use input().split() method
print("====how to read data in single line====")
'''
a, b ,=input("Enter two numbers separated by space: ").split()
print(a, b) # 5 6
'''

a,b = map(int, input("Enter two numbers separated by space: ").split())
print(a, b) # 5 6


a,b = map(float, input("Enter two numbers separated by space: ").split())
print(a, b) # 5 6