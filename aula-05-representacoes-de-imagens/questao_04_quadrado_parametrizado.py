"""Prática 4: quadrado vermelho definido pelo tamanho e pelo centro."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def criar_imagem(largura=200, altura=200, tamanho=60):
    if any(type(valor) is not int for valor in (largura, altura, tamanho)):
        raise ValueError("Largura, altura e tamanho devem ser números inteiros.")
    if largura <= 0 or altura <= 0 or not 1 <= tamanho <= min(largura, altura):
        raise ValueError("As dimensões devem ser positivas e o quadrado deve caber na imagem.")

    centro_x = largura // 2
    centro_y = altura // 2
    x0 = centro_x - tamanho // 2
    y0 = centro_y - tamanho // 2
    x1 = x0 + tamanho
    y1 = y0 + tamanho

    imagem = np.zeros((altura, largura, 3), dtype=np.uint8)
    imagem[y0:y1, x0:x1] = [255, 0, 0]
    return imagem


def main():
    imagem = criar_imagem()
    destino = Path(__file__).resolve().parent / "resultados"
    destino.mkdir(exist_ok=True)
    arquivo = destino / "questao_04_quadrado_parametrizado.png"
    plt.imsave(arquivo, imagem)
    print("Quadrado vermelho: 60 × 60 pixels, em uma imagem de 200 × 200 pixels.")
    print(f"PNG salvo em: {arquivo}")


if __name__ == "__main__":
    main()
