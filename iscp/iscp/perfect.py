
MAX_CHAR = 100
 
# Returns true if all values
# in freq[] are either 0 or k.
def check(freq, k):
    for i in range(0, MAX_CHAR):
        if(freq[i] and freq[i] != k):
            return False
    return True
 
# Returns count of substrings where
# frequency of every present character is k
def PerfectSubstring(s, k):
    res = 0 # Initialize result
 
    # Pick a starting point
    for i in range(0, len(s)):
 
        # Initialize all frequencies as 0
        # for this starting point
        freq = [0] * MAX_CHAR
 
        # One by one pick ending points
        for j in range(i, len(s)):
             
            # Increment frequency of current char
            index = ord(s[j]) - ord('a')
            freq[index] += 1
 
            # If frequency becomes more than
            # k, we can't have more substrings
            # starting with i
            if(freq[index] > k):
                break
             
            # If frequency becomes k, then check
            # other frequencies as well
            elif(freq[index] == k and
                 check(freq, k) == True):
                res += 1
             
    return res
 
# Driver Code
s=input()
k=int(input())
print(PerfectSubstring(s,k))