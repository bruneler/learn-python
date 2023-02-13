import numpy as np  # library for scientific computing.

# Basic and Array Creation
a = np.array([0, 1, 2, 3, 4])
print(type(a))  # print the datatype
print(a.dtype)  # print the type of the array elements
print(a.size)  # size of content
print(a.ndim)  # nummer der Array Dimensionen oder den Rang des Arrays.
print(a.shape)  # ist ein Tupel aus Integers, welche die Grösse des Arrays in jeder Dimension anzeigt.

# Array Creation mit reelen Zahlen
b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
print(type(b))
print(b.dtype)


#  Indexing and Slicing  #
c = np.array([20, 1, 2, 3, 4])
c[0] = 100  # Change the first element of the array
d = c[1:4]  # Zahlen 2-4 des Arrays in ein neues Array.
c[2:4] = 145, 187
print(c)

# Basic Operations in numpy
# Vector Addition and Subtraction
# Beispiel Vector Additon siehe vector_addition.png und visualisation_vector_addition.png

# addieren die beiden Listen und stellen das Ergebnis in Liste z.
# standard addition
u = [1, 0]
v = [0, 1]
z = []
for n, m in zip(u, v):
    z.append(n+m)
print(z)

# addition in numpy

u = np.array([1, 0])
v = np.array([0, 1])
z = u + v
print(z)

# Vektor Subtraktion

u = np.array([1, 0])
v = np.array([0, 1])
z = u - v
print(z)

# Array multiplication with a Scalar value
u = np.array([1, 2])
z = 2*u
print(z)

# Oder Multiplikation mit 2 Arrays
u = np.array([3, 4])
v = np.array([5, 8])
z = u * v
print(z)

# Dot Product / Skalarprodukt
# ist eine einzige Zahl,
# repräsentiert, wie ähnlich zwei Vektoren sind.

u = np.array([1, 2])
v = np.array([3, 1])
result = np.dot(u, v)
print(result)

# Eine Konstante zu einem Array hinzufügen

u = np.array([1, 2])
z = u + 3  # wie broadcasting
print(z)

# Universal Functions
# mittelwert eines Arrays

u = np.array([1, 2, 5, 3, 6, 1, 99, 45, 3])
mittel_u = u.mean()  # mittelwert
print(mittel_u)

max_u = u.max()  # Die grösste Zahl
print(max_u)


# PI Zahl
x = np.array([0, np.pi/2, np.pi])
y = np.sin(x)  # sin function to all elements in the array
print(y)

# linspace

X = np.linspace(0, 2*np.pi, 100)
print(x)
y = np.sin(x)

# import matplotlib.pyplot as plt
# %matplotlib inline
# plt.plot(x,y)

# Arrays mit 2 Dimensionen

a = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 35]]
A = np.array(a)
print(A)
print(A.shape)  # ist ein Tupel aus Integers, welche die Grösse des Arrays in jeder Dimension anzeigt.

# Slicing
print(A[0, 0:2]) # Zeile 0, Index 0 bis 2
print(A[0:2, 2]) # Zeile 1 und 2, spalte 3


x = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 35]]
X = np.array(x)

y = [41, 42, 43, 44], [51, 52, 53, 54], [51, 52, 53, 55]
Y = np.array(y)

Z =X + Y
print(Z)

# Matrix Multiplikation
a = [[0, 1, 1], [1, 0, 1]]
b = [[1, 1], [1, 1], [-1, 1]]
A = np.array(a)
B = np.array(b)
C = np.dot(A, B)
print(C)
print(np.dot(A, B))

