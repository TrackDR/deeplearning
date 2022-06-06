import tensorflow as tf
import time

print( tf.constant( 'Hello from TensorFlow ' + tf.__version__ ) )
device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
  raise SystemError('GPU device not found')
print('Found GPU at: {}'.format(device_name))

