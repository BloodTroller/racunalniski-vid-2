import math

import cv2 as cv
import numpy as np


def konvolucija(slika, jedro):
    '''Izvede konvolucijo nad sliko. Brez uporabe funkcije cv.filter2D, ali katerekoli druge funkcije, ki izvaja konvolucijo.
    Funkcijo implementirajte sami z uporabo zank oz. vektorskega računanja.'''
    output = slika.copy()
    vis, sir = slika.shape
    vis_j, sir_j = jedro.shape
    vispad = vis_j // 2
    sirpad = sir_j // 2
    calc = np.pad(slika, ((vispad, vispad), (sirpad, sirpad)), 'reflect')

    for i in range(vis):
        for j in range(sir):
            output[i, j] = np.sum(calc[i:(vispad * 2 + 1 + i), j:(sirpad * 2 + 1 + j)] * jedro)

    return output


def filtriraj_z_gaussovim_jedrom(slika, sigma):
    '''Filtrira sliko z Gaussovim jedrom..'''
    velikost_jedra = int(2 * sigma * 2 + 1)
    k = np.float32(velikost_jedra / 2 - 1 / 2)
    jedro = np.zeros((velikost_jedra, velikost_jedra))
    for i in range(velikost_jedra):
        for j in range(velikost_jedra):
            a = 1 / (2 * np.pi * sigma ** 2)
            b = -(((i-k)**2 + (j-k)**2)/(2*sigma**2))
            jedro[i, j] = a * np.exp(b)
    return konvolucija(slika, jedro)


def filtriraj_sobel_smer(slika):
    '''Filtrira sliko z Sobelovim jedrom in označi gradiente v orignalni sliki glede na ustrezen pogoj.'''
    jedro = np.array([[1, 2, 1],
                      [0, 0, 0],
                      [-1, -2, -1]])

    return konvolucija(slika, jedro)


if __name__ == '__main__':
    slika = cv.imread(".utils/lenna.png")
    slika = cv.cvtColor(slika, cv.COLOR_BGR2GRAY)
    # slika = cv.resize(slika, (1000, 1000))
    slika = filtriraj_sobel_smer(slika)
    show = cv.cvtColor(slika, cv.COLOR_GRAY2BGR)
    vis, sir = slika.shape
    for i in range(vis):
        for j in range(sir):
            if slika[i, j] > 120:
                show[i, j] = (255, slika[i, j] / 2, slika[i, j] / 2)
    cv.imshow("Filtered", show)
    cv.waitKey(0)
    cv.destroyAllWindows()
    pass
