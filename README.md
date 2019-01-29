# Q2. Birthday attack on a 40-bit hash (5 pt)

Write a program that returns a tuple (s, t, n), where 
- s and t are different ASCII strings 
- their SHA-1 hashes have the same high-order 40 bits (same 10 initial hex digits) 
- n is the number of calls to SHA-1 

You can generate random ASCII strings by converting random integers to hex. By the theory of these birthday attacks, you will need to compute somewhat more than 1 million hashes to find this collision with probability greater than ½. 

You need to do the following:
- Upload your code to Github
- Include the link to the code and TWO tuples (s,t,n) and their corresponding SHA-1 hashes in your solution. That is, you need to find TWO pairs of strings whose SHA-1 hashes are the same.

**Hint:**
To find the SHA-1 hash value of a string s, you can execute the following Python code:
import hashlib
hashval=hashlib.sha1(s).hexdigest()

## Answers:
Two Tuples:
1) It took 997,788 SHA-1 calls.
Matched 91b393d39c36008acefe08f6a1c67fa6bcfdde4f to 91b393d39cadbc8dd68169c4be22f4f1f1843e30, which are ASCII b'0x2509220' and b'0x258e279'.
2) It took 1,256,814 SHA-1 calls.
Matched 99d857777ec785232554753e19a8ac4f6995edd0 to 99d857777e9f0d2e074a3f04d3e102e3e3c28675, which are ASCII b'0x17e5b3e' and b'0x4e66237'.
