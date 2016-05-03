import string

def is_palindrome(s,case_sensitive=False):
    if not case_sensitive:
	s = s.lower()
    s = s.replace(" ","")
    s = s.translate(None, string.punctuation)
    s_rev = s[::-1]
    print s
    print s_rev
    if s == s_rev:
	return True
    return False

phrases = [
    'Taco cat',
    'Race car',
    'Not a palindrome',
    'Never odd or even',
    'Bob',
    'Derp',
]

for i in phrases:
    ans = is_palindrome(i)
    if ans == True:
        print('{} is a palindrome').format(i)    
    
