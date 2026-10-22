import random

class Hangman:
    def __init__(self):
        self.secret = ''
        self.correct = []
        self.wrong = []
        self.disp = ''

    def get_random_word(self):
        words = ['programming', 'debugging', 'inheritance', 'polymorphism', 'encapsulation', 'composition']
        r = random.randint(0, len(words)-1)
        self.secret = words[r]
        self.create_display_from_secret()

    def create_display_from_secret(self):
        disp = self.secret[0]
        for i in range(1, len(self.secret)-1):
            if self.secret[i] in self.correct:
                disp += self.secret[i]
            else:
                disp += '_'
        disp += self.secret[-1]
        self.disp = disp

    def display_secret(self):
        print(self.disp)

    def play(self):
        ch = input("Guess a character: ")
        if ch in self.secret and ch not in self.correct:
            self.correct.append(ch)
        if ch not in self.secret and ch not in self.wrong:
            self.wrong.append(ch)
        self.create_display_from_secret()

    def word_found(self):
        if self.disp == self.secret:
            return True 
        else:
            return False

    def is_hanged(self):
        if len(self.wrong) == 6:
            return True 
        else:
            return False

    def can_play(self):
        if not self.word_found() and not self.is_hanged():
            return True
        else:
            return False


h = Hangman()
h.get_random_word()
while h.can_play():
    h.display_secret()
    h.play()
    if h.word_found():
        print("You found it!")
    elif h.is_hanged():
        print("You are hanged ...")
print("GAME OVER")

