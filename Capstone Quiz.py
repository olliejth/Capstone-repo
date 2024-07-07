# CHANGING QUIZ
# ADD HINTS!!
# ADD GRAPHICS (picture questions?)
# ADD MUSIC SOUND QUESTIONS

import random
categories = {1: 'Nature', 2: 'Film', 3: 'Science',
              4: 'Music', 5: 'History', 6: 'SigmaLabs'}

Nature = [
    ['''What colour is the skin of a polar bear?
a) White
b) Yellow
c) Black
d) Tan''', 'c'],
    ['''How many eyes does a spider have?
a) 2
b) 16
c) 8
d) 10''', 'd'],
    ['''What is a collection of crows more commonly referred to as?
a) Huddle
b) Murder
c) Cult
d) Swarm''', 'b'],
    ['''What was the height of the tallest tree ever recorded to the nearest metre?
a) 116m
b) 204m
c) 89m
d) 103m''', 'a'],
    ['''Which of these animals is suspected to have come from space due to it's ability to survive in a vacuum?
a) Ant
b) Amoeba
c) Tardigrade
d) Cockroach''', 'c'],
    ['''What is the fastest moving animal on the planet?
a) Peregrine Falcon
b) Sailfish
c) Cheetah
d) Gazelle''', 'a']]
Film = [
    ['''Which actor played Marty McFly in the Back to the Future Films?
a) Mel Gibson
b) Michael J. Fox
c) Christopher Lloyd
d) Thomas F. Wilson''', 'b'],
    ['''Who composed the score for the 2014 film Interstellar?
a) John Williams
b) Amy Portman
c) Maurice Jarre
d) Hanz Zimmer''', 'd'],
    ['''In what country was most of the Lord of the Rings Trilogy Filmed?
a) United Kingdom
b) Canada
c) USA
d) New Zealand''', 'd'],
    ['''What is the youngest age that someone has won an Oscar?
a) 10
b) 14
c) 17
d) 8''', 'a'],
    ['''Who is the highest grossing film director of all time?
a) The Russo brothers
b) Michael Bay
c) Steven Spielberg
d) James Cameron''', 'c'],
    ['''The code in the matrix comes from what food recipes?
a) Dumplings
b) Stir-fry
c) Pad thai
d) Sushi''', 'd']]
Science = [
    ['''Which country was the first to discover that the earth was round?
a) England
b) Greece
c) Italy
d) Eqypt''', 'b'],
    ['''How many \"fundamental\" forces are there?
a) 1
b) 2
c) 3
d) 4''', 'd'],
    ['''What is the name of the galaxy we are in?
a) Andromeda
b) The Milky Way
c) Orion
d) The Solar System''', 'b'],
    ['''What is the most reactive element on the periodic table?
a) Caesium
b) Hydrogen
c) Oxygen
d) Fluorine''', 'd'],
    ['''What famous astrologist had a telescope named after them that was launched in 2005?
a) Galileo
b) Copernicus
c) Isaac Newton
d) Stephen Hawking''', 'a'],
    ['''Around how long would it take to reach space travelling at 60mph?
a) 1 Hour
b) 4 Hours
c) 2 Weeks
d) 3 Months''', 'a']]
Music = [
    ['''What class of instrument does the piano belong to?
a) Strings
b) Woodwind
c) Percussion
d) Brass''', 'c'],
    ['''Which of these songs are NOT on the voyager 1 satellite?
a) Beethoven, Fifth Symphony, First Movement
b) Johnny B. Goode - Chuck Berry
c) El Cascabel - Lorenzo Barcelata
d) Winter, The Four Seasons - Antonio Vivaldi''', 'd'],
    ['''Who is the most streamed artist of all time on spotify?
a) Bad Bunny
b) Taylor Swift
c) Drake
d) Ed Sheeran''', 'c'],
    ['''Which artist boasted the largest crowd in musical history?
a) Queen
b) Metallica
c) Rod Stewart
d) Madonna''', 'c'],
    ['''Approximately how much did Kanye West allegedly lose after making offensive comments in 2023?
a) $200 million
b) $800 million
c) $1.1 billion
d) $1.6 billion''', 'd'],
    ['''Who had number one hits with all of the following song titles: HONEY, HERO, FANTASY, SOMEDAY?
a) Mariah Carey
b) Beyonce
c) Katy Perry
d) Jessie J''', 'a']]
History = [
    ['''
a) 
b) 
c) 
d) ''', ''],
    ['''
a) 
b) 
c) 
d) ''', ''],
    ['''
a) 
b) 
c) 
d) ''', ''],
    ['''
a) 
b) 
c) 
d) ''', ''],
    ['''
a) 
b) 
c) 
d) ''', ''],
    ['''
a) 
b) 
c) 
d) ''', '']]
SigmaLabs = [
    ['''
a) 
b) 
c) 
d) ''', ''],
    ['''
a) 
b) 
c) 
d) ''', ''],
    ['''
a) 
b) 
c) 
d) ''', ''],
    ['''
a) 
b) 
c) 
d) ''', ''],
    ['''
a) 
b) 
c) 
d) ''', ''],
    ['''
a) 
b) 
c) 
d) ''', '']]

score = 0
already_asked = []
i = 0
options1 = ['1', '2', '3', '4', '5', '6']
options2 = ['a', 'b', 'c', 'd']

num_choice = input('''- - - - - - - - - -
Enter a number from the list below to choose your quiz:
(1) Nature
(2) Film
(3) Science
(4) Music
(5) History
(6) SigmaLabs
- - - - - - - - - - - 
Enter number here: ''')

selection = int(num_choice)
quiz_str = categories[selection]
quiz = globals()[quiz_str]
print(f'''----------\nYou have chosen: {quiz_str.upper()}''')

while i < 3:
    q = random.randint(0, 5)
    if q not in already_asked:
        ans = input(
            f'----------\n{quiz[q][0]}\n \nAnswer: ')
        if ans.lower() == quiz[q][1]:
            score += 1
        already_asked.append(q)
        i += 1

print(
    f'\n* * * * * * * * * * * * * *\nCongrats! Your Score is: {score}\n* * * * * * * * * * * * * *\n')
