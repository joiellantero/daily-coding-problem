# the given function cons returns a function
def cons(a, b):
  def pair(f):
    return f(a, b)
  return pair

# we pass the returned function from cons to take out the first element
def car(f):
    def first(a, b):
        return a
    return f(first)

# using the same concept as function car, we can implement it using Python lambda
def cdr(f):
    return f(lambda a, b : b)

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))
