from Question import Q1

Quiz = [
    "The first layer in OSI model is:\n(a) Physical\n(b) Transport\n(c) Network\n\n",
    "HTTP is in ...... layer\n(a) Physical\n(b) Application\n(c) Transport\n\n",
    "OSI model has ..... layers\n(a) 7\n(b) 5\n(c) 3\n\n",
    "IP addresses are in ....... layer \n(a) Network\n(b) Physical\n(c) Presentation\n\n",
    "Data in network layer are called \n(a) Segments\n(b) Frames\n(c) Packets\n\n",
]

Answeres = [
    Q1(Quiz[0], "a"),
    Q1(Quiz[1], "b"),
    Q1(Quiz[2], "a"),
    Q1(Quiz[3], "a"),
    Q1(Quiz[4], "c"),
]

def start (Answeres):
    score = 0
    for question in Answeres:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            percentage = (score / 500) * 100;
    if percentage > 0.5:
            print("Good")
    else:
            print("Not Good")


    print("You got" + str(score) + "/" + str(len(Answeres)) + "correct")
start(Answeres)
