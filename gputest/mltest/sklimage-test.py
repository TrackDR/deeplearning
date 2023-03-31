# https://scikit-image.org
# https://github.com/scikit-image/skimage-tutorials

from skimage import data, io, filters
image = data.coins()
edges = filters.sobel(image)
io.imshow(edges)
io.show()
io.imshow(image)
