import imageio.v3 as iio

filenames = [
    'final_project/Gengar/1.jpg',
    'final_project/Gengar/2.jpg',
    'final_project/Gengar/3.jpg',
]

images = [ ]

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('gengar.gif', images, duration = 100, loop = 0 )