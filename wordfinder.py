from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""
   
    def __init__(self, file_path):
        self.file_path = file_path
        self.word_list = []
        self.read_file()
        self.words_read()

    def __repr__(self):
        return f'WordFinder(file_path = "words.txt")'    

    def read_file(self):
        file = open(self.file_path, 'r')

        for line in file:
            new_line = line.strip()
            self.word_list.append(new_line)

        file.close()  

    def words_read(self):
        print(f'read {len(self.word_list)} words')      

    def random_word(self):
        return choice(self.word_list)

class WordParser(WordFinder):
    """WordParser: Parses words out of txt files contain words, comments and blank spaces. """

    def __init__(self, file_path):
        super().__init__(file_path)
        self.parse()
        

    def __repr__(self):
        return f'WordParser(file_path = "words.txt")'

    def parse(self):
        new_list = []
        for word in self.word_list:
            if word != '':
                if word[0] != '#':
                    new_list.append(word)

        self.word_list = new_list         


