import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def showPopUp(path):
    ImageItself = Image.open(path)
    ImageNumpyFormat = np.asarray(ImageItself)
    plt.imshow(ImageNumpyFormat)
    plt.show()
