import statistics

"""
score1 = 72
score2 = 73
score3 = 33

Average =  score1+score2+score3/3 

print(f"Average is {Average}")
print("Average is: {0}".format(Average)) 

array_size = 10
#score = int(input("Enter score: "))
score_list = []
for score in range(array_size):
    score = int(input("Enter score: "))
    score_list.append(score)
    
print("Average of these numbers is", (score_list[0] + score_list[1] + score_list[2])/3) """

list_size = 3

score_list1 = []

for scores in range(list_size):
    score = int(input("Enter score: "))
    score_list1.append(score)

def average():
    calculate_average = statistics.mean(score_list1)
    return calculate_average

print(average())    
    
    
    
