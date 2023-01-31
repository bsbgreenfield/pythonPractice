from random import choice


class WordFinder:
    def __init__(self, filename):
        file = open(filename, 'r')
        self.word_list = self.make_list(file)
        print(f'{len(self.word_list)} words read')

    def make_list(self, file):
        return [word.strip() for word in file]

    def get_random(self):
        return choice(self.word_list)


class RandomWordFind(WordFinder):

    def make_list(self, file):
        return [word.strip() for word in file if word.strip() and not word.startswith("#")]


rwf = RandomWordFind("C:\\Users\\bsbgr\\PycharmProjects\\OOOprac\\words.txt")
