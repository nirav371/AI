
import time
import math
max_jug1 = int(input("Enter the maximum capacity of the jug 1: "))
max_jug2 = int(input("Enter the maximum capacity of the jug 2: "))
goal = int(input("Enter target quantity: "))
print()

if (max_jug1>max_jug2):
    max_jug1, max_jug2 = max_jug2, max_jug1

def waterjug_problem(jug1, jug2, max1, max2, goal):
    
    print(" ","Jug1: ",jug1,"   ","Jug2: ",jug2)

    if jug2 == goal:
        return
    elif jug2 == max2:
        waterjug_problem(0,jug1,max1,max2,goal)
    elif jug1 != 0 and jug2 == 0:
        waterjug_problem(0,jug1,max1,max2,goal)
    elif jug1 == goal:
        waterjug_problem(jug1,0,max1,max2,goal)
    elif jug1 < max1:
        waterjug_problem(max1,jug2,max1,max2,goal)
    elif jug1<(max2-jug2):
        waterjug_problem(0,jug1+jug2,max1,max2,goal)
    else:
        waterjug_problem(jug1-(max2-jug2),(max2-jug2)+jug2,max1,max2,goal)

gcd = math.gcd(max_jug1,max_jug2)

if (goal%gcd!=0) or (goal>max_jug1 and goal>max_jug2):
    print("No Solution.")
else:
    t = time.time()
    waterjug_problem(0,0,max_jug1,max_jug2,goal)
    end = time.time()-t
    print("\n Time Taken: ", end)