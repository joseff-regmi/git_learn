x = int(input("enter the first number "))
y = int(input("enter the second number"))


def sum_1():
    z = x + y
    return z


print("the sum of the two provided number is " + str(sum_1()))

# i am working in develop branch 

# i wanna test this thing in git hub

num1 = int(input("enter the first number"))
num2 = int(input("enter the secon number"))

def sub_1(a, b):
    c = a - b
    return c


print(sub_1(num1, num2))

# making list of words from sentence

def word():
    
    word_list = []
    sentence = str(input("enter any sentence to list the words of it "))
    words_of_the_sentence = sentence.split()
    for i in words_of_the_sentence:
        word_list.append(i)
    print(word_list)

word()

print("hello world")

fruit_list = ["apple", "banana", "orange", "kiwi"]

for i in fruit_list:
    print("this fruit has a good test")
    

