class Params:
    def __init__(self, q, locationsearch, startrow):
        self.q = q
        self.locationsearch = locationsearch
        self.startrow = startrow

    def as_dict(self):
        return {
            "q": self.q,
            "locationsearch": self.locationsearch,
            "startrow": self.startrow
        }
