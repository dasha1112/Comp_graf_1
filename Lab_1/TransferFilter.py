import numpy as np
import math

def transfer_filter (img):
    x, y = img.shape[:2] # получаем высоту и ширину исходного изображения
    result_img = np.zeros((x, y, 3), dtype=np.uint8)  # новое изображение для результата

    # Применяем формулу для переноса пикселей ( x(k, l) = k +50, y(k, l) = l)
    for k in range(y - 50):  # вычитаем 50, чтобы не выйти за пределы изображения
        for l in range(x):
            result_img[l, k] = img[l, k + 50]

    return result_img


def volna_filter(img):
    x, y = img.shape[:2]  # получаем высоту и ширину исходного изображения
    result_img = np.zeros((x, y, 3), dtype=np.uint8)  # новое изображение для результата

    for k in range(y):  # перебираем все столбцы пикселей
        for l in range(x):  # перебираем все строки пикселей
            wave_shift = int(
                20 * math.sin((2 * math.pi * l) / 60))  # вычисляем смещение для каждой строки по синусоидальной функции
            result_k = k + wave_shift  # применяем смещение к столбцу
            if result_k >= 0 and result_k < y:  # проверяем, чтобы новый индекс находился в пределах изображения
                result_img[l, k] = img[l, result_k]  # сохраняем значение пикселя из исходного изображения
            else:
                result_img[l, k] = img[
                    l, k]  # если индекс выходит за пределы изображения, оставляем значение без изменений

    return result_img

def povorot_filter(img, angle):
    x, y = img.shape[:2]  # получение высоты и ширины изображения
    result_img = np.zeros((x, y, 3), dtype=np.uint8)  # новое изображение для результата

    angle_rad = math.radians(angle)  # перевод угла в радианы
    center_x = x // 2
    center_y = y // 2

    # Поворот изображения
    for k in range(y):
        for l in range(x):
            new_k = int((k - center_x) * math.cos(angle_rad) - (l - center_y) * math.sin(angle_rad) + center_x)
            new_l = int((k - center_x) * math.sin(angle_rad) + (l - center_y) * math.cos(angle_rad) + center_y)

            if 0 <= new_k < x and 0 <= new_l < y:
                result_img[l, k] = img[new_l, new_k]

    return result_img

def steclo_filter (img):
    x, y = img.shape[:2]  # получаем высоту и ширину исходного изображения
    result_img = np.zeros((x, y, 3), dtype=np.uint8)  # новое изображение для результата

    for k in range(y):
        for l in range(x):
            offset = int((np.random.random() - 0.5) * 10)  # генерация случайного целочисленного смещения
            new_k = k + offset  # новое значение k с учетом смещения
            if 0 <= new_k < y:  # проверка, чтобы не выйти за пределы изображения
                result_img[l, k] = img[l, new_k]
            else:
                result_img[l, k] = img[l, k]  # если значение выходит за пределы, оставляем без изменений

    return result_img

def motion_blur_filter(img, size):
    x, y = img.shape[:2]  # получаем высоту и ширину исходного изображения
    result_img = np.copy(img)  # создаем копию исходного изображения для результата

    kernel = np.zeros((size, size))  # создаем матрицу размытия заданного размера
    np.fill_diagonal(kernel, 1)  # заполняем диагональ матрицы размытия единицами

    # Применяем матрицу размытия к каждому пикселю изображения
    for i in range(y - size):
        for j in range(x):
            result_img[j, i:i + size] = np.dot(result_img[j, i:i + size], kernel.T)

    return result_img
