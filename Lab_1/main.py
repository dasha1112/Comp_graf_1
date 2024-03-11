import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import GreyWorldCorrection
import MatrixFilters
import Roberts
import TransferFilter
import MorfAlgorithms
import MedianFilter
from PIL import Image

image = mpimg.imread('img_lab1.jpg')
image_1 = mpimg.imread('img_lab1a.png')
image_2 = mpimg.imread('img_lab1b.jpg')
image_3 = mpimg.imread('noisyimg.png')
image_4 = Image.open('img_lab1.jpg')
filter_rezkost = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
filter_tisnenie = np.array([[0, 1, 0], [1, 0, -1], [0, -1, 0]])
blue = np.mean(image[:, :, 0])

print("Введите размерность матрицы:")
a=int(input())
mas = []
print("Введите матрицу:")
for i in range(a):
    mas.append(list(map(int, input().split())))
print(mas)

# Изображения со смещением пикселей
result = TransferFilter.transfer_filter(image)
result_0 = MatrixFilters.apply_filter(image, filter_rezkost)
result_1 = TransferFilter.volna_filter(image)
result_2 = TransferFilter.steclo_filter(image)
result_3 = TransferFilter.povorot_filter(image, 30)
result_3b = MatrixFilters.tisnenie_filter(image, filter_tisnenie)

# Изображения после операций мат. морфологии
result_4 = MorfAlgorithms.dilation(image_1, mas)
result_5 = MorfAlgorithms.erosion(image_1, mas)
result_6 = MorfAlgorithms.closing(image_1, mas)
result_7 = MorfAlgorithms.opening(image_1, mas)
result_7a = MorfAlgorithms.black_hat(image_1, mas)
result_7b = MorfAlgorithms.top_hat(image_1, mas)

# Изображения после медианных фильтров
result_8 = MedianFilter.median_filter(image_3, 3)
result_9 = Roberts.roberts_operator(image)
result_10 = Roberts.sobel_operator(image)
result_11 = Roberts.prewitt_operator(image)
result_11b = image # Результат работы функции Светящиеся края

# Изображения с коррекцией цвета
result_12 = GreyWorldCorrection.grey_world_correction(image)
result_13 = GreyWorldCorrection.perfect_reflector_correction(image)
result_14 = GreyWorldCorrection.reference_color_correction(image, blue)  # Опорный цвет голубой

result_15 = GreyWorldCorrection.histogram_stretching(image_2)

current_index = 0
images = [image_1, result_4, result_5, result_6, result_7, result_7a, result_7b, image, result, result_0, result_1,
          result_2, result_3, result_3b, result_9, result_10, result_11, result_11b, result_12, result_13, result_14,
          image_3, result_8, image_2, result_15]
titles = ['Original picture', 'Dilation', 'Erosion', 'Closing', 'Opening', 'Black hat', 'Top hat',
          'Оригинальное изображение', 'Изображение после переноса', 'Изображение после фильтра резкость',
          'Изображение после фидтра Волна', 'Изобрапосле фильтра стекло', 'Изображение после поворота',
          'Изображение после фильтра тиснение', 'Изобрачение после фильтра Робертса', 'Изображение после фильтра Собеля',
          'Изображение после фильтра Превитта', 'Изображение после фильтра Светящиеся края',
          'Изображение после коррекции "Серый мир"', 'Изображение после коррекции "Идеальный отражатель"',
          'Изображение после коррекции с опорным цветом', 'Исходное изображение', 'Изображение после медианного фильтра',
          'Исходное изображение', 'Изображение после растяжения гистограммы']

def on_click(event):
    global current_index
    current_index = (current_index + 1) % 25
    ax.imshow(images[current_index])
    ax.set_title(titles[current_index])
    plt.draw()

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.imshow(images[0])
ax.set_title(titles[0])
ax.axis('off')

fig.canvas.mpl_connect('button_press_event', on_click)

plt.show()
