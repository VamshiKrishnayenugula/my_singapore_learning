#index of a number

x = [12, 45, 67, 89, 34, 67, 13]

max_num = max(enumerate(x,start = 0 ), key = lambda x:x[1])

print(max_num[0])