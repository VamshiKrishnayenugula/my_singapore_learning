"""Given a number, can you write a code that returns a list of all 
the prime numbers in its range? For example, 6 should return 
[2, 3, 5]. The code below returns a list of all prime numbers in a 
given range of a given number. A prime number has two factors: 
one and itself. Prime numbers start at 2. Here is the code below:

"""
def prime_num(n:int)-> list:
    prime_list = []

    for i in range(0,n+1):
        if i >1:
             
            for j in range(2,i):
                 if i%j == 0:
                     break 
            else:
             prime_list.append(i)

    return prime_list


print(prime_num(6))