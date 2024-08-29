from question_model import Question
from data import question_data
from quiz_brain import Quizbrain


question_bank = []

for question in question_data:         
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)  #assign new question to class objects
    question_bank.append(new_question)    #append question to q bank

quiz = Quizbrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("Completed the quiz")
print(f"Your final score is: {quiz.total_score()}")

