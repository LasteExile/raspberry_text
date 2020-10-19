import time
import random
import neopixel
import board
import sys

from chars import chars

pixels = neopixel.NeoPixel(board.D18, 256, auto_write=False)


def main(message, color):
    field = [[(0, 0, 0) for i in range(0, 16)] for j in range(0, 16)]
    display(field[:], create_pixel_set(message, color))


def create_pixel_set(phrase, color):
    pixel_set = []
    index = 16
    for figure in phrase:
        char = chars.get(figure)
        for pixel in char:
            if type(pixel) == list:
                new_pixel = pixel[:]
                new_pixel[1] += (index)
                if figure != ' ':
                    pixel_set.append([new_pixel, color])
                else:
                    pixel_set.append([new_pixel, (0, 0, 0)])
        index += char[0] + 1
    return pixel_set[:]


def display(field, pixel_set):
    j = 0
    finish = False
    while True:
        if finish:
            break
        for pixel in pixel_set:
            if pixel == pixel_set[-1] and pixel[0][1] - j < 0:
                finish = True
                break
            if pixel[0][1] - j in range(0, 16):
                field[pixel[0][0]][pixel[0][1] - j] = pixel[1]
        render(field[:])
        time.sleep(0.25)
        for pixel in pixel_set:
            if pixel[0][1] - j in range(0, 16):
                field[pixel[0][0]][pixel[0][1] - j] = (0, 0, 0)
        j += 1
        render()


def convert(array):
    monoarray = []
    for i in range(0, 16):
        for j in range(0, 16):
            if i % 2 == 0:
                monoarray.append(array[j][i])
            else:
                monoarray.append(array[::-1][j][i])
    return monoarray


def render(array=[]):
    if not array == []:
        monoarray = convert(array[:])
        for i in range(0, 256):
            pixels[i] = monoarray[i]
    else:
        pixels.fill((0, 0, 0))
    pixels.show()


if __name__ == '__main__':
    main(input(), tuple(map(int, input.split())))
