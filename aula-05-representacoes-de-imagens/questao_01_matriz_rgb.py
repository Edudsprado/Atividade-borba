"""Prática 1: imagem RGB vermelha de 100 × 100 pixels."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def criar_imagem():
    imagem = np.zeros((100, 100, 3), dtype=np.uint8)
    imagem[:, :, 0] = 255
    return imagem


def main():
    imagem = criar_imagem()
    destino = Path(__file__).resolve().parent / "resultados"
    destino.mkdir(exist_ok=True)
    arquivo = destino / "questao_01_matriz_rgb.png"
    plt.imsave(arquivo, imagem)
    print(f"Imagem criada: {imagem.shape[1]} × {imagem.shape[0]} pixels.")
    print(f"Cor RGB: {imagem[0, 0].tolist()}")
    print(f"PNG salvo em: {arquivo}")


if __name__ == "__main__":
    main()
