
"""import random

# Define function

def hello():
    print("Misbah")
    print("Javaid")

# Call function

hello()

def hellofunct2(name):
    print('Hello', name)
    
hellofunct2('Misbah Javaid')    
hellofunct2('name')

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidely so'
    elif answerNumber == 3:
        return "Yes"
    
    elif answerNumber == 4:
        return "Reply Misbah try again"
    
    elif answerNumber == 5:
        return "Ask again later"
    
    elif answerNumber == 6:
        return "Concentrate and ask again"
    
    elif answerNumber == 7:
        return "My reply is no"
    
    elif answerNumber == 8:
        return "Outlook not so good"
    
    elif answerNumber == 9:
        return "Very doubtful"

random_number = random.randint(1,10)

print(random_number, getAnswer(random_number))

print('Hello', end = " ")
print("Misbah")

print('Misbah' , "Javaid", "Sarwat", sep = ",")


def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    print(ham)
    eggs = 0
        
spam()

eggs = 42

def skin():
    print(eggs)


skin()
print("\n\n new concept")

def spann():
    global eg
    eg = 'cook'

def beacon():
    eg = 'beacon'
    
def hen():
    print(eg)
        
eg = 42
spann()
beacon()
#hen()
print(eg)  """

def spam(divideBy):
    return 42/divideBy

try:
    print(spam(10))
    print(spam(1))
    print(spam(2))
    print(spam(12))
    print(spam(0))  
except ZeroDivisionError:
    print('Error: Invalid argument')
    

    



 