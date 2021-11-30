from __future__ import print_function
import torch

x = torch.rand(5, 3)
print(x)

print("Cuda Available:",torch.cuda.is_available())
print("Cuda version:",torch.version.cuda)
