import requests
import time
import sys


if len(sys.argv) == 1:
    print(" Usage: python score.py url")
    exit(1)

#set the URL for the match
URL = sys.argv[1]
#location of the current score, batsmen and bowler by "mining"(actually lucked out)
parseLine = '<meta property="og:description" content="'

#frequency resend request for new score
refreshSpeed = 15

#useful data start and end locations
parseStart = 0
parseEnd = 0

#to print only when the number of balls bowled has changed
oldBall = -1
newBall = 0

while(True):
    #get the new score
    getData = requests.get(URL)

    #useful data starts at
    parseStart = getData.text.find(parseLine) + len(parseLine)
    #useful data ends at
    parseEnd = getData.text.find(")", parseStart) + 1

    #get the ball bowled
    newBall = parseLocation[1] = getData.text.find(".", parseStart) + 1

    #if there's a change in number of balls bowled then show score
    if newBall != oldBall:
        score = getData.text[parseStart:parseEnd]
        print(score)

    #replace the old value so keeps running
    oldBall = newBall

    #sleep every frequency time
    time.sleep(refreshSpeed)
