import sys
sys.path.append('./tagger')
import NLPlib

def read_file(file_name):
    """(str of file name) ->Table
    Input a string which is the file name of a table
    """
    file = open(file_name, 'r')
    # read table to get all of the content of the table
    file_list = file.readlines()
    file.close()
    return file_list

def extractTweetText(line):
    #TODO
    return

def removeHTMLTagAttr(tweetText):
    #TODO - rita
    return

def replaceHTMLChars(tweetText):
    #TODO
    return

def removeURL(tweetText):
    #TODO - rita
    return

def removeFirstCharOfUserNameHashTag(tweetText):
    #TODO
    return

def findLineEnding(tweetText):
    #TODO - rita
    return

def getTokenList(tweetText):
    #TODO
    return

def addTagToToken(token):
    #TODO - rita
    return

def addDemarcation(line):
    #TODO
    return

if __name__ == "__main__":
    print (read_table("tweets/testdata.manual.2009.06.14.csv"))