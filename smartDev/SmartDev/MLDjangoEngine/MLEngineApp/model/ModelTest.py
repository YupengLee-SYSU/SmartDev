import matplotlib.pyplot as plt
import torch
from MLEngineApp.model.ModelDemo import DemoNet
from MLEngineApp.executors.Trainer import Trainer

x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)  # x data (tensor), shape=(100, 1)
y = x.pow(2) + 0.2 * torch.rand(x.size())  # noisy y data (tensor), shape=(100, 1)

plt.scatter(x.data.numpy(), y.data.numpy())
plt.show()

net = DemoNet(n_feature=1, n_hidden=10, n_output=1)

print(net)

trainer = Trainer(net=net,loss_func=torch.nn.MSELoss(), optimizer=torch.optim.SGD)

trainer.test()
#
# trainer.model_train(x, y)

