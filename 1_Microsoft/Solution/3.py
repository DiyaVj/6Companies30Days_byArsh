# You are playing the Bulls and Cows game with your friend.

# You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

# The number of "bulls", which are digits in the guess that are in the correct position.
# The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

 
class Solution(object):
    def getHint(self, secret, guess):
        bull, cow = 0,0
        s = list(secret)
        g = list(guess)

        i,j = 0,0
        while i< len(secret):
            if s[j] == g[j]:
                bull +=1
                s.pop(j)
                g.pop(j)
            else:
                j+=1
            i += 1

        count = Counter(s)
        for l in g:
            if l in count and count[l] >0:
                cow+=1
                count[l] -=1
        
        return "{}A{}B".format(bull,cow)
