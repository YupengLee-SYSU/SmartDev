from MLEngineApp.model.ModelDemo import DemoNet
import torch
import matplotlib.pyplot as plt

class Trainer:
    def __init__(self, net, optimizer, loss_func):
        self.optimizer = None
        self.net = net
        self.optimizer = optimizer
        self.loss_func = loss_func
        self.loss = None

    def test(self):
        print(self.net.parameters)

    def model_train(self, data, object):
        self.optimizer = self.optimizer(self.net.parameters(), lr=0.2)
        for i in range(100):
            prediction = self.net.forward(data)
            self.loss = self.loss_func(prediction, object)
            self.optimizer.zero_grad()
            self.loss.backward()
            self.optimizer.step()
            if i % 5 == 0:
                # plot and show learning process
                plt.cla()
                plt.scatter(data.data.numpy(), object.data.numpy())
                plt.plot(data.data.numpy(), prediction.data.numpy(), 'r-', lw=5)
                plt.text(0.5, 0, 'Loss=%.4f' % self.loss.data.numpy(), fontdict={'size': 20, 'color': 'red'})
                plt.pause(0.1)
        return

