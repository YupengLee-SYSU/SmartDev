import torch
import matplotlib.pyplot as plt
import torch.nn.functional as func

class DemoNet(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(DemoNet, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)
        self.predict = torch.nn.Linear(n_hidden, n_output)
        self.loss = None
        self.optimizer = None
        self.loss_func = None
        self.loss = None

    def forward(self, x):
        x = func.relu(self.hidden(x))
        x = self.predict(x)
        return x


