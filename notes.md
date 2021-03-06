# Notes for MIT Intro to CS

This is what I have learned by watching the online lectures, reading the textbook, and solving the problem-set questions.

## What is computation?
> Computers don't know anything. They only do what you tell them to do.

## Types of knowledge:
* Declarative knowledge is statement of fact.
* Imperative knowledge is recipe or "how to". The sequence of steps.

## A numerical example:
### Declarative:
1. Square root of a number x is y such that x * x = y

### Imperative: 
1. Start with a guess g.
2. If g*g is close enough, stop and say g is the answer.
3. Else make a new guess by averaging g and x/g.
4. Using the new number, repeat the process until close enough.

## What is a recipe?
1. Sequence of simple steps.
2. Flow of control porcess that specifies when each step is excuted.
3. A means of determining when to stop.
4. This is an algorithm.

## Everything is an object in Python.

Changing Bindings:

```python
pi = 3.14
r = 2.2
area = pi * (r**2)
r += 1
```

The old `r` value gets lost, Python has an automatic garbage collector.

Python's **garbage collector** runs during program execution and is triggered when an object's reference count reaches zero.

## What is an algorithm?
An algorithm is a finite list of instructions that describe a computation that when executed on a provided set of inputs will proceed through a set of well-defined states and eventually produce an output.

The first truly modern computer was the Manchester Mark 1. It was a stored-program computer. Such a computer stores (and manipulates) a sequence of instructions, and has a set of elements that will execute any instructions in that sequence.

Within the computer, values of type float are stored in the computer as floating point numbers.

Objects and operators can be combined to form expressions, each of which evaluates to some type. This is refered to as the value of the expression.

```python
3 + 2 == 5 # int
3.0 + 2.0 == 5.0 # float 
```

### Input function

Using the input function, the program pauses and waits for the user to enter something. Anything that the user enters, a number or float or string, becomes a string in the program.

Juliet: "What's in the name? That which we call a rose by any other name would smell as sweet".

Consider the two code fragments:

```
# Case A         # Case B
a = 3.14         pi = 3.14
b = 11.20        diameter = 11.20
c = a*(b**2)     area = pi*(diameter**2)
```

When we read the fragment on the left, there is no a priori reason to suspect that anything is amiss. However, a quick glance at the code on the right should prompt us to be suspicious that something is wrong.

When a float is converted to an int, the number is truncated (not rounded but floored), e.g., the value of float 4.91 is the int 4.

Slice:

```python
foo = "abc"
foo[0] == "a"
foo[-1] == "c"
foo[-len(foo)] == "a"
```

```python
range(start=, stop=, step=)
slice[start:stop:step]
```
Strings are immutable.

```python
bar = "hello"
bar[0] = "y"  # Gives an error
bar = "y" + bar[1:] + "w"  # This works!
```

It is almost always more appropriate to ask whether two floating point values are close enough to each other, not whether they are identical. So, for example, it is better to write `abs(x-y) < 0.0001`, rather than `x == y`.

Understanding Scope Details:

```python
def g(x):
  def h():
    x = "abc"
  x += 1
  print("g: x =", x)
  h()
  return x

x = 3
z = g(x)
```

The code inside functions are ignored, until they are called or invoked.

### Global scope
```
g: [some code]
x: 3
z: 4
```

When g is called, we go inside the g scope. Then parameters are mapped to the arguments defined inside the function.

### g scope
```
x: 3
h: [some code]
x gets incremented, x: 4
None
return 4
```

Function h is called.

### scope
``` 
x: "abc"
return None
```

Compound data-types like arrays, objects, or tuples are made out of primitive data-types like ints, strings, and booleans.

A function is called polymorphic if the arguments of many different types.

Tuples are immutable just like strings. Example:
```
(x, y) = (y, x)  # This swaps the two variables.
```

> Lists or arrays are mutable objects.

Mutating an array can have side-effects in your program.
Many variables can point to a single array, these vairable names are called aliases. If the list is mutated, the side-effect is caused.

