class Predicter:
    def __init__(self, net):
        self.net = net

    def predict(self, input):
        return self.net.forward(input)