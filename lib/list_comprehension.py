def return_evens(numbers):
    return [n for n in numbers if n % 2 == 0]


def make_exclamation(sentences):
    return [sentence + "!" for sentence in sentences]


# function 1 test
return_evens([0, 1, 3, 5, 7, 8, 9])
# use print
print(return_evens([0, 1, 3, 5, 7, 8, 9]))

#function 2 test
make_exclamation(["Hello", "I'm doing great", "Python is fun"])
#use print 
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"])
)