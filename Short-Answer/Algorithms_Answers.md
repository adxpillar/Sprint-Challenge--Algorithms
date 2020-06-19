#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(1) - the notation here is constant becasue there is no complexity to the while loop and the size of n
stays the same. The space used is linear. 


b) O(nlogn) - This loop will run in a time proportional to log(n) because the inner loop is executed as many times as the number of n increases


c) O(n) - This function is being called  bunnies n times recursively before reaching its base case and we can conclude it will 
run a number of time that is proportional to bunnies n time


## Exercise II

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

The right algorithm here will be a recursive binary search algorithm to determine at what floor 
is the middle point. 

First we get the total number of floors or len(f)
we assume a target floor of the middle floor - half of the len(of floor)
The we traverse our floors from top to bottom 
We move recursively through each floor from the top 
and we take note of the number of dropped + broken eggs on each floor 
Once we get to a floor with the least number of dropped + broken eggs - 
We can select that floor as the new middle floor 
Our base case is when there are no more floors to drop eggs from 

The proposed algorithm should have a runtime complexity of Olog(n)


