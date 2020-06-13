class Cat:
    _all = []

    def __init__(self, name, age, img_url):
        self.name = name
        self.age = age
        self.img_url = img_url
        self._save()

    def _save(self):
        self._all.append(self)

    @classmethod
    def all(cls):
        return cls._all



Cat('Jeremy', 4, 'http://www.cutestpaw.com/wp-content/uploads/2016/02/s-Kitty-yoga.%281%29.jpg')
Cat('Rumble', 7, 'http://www.cutestpaw.com/wp-content/uploads/2016/02/s-Silly-kitty-all-the-birds-went-south....jpg')