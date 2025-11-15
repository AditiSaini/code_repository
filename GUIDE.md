### Question 1: Longest Consecutive Sequence
1. Convert list into a set
2. Use a for loop to parse each element in the set 
    a. Check if n-1 exists, if yes then continue the loop
    b. Use a while loop inside it to check if there was an n+1 in the set and continue to capture the max window 

### Question 2: Creating Trie
1. Create a Node class with value (str), is a leaf node (bool) and child (dict)
2. Create a common method called findNode that parses through the nodes to get to the final node
3. Use the findNode method in both prefix and search

### Question 3: Coin Change (q__, dp)
1. Initialise dp array minAmt to float('inf')
2. Find the base case minAmt[0]=0
3. Iterative condition that iterates through amount from 1 to N and coins from 1 to C with condition minAmt[i] = min(minAmt[i], minAmt[i-c]+1)
4. Finally, return minAmt[-1]