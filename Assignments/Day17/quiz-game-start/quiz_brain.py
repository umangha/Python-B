class QuizBrain:

    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        """Returns True if there are more questions"""
        # length_of_list = len(self.question_list)
        # if self.question_number < length_of_list:
        #     return True
        # return False

        return self.question_number < len(self.question_list)

    def next_question(self):
        """ Asks user question according to the index in list"""
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_input = input(f"Q.{self.question_number}: {current_question.text}. (True or False): ")
        self.check_score(user_input,current_question.answer)
    
    def check_score(self,user_answer,correct_answer):
        """If answer correct increases score and prints the result"""
        if user_answer.lower() == correct_answer.lower():
            self.score +=1
            print("You are right!!")
        else: 
            print("You are wrong")
        print(f"The Correct answer was: {correct_answer}")
        print(f"Your Current Score is: {self.score}/{len(self.question_list)}\n")

