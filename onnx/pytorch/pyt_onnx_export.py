# https://deci.ai/resources/blog/how-to-convert-a-pytorch-model-to-onnx/
# conda install -c conda-forge onnx

import torch
import torchvision.models as models
model = models.resnet50(pretrained=True)

# ensure model is in inference mode
model.eval()

# Next, we create that dummy input variable.
dummy_input = torch.randn(1, 3, 224, 224)

# Let’s also define the input and output names.
input_names = [ "actual_input" ]
output_names = [ "output" ]

torch.onnx.export(model, 
                  dummy_input,
                  "resnet50.onnx",
                  verbose=False,
                  input_names=input_names,
                  output_names=output_names,
                  export_params=True,
                  )
