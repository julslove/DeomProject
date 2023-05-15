

# the function will return a string in reverse mode
def isPalindrom(s):
    #print (s)      prints s for checking
    #print (s[::-1])  prints the reverse of the str
    return s.lower() == s[::-1].lower()

s = "detartrated"
result = isPalindrom(s)

if result:
    print("True")
else:
    print("False")






