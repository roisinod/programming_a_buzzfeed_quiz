results = []
def question1():
    questionslist = ['What form does a boggart take in front of Molly Weasley?', 'How many players are on a Quidditch team?', 'Which of these is NOT an ingredient of Polyjuice Potion?']
    print(questionslist[0])
    print('A: Her dead family ')
    print('B: Voldemort\'s face')
    print('C: The Burrow burning')
    print('D: Hogwarts destroyed')
    Answer = input('Answer A, B, C or D: ').upper()
    print(Answer)
    if Answer == 'A':
        print('Correct!')
        results.append(1)
    else:
        print('Incorrect')
question1()

def question2():
    questionslist = ['What form does a boggart take in front of Molly Weasley?', 'How many players are on a Quidditch team?', 'Which of these is NOT an ingredient of Polyjuice Potion?']
    print(questionslist[1])

    print('A: 7')
    print('B: 9')
    print('C: 12')
    print('D: 14')
    Answer = input('Answer A, B, C or D: ').upper()
    print(Answer)
    if Answer == 'A':
        print('Correct!')
        results.append(1)
    else:
        print('Incorrect')

question2()
def question3():
    questionslist = ['What form does a boggart take in front of Molly Weasley?', 'How many players are on a Quidditch team?', 'Which of these is NOT an ingredient of Polyjuice Potion?']
    print(questionslist[2])
    print('A: Boomslang skin')
    print('B: Lacewing flies')
    print('C: Horn of Bicorn')
    print('D: Unicorn hair')
    Answer = input('Answer A, B, C or D: ').upper()
    print(Answer)
    if Answer == 'D':
        print('Correct!')
        results.append(1)
    else:
        print('Incorrect')

question3()

print('You got', sum(results), 'out of 3')