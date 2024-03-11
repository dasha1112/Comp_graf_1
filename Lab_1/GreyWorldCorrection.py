import numpy as np

def grey_world_correction (img):
    # Рассчитываем средние значения яркости по каналам
    avg_b = np.mean(img[:, :, 0])
    avg_g = np.mean(img[:, :, 1])
    avg_r = np.mean(img[:, :, 2])

    # Рассчитываем коэффициенты масштабирования яркости
    avg_gray = (avg_b + avg_g + avg_r) / 3
    scale_b = avg_gray / avg_b
    scale_g = avg_gray / avg_g
    scale_r = avg_gray / avg_r

    # Масштабируем значения пикселей
    corrected_img = np.zeros_like(img, dtype=np.float64)
    corrected_img[:, :, 0] = img[:, :, 0] * scale_b
    corrected_img[:, :, 1] = img[:, :, 1] * scale_g
    corrected_img[:, :, 2] = img[:, :, 2] * scale_r

    # Ограничиваем значения пикселей до максимально возможного диапазона (0-255)
    corrected_img = np.clip(corrected_img, 0, 255)
    corrected_img = np.uint8(corrected_img)
    return corrected_img

def histogram_stretching (img):
    # Находим минимальное и максимальное значение пикселя в изображении
    min_val = np.min(img)
    max_val = np.max(img)

    # Растягиваем гистограмму
    stretched_image = (img - min_val) / (max_val - min_val) * 255

    # Приведение значений к допустимому диапазону для отображения
    stretched_image = np.clip(stretched_image, 0, 255)

    return stretched_image.astype(np.uint8)


def reference_color_correction(img, color):
    avg_b = np.mean(img[:, :, 0])
    avg_g = np.mean(img[:, :, 1])
    avg_r = np.mean(img[:, :, 2])

    #avg_gray = (avg_b + avg_g + avg_r) / 3
    scale_b = color / avg_b
    scale_g = color / avg_g
    scale_r = color / avg_r

    corrected_img = np.zeros_like(img, dtype=np.float64)
    img_mean = np.mean(corrected_img, axis=(0, 1))
    ref_mean = np.mean(corrected_img, axis=(0, 1))

    corrected_img_corr = corrected_img - img_mean + ref_mean
    corrected_img[:, :, 0] = img[:, :, 0] * scale_b
    corrected_img[:, :, 1] = img[:, :, 1] * scale_g
    corrected_img[:, :, 2] = img[:, :, 2] * scale_r

    corrected_img = np.clip(corrected_img, 0, 255)
    corrected_img = np.uint8(corrected_img)
    return corrected_img

def perfect_reflector_correction(img):
    # Рассчитываем средние значения яркости по каналам
    avg_b = np.mean(img[:, :, 0])
    avg_g = np.mean(img[:, :, 1])
    avg_r = np.mean(img[:, :, 2])

    # Находим максимальное среднее значение яркости
    max_avg = max(avg_b, avg_g, avg_r)

    # Рассчитываем коэффициенты масштабирования яркости на основе максимального значения
    scale_b = max_avg / avg_b
    scale_g = max_avg / avg_g
    scale_r = max_avg / avg_r

    # Масштабируем значения пикселей
    corrected_img = np.zeros_like(img, dtype=np.float64)
    corrected_img[:, :, 0] = img[:, :, 0] * scale_b
    corrected_img[:, :, 1] = img[:, :, 1] * scale_g
    corrected_img[:, :, 2] = img[:, :, 2] * scale_r

    # Ограничиваем значения пикселей до максимально возможного диапазона (0-255)
    corrected_img = np.clip(corrected_img, 0, 255)
    corrected_img = np.uint8(corrected_img)
    return corrected_img
