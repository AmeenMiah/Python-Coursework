# Ameen Miah               <--- Name
# F28PL Coursework 1, Python         <--- leave this line unchanged 


# It is not your marker's role to debug basic syntax errors.
# Therefore, if your script won't compile then it might not be marked.
# In other words: if `python3 py_cw.py` won't execute, then your marker is not obliged to mark your answers. 

# To do this coursework, FORK, THEN CLONE the gitlab project.

# If you do it the other way around, then you'll have cloned *my* project (which you can't `git push` to), rather than cloned *your fork* of the project (which you can `git push` to).  
# Any questions, don't guess: ask.

# You may assume variables, procedures, and functions defined in earlier questions
# in your answers to later questions, though you should add comments in code explaining
# this if any clarification might help read your code.

# The test file test_cw.py is not exhaustive. 
# Just because your answer passes it does not mean it's correct.
# You would do well to consider where errors might be lurking and to add these to test_cw.py.   
# You are not marked directly on the quality of additional tests, however your marker may be
# able to assign marks for understanding as demonstrated in any tests you may write, 
# even if the code itself isn't quite right. 

# This coursework is live exam material so KEEP YOUR ANSWERS PRIVATE.  

# Before submitting this coursework please complete the Student authorship declaration here:
#   https://canvas.hw.ac.uk/courses/20804/assignments/102574 
 

# Do not delete the text from here ... 
################################################################################
# Question 1   


"""
The complex numbers are explained here (and elsewhere):
 http://www.mathsisfun.com/algebra/complex-number-multiply.html
Represent a complex integer as a pair of integers, so (4,5) represents 4+5i (or 4+5j, depending on the complex numbers
notation you use).
1a. Using def, define functions cadd and cmult representing complex integer addition and
multiplication.
For instance,
 cadd((1,0),(0,1))
should compute
 (1,1).
1b. Python has its own native implementation of complex numbers. Write translation functions
* tocomplex and 
* fromcomplex 
that map the pair (x1,y1) to the complex number x1+(y1)j and vice versa. 
You may use the python methods real and imag without comment, but not complex -- use j directly instead.
"""
# ... to here

# Check: have you read the question?  Have you read the link above to see how complex number addition and multiplication work?   


# Your answer here


#####################################
# Question 1a


import array
from glob import iglob
from tkinter import E
from typing import final


def cadd(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])


def cmult(c1,c2):
    #Uses the rule i * i is -1
    num1 = c1[0] * c2[0]
    num2 = c1[0] * c2[1] 
    num3 = c1[1] * c2[0] 
    num4 = c1[1] * c2[1] 
    return (num1 - num4, num2 + num3)


#####################################
# Question 1b

def tocomplex(x1, y1):
    num1 = y1 * 1j
    return x1 + num1


def fromcomplex(c):
    return (c.real, c.imag)


# END ANSWER TO Question 1
################################################################################


################################################################################
# Question 2


"""
2a. Using def, write iterative functions 
* seqandi and 
* seqxori 
that implement pointwise AND (https://en.wikipedia.org/wiki/Logical_conjunction) and XOR (https://en.wikipedia.org/wiki/Exclusive_or) of boolean sequences.
For instance
 seqandi([True,True,False],[True,False,True])
should compute
 [True, False, False]
and
 seqxori([True,True,False],[True,False,True])
should compute
 [False, True, True]
You need not write error-handling code to handle the cases that sequences have different
lengths.
2b. Do as for 2a, but make your functions recursive (like OCaml).
Call them seqandr and seqxorr.
2c. Do it again. This time use list comprehensions instead of iteration or recursion.
Call them seqandlc and seqxorlc.
"""

#####################################
# Question 2a


def seqandi(l1, l2):
    array = []
    for i in range(len(l1)):
        if l1[i] == True and True == l2[i]:
            array.append(True)
        else:
            array.append(False)
    return array



def seqxori(l1, l2):
    array = []
    for i in range(len(l1)):
        if (l1[i] or l2[i]) and (l1[i] != l2[i]):
            array.append(True)
        else:
            array.append(False)
    return array


#####################################
# Question 2b


def seqandr(l1, l2):
    n = len(l1) - 1
    if n == 0:
        if (l1[0] == True and True == l2[0]):
            l2[n] = True
            return l2
        else:
            l2[n] = False
            return l2
    else:
        if (l1[n] == True and True == l2[n]):
            l2[n] = True
            seqandr(l1[0: n], l2)
            return l2
        else:
            l2[n] = False
            seqandr(l1[0: n], l2)
            return l2



