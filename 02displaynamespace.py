class hello:
    def __init__(self):
        pass
    def displayhello(self):
        return "Hello world"

for name in hello.__dict__:
    print(name)
