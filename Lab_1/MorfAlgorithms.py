import numpy as np

def dilation(binary_image, maska):
    height, width = binary_image.shape[:2]  # Размер изображения
    result = np.zeros_like(binary_image)  # Массив для хранения результата
    maska_size = len(maska) # Размер маски (структурного множества)
    half_size = maska_size // 2

    # Проходимся по изображению
    for y in range(half_size, height - half_size):
        for x in range(half_size, width - half_size):
            # Проверяем есть ли хоть один пиксель со значением больше 0 и если да, то результирующий пиксель равняется 1
            if np.any(binary_image[y - half_size:y + half_size + 1, x - half_size:x + half_size + 1] * maska):
                result[y, x] = 1
    return result

def erosion(binary_image, maska):
    height, width = binary_image.shape[:2]  # Размер изображения
    result = np.zeros_like(binary_image)  # Массив для хранения результата
    maska_size = len(maska)  # Размер маски (структурного элемента)
    half_size = maska_size // 2

    for y in range(half_size, height - half_size):
        for x in range(half_size, width - half_size):
            # Проверяем все ли элементы получееной области равны 1 и если да, то результирующий пиксель равняется 1
            if np.all(binary_image[y - half_size:y + half_size + 1, x - half_size:x + half_size + 1] * maska == maska):
                result[y, x] = 1
    return result

def opening(binary_image, kernel):
    result = erosion(binary_image, kernel)  # Применяем эрозию
    result = dilation(result, kernel)  # Затем применяем расширение
    return result

def closing(binary_image, kernel):
    result = dilation(binary_image, kernel)  # Применяем расширение
    result = erosion(result, kernel)  # Затем применяем эрозию
    return result

def black_hat(binary_image, kernel):
    result = binary_image - erosion(binary_image, kernel)  # Разница между изображением и его эрозией
    return result

def top_hat(binary_image, kernel):
    result = dilation(binary_image, kernel) - binary_image  # Разница между расширением и изображением
    return result