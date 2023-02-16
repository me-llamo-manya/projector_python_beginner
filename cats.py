# One day you decide to arrange all of your 100 cats in a giant circle. 
# Initially, none of your cats have any hats on. 
# You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). 
# Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.
# The first round, you stop at every cat, placing a hat on each one. 
# The second round, you only stop at every second cat (#2, #4, #6, #8, etc.). 
# The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
# You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat). 
# Write a program that simply outputs which cats have hats at the end.
# [Optional]: Make function that can calculate hat with any amount of rounds and cats.

# Here you should write an algorithm, after that, try to make pseudo code. 
# Only after that start to work. Code is simple here, but you might struggle with algorithm. 
# Therefore don't try to write a code from the first attempt.

# 
# 
# at the start we have a hashmap with cat's order number and it's state
#  -- initially it will be 0 -- any has a hat
# (whether he has a hat 1 or not 0)

rounds = 100
cats = [0 for i in range(100)]

for i in range(1, rounds+1): #-- iteration through 100 rounds 
    for j in range(0, 100, i): #--iteration through cats with a step
        if cats[j] == 0:
            cats[j] = 1
        else:
            cats[j] = 0
print(cats)
for x in range(len(cats)):
    if cats[x] == 1:
        print(x+1, end =" ")

    



