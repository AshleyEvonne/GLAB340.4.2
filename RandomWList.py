import random

#Select multiple items from a list without repetition.

aList= [20, 40, 80, 100, 120]

sampled_list = random.sample(aList, 3)
print(sampled_list)

# You can use random.randint() and random.randrange() to generate the random numbers, but it can repeat the numbers. 
# To create a list of unique random numbers, we need to use the sample() method.
# Warp a range() function inside a sample() to create a list of random numbers without duplicates. The range() function generates the sequence of random numbers.
# Let’s see a random sample generator to generate five sample numbers from 1 to 100.

#Create list of 5 random numbers
num_list = random.sample(range(100), 5)
print(num_list)