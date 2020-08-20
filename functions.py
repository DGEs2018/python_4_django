import functiontobeimported
def multiplication(x, y, z):
    return x*y*z

# def square(x):
#     return x*x

for i in range(10):
    print(f"The square of {i} is {functiontobeimported.square(i)}")