Based on https://www.pugetsystems.com/labs/hpc/How-to-Install-TensorFlow-with-GPU-Support-on-Windows-10-Without-Installing-CUDA-UPDATED-1419/

and

https://pytorch.org/get-started/locally/#anaconda

https://pytorch.org/get-started/locally/#windows-verification

https://pytorch.org/tutorials

### Update (Ana)conda first 
conda update conda

conda update anaconda

conda update python

conda update --all

### Tensorflow-gpu install
conda create --name tf-gpu python=3.9

conda info --envs

conda activate tf-gpu

conda install tensorflow-gpu

conda install keras

conda install shapely

conda install scikit-image

conda install ipykernel jupyter

conda install pandas

conda install spyder

OPTIONAL: pip install tf-nightly

python -m ipykernel install --user --name tf-gpu --display-name "TensorFlow-GPU"

### Pytorch install
conda create --name pyt-gpu python=3.9

conda info --envs

conda activate pyt-gpu

conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch

conda install ipykernel jupyter

conda install spyder

conda install matplotlib

python -m ipykernel install --user --name pyt-gpu --display-name "PyTorch-GPU"

conda install -c conda-forge onnx

pip install onnxruntime

conda install -c conda-forge opencv

### Pytorch install alt
conda create --name pyt-gpu2 python=3.9

conda info --envs

conda activate pyt-gpu2

git clone https://github.com/pytorch/tutorials.git

cd tutorials

conda install pytorch torchvision cudatoolkit=10.2 -c pytorch

pip install -r requirements.txt

git clone https://github.com/TrackDR/tutorials-1.git

cd tutorials-1

pip install -r requirements.txt

conda install torchaudio -c pytorch

pip install -r requirements.txt

conda install ipykernel jupyter

conda install spyder

conda install matplotlib

python -m ipykernel install --user --name pyt-gpu2 --display-name "PyTorch-GPU2"

conda uninstall pillow

pip install pillow

conda install torchvision -c pytorch


