import numpy as np
import matplotlib.pyplot as plt
def gaussian_kernel_1d(size):
	size = int(size)
	x = np.mgrid[-size:size+1]

	g = np.exp(-(x**2/float(size)))

	return g


# blur with customized Gaussian filter
size = 1
g1= gaussian_kernel_1d(size)
print(g1.shape)

plt.plot(g1)
plt.show()

g_2 = np.outer(np.transpose(g1),g1)

print(g_2.shape)


plt.imshow(g_2,cmap=plt.cm.gray)
plt.show()