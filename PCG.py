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

def zprompt():
    global results
    global traits
    global ability
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
        traits['ability'] = 'Big Horn: ' + ability['Big Horn']
    elif q == 'b':
        results['zodiac'] = 'Taurus'
        traits['ability'] = 'Great Courage: ' + ability['Great Courage']
    elif q == 'c':
        results['zodiac'] = 'Gemini'
        results['ability'] = 'Duality: ' + ability['Duality']
    elif q == 'd':
        results['zodiac'] = 'Cancer'
        results['ability'] = 'Performance in a Pinch: ' + ability['Performance in a Pinch']
    elif q == 'e':
        results['zodiac'] = 'Leo'
        traits['ability'] = 'Great Courage: ' + ability['Great Courage']
    elif q == 'f':
        results['zodiac'] = 'Virgo'
        traits['ability'] = 'Elemental Blessing: ' + ability['Elemental Blessing']
    elif q == 'g':
        results['zodiac'] = 'Libra'
        results['ability'] = 'Duality: ' + ability['Duality']
    elif q == 'h':
        results['zodiac'] = 'Scorpio'
        results['ability'] = 'Performance in a Pinch: ' + ability['Performance in a Pinch']
    elif q == 'i':
        results['zodiac'] = 'Sagittarius'
        traits['ability'] = 'Steady Hands: ' + ability['Steady Hands']
    elif q == 'j':
        results['zodiac'] = 'Capricorn'
        traits['ability'] = 'Big Horn: ' + ability['Big Horn']
    elif q == 'k':
        results['zodiac'] = 'Aquarius'
        traits['ability'] = 'Elemental Blessing: ' + ability['Elemental Blessing']
    elif q == 'l':
        results['zodiac'] = 'Pisces'
        traits['Fluid'] = 'Fluid: ' + ability['Fluid']
    else:
        print('Error: Invalid input.')
        zprompt()

def progresscheck(): #testing only
    global i
    global e
    global n
    global s
    global t
    global f
    global j
    global p
    print('i = ' + str(i))         
    print('e = ' + str(e))
    print('n = ' + str(n))
    print('s = ' + str(s))
    print('t = ' + str(t))
    print('f = ' + str(f))
    print('j = ' + str(j))
    print('p = ' + str(p))

def checkscores(): #testing only
    global results
    global ability
    print('Your Score: ')
    progresscheck()
    print('Sign: ' + results['zodiac'])
    print(traits['ability'])

def getresults():
    global i
    global e
    global n
    global s
    global t
    global f
    global j
    global p
    global results
    if i == e:
        print('Oops! Can you answer this one too?')
        iprompt('[Insert Tiebreaker Here]')
        print('Thanks!')
        getresults1()
    else:
        if i > e:
            results['InEx'] = 'Introverted'
        else:
            results['InEx'] = 'Extroverted'
    if n == s:
        print('Oops! Can you answer this one too?')
        nprompt('[Insert Tiebreaker Here]')
        print('Thanks!')
        getresults2()
    else:
        if n > s:
            results['iNSe'] = 'Intuitive'
        else:
            results['iNSe'] = 'Sensing'
    if t == f:
        print('Oops! Can you answer this one too?')
        tprompt('[Insert Tiebreaker Here]')
        print('Thanks!')
        getresults3()
    else:
        if t > f:
            results['ThFe'] = 'Thinking'
        else:
            results['ThFe'] = 'Feeling'
    if j == p:
        print('Oops! Can you answer this one too?')
        jprompt('[Insert Tiebreaker Here]')
        print('Thanks!')
        getresults4()
    else:
        if j > p:
            results['JuPe'] = 'Judging'
        else:
            results['JuPe'] = 'Percieving'
    
def checkresults(): #testing only
    global results
    for key in results:
        print(key + ' = ' + results[key])

def gettraits():
    global results
    global traits
    if results['InEx'] == 'Introverted':
        traits['atkrange'] = 'Ranged'
    else:
        traits['arkrange'] = 'Short Ranged'
    if results['iNSe'] == 'Intuitive':
        traits['atkresist'] = 'Elemental'
    else:
        traits['atkresist'] = 'Physical'
    if results['ThFe'] == 'Thinking':
        traits['atktype'] = 'Elemental'
    else:
        traits['atktype'] = 'Physical'
    if results['JuPe'] == 'Judging':
        traits['luck'] = 'Percise'
    else:
        traits['luck'] = 'Unpredictable'

def checktraits(): #testing only
    global traits
    for key in traits:
              print(key + ' = ' + traits[key])

#Global Variables

i = 0
e = 0
n = 0
s = 0
t = 0
f = 0
j = 0
p = 0

#Dicts

results = { 'zodiac' : 'Unknown',
            'InEx' : 'Unknown',
            'iNSe' : 'Unknown',
            'ThFe' : 'Unknown',
            'JuPe' : 'Unknown'}
traits = { 'atkrange' : 'Unknown',
           'atktype' : 'Unknown',
           'atkresist' : 'Unknown',
           'luck' : 'Unknown',
           'ability' : 'Unknown'}

ability = { 'Big Horn': 'Your monster has horns. If the opponent uses a physical attack on the opponent, they receive 25% recoil damage. It has small increase in physical attack, but a small decrease in speed and dexterity,',
           'Performance in a Pinch' : 'Near defeat, these monsters can become a major threat. With this ability, its attacks will always land and have a high critical hit chance.',
           'Elemental Blessing' : 'Significant elemental attack and resistance bonus',
           'Great Courage' : 'If your monster specializes in physical attacks,  physical attacks are 25% stronger, but your monster has 25% less resistance to elemental attacks. If your monster specializes in elemental attacks, elemental attacks are 25% stronger, but your monster is 25% less resistant to physical attacks.',
           'Duality' : '25% Chance of attacking twice in one turn.',
           'Steady Hands' : 'Introverted monsters with this ability get an attack bonus; extraverted monsters with this ability get additional range.',
           'Fluid' : 'Gains a bonus to both elemental and physical resistance.'}

print('Welcome to the world of Pymon! My name is Shell!')
print('Pymon are an experiment in python based RPG character generation.')
print('They are virtual monsters with strengths, weaknesses, and abilities uniquely based on your personality.')
print('The following survey will determine what skills your monster will be able to bring into combat!')
print('How?  Carl G. Jungs theory of psychological types.')
print('According to Jung their are 16 main types of personalities.')
print('These are determined by 4 pairs of opposite tendencies:')
print('Extroversion / Introversion (e / i)')
print('Sensing / Intuition (s / n)')
print('Thinking / Feeling (t / f)')
print('Judging / Percieving (j / p)')
print('Determining which behavioral tendency in each pair you leaves you with one of 16 4-letter types.')
print('Each pair of traits represents 2 possible traits that will be assigned to each of its 4 trait catagories.')
print('Your monster will also recieve a special ability that makes it unique, and is not based on personality type.')
print('But I will explain all these details later. Its time figure put what your monster is made of!')
print('Let the test begin!')      
print('Input the answer that best represents your feelings about the statement.')
print('a) strongly agree')
print('b) agree')
print('c) disagree')
print('d) strongly disagree')
print('Please answer using only a single lowercase letter.')
#Part Part I
#Introversion vs Extroversion

#Introversion

iprompt('You are a person somewhat reserved and distant in communication.')
progresscheck() #testing only
iprompt('After prolonged socializing you feel you need to get away and be alone.')
progresscheck() #testing only
iprompt('You find it difficult to speak loudly.')
progresscheck() #testing only
iprompt('[Insert Question Here]')
progresscheck() #testing only

#Extroversion

eprompt('You enjoy having a wide circle of acquaintances.')
progresscheck() #testing only
eprompt('You spend your leisure time actively socializing with a group of people, attending parties, shopping, etc.')
progresscheck() #testing only
eprompt('You rapidly get involved in the social life of a new workplace.')
progresscheck() #testing only
eprompt('The more people you speak to, the better you feel.')
progresscheck() #testing only

#Part II
#Sensing vs Intuitive

#Sensing

sprompt('[Insert Question Here]')
progresscheck() #testing only
sprompt('[Insert Question Here]')
progresscheck() #testing only
sprompt('[Insert Question Here]')
progresscheck() #testing only
sprompt('[Insert Question Here]')
progresscheck() #testing only

#iNtuitive

nprompt('[Insert Question Here]')
progresscheck() #testing only
nprompt('[Insert Question Here]')
progresscheck() #testing only
nprompt('[Insert Question Here]')
progresscheck() #testing only
nprompt('[Insert Question Here]')
progresscheck() #testing only

#Part III
#Thinking vs Feeling

#Thinking

tprompt('You trust reason rather than feelings.')
progresscheck() #testing only 
tprompt('You usually plan your actions in advance.')
progresscheck() #testing only
tprompt('[Insert Question Here]')
progresscheck() #testing only
tprompt('[Insert Question Here]')
progresscheck() #testing only

#Feeling

fprompt('You are usually the first to react to a sudden event: the telephone ringing or unexpected question.')
progresscheck() #testing only
fprompt('You feel involved when watching TV soaps.')
progresscheck() #testing only
fprompt('You prefer to act immediately rather than speculate about various options.')
progresscheck() #testing only
fprompt('You frequently and easily express your feelings and emotions.')
progresscheck() #testing only

#Judging vs Percieving

#Judging

jprompt('You value justice higher than mercy.')
progresscheck() #testing only
jprompt('[Insert Question Here]')
progresscheck() #testing only
jprompt('[Insert Question Here]')
progresscheck() #testing only
jprompt('[Insert Question Here]')
progresscheck() #testing only
        
#Percieving

pprompt('[Insert Question Here]')
progresscheck() #testing only
pprompt('[Insert Question Here]')
progresscheck() #testing only
pprompt('[Insert Question Here]')
progresscheck() #testing only
pprompt('[Insert Question Here]')
progresscheck() #testing only
        
#Part V
Astrology

zprompt()

checkscores() #testing only

#Generating Results

getresults()
checkresults() #testing only

#Generating Traits

gettraits()
checktraits() #testing only
        
