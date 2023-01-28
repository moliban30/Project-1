# Summary:
# author: Mohamed Abdullahi
# date:1/5/22


import random

# Constants for the parts of a question
CATEGORY = 0
VALUE = 1
QUESTION = 2
ANSWER = 3

# Constant representing a used question
NO_QUESTION = "____"



# Copy your getInfo function from the minitask
def getInfo(questInfo, whichInfo):
    nameQuestion = questInfo.split(',')

    
    return str(nameQuestion[whichInfo])

# Read in a file and return a list containing the lines in the file
# parameter: filename - name of CSV file to read
# return: list containing stripped lines of the file
def loadCSV (filename):
    outputList = []
    try:
        source = open(filename,"r", encoding="UTF-8")
        outputList =  source.readlines()
        source.close()
        newList = []        
        for item in outputList:
            newList.append (str(item).strip('\n'))
    except FileNotFoundError:
        print("Unable to open input file: " + filename)
    return newList
    
    


# Takes a list containing every line from the question csv list
# Returns a new list containing only the categories
# parameter:  fileList - list containing lines of a CSV file containing quiz data
# return : list of strings containing unique categories of questions
def getCategoryList(fileList):

        categoryList = []
        for items in fileList:
            category = getInfo(items , CATEGORY) 
            if category not in categoryList:
                categoryList.append(category)

        getCat = random.sample(categoryList,3)

       
        
        return getCat




# Takes a list containing every line from the question csv list
# Returns a new list containing only the questions whose category is in categoryList
# parameter:  fileList - list containing lines of a CSV file containing quiz data
#             categoryList - list containing categories from which to choose questions
# return : list of strings containing CSV formatted question info
#                  from only the categories contained in categoryList
def getQuestionList(fileList, categoryList):

    questList = []
    for item in fileList:
        csvList = getInfo(item , CATEGORY)
        if csvList in categoryList:
            questList.append(item)
            
           
    getQuest = random.sample(questList , 9)
        
                         
    
    return getQuest

    



# Prints question board
# For example:
# Q0($100)  Q1($200)  Q2($400)
# Q3($200)  Q4($150)  Q5($600)
# Q6($200)  Q7($150)  Q8($600)
#
# parameter:  questionList - list of 9 CSV formatted questions
def printBoard(questionList):
    print("PRINTING BOARD")

    for i in range (0, 3):
        printList = getInfo(questionList[i] , VALUE)

        if NO_QUESTION not in getInfo(questionList[i], QUESTION):
            print('Q' + str(i) + "(" + printList + ")" , " " , end="")
        else:
            print('Q' + str(i) + "(" + NO_QUESTION + ")" , " " , end="")
    print()

    for i in range (3, 6):
        printList = getInfo(questionList[i] , VALUE)

        if NO_QUESTION not in getInfo(questionList[i], QUESTION):
            print('Q' + str(i) + "(" + printList + ")" , " " , end="")
        else:
            print('Q' + str(i) + "(" + NO_QUESTION + ")" , " " , end="")
    print()
    
    for i in range (6, 9):
        printList = getInfo(questionList[i] , VALUE)

        if NO_QUESTION not in getInfo(questionList[i], QUESTION):
            print('Q' + str(i) + "(" + printList + ")" , " " , end="")
        else:
            print('Q' + str(i) + "(" + NO_QUESTION + ")" , " " , end="")
    print()
        

      
    


# Checks question list for a valid question
# If every element is NO_QUESTION, return false
# If at least one element has text, return true
# parameter:  questionList - list of 9 CSV formatted questions
# return: true if at least one question is unused, false otherwise
def hasQuestions(questionList):
    
    numQuestions = 0
    for i in questionList:

        if getInfo(i,QUESTION) != NO_QUESTION:
            numQuestions += 1
    if numQuestions > 0:
        return True
    else:
        return False
    



# Asks user which question he/she wants to answer
# See Day 26 slides for example try/except
# parameter:  questionList - list of 9 CSV formatted questions
# return: a valid index into questionList
def getQuestionIndex(questionList):
    while True:
        try:
            getQuest = int(input("Choose a number"))
            nonIndex = getInfo(questionList[getQuest], QUESTION)
            if getQuest >= 0 and getQuest <= 9 and nonIndex != NO_QUESTION:
                return getQuest
                           

            


            else:
                print("invalid error")

        except Exception:
            print("invalid error")
        
                       

                       

    





##########################################
## Main
##################################

# Put your main game loop code here!

# Constant for filename
QUESTION_FILENAME = "jeopardy.csv"

#newList = loadCSV(QUESTION_FILENAME)


#categoryList = getCategoryList(newList)


#questList = getQuestionList(newList, categoryList)


#printList = printBoard(questList)
#print(printList)


###############################################
#main game loop function
###############################################
def mainGame():

    winValues = 0

    newList = loadCSV(QUESTION_FILENAME)
    categoryList = getCategoryList(newList)
    questList = getQuestionList(newList, categoryList)

    print("The categories for this game are" , categoryList)

    while hasQuestions(questList):
        print("Your current winnings are" , winValues)
        printBoard(questList)

        indexCue = getQuestionIndex(questList)
        print('You got this question:' , indexCue)

        file = input("The category for this round is:" + getInfo(questList[indexCue], CATEGORY) + "\nThe question is: " + getInfo(questList[indexCue], QUESTION))

        if getInfo(questList[indexCue], ANSWER) in file:
            winValues += int(getInfo(questList[indexCue], VALUE))
            print('YOU ARE CORRECT')

        else:
            print('You are wrong!, the correct answer is:', getInfo(questList[indexCue], ANSWER))

    print('GAME OVER')
    print('Your total winnings for this game of jeopardy :' , winValue)

mainGame()
                            
                     
        
        
    

    



