import random

class Question:
 def __init__(self, questionText, multipleChoiceOptions):
    self.questionText = questionText
    self.multipleChoiceOptions = multipleChoiceOptions

quizQuestions = [
  Question("What is India's capital city?", ["(a) Hyderabad", "(b) New Delhi", "(c) Bangalore", "(d) Mumbai"]),
  Question("Who is the prime minister of India?", ["(a) Narendra Modi", "(b) Pranab Mukharji", "(c) Venkaiah Naidu", "(d) Amit Shah"]),
  Question("Who is the present Indian Cricket Team Captain?", ["(a) KL Rahul", "(b) Virat Kohli", "(c) Rohit Sharma", "(d) Hardik Pandya"])
]

answersSubmitted = []

def ask_question(question):
    print(f"{question.questionText}?")
    for option in question.multipleChoiceOptions:
        print(option)
    answer = input("\nChoice? ") 
    print("\n")
    if answer.lower() not in ('a', 'b', 'c', 'd', 'quit'):
        print("Accepted answers: 'a','b','c','d' or 'quit' to quit",end="\n\n")
        ask_question(question)
    else:
        if answer.lower() != "quit":
            answersSubmitted.append((question.questionText,answer))
    if answer == "quit":
        print_question(answersSubmitted)
        quit()
        
def print_question(answersSubmitted):
    print("\nAnswers Submitted: ", end="\n\n")
    for (question, answer) in answersSubmitted:
        print(question + " : " + answer, end="\n\n")
    
for question in random.sample(quizQuestions,len(quizQuestions)):
    ask_question(question)

print_question(answersSubmitted)