from itertools import count
import os
from pathlib import Path
from nltk.sentiment.vader import SentimentIntensityAnalyzer

directory = 'comments'
document = 'comments\Fantastic_Beasts_The_Secrets_of_Dumbledore_2022.txt'
sid = SentimentIntensityAnalyzer()

allCommentFiles = Path(directory).glob('*')


def newCompound(compound):
    if compound > 0:
        compound = 1
    if compound < 0:
        compound = -1
    return int(compound)


def attractiveness(commentResult, commentCount):
    if commentResult > ((3*commentCount)/4):
        commentResult = "Very Good"
    elif commentResult > (commentCount/4):
        commentResult = "Good"
    elif commentResult > (((-1)*commentCount)/4):
        commentResult = "Normal"
    elif commentResult > (((-3)*commentCount)/4):
        commentResult = "Bad"
    elif commentResult >= ((-1)*commentCount):
        commentResult = "Very Bad"
    return commentResult


def main(commentfile):
    commentCount = 0
    commentResult = 0
    list = []
    with open(commentfile, encoding='ISO-8859-2') as f:
        # print(end='\n')
        for text in f.read().split('\n'):
            scores = sid.polarity_scores(text)
            commentResult += newCompound(scores['compound'])
            commentCount += 1
            list.append(newCompound(scores['compound']))
            # print(text)
            # print('--> Compound {0:.2f}% Negative {1:.2f}% Neutral {2:.2f}% Positive {3:.2f}% '.format(
            #     scores['compound']*100, scores['neg']*100, scores['neu']*100, scores['pos']*100))
            # print(end='\n')
        print(list)
        print("commentResult", commentResult)
        print("commmentCount", commentCount)
        print(attractiveness(commentResult, commentCount))


# show all file comments
for file in allCommentFiles:
    print(file)
    main(file)
    print()
# show one file comment
# main(document)
