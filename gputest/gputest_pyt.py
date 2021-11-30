from __future__ import print_function
import torch
from torch.utils.collect_env import get_pretty_env_info

x = torch.rand(5, 3)
print(x)

print("Cuda Available:",torch.cuda.is_available())
print("Cuda version:",torch.version.cuda)
print("Cuda Device Name:", torch.cuda.get_device_name())
print("Cuda Device Capability:", torch.cuda.get_device_capability())
current_device = torch.cuda.current_device()
print("Current Device:",current_device)
torch.cuda.get_device_properties(current_device)
print(get_pretty_env_info())
