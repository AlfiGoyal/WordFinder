# Read all the words found in /usr/share/dict/words
dictWords = [line.strip() for line in open('/usr/share/dict/words')]

# Entering the puzzle string
puzzleString ='''A T L L F U V D E Y O B Z V D
W F B N E D X G H E A N P O R
O T V B Y L A L G T D K E A A
D O O W D R A H H E L A S P Z
A P P E A K H R O F X W L X O
W B R G A S O M M B R O K E R
M C X G X O U I E O K M Y K W
A O E F M R S L S N L R S I I
S N P D B C E Q P R I U K U Q
T E G R I P E B O Q U I Q S C
B P A S D Q P E T X J P S E S
B R K R R E U E T T D Z D K L
L B J B C B B L E U B I U R F
L N H S F H T K R K G H Y A M
O J H D N Q A J S Q P L R M U
'''

# Removing spaces in between the letters to make it computer readable string
readableWordGrid = puzzleString.replace(' ','')

# Getting the row length of the puzzleString,/n being the
# last character adding + 1 to the length
length = readableWordGrid.index('\n')+1

# Getting each character and corresponding index
charOfStringWithIndex = [(letter, divmod(index, length))
            for  index, letter in enumerate (readableWordGrid)]


wordlines = {}
#Convert the charOfStringWithIndex in various directions i.e left,right,upwards and downwards
wordlines['down'] = []
for x in range(length):
    for i in range(x, len(charOfStringWithIndex), length):
        wordlines['down'].append(charOfStringWithIndex[i])
    wordlines['down'].append('\n')
wordlines['right'] = charOfStringWithIndex
wordlines['left'] = [i for i in reversed(charOfStringWithIndex)]
wordlines['upwards'] = [i for i in reversed(wordlines['down'])]

# Function to return list of all possible words that could be
# formed using the given puzzle string in all directions and have 
# length greater than 3(i.e. words of length 4 or greater)
def get_all_substrings(string):
  length = len(string)
  alist = []
  for i in xrange(length):
    for j in xrange(i,length):
        if (len(string[i:j + 1])) > 3:
            alist.append(string[i:j + 1])
  return alist

# Function to return the words matched between dicttionary words
# and the given string
def returnFinalList(lines):
    directions=['down','right','left','upwards']
    finalList = []
    for directions, tuple in lines.items():
        string = ''.join([i[0] for i in tuple])
        t = list(string.split('\n')[:-1])
        n = []
        for i in range(0,len(t)-1):
            n = get_all_substrings(t[i])
            for word in n:
                if word.lower() in dictWords:
                    finalList.append(word)
    finalList = sorted(finalList, key = len)
    # print finalList in order to retrieve list of matched substrings as well
    # Here printed only the list where substrings are removed.
    print [j for i, j in enumerate(finalList) if all(j not in k for k in finalList[i + 1:])]

returnFinalList(wordlines)
                                                     
