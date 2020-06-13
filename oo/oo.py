class Language:
    _all = []

    def __init__(self, name, eng_name):
        self.name = name
        self.in_english = eng_name
        self.words = {}
        self._save()

    def _save(self):
        self._all.append(self)
    
    def add_word(self, english, translation):
        self.words[english] = translation
    
    def _translate(self, word):
        return self.words[word]

    def how_do_you_say(self, word):
        print(f"In {self.name}, '{word}' is '{self._translate(word)}'.")

    @classmethod
    def print_all(cls):
        print("We have the following languages:")
        for lang in cls._all:
            print(lang.name)


spanish = Language("Español", "Spanish")
german = Language("Deutsch", "German")

spanish.add_word("Hello", "Hola")
spanish.how_do_you_say("Hello")


Language.print_all()