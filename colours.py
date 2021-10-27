import os

class Colour:
    QUESTION = '\033[94m'
    CORRECT = '\033[92m'
    ERROR = '\033[91m'
    END = '\033[0m'
    
    @staticmethod
    def question(x):
        return (Colour.QUESTION + x + Colour.END)

    @staticmethod
    def correct(x):
        return (Colour.CORRECT + x + Colour.END)

    @staticmethod
    def error(x):
        return (Colour.ERROR + x + Colour.END)

if __name__ == '__main__':
    print(Colour.question("Hello\tGood"))
    print(Colour.solution("Hello\tOk"))