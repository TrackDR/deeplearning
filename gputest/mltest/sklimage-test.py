# https://scikit-image.org/

from skimage import data, io, filters
image = data.coins()
edges = filters.sobel(image)
io.imshow(edges)
io.show()
io.imshow(image)
