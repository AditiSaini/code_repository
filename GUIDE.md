### Question 1: Longest Consecutive Sequence
1. Convert list into a set
2. Use a for loop to parse each element in the set 
    a. Check if n-1 exists, if yes then continue the loop
    b. Use a while loop inside it to check if there was an n+1 in the set and continue to capture the max window 

### Question 2: Creating Trie
1. Create a Node class with value (str), is a leaf node (bool) and child (dict)
2. Create a common method called findNode that parses through the nodes to get to the final node
3. Use the findNode method in both prefix and search