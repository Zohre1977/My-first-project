import numpy as np
import pandas as pd
import matplotlib
import requests

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np.__version__)

a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(a)
print(a.shape)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])

arr = np.array([23424, 24, 242, 24, 22, 2222, 17])
print(arr[4:6])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])

a = np.array([1, 2, 3, 4, 5])
b = a.copy()
b[1] = 20
print(a)
print(b)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

arr = np.array([1, 2, 3, 4, 5, 6, 7])
X = np.where(arr % 2 == 0)
print(X)

bit = pd.read_csv('bitcoin.csv')
print(bit.head())
print(bit.tail(5))

r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())

X = requests.get('https://google.com')
print(X.text)

X = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(X.text)
