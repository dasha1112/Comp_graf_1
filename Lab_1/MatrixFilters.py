import numpy as np

def apply_filter(imп, filter_matrix, padding_type='reflect'):
    result_image = np.zeros_like(imп)  # матрица для хранения результата
    filter_height, filter_width = filter_matrix.shape  # размер матрицы фильтра
    image_height, image_width, _ = imп.shape  # размер изображения
    radius = filter_width // 2

    # добавляем дополнительные строки и столбцы по границам изображения, для обработки границ
    padded_image = np.pad(imп, ((radius, radius), (radius, radius), (0, 0)), mode=padding_type)

    for y in range(radius, image_height + radius):  # проходимся по каждой оси
        for x in range(radius, image_width + radius):
            for c in range(3):  # цикл по каналам (RGB)
                # Применение фильтра к участку изображения (умножение окрестности пикселя и матрицы фильтра)
                result_image[y - radius, x - radius, c] = np.sum(
                    padded_image[y - radius:y + radius + 1, x - radius:x + radius + 1, c] * filter_matrix)

    return result_image


def tisnenie_filter(img, filter_matrix, padding_type='reflect'):
    gray_img = np.dot(img[..., :3], [0.299, 0.587, 0.114])

    result_image = np.zeros_like(gray_img)  # Матрица для хранения результата
    filter_height, filter_width = filter_matrix.shape  # Размер матрицы фильтра
    image_height, image_width = gray_img.shape  # Размер изображения

    radius = filter_width // 2

    # Добавляем дополнительные строки и столбцы по границам изображения для обработки границ
    padded_image = np.pad(gray_img, ((radius, radius), (radius, radius)), mode=padding_type)

    for y in range(radius, image_height + radius):
        for x in range(radius, image_width + radius):
            # Применение фильтра к участку изображения (умножение окрестности пикселя и матрицы фильтра)
            result_image[y - radius, x - radius] = np.sum(
                padded_image[y - radius:y + radius + 1, x - radius:x + radius + 1] * filter_matrix)

    # Увеличение значений на 255 и деление на 2
    adjusted_result = (result_image + 255) / 2

    return adjusted_result