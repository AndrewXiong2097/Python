'''
The Objective of this program is to quiz the user on basic high school
trivia. The tasks to complete are:
Ask the user each of the following questions:
    1) What is the powerhouse of the cell?
        A) mitochondria B) nucleus C) ribosome
    2) How many states comprise the United States?
        A) 13 B) 45 C) 50
    3) In y = mx + b, what does m stand for?
        A) slope B) output C) I don't understand math
    4) In English, a person, place or thing is called:
        A) verb B) adjective C) noun
The user should input a letter for each question. (A, B, or C)
Check the users answer, if it is correct print "Correct",
 else it should print "Incorrect, the correct answer is [insert]"
Additionally, the program should track how many questions the user 
got correct and at the end give them a score out of 4. And give them a percentage.

@author: Andrew Xiong
'''
#Make a variable called score to keep track of the correct answers. And set
#it to 0.
score = 4
#Ask the user question one. And store the users answer.
"What is the powerhouse of the cell?"
a = "mitochondria"
b = "nucleus"
c = "ribosome"
choice = a
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
print("Correct")
#Ask the user question two. And store the users answer.
"How many states comprise the United States?"
a = 13
b = 45
c = 50
choice = c
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
print("Correct")
#Ask the user question three. And store the users answer.
"In y = mx + b, what does m stand for?"
a = "slope"
b = "output"
c = "I don't understand math"
choice = a 
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
print("Correct")
#Ask the user question four. And store the users answer.
"In English, a person, place or thing is called:"
a = "verb"
b = "adjective"
c = "noun"
choice = c
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
print("Correct")
#Calculate the percentage the user got. And store it in a variable called p
p = 100
#Print out the users score: "You got a [score]/4. Or a [p]%."
print("You got a 4/4. or 100%.")