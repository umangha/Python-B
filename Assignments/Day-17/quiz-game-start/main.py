from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# TODO List of Objects of Question class needed
questions=[]

for question in question_data:
    # 'question_data' is a list of dictionary so 'question' is dict
    text = question["text"]
    answer = question["answer"]

    new_question = Question(text,answer)
    questions.append(new_question)


# Creating a object of QuizBrain Class
quiz_brain = QuizBrain(question_list=questions)

while quiz_brain.still_has_question():
    quiz_brain.next_question()

# Printing the result of the game
print("You have completed the quiz game.")
print(f"Your final score is {quiz_brain.score}/{len(questions)}")
