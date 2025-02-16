# Monkey patching
# https://medium.com/analytics-vidhya/monkey-patching-in-python-dc3b3f52906c
class MonkeyPatch:
    def __init__(self, num):
        self.num = num

    def addition(self, other):
        #return (self.num + other)
        raise Exception('Something went wrong', self.num, other)

#obj = MonkeyPatch(10)
#obj.addition(20) # 30

#def subtraction(self, num2):
#    return self.num - num2

#MonkeyPatch.subtraction = subtraction
#obj.subtraction(1)
