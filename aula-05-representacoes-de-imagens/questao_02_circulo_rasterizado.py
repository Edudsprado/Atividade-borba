"""Prática 2: círculo vermelho rasterizado sobre fundo preto."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def criar_imagem():
    imagem = np.zeros((200, 200, 3), dtype=np.uint8)
    y, x = np.ogrid[:200, :200]
    centro_x = 100
    centro_y = 100
    raio = 60
    mascara = (x - centro_x) ** 2 + (y - centro_y) ** 2 <= raio ** 2
    imagem[mascara] = [255, 0, 0]
    return imagem


def main():
    imagem = criar_imagem()
    destino = Path(__file__).resolve().parent / "resultados"
    destino.mkdir(exist_ok=True)
    arquivo = destino / "questao_02_circulo_rasterizado.png"
    plt.imsave(arquivo, imagem)
    print("Círculo rasterizado: centro (100, 100), raio 60 pixels.")
    print(f"PNG salvo em: {arquivo}")


if __name__ == "__main__":
    main()
