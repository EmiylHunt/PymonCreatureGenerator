def zprompt():
    global results
    print('Between which of the following dates were you born?')
    print('a) 3/21 - 4/19')
    print('b) 4/20 - 5/20')
    print('c) 5/21 - 6/20')
    print('d) 6/21 - 7/22')
    print('e) 7/23 - 8/22')
    print('f) 8/23 - 9/22')
    print('g) 9/23 - 10/22')
    print('h) 10/23 - 11/21')
    print('i) 11/22 - 12/21')
    print('j) 12/22 - 1/19')
    print('k) 1/20 - 2/18 ')
    print('l) 2/19 - 3/20')
    q = str(raw_input('>> '))
    if q == 'a':
        results['zodiac'] = 'Aries'
    elif q == 'b':
        results['zodiac'] = 'Taurus'
    elif q == 'c':
        results['zodiac'] = 'Gemini'
    elif q == 'd':
        results['zodiac'] = 'Cancer'
    elif q == 'e':
        results['zodiac'] = 'Leo'
    elif q == 'f':
        results['zodiac'] = 'Virgo'
    elif q == 'g':
        results['zodiac'] = 'Libra'
    elif q == 'h':
        results['zodiac'] = 'Scorpio'
    elif q == 'i':
        results['zodiac'] = 'Sagittarius'
    elif q == 'j':
        results['zodiac'] = 'Capricorn'
    elif q == 'k':
        results['zodiac'] = 'Aquarius'
    elif q == 'l':
        results['zodiac'] = 'Pisces'
    else:
        print('Error: Invalid input.')
        zprompt()
          
def iprompt(question):
    global i
    global e
    q = str(raw_input(question + ' >> '))
    if q == 'a':
        i += 2
    elif q == 'b':
        i += 1
    elif q == 'c':
        e += 1
    elif q == 'd':
        e += 2
    else:
        print('Error: Invalid input.')
        iprompt(question)
    
def eprompt(question):
    global e
    global i
    q = str(raw_input(question + ' >> '))
    if q == 'a':
        e += 2
    elif q == 'b':
        e += 1
    elif q == 'c':
        i += 1
    elif q == 'd':
        i += 2
    else:
        print('Error: Invalid input.')
        eprompt(question)

def sprompt(question):
    global s
    global n
    q = str(raw_input(question + ' >> '))
    if q == 'a':
        s += 2
    elif q == 'b':
        s += 1
    elif q == 'c':
        n += 1
    elif q == 'd':
        n += 2
    else:
        print('Error: Invalid input.')
        sprompt(question)

def nprompt(question):
    global n
    global s
    q = str(raw_input(question + ' >> '))
    if q == 'a':
        n += 2
    elif q == 'b':
        n += 1
    elif q == 'c':
        s += 1
    elif q == 'd':
        s += 2
    else:
        print('Error: Invalid input.')
        nprompt(question)
    
def tprompt(question):
    global t
    global f
    q = str(raw_input(question + ' >> '))
    if q == 'a':
        t += 2
    elif q == 'b':
        t += 1
    elif q == 'c':
        f += 1
    elif q == 'd':
        f += 2
    else:
        print('Error: Invalid input.')
        tprompt(question)
    
def fprompt(question):
    global f
    global t
    q = str(raw_input(question + ' >> '))
    if q == 'a':
        f += 2
    elif q == 'b':
        f += 1
    elif q == 'c':
        t += 1
    elif q == 'd':
        t += 2
    else:
        print('Error: Invalid input.')
        fprompt(question)

def jprompt(question):
    global j
    global p
    q = str(raw_input(question + ' >> '))
    if q == 'a':
        j += 2
    elif q == 'b':
        j += 1
    elif q == 'c':
        p += 1
    elif q == 'd':
        p += 2
    else:
        print('Error: Invalid input.')
        jprompt(question)

    
def pprompt(question):
    global p
    global j
    q = str(raw_input(question + ' >> '))
    if q == 'a':
        p += 2
    elif q == 'b':
        p += 1
    elif q == 'c':
        j += 1
    elif q == 'd':
        j += 2
    else:
        print('Error: Invalid input.')
        pprompt(question)

