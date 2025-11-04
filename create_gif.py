import imageio.v3 as iio

filenames = [
    'gengar/1.jpg',
    'gengar/2.jpg',
    'gengar/3.jpg',
]

images = [ ]

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('gengar.gif', images, duration = 100, loop = 0 )