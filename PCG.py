def space():
    print(' ')
    
def choices():
    space()
    print('a) strongly agree')
    print('b) agree')
    print('c) disagree')
    print('d) strongly disagree')
    space()
    print('Input lowercase answers a - d only, or prompt will be repeated.')
   

def iprompt(question):
    global i
    global e
    choices()
    space()
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
    choices()
    space()
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
    choices()
    space()
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
    choices()
    space()
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
    choices()
    space()
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
    choices()
    space()
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
    choices()
    space()
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
    choices()
    space()
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
    space()
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
    print('Input lowercase answers a - l only, or prompt will be repeated.')
    q = str(raw_input('>> '))
    if q == 'a':
        results['zodiac'] = 'Aries'
        traits['ability'] = 'Big Horn: ' + ability['Big Horn']
    elif q == 'b':
        results['zodiac'] = 'Taurus'
        traits['ability'] = 'Great Courage: ' + ability['Great Courage']
    elif q == 'c':
        results['zodiac'] = 'Gemini'
        traits['ability'] = 'Duality: ' + ability['Duality']
    elif q == 'd':
        results['zodiac'] = 'Cancer'
        traits['ability'] = 'Performance in a Pinch: ' + ability['Performance in a Pinch']
    elif q == 'e':
        results['zodiac'] = 'Leo'
        traits['ability'] = 'Great Courage: ' + ability['Great Courage']
    elif q == 'f':
        results['zodiac'] = 'Virgo'
        traits['ability'] = 'Elemental Blessing: ' + ability['Elemental Blessing']
    elif q == 'g':
        results['zodiac'] = 'Libra'
        traits['ability'] = 'Duality: ' + ability['Duality']
    elif q == 'h':
        results['zodiac'] = 'Scorpio'
        traits['ability'] = 'Performance in a Pinch: ' + ability['Performance in a Pinch']
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
    space()
    print('Checking personality score...')
    print('i = ' + str(i))         
    print('e = ' + str(e))
    print('n = ' + str(n))
    print('s = ' + str(s))
    print('t = ' + str(t))
    print('f = ' + str(f))
    print('j = ' + str(j))
    print('p = ' + str(p))

def checkscores(): #testing only
    space()
    print('Your final score is... ')
    progresscheck()
    
def getresults():
    space()
    global i
    global e
    global n
    global s
    global t
    global f
    global j
    global p
    global results
    print('Processing your results...for any ties that occur you should be asked an additional question.')
    if i == e:
        space()
        print('Oops, there was a tie! Can you answer this one too?')
        iprompt('You would rather have a close friendship with small number than have a less intimate friendship with the majority of my peers.')
        print('Thanks!')
        if i > e:
            results['InEx'] = 'Introverted'
        else:
            results['InEx'] = 'Extroverted'
    else:
        if i > e:
            results['InEx'] = 'Introverted'
        else:
            results['InEx'] = 'Extroverted'
    if n == s:
        space()
        print('Oops, there was a tie! Can you answer this one too?')
        nprompt('If forced to choose between them, you will make the choice that feels right, opposed to the one that is logical.')
        print('Thanks!')
        if n > s:
            results['iNSe'] = 'Intuitive'
        else:
            results['iNSe'] = 'Sensing'
    else:
        if n > s:
            results['iNSe'] = 'Intuitive'
        else:
            results['iNSe'] = 'Sensing'
    if t == f:
        space()
        print('Oops, there was a tie! Can you answer this one too?')
        tprompt('Games are more fun if they require the use of strategy to be more sucessful.')
        print('Thanks!')
        if t > f:
            results['ThFe'] = 'Thinking'
        else:
            results['ThFe'] = 'Feeling'
    else:
        if t > f:
            results['ThFe'] = 'Thinking'
        else:
            results['ThFe'] = 'Feeling'
    if j == p:
        space()
        print('Oops, there was a tie! Can you answer this one too?')
        pprompt('Someone is more likely to be sucessful if they are willing to take risks.')
        print('Thanks!')
        if j > p:
            results['JuPe'] = 'Judging'
        else:
            results['JuPe'] = 'Percieving'
    else:
        if j > p:
            results['JuPe'] = 'Judging'
        else:
            results['JuPe'] = 'Percieving'
    
def checkresults(): #testing only
    global results
    space()
    print('Verifying your results...')
    for key in results:
        print(key + ' = ' + results[key])

def gettraits():
    space()
    print('Generation complete!')
    global results
    global traits
    if results['InEx'] == 'Introverted':
        traits['atkrange'] = 'Ranged'
        print('According to your score, you are more introverted than extroverted.')
        print('Your monster keeps its distance from its opponents. It has increased range in exchange for a small damage penalty.')
        space()
    else:
        traits['arkrange'] = 'Short Ranged'
        print('According to your score, you are more extroverted than introverted.')
        print('Your monster does not mind getting up close an personal with the opponent. Its attacks are short ranged, but get recieve a small damage bonus.')    
        space()
    if results['iNSe'] == 'Intuitive':
        traits['atkresist'] = 'Elemental'
        print('According to your score, you rely on your intuition more than your senses.')
        print('Your monster has strong natural instincts, and is resisistant to elemental attacks.')  
        space()
    else:
        traits['atkresist'] = 'Physical'
        print('According to your score, you rely more on your senses than your intuition.')
        print('Your monster is better observing its opponents movements, and can block some of the damage from physical attacks.')
        space()
    if results['ThFe'] == 'Thinking':
        traits['atktype'] = 'Elemental'
        print('According to your score, your choices are based more on reason than emotion.')
        print('Your monsters understanding of nature make it an expert at elemental magic!')  
        space()
    else:
        traits['atktype'] = 'Physical'
        print('According to your score, your choices are based more on your emotions than reason.')
        print('Your monster channels its passion through the martial arts(short ranged) or acrobatics(ranged)! It is a physical attacker.')
        space()
    if results['JuPe'] == 'Judging':
        traits['luck'] = 'Percise'
        print('According to your score, you prefer to take a relaible approach over a creative approach.')
        print('Your monsters movements are precise! Its attacks that are within range miss only 10% of the time.')
        print('In comparision, monsters with unpredictable movements miss 40% of the time.')
        print('However, it only has a 10% critical hit (deals 25% more damage) chance, whereas unpredicable movements give monsters a 40% chance.')      
        space()
    else:
        traits['luck'] = 'Unpredictable'
        print('According to your score, you are more willing to take risks and like to solve problems using creativity.') 
        print('You monster has unpredictable movements! It is more likely to use risky attacks!')
        print('It has a whopping 40% critical hit (deals 25% more damage) chance compared to monsters with precise movements, whose chance is only 10%.')
        print('However, its attacks that are used within range only have 60% chance of hitting and 40% chance of missing.')
        print('In comparison, monsters that have precise movements hit 90% of time when used within range.')
    space()
    print('Your astrological sign determines your monsters ability!')
    print('Your sign is ' + results['zodiac'] + '.')
    print('Your monsters ability is...')
    print(traits['ability'])
                
        
def checktraits(): #testing only
    print('Trait Summary:')
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

print('EMILY HUNT PRESENTS - PYMON CREATURE GENERATOR (BETA TEST) - THANKS FOR PARTICIPATING, EVERYONE!')
space()
print('Welcome to the world of Pymon!')
space()
print('Pymon are an experiment in python based RPG character generation.')
space()
print('They are virtual monsters with strengths, weaknesses, and abilities uniquely based on your personality.')
space()
print('The following survey will determine what skills your monster will be able to bring into combat!')
space()
print('How you might ask?  Carl G. Jungs theory of psychological types.')
print('According to Jung there are 16 main types of personalities.')
space()
print('These are determined by 4 pairs of opposite tendencies:')
space()
print('Extroversion / Introversion (e / i)')
print('Sensing / Intuition (s / n)')
print('Thinking / Feeling (t / f)')
print('Judging / Percieving (j / p)')
space()
print('Determining which behavioral tendency in each pair you leaves you with one of 16 4-letter types.')
print('Each pair of traits represents 2 possible traits that will be assigned to each of its 4 trait catagories.')
space()
print('Your monster will also recieve a special ability that makes it unique, and is not based on personality type.')
print('But I will explain all these details later. Its time figure put what your monster is made of!')
print('Let the test begin!')
space()
print('(This is the beta version! Your scores progressively checked to test this programs functionality.)')
space()
print('Input the answer that represents your level of agreement or disagreement with the statement')

#Part Part I
#Introversion vs Extroversion

#Introversion

iprompt('You are a person somewhat reserved and distant in communication.')
progresscheck() #testing only
iprompt('After prolonged socializing you feel you need to get away and be alone.')
progresscheck() #testing only
iprompt('You find it difficult to speak loudly.')
progresscheck() #testing only
iprompt(' You prefer to spend your free time relaxing by yourself, or somewhere that is quiet and calm.')
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

sprompt('You are a tactile learner.')
progresscheck() #testing only
sprompt('You are not comfortable with a product unless you understand how it works.')
progresscheck() #testing only
sprompt('You would rather watch a demonstration than hear an explanation.')
progresscheck() #testing only
sprompt('A concept is not worth your consideration if there is no evidence to support it.')
progresscheck() #testing only

#iNtuitive

nprompt('In most situations, you are only skeptical if there is probable cause.')
progresscheck() #testing only
nprompt('What is logical or illogical does not necessarily correlate with what is right and wrong.')
progresscheck() #testing only
nprompt('You are facinated by phenomena that cannot be explained.')
progresscheck() #testing only
nprompt('Abstract concepts are as valuable as concrete ones.')
progresscheck() #testing only

#Part III
#Thinking vs Feeling

#Thinking

tprompt('You trust reason rather than feelings.')
progresscheck() #testing only 
tprompt('You usually plan your actions in advance.')
progresscheck() #testing only
tprompt('You are not easily excited.')
progresscheck() #testing only
tprompt('You can usually come up with potential outcomes of a situation with relative ease.')
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
jprompt('You prefer look up an exsiting solution for a problem or consult a peer before solving a problem on you own.')
progresscheck() #testing only
jprompt('The viewpoints of those around have are a significant factor in the choices you make.')
progresscheck() #testing only
jprompt('You would rather stick to an approach you can rely on, rather than experimenting with new methods.')
progresscheck() #testing only
        
#Percieving

pprompt('You think that never breaking rules will not usually get someone far in life.')
progresscheck() #testing only
pprompt('You rely on improvisation more often that prior planning.')
progresscheck() #testing only
pprompt('Generally speaking, you learn best through hands on application.')
progresscheck() #testing only
pprompt('When confronted with a problem, you would prefer to solve it independently before consulting with someone else.')
progresscheck() #testing only
        
#Part V
#Astrology

zprompt()

checkscores() #testing only

#Generating Results

getresults()
checkresults() #testing only

#Generating Traits

gettraits()
#checktraits() #testing only