```python
hot = ["red"`, "yellow", "orange"]
warm = hot
hot.append("pink")
print(warm)  # [`"red", "yellow", "orange", "pink"]
```
```python
a = 1
b = a
b += 1
print(a, b)  # 1 2
```

## What is recursion?
* Algorithmically: a way to design solutions to problems by divide-and-conquer. Basically, reduce a problem to simpler versions of the same problem.

* Semantically: a programming technique where a function calls itself. The goal is to not have infinite recursion. Ensure we have a base case.

```
a * b == a + a * (b-1)
```

Factorial Recursion Example:
```
def fact(n):
  if n == 1:
    return 1
  else:
    return n * fact(n - 1)

print(fact(3))
```
gloabl scope
```
fact: some code
invoke fact(n=3)
```
fact scope
```
n: 3
check if n == 1
else: return 3 * fact(2)
```

fact scope
```
n: 2
check if n == 1
else: return 2 * fact(1)
```

fact scope
```
n: 1
return 1 {base case}
```

So, `1 * 2 * 3 = 6`

* Each recursive call to func creates its own scope/env.
* The variable bindings don't change in a particular scope.
* Flow of control passes back to previous scope once function call returns value.

The point of execution moves from the point of invocation to the first statement in the body of the function.
The code in the function body is executed, until a return statement is encountered, the value of invocation becomes the return value. Returns "None" if no return statement.
The point of execution is transfered back to the code immediately following the invocation.

**Decomposition creates structure**: It allows us to break a problem into modules that are reasonably self-contained, and that may be reused in different settings.

**Abstractions hides detail**: It allows us to use a piece of code as if it were a black box, something whose interior details we cannot see {projector example} and don't need to see, and shouldn't even see. The essence of abstraction is preserving information that is relevant in a given context, and forgetting information that is irrelevant in that context.

When two Boolean-valued expressions are connected by "and", each expression is called a conjunct. If they are connected by "or", they are called disjuncts.

The problem-solving principle is to conquer a hard problem by breaking it into a set of sub-problems with the properties that:
* the sub-problems are easier to solve than the original problem
* solutions of the sub-problems can be combined to solve the original problem

## Testing & Debugging

Testing is the process of running a program to try and ascertain whether or not it works as intended. 

Debugging is the process of trying to fix a program that you already know does not work as intended.

### Types of Bugs

Overt & covert: 
* An overt bug has obvious manifestation, the program crashes or takes far longer (forever in some cases) to run than it should. 
* A covert bug has no obvious manifestation. The program may run to conclusion with no problem, other than outputing the incorrect answer.

Persistent & intermittent: 
* A persistent bug occurs every time the program is run with the same inputs. 
* An intermittent bug occurs only some of the time, even when the program is run on the same inputs and same conditions.

### Types of Testing
Unit testing - During this phase testers construct and run tests designed to ascertain whether individual units of code, functions, work properly.

Integration testing - This is designed to ascertain whether the program as a whole behaves as intended.

In practice, testers cycle through these two phases, since failures during integration testing lead to making changes to individual components.

## Assert

In an assert statement, condition is provided that signifies what the function expects it could be an input, or even the logic itself.

```python
def avg(grades):
  """
  grades: list of floats

  return average grades scored on all tests.
  """

  assert len(grades) != 0, "no grades data"

  return sum(grades)/len(grades)

  avg([])
```

The above example raises an AssertionError, otherwise returns the average grades of a student. As soon as the assert condition becomes false, the function stops executing (function immediately terminates).

Assert is usually used for mentioning a per-condition. So, instead of propagating a problem throughout the program and getting an output that you didn't expect, an assert terminates the funciton call and makes identifying bugs alot easier.

### Good Points!

Increasingly, society relies on software to perform critical computations that are beyond the ability of humans to carry out or even check for correctness.

Remember, as many have said, ???insanity is doing the same thing, over and over again, but expecting different results.???

If there are many unexplained errors, you might consider whether finding and fixing bugs one at a time is even the right approach. Maybe you would be better off thinking about whether there is some better way to organize your program or some simpler algorithm that will be easier to implement correctly.

When an exception is raised that causes the program to terminate, we say that an unhandled exception has been raised.

An exception can and should be handled by the program.

The python raise statement forces a specified exception to occur.
```python
raise exceptionName(args)
```

We can define new exceptions by creating a subclass of the built-in-class Exception.

An abstract data type is a set of objects and the operations on those objects.

## Object Oriented Programming

Functions defined within a class definition is called a method, or a method attribute of the class. Similarly, if we define a variable within a class it becomes a class variable.

When we instantiate a class, we trigger call the __init__() method. If a instance variable is declared within the constructor function, then the value assigned becomes the data attribute of the class instance.

When data attributes are associated with a class we call them class variables. When they are associated with an instance we call them instance variables.

Data abstractions encourages one to think about programming as a process of combining relatively large chunks, which leads us to think of the essence of programming as a process of composing abstractions, rather than individual lines of code.

```python
c = Coordinate(3, 4) # Coordinate Type
zero = Coordinate(0, 0) # Origin

