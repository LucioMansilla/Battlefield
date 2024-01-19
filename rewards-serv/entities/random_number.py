
class RandomNumber:
    def __init__(self, value):
        self.value = value

    def to_dict(self):
        return {'rng': self.value}
