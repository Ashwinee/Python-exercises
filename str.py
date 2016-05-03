def wsv_to_csv(s):
    s = s.split(' ')
    s = ','.join(s)
    return s

string = wsv_to_csv('Shake down the thunder!')
print string
