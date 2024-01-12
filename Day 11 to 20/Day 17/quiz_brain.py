

class Quiz():

    def __init__(self, qlist):
        self.qno = 0
        self.qlist = qlist
        self.score = 0

    def still(self):
        return self.qno < len(self.qlist)

    def next(self):
        curq = self.qlist[self.qno]
        self.qno += 1
        cans = input(f"Q.{self.qno}:{curq.text} (True/False) : ").lower()
        self.check(cans, curq.value)

    def check(self,cans,cqns):
        if cans == cqns.lower():
            print("You got it!")
            self.score += 1
            print(f"Your current score is {self.score}/{self.qno}")
        else:
            print("The Answer is wrong")
            print(f"The correct answer is {cqns}")
            print(f"Your current score is {self.score}/{self.qno}")