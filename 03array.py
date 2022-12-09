import random

q = [
    "What is India's capital city? a. Hyderabad b. New Delhi c. Bangalore d. Mumbai",
    "Who is the prime minister of India? a. Narendra Modi b. Pranab Mukharji c. Venkaiah Naidu d. Amit Shah",
    "Who is the present Indian Cricket Team Captain? a. KL Rahul b. Virat Kohli c. Rohit Sharma d. Hardik Pandya"
]

a = []

for value in random.sample(q,len(q)):
    print(f"{value}", end="\n")
    answer = input("\nChoice? ")
    if answer.lower() not in ('a', 'b', 'c', 'd', 'quit'):
        print("Accepted answers: 'a','b','c','d' or 'quit' to quit",end="\n\n")
        continue
    if answer == "quit":
        break
    a.append((value,answer))

print("Answers Submitted: ", end="\n\n")
    
for (question, answer) in a:
    print(question + " : " + answer, end="\n\n")