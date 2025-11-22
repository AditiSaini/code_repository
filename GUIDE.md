# BLIND 75
## STRINGS

### Question 1: Longest Substring Without Repeating Characters (q56)
1. Initialise a window set and left = 0 
2. Use the window to track the current elements in the string within a valid window
3. Add s[left] to the window
4. Use a for loop to track right and start with index 1
5. Use a while loop to check if the cur[right] is in window set and continue adding +1 to left while cur is in window
6. Use a max_window to get max of window_size and right-left+1
7. return max_window

### Question 2: Longest Repeating Character Replacement (q78)
1. Create a dictionary to keep track of frequencies of the window
2. Use a window variable to keep track of window lenght
3. Initialize left pointer to 0 and add string[left] to dictionary of frequencies
4. Start a for loop with right pointer
5. Add current string[right] character to frequency dictionary 
6. Update window variable using right-left+1
7. Update max_freq to keep track of max_freq in the dictionary of frequencies
8. If window - max_freq > k => remove left from dictionary, maxFreq-=1, window-=1 and left+=1
9. Update max_window_size with max(max_window_size, right-left+1)
10. return max_window_size

### Question 3: Minimum Window Substring
- Intuition: move right pointer such that it has all char in string t and then update left pointer to min length such that all char in t in that substring
- Initialize variables start, end, window = (cur_start, cur_end), target_remaining to keep track of elements that are not in the current window subset 
- Initialise start = 0 and window = (0, inf)
- Use a for loop as end index and with index 0
- continue to iterate in the for loop until we have all the char in target string in the current string and keep track using freq_t
- freq_t = 0; just enough letters from target, freq_t<1: more than enough char, freq_t>1: needs more char in the window
- decrement freq_t at each iteraction of for loop and decrement target_remaining if freq_t[char] > 0
- in the for loop if target_remaining char == 0: increase start index until all elements satisfy the condition from target string
- update window if end-start < window size
- finally increment start+=1, target_remaining+=1 and freq[char at start]+=1 to expand to other combinations
- in the end, return window substring  

### Question 4: Longest Consecutive Sequence
1. Convert list into a set
2. Use a for loop to parse each element in the set 
    a. Check if n-1 exists, if yes then continue the loop
    b. Use a while loop inside it to check if there was an n+1 in the set and continue to capture the max window 

## TRIE
### Question 2: Creating Trie
1. Create a Node class with value (str), is a leaf node (bool) and child (dict)
2. Create a common method called findNode that parses through the nodes to get to the final node
3. Use the findNode method in both prefix and search

## DP
### Question 3: Coin Change (q__, dp)
1. Initialise dp array minAmt to float('inf')
2. Find the base case minAmt[0]=0
3. Iterative condition that iterates through amount from 1 to N and coins from 1 to C with condition minAmt[i] = min(minAmt[i], minAmt[i-c]+1)
4. Finally, return minAmt[-1]