# https://deci.ai/resources/blog/how-to-convert-a-pytorch-model-to-onnx/
# pip install onnxruntime

import onnxruntime as onnxrt
import torch

onnx_session= onnxrt.InferenceSession("resnet50.onnx")

img = torch.randn(1, 3, 224, 224)
input_name = onnx_session.get_inputs()[0].name
onnx_inputs = {input_name:img.numpy()}
onnx_output = onnx_session.run(None, onnx_inputs)
img_label = onnx_output[0]
maxidx = img_label.argmax()
maxval = img_label[0,maxidx]
