
class GTFSFile:
    name = None
    variables = []
    data = []

    def json(self):
        return {
            "name": self.name,
            "variables": self.variables,
            "data": [x.__dict__ for x in self.data]
        }