def seqxorr(l1, l2):
    n = len(l1) - 1
    if n == 0:
        if (l1[0] or l2[0]) and (l1[0] != l2[0]):
            l2[n] = True
            return l2
        else:
            l2[n] = False
            return l2
    else:
        if (l1[n] or l2[n]) and (l1[n] != l2[n]):
            l2[n] = True
            seqxorr(l1[0: n], l2)
            return l2
        else:
            l2[n] = False
            seqxorr(l1[0: n], l2)
            return l2



#####################################
# Question 2c


def seqandlc(l1,l2):
    return [True if (l1[i] == True and l2[i] == True) else False for i in range(len(l1))]


def seqxorlc(l1,l2):
    return [True if ((l1[i] or l2[i]) and (l1[i] != l2[i])) else False for i in range(len(l1))]




# END ANSWER TO Question 2
################################################################################


###############################################################################
# Question 3


"""
Write an essay on Python data representation. Be clear, to-the-point, and concise. Convince
your marker that you understand:
a. Mutable vs immutable types. Give at least two examples of each, with explanation.
b. Integer vs float types.
c. Assignment = vs equality == vs identity is.
d. The computational effects of a call to list on an element of range type, as in
 list(range(5**5**5)).
e. Slices, with examples. Including an explanation of the difference in execution between
 list(range(10**10)[10:10]) and
 list(range(10**10))[10:10]
Include short code-fragments where appropriate (as I do when lecturing) to illustrate your
observations.
"""

"""Answers to the questions
a.  Mutable types are types that can be modified whereas immutable types are types that can't be modified directly. Mutable types have functions that allow you to edit the variable (such as append for lists) whereas immutable types don't. 
    Arrays and dictionaries are both mutables, both them have functions that allow you to modify the variable directly.Booleans and integers are both immutables. Look at the example below:
        num1 = 1
        id(num1)
        > 2643208962288
        num1 = 1 + 1
        > 2643208962384
    As you can see using id, we can see that the second num1 is not the same as the first num1.
        list1 = [1]
        id(list1)
        > 2643247699648
        list1.append(2)
        id(list1)
        > 2643247699648
    The append changes the list without changing the pointer. 
b.  Floats represent numbers with floating point whereas integers represent all integers. Integers have infinite precision whereas floats don't. This means that python will represent any integers you want assuming you have the memory for it. 
    Whereas, Python will return an error if you try to represent a float too big. For example:
        e = 192939.329 ** 1233.232
    will return an overflow error since floats have a max size whereas:
        e = 100000000000 ** 100000000000000
    will not return an error (assumming you have enough memory for it) since integers can go as large as how much memory you have.
c.  Equality checks if the values are equal to each other then returns true if they are and false otherwise. Identity checks if the two variables point to the same thing in memory. Asignment changes where the variable points to. Look at the example below:
        x = 10
        y = x
        z = 10
d.  Range before using list is just an idea of range of numbers which is called a range object. Generating a range object takes very little computation. 
    Once you call list, it has to actually take that range object and use to generate a list of the range specified in the range object. So turning that range object into a list takes a lot of computation compared to generating a range object. 
    You can imagine it as you writing down a range from 0 to 2.98023224E17 (the range of range(5**5**5)) on a piece of paper then handing to someone to write down every number in that range. The creation of the range would take very little effort
e.  list(range(10**10)[10:10]) first makes a range object sliced then turns the range object into a list. list(range(10**10))[10:10] first makes the range object then turns the range object into a list then slices the lists. They both still will return the same value of the empty list.
    In terms of computation power, the first one is sginicantly faster since the second has to create a list of that size takes a lot of processing power and memory and then does the slice which in this case, isn't too demanding of a slice but getting there for the computer
    is the hard part. The first one on the otherhand, just slices the range object and since the range object has very minimal effects on the computer's performance, it can do extremely quickly and store the empty list in the range object. So when list is called, it can quickly just return the empty list.
"""

# END ANSWER TO Question 3
################################################################################


###############################################################################
# Question 4

"""
Recall that `map(f, l)` applies a function pointwise to a list, so that 
   map(f, [x, y, z]) 
computes 
   [f(x), f(y), f(z)]
Call a *datum* something that is either an integer, or a list of data (datums).
Write a generalised mapping function `supermap` that applyies `f` pointwise to any integers inside a datum. 

So for example:
* supermap(f, -5) should return 'f(-5)'
* supermap(f, []) should return '[]'
* supermap(f, [5, [5]) should return '[f(5), [f(5)]]'. 

You may find it useful to consider `isinstance` or the following code fragment
   type(5) == int 

An answer that guts the question (e.g. by calling a supermap-like function in a Python library) may score no marks.
"""


def supermap(f, dat):
    finalValue = []
    if type(dat) == int:
        return f(dat)
    else:
        for i in (dat):
            if type(i) == int:
                finalValue.append(f(i))
            else:
                tempValue = []
                for x in i:
                    tempValue.append(f(x))
                finalValue.append(tempValue)
            
    return finalValue

# END ANSWER TO Question 4
################################################################################


###############################################################################
# Question 5


"""
An encoding f of numbers in lists is as follows:
* f(0) = [] (0 maps to the empty list)
* f(n+1) = [f(n),[f(n)]] (n+1 maps to the list that contains f(n) and singleton f(n))
Implement encode and decode functions in Python, that map correctly between nonnegative
integers and this representation. Call them fenc and fdec.

This is an implementation of one possible encoding of the natural numbers in sets:
   https://en.wikipedia.org/wiki/Set-theoretic_definition_of_natural_numbers
"""


def fenc(i):
    if i == 0:
        return []
    else:
        return [fenc(i-1), [fenc(i-1)]]
    

def fdec(l):
    if l == []:
        return 0
    else:
        try:
            if l[0] == [] and l[1] == [[]]:
                return 2
            else:
                return 1 + fdec([l[0][0], l[1][0]])
        except IndexError:
            return 1



# END ANSWER TO Question 5
################################################################################


###############################################################################
# Question 6


"""
Implement a generator `love` such that if we assign
 x = love()
then repeated calls to
 next(x)
return the strings 
 I love you 
 You love that I love you
 I love that you love that I love you
 You love that I love that you love that I love you
 I love that you love that I love that you love that I love you
 ...
For full marks, your answer should respect correct capitalisation, as above.

Note that this question is not asking you to program an endless loop that prints these values; your answer should be a generator that yields these values.
"""


def love():
    a = ""
    for i in (range(100)):
        if i % 2 == 0:
            if a != "":
                a = a[0].lower() + a[1:]
                a = "I love that " + a
            else:
                a = "I love you"
        else:
            a = "You love that " + a
        yield a




# END ANSWER TO Question 6
################################################################################


#################################################################################
# Question 7

"""
Consider functions that remove all instances of an integer `i` from a list of integers `l`, implemented in three distinct ways:

1. `removeall_oo` repeatedly applies the list .remove method until there are no instances of `i` left (you may use other programming constructs, such as counting the number of integers in `l`, or using exception raisers and handles).  
2. `removeall_ft` uses `import functools` and `filter`.  
3. `removeall_rd` uses `import functools` and `reduce` (but not filter). 

So for example, 
   removeall_oo(0, [0, 0, 1])
should return
   [1]
and
   removeall_oo(0, [0, 0])
should return
   []
"""

def removeall_oo(i, l):
    while True:
        try:
            l.remove(i)
        except ValueError:
            print ("Not in list")
            break
    return l

def removeall_ft(i, l):
    import functools
    return list(filter(lambda a: a != i, l))
    

def removeall_rd(i, l):
    import functools
    return functools.reduce(lambda a, b: a + [b] if b != i else a, l, [])

# END ANSWER TO Question 7
################################################################################


##########################################################
# Question 8

"""
The *Sudan* function is documented here:
   https://en.wikipedia.org/wiki/Sudan_function
Implement the Sudan function as a Python function `sudan(n, x, y)` by orienting the equalities and making recursive calls as appropriate.

Be careful: even `sudan(2,2,2)` freezes up my machine.
"""

def sudan(n, x, y):
    if (n == 0):
        return x + y
    elif (y == 0):
        return x
    else:
        return sudan(n-1, sudan(n, x, y-1), sudan(n, x, y-1) + y)
    


# END ANSWER TO Question 8
################################################################################



###############################################################################
# Question 9 

"""
Write a brief but comprehensive essay that:
1. Surveys the modern uses and applications of Python.
2. Speculates on what it is about Python that has led to its popularity.
3. Speculates on the evolution of Python into the future.  

Your essay should not be long.  

For full marks your answer should demonstrate both factual and technical understanding of the programming languages landscape in general, and of Python's role --- technically, economically, and socially --- within it.
"""

""" Answers to question 9
Python is now used in wide array of fields from accounting to web scripiting. Python's simplicity and readability has allowed it to become one of the standard languages used to teach students how to learn programming and why it's so popular. It also because of it's simplicity allowed many non programmers like
accountants to do some automations for tasks that can quickly become tedious and time consuming e.g. sending emails. There are several reasons why Python is popular with such a large number of people, two I already listed were simplicity and readability. Here are some more:
code written will usually be shorter than if you were to write it in a programming language such as Java, you can do functional and object oriented programming which is great since more choice incentivised more people to use it and the massive community which means 
companies and people are more likely to invest time and/or money into Python since Python isn't likely to stop being developed and can ask for help and usually get an answer. 
Python is also heavily used machine learning and AI. There are several reasons for this such as how many fleshed out external libraries python already has meaning less time to set up and python already has a lot of libraries such as 
numpy which are good for manipulating data. These libraries for manipulating data are also great for scientists in general since how easily they can be imported into a file and then used. The robustness is another reason why they use Python, Python allows you to
do a lot more wihtout crashing e.g. adding an int to a list filled with strings. Which is important because they'll be dealing with thousands of data.
Python will continue to grow in the future as machine learning becomes even popular in the near future and as coding becomes even more popular, many people choose to start with python because of its simplicity. Due to machine learning and AI, we can expect Python to start adding even more features gearing towards data scientist such as new classes or built in functions.
"""

"""
Here's a very brief example answer to Q11 above where "Python" is replaced by "Eggs".  Enjoy:

A chicken is cheap to keep, can produce an egg a day, and eggs come prepackaged and naturally resist spoilage.  For instance, eggs come out of a chicken with a natural antibacterial coating on their shells so that they can be stored at room temperature, which keeps transport costs low --- in the US eggs are washed, which stops them smelling of chickens' bottoms but removes this coating, which is why US eggs require refrigeration and UK eggs don't. 
[note now this combines *factual* and *technical* elements; an awareness of the egg as a thing, but also of supply chain economics, food safety, and a nice factoid which really proves I went beyond the first page of Google results -mjg] 

Eggs are nutritious, tasty, and filling.  They are easy to cook and are culturally well-established in the UK.  A proper superfood, in fact.  

Eggs do have dangers: when improperly handled they can carry salmonella.  More information at [hyperlink].  Eggs can crack, and then spoil quickly.  Occasionally eggs go invisibly bad, or the embryo incubates prematurely (nowadays, sophisticated scanning machines eliminate these from the food chain). 

Eggs also have applications in vaccine development, and unfortunately also in biological warfare as incubators for germs, and [more stuff here -mjg].

For the future, [stuff about vegans, changes in food preferences, vat-grown protein, environmental costs of keeping chickens, etc etc].

[I could keep this up for pages, I won't: we've gone beyond the shell of an answer, we've cracked it, and if we allow our enthusiasm to egg us on then it would over-egg the pudding and we'd get egg on our faces for writing a not-eggsactly-concise answer:  we stuffed enough eggs in this basket and should stop, before the reader finds it eggscrutiating.   
Now your turn please, with "Python" instead of "Egg".  Make me proud.  -mjg]
""" 

# END ANSWER TO Question 9 
###############################################################################


###############################################################################
# Question 10

"""
a. Explain in words the difference between 
   ([],[],[]) 
and 
   [[]]*3.
b. Explain in words what x points to in memory after we execute the following two commands:
     x = []
     x.append(x)
"""

"""Answers to Question 10:

a.  [[]] * 3 creates [[], [], []]. The pointers of the [] in the list, point to the same thing in memory. 
    This means that when you do listName[1].append(10), it will modify every element in the list. [[], [], []] on the otherhand, all point to different values, if you append to the first element of the list then it only modifies the first one leaving the rest still empty
    lists. 
b. x is first assigned with the empty list. Then add x to the list x. This causes basically an infinite loop. The first element of list x points to x in memory then the first element of first element of list x points to x and so on. Creating something that effectively looks like
    this: [[[[[[[[[[[...]]]]]]]]]]]. But this does not consume memory since x is still just pointing to it's own pointer.
"""

# END ANSWER TO Question 10 
###############################################################################

###############################################################################
# Question 11

"""
Python has infinite precision integer arithmetic.

Write your own infinite precision "sum", "product", and "to the power of" functions, that represent numbers as lists of digits between 0 and 9 with least significant digit first. 
Thus: 0 is represented as the empty list [], and 10 is represented as [0,1]. 
You may assume that numbers are non-negative (no need for negative numbers, or for subtraction).
Do NOT gut the question by mapping to python's native integers, performing the arithmetic there, and mapping back!
You may use earlier functions in the definitions of later ones. 

Add your own tests to the `test_cw.py` file.
"""

# map an integer n to its representation as a string of digits.
# no need to error-check for the case that n is negative
# e.g. iint(12) == [2,1]
def iint(n):
    list1 = []
    nStr = str(n)
    for x in range(len(str(nStr))):
        list1.insert(0, int(nStr[x]))
    return list1

# map the string-of-digit representation back to integers
# e.g. pint(iint(12)) == 12 
def pint(I):
    num1 = ""
    if I == []:
        return 0
    else:
        for x in range(len(I)):
            num1 += str(I[x])
            print(num1)

        return int(num1[::-1])

# add two infinite integers
# e.g. iadd([5], [5]) = [0,1]
def iadd(I,J):
    if I == [] and J == []:
        return []
    elif I == []:
        return iint(pint(J))
    elif J == []:
        return iint(pint(I))
    else:
        i = pint(I)
        j = pint(J)
        #Do Binary addition
        while (j != 0):
            sum = (~i & j) | (~j & i)
            carry = i & j
            i = sum
            j = carry << 1
        return iint(i)


# multiply two infinite integers
# e.g. imult([], [5]) = []
def imult(I,J):
    if I == [] or J == []:
        return []
    else:
        product = I
        for x in range(pint(J) - 1):
            product = iadd(I, product)
            print(product)
        return product

# raise I to the power of J
def ipow(I,J):
    if J == []:
        return ['1']
    elif I == []:
        return []
    else:
        powerOfTwo = I
        for x in range(pint(J) - 1):
            powerOfTwo = imult(I, powerOfTwo)
        return powerOfTwo


# END ANSWER TO Question 11 
###############################################################################


###############################################################################
# Question 12

"""
Recall from Question 4 the notion of a *datum*.

a. Write a command `abstractsize` which inputs a datum and returns an integer measure of how much memory it occupies (cf. Question 10).
Note this measure should be in an abstract unit in which each integer occupies one unit of memory and each pair of square brackets occupies one unit of memory, modulo sharing, so that (for example) `[5,5]` has measure 3 --- one for the square brackets, and one for the two integer payloads.  (Do not try to return actual memory usage in bytes, since this will depend on implementation and on the size of the integer payload!) 
b. Write a command `compress` which inputs a datum, and outputs a datum that represents it and minimises abstract size.  Your code should be clear and well-commented with an explanation (if required) of the algorithm you use.

We're not looking for precise bytecounts and certainly not looking for speed or optimal performance.  Marks will be awarded for elegance, clear commenting, and understanding of the issues involved. 
"""

def abstractsize(datum):
    #finalValue is used to count the abstractisize
    finalValue = 0
    if type(datum) == int:
        return 1
    else:
        
        finalValue = 1
        for i in datum:
            if type(i) == int:
                finalValue += 1
            else:
                finalValue +=1
                if i != []:
                    for x in i:
                        finalValue += 1
                
                #Check for how many instances of i from datum list there is in datum then remove all apart from one
                count = sum(i is e for e in datum)
                if (count > 1):
                    for s in range(count-1):
                        datum.remove(i)       
        return finalValue

def compress(datum):
    superList = []
    for x in datum:
        superList.append(x)
        #Check for how many instances of i from datum list there is in datum then remove all apart from one
        count = sum(x is i for i in datum)
        if (count > 1):
            for s in range(count-1):
                datum.remove(x)
    return superList


# print(abstractsize([[]]*3))
# END ANSWER TO Question 12 
###############################################################################

###############################################################################
# Question 13 (bonus question) 

"""
The code below to define `equals23` takes up five lines and 83 characters, by my count. 
It is also ugly, redundant, and indirect.
Rewrite it, so that it is clean, compact, direct --- and takes up one line and 23 characters.
"""

equals23=lambda a:a==23

# END ANSWER TO Question 13 
###############################################################################
