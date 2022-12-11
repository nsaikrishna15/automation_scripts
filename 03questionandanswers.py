import random

class Question:
 def __init__(self, questionText, multipleChoiceOptions):
    self.questionText = questionText
    self.multipleChoiceOptions = multipleChoiceOptions

quizQuestions = [
  Question("What is your favourite colour?", ["(a) Red", "(b) Green", "(c) Blue", "(d) Orange"]),
  Question("Who is your favorite mobile phone brand?", ["(a) Samsung", "(b) Apple", "(c) Huawei", "(d) Oneplus"]),
  Question("Which cricket team do you like", ["(a) India", "(b) England", "(c) Australia", "(d) NewZealand"]),
  Question("Whis season do you like the most", ["(a) Summer", "(b) Autumn", "(c) Winter ", "(d) Rainy"]),
  Question("What is your favorite sport?", ["(a) Cricket", "(b) Hockey", "(c) Football", "(d) Basketball"]),
  Question("What is your favorite web browser?", ["(a) Chrome", "(b) Firefox", "(c) Safari", "(d) MS-edge"]),
  Question("In which cloud have you worked most?", ["(a) AWS", "(b) Azure", "(c) GCP", "(d) IBMCloud"]),
  Question("Who is your favorite actor?", ["(a) Brad Pitt", "(b) Dwayne Johnson", "(c) Leonardo Decaprio", "(d)Matt damon "]),
  Question("What operating system do you prefer?", ["(a) Windows", "(b) Mac", "(c) Ubuntu", "(d) Bsd"]),
  Question("What is your age group?", ["(a) 10-25", "(b) 26-50", "(c) 51-70", "(d) 71-90"])

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