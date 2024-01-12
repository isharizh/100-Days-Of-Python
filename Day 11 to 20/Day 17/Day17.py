from question_model import Questions
from data import question_data
from quiz_brain import Quiz

question_bank = []
for q in question_data:
    qtext = q["question"]
    qans = q["correct_answer"]
    nq = Questions(qtext,qans)
    question_bank.append(nq)

quiz = Quiz(question_bank)
while quiz.still():
    quiz.next()
    print('\n')
print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.qno}")