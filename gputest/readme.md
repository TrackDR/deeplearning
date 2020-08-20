### Update (Ana)conda first 
conda update conda

conda update anaconda

conda update python

conda update --all

### Tensorflow-gpu install
conda create --name tf-gpu

conda info --envs

conda activate tf-gpu

conda install tensorflow-gpu

conda install shapely

conda install scikit-image

conda install ipykernel jupyter

conda install pandas

conda install spyder

OPTIONAL: pip install tf-nightly

python -m ipykernel install --user --name tf-gpu --display-name "TensorFlow-GPU"

### Pytorch install
conda create --name pyt-gpu

conda info --envs

conda activate pyt-gpu

conda install pytorch torchvision cudatoolkit=10.2 -c pytorch
