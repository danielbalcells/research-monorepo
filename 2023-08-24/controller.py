from chain import MyChain
from question import Question


class MTMController:

    def __init__(self, verbose=True):
        self.verbose = verbose
        self.chain = MyChain(verbose=self.verbose)
        self.questions = []
        self.responses = []

    def run(self):
        human_input = self.get_initial_question()
        while human_input != 'quit':
            next_questions = self.get_questions(human_input)
            self.questions += next_questions
            human_input = self.get_answer(next_questions)
            self.responses.append(human_input)

    def get_initial_question(self):
        question = input("What's on your mind?\n")
        self.initial_question = question
        return question

    def get_questions(self, human_input):
        questions_str = self.chain.interact(human_input)
        return [Question(q) for q in questions_str]

    def get_answer(self, next_questions):
        for q in next_questions:
            print(q)
        answer = input(
            "\nPlease enter your answer to one of the questions above.\n"
        )
        return answer
