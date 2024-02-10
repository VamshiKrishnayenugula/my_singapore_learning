"""the sorted() function is a hig order function because it takes abother function as a parameter.
Here we careate a lambda function that is then passed as a argumnet to the sorted() fucntion key parameer. by using a negative index[-1] , we are telling the sorted() 
function to sort the the list in descending order"""

list1 = [ 'mary','peter','kelly']

a = lambda x : x[-1]
y = sorted(list1,key=a)

print(y)