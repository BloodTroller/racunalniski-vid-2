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
    pass

def filtriraj_z_gaussovim_jedrom(slika, sigma):
    '''Filtrira sliko z Gaussovim jedrom..'''

    pass


def filtriraj_sobel_smer(slika):
    '''Filtrira sliko z Sobelovim jedrom in označi gradiente v orignalni sliki glede na ustrezen pogoj.'''

    pass


if __name__ == '__main__':
    pass
