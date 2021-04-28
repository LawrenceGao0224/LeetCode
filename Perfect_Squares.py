'''
Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

'''
First of all, there is a statement that any number can be represented as sum of 4 squares:
https://en.wikipedia.org/wiki/Lagrange's_four-square_theorem. So, answer always will be 4? No, when we talk about 4 squares, it means that some of them can be equal to zero. So, we have 4 options: either 1, 2, 3 or 4 squares and we need to choose one of these numbers.

How to check if number is full square? Just compare square of integer part of root and this number. Complexity of this part is O(1).
How to check if number is sum of 2 squares: n = i*i + j*j? iterate ovell all i < sqrt(n) and check that n - i*i is full square. Complexity of this part is O(sqrt(n)).
How to check that number is sum of 4 squares? In the same link for wikipedia:
by proving that a positive integer can be expressed as the sum of three squares if and only if it is not of the form 4^k(8m+7) for integers k and m. So, what we need to do is to check this condition and return true if it fulfilled. Complexity is O(log n)
Do we need to check anything else? No, because we have only one options left: 3 squares.
Complexity: time complexity is O(sqrt(n)) and space complexity is O(1).
'''
import math
class Solution:
    def numSquares(self, n):
        if int(math.sqrt(n))**2 == n: return 1
        for j in range(int(math.sqrt(n)) + 1):
            if int(math.sqrt(n - j*j))**2 == n - j*j: return 2
            
        while n % 4 == 0: 
            n >>= 2
        if n % 8 == 7: return 4
        return 3

'''
Further discussion. What if you do not know this 4^k(8m+7) formula on real interview? Then you need to check if number is sum of 3 squares by hands: n = i*i + j*j + k*k with complexity O(n): we check all pairs i,j < sqrt(n). What if we do not know, that each number is sum of 4 squares? Then we need to check also possible sums of 4 squares with complexity O(n sqrt(n)).

We can handle our problem as dynamic programming one, where dp[i] is minumum numer of squares to get i. Then to evaluate dp[i] we need to look at all j, such that j*j <= i. Complexity of this approach is O(n sqrt(n)).

Note, that there is also a way to check if n is sum of two squares, https://en.wikipedia.org/wiki/Sum_of_two_squares_theorem, each odd prive divisor should have a form 4k + 1, but this is a bit more difficult to check and complexity will be also O(sqrt(n)).

Open question, is there solution with comlexity better than O(sqrt(n)). If you have ideas, let me know!
'''

