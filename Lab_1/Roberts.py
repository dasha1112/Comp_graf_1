import numpy as np
import math

def roberts_operator(image):
    weights = [0.2989, 0.5879, 0.1140]
    img1 = np.dot(image[..., :3], weights)
    img2 = np.zeros_like(img1)

    img2 = np.zeros_like(img1)

    height, width = img1.shape

    hor_filter = np.array([[1, 0], [0, -1]]) # определение горизонтального фильтра
    ver_filter = np.array([[0, 1], [-1, 0]]) # определение вертикального фильтра

    for i in range(0, height - 1):
        for j in range(0, width - 1):
            pixels1 = np.array([
                [img1[i, j], img1[i, j + 1]],
                [img1[i + 1, j], img1[i + 1, j + 1]]
            ])

            pixels2 = np.array([
                [img1[i, j], img1[i, j + 1]],
                [img1[i + 1, j], img1[i + 1, j + 1]]
            ])

            x = abs(np.sum(np.multiply(hor_filter, pixels1)))
            y = abs(np.sum(np.multiply(ver_filter, pixels2)))
            result = math.sqrt(x ** 2 + y ** 2)
            img2[i, j] = result

    return img2

def sobel_operator(image):
    weights = [0.2989, 0.5870, 0.1140]
    img1 = np.dot(image[..., :3], weights)
    img2 = np.zeros_like(img1)

    height, width = img1.shape

    horizontal_sobel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    vertical_sobel = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            pixels = img1[i-1:i+2, j-1:j+2]
            x = np.sum(horizontal_sobel * pixels)
            y = np.sum(vertical_sobel * pixels)
            img2[i, j] = np.sqrt(x**2 + y**2)

    return img2

def prewitt_operator(image):
    weights = [0.2989, 0.5870, 0.1140]
    img1 = np.dot(image[..., :3], weights)
    img2 = np.zeros_like(img1)

    height, width = img1.shape

    horizontal_prewitt = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    vertical_prewitt = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            pixels = img1[i-1:i+2, j-1:j+2]
            x = np.sum(horizontal_prewitt * pixels)
            y = np.sum(vertical_prewitt * pixels)
            img2[i, j] = np.sqrt(x**2 + y**2)

    return img2
