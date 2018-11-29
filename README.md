# WordFinder
Alfi Goyal <alfigoyal@gmail.com>

## Overview
Given a 2D string input, this program identifies all the words equal to length 4 or more letters in the string in four directions i.e upwards, downwards, right and left. The program is also intelligent enough to print the longest valid word i.e it excludes all the substrings from a given list.

## Environment Setup
Spun up an Amazon EC2 instance(you could work on any linux machine).Also, I am using Python 2.7.14.

## Approach
I started my script by retrieving the local dictionary words present in the location /usr/share/dict/words. Next I input my string. I could use string of any length and height. The string should be given in similar format:
```
'''
A T L L F U V D E Y O B Z V D
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
```
In case you want to read the string interactively in the command line simply add ```.read``` to the input variable. Next I removed the spaces in between the letters to make it computer readable string. The output in our example looks like:
```
ATLLFUVDEYOBZVD
WFBNEDXGHEANPOR
OTVBYLALGTDKEAA
DOOWDRAHHELASPZ
APPEAKHROFXWLXO
WBRGASOMMBROKER
MCXGXOUIEOKMYKW
AOEFMRSLSNLRSII
SNPDBCEQPRIUKUQ
TEGRIPEBOQUIQSC
BPASDQPETXJPSES
BRKRREUETTDZDKL
LBJBCBBLEUBIURF
LNHSFHTKRKGHYAM
OJHDNQAJSQPLRMU
```
Next I calculated the row length of the puzzleString. I simply tracked index of /n character and incremented it by 1 as the index starts with 0. Next I tried to get each letter from the string with their position index whose output looked similar to:
```
charOfStringWithIndex = [('A', (0, 0)), ('T', (0, 1)), ('L', (0, 2)), ('L', (0, 3)), .....
```
Going further, my approach is to rearrange the ```charOfStringWithIndex``` into 4 different list in the directions ```down```,```upwards```,```left```and ```right```. Basically an act of transposing the string which should output ```down <- AWODA...```, ```upwards <- UMFLS...```, ```right <- ATLLFU...``` and ```left <- DVZB...``` with their respective indexes. Basically I am trying to capture possible strings(in the form of letter and their corresponding indexes) in each direction since the computer can read the strings only from left to right.

Next we call a function ```returnFinalList```. Here we first combine the above letters to one string i.e. of each row in the form:
```
string = 

UMRLPQSJAQNDHJO
MAYHGKRKTHFSHNL
FRUIBUELBBCBJBL
LKDZDTTEUERRKRB
SESPJXTEPQDSAPB
CSQIUQOBEPIRGET
QUKUIRPQECBDPNS
IISRLNSLSRMFEOA
WKYMKOEIUOXGXCM
REKORBMMOSAGRBW
OXLWXFORHKAEPPA
ZPSALEHHARDWOOD
AAEKDTGLALYBVTO
ROPNAEHGXDENBFW
DVZBOYEDVUFLLTA
```
Note: This is only for one direction. Similar strings are computed for other directions as well.
Then we covert these into list of strings in which each string element is the row of that string. For example ```t``` for above string will be:

```
t = 
['', 'UMRLPQSJAQNDHJO', 'MAYHGKRKTHFSHNL', 'FRUIBUELBBCBJBL', 'LKDZDTTEUERRKRB', 'SESPJXTEPQDSAPB', 'CSQIUQOBEPIRGET', 'QUKUIRPQECBDPNS', 'IISRLNSLSRMFEOA', 'WKYMKOEIUOXGXCM', 'REKORBMMOSAGRBW', 'OXLWXFORHKAEPPA', 'ZPSALEHHARDWOOD', 'AAEKDTGLALYBVTO', 'ROPNAEHGXDENBFW']
```
Now we call the function ```get_all_substrings()``` which inputs each string for the list as input and returns list of all the words of length 4 or more possible using that string to ```returnFinalList()```. Next returnFinalList() matches this list to the dictionary words and returns the matched words in the string finalList. Next, I sort this finalList to decrease the run time.
If you print the finalList(for this example) it comes out to be:
```
['SALE', 'HARD', 'WOOD', 'MAST', 'CONE', 'USEE', 'SEEP', 'HOME', 'SPOT', 'POTT', 'MARK', 'FETE', 'TOPS', 'PEES', 'PEAK', 'ROKE', 'OKER', 'GRIP', 'RIPE', 'BLEU', 'HOUSE', 'HOMES', 'OTTER', 'RAZOR', 'HELAS', 'BROKE', 'ROKER', 'GRIPE', 'POTTER', 'OTTERS', 'BROKER', 'SPOTTER', 'POTTERS', 'HARDWOOD', 'SPOTTERS']
```

## Final Results
In order to print the words that removes all the substrings from above finalList I used the command
```
 print [j for i, j in enumerate(finalList) if all(j not in k for k in finalList[i + 1:])]
```
which gave me the final result: A list with the longest matched words.
```
['SALE', 'MAST', 'CONE', 'USEE', 'SEEP', 'MARK', 'FETE', 'TOPS', 'PEES', 'PEAK', 'BLEU', 'HOUSE', 'HOMES', 'RAZOR', 'HELAS', 'GRIPE', 'BROKER', 'HARDWOOD', 'SPOTTERS']
```