# Both are the same.
print(c.getDistance(zero))
print(Coordinate.getDistance(c, zero))
```

Directly accessing instance variables is considered poor form of programming and should be avoided.

### Inheritance

Indian is a subclass of Human, and therefore inherits the attributes of its superclass.

Inheritance allows us to create a type hierarchy in which each type inherits attributes, data and methods, from the types above it in the hierarchy.

When defining a subclass, think of it as extending the behavior of their superclass. As we can add new attributes or override attributes inherited from the superclass.

### Backwards Compatibility

If client code works correctly using an instance of the supertype, it should also work correctly when an instance of the subtype is substitued for the instance of the supertype. But not necessarily the other way round.

Some programming languages like Java and C++ provide mechanisms for enforcing information hiding. Programmers can make the data attributes of a class invisible to the user, thus require that the data be accessed only through the object's methods.

This is how one should access instance attributes:

```python
vik.lastName  # Direct access to data attribute
vik.getLastName()  # Indirect access to data attribute or sometimes even a copy of the data attribute
```

This is a flaw in Python, as it lets programs read instance and class variables from outside the class definition that means user/client can change or even add important data attributes from outside the class, which can produce a runtime error.

A disciplined programmer can simply follow the sensible rule of not direcly accessing data attributes from outside the class in which they are defined.

## Yield Statements

The presence of a yield statement tells that the function is a generator. Generators are typically used in conjunction with for statements.

A for loop can iterate over the values provided by a method regardless of whether the method returns a list of values or yields a single value at a time.

## Introduction to Algorithmic Complexity

### Understanding Program Efficiency:

Why do we need to understand the efficiency of our algorithms?

* Simple answer because it matters! 
* Size and problems are getting huge, we need efficiency algorithms.
* We need to understand how algorithm design choices affects the cost accosiated with it.

###  Two types of efficiency: Time & Storage

By using abstract notion of "order of growth" we can evaluate the efficiency of programs. It will argue that this is the most appropriate way of assessing the impact of choices of algorithm in solving a problem; and in measuring the inherent difficulty in solving a problem.

**GOAL**: to evaluate different algorithms
* count depends on algorithm
* count depends on implementations
* count independent of computers
* no clear definition of which operations to count

We assume that these steps take constant time:
* mathematical operations
* coparisons
* assignments
* accessing objects in memory

```python
def c_to_f(c):
  return c * 9.0/5 +32  # 3ops
```

`O(1) -> Constant Growth`

```python
def mysum(x):
  total = 0  # 1ops
  for i in range(x + 1):  # 1op  # loop x times
    total += 1  # 2ops
  return total  # 1ops
```

`mysum -> 3x + 2 ops`

`O(x) -> Linear Growth`

We express efficiency in terms of size of input.

### Law of addition for O():
* used with sequential statements
* `O(f(n)) + O(g(n)) = O(f(n) + g(n))`

### Law of multiplication for O():
* used with nested statements
* `O(f(n)) * O(g(n)) = O(f(n) + g(n))`

Note: c == constant

* `O(1)` -> Constant running time
* `O(log(n))` -> Logarithmic running time
* `O(n)` -> Linear running time
* `O(n*log(n))` -> Log-linear running time
* `O(n**c)` -> polynomial running time
* `O(c**n)` -> exponential running time
