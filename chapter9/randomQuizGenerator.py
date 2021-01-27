#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random
import os

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 
   'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# go to quiz directory to keep created files in one place
os.chdir('/Users/laurencefinch/Desktop/AutomateBoringStuff/Quizes')

# Generate 35 quiz files.
for quizNum in range(35):
    # Create the quiz and answer key files.
    quizName = 'Quiz' + str(quizNum + 1)
    answerName = 'Answer' + str(quizNum + 1)
    quizFile = open(quizName, 'w')
    answerFile = open(answerName, 'w')

    # Write out the header for the quiz.
    quizFile.write(f"this is {quizNum} quiz\nName:\nDate:\n")
    answerFile.write(f"this is {quizNum} answer\n")

    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
    
        # add question (state) and answers (capital)
        # write state
        quizFile.write(f'Question: {questionNum +1}\tWhat is the capital of {states[questionNum]}?\n')
        # write answer options
        for i in range(4):
            quizFile.write(f"\t{'ABCD'[i]}.{answerOptions[i]}\n")
        # write answer file
        answerFile.write(f"{questionNum +1}: {'ABCD'[answerOptions.index(correctAnswer)]}\n")
    
    # close the files
    quizFile.close()
    answerFile.close()
    




