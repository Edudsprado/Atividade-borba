# Atividade Borba — Aula 5: Representações de Imagens

Este repositório apresenta as quatro práticas em arquivos independentes, com análise do problema, justificativa da correção e código completo de cada versão atualizada.

A análise usa o arquivo fornecido `Aula_05_OneCompiler_Praticas.py`. O material não inclui os enunciados completos nem a mensagem do erro anterior. As práticas 1 e 2 têm cálculos corretos: suas limitações são de execução e visualização. A prática 3 é válida como descrição conceitual, mas precisa de uma etapa adicional para gerar uma imagem vetorial. A prática 4 tinha um erro de tamanho para valores ímpares.

## Problemas e soluções

| Questão | Problema ou limitação identificada | Versão corrigida |
| --- | --- | --- |
| 1 — Matriz RGB | `plt.show()` depende de um ambiente que exiba gráficos. NumPy e Matplotlib também precisam estar instalados. A matriz vermelha está correta. | Programa independente que salva um PNG de 100 × 100 pixels e informa o caminho. |
| 2 — Círculo rasterizado | O bloco original, copiado isoladamente, não tinha seus próprios imports. A exibição também dependia de `plt.show()`. A equação do círculo está correta. | Programa com seus próprios imports, máscara circular preservada e exportação para PNG. |
| 3 — Descrição vetorial | Imprimir um dicionário não produz um arquivo de imagem. Isso é suficiente para uma descrição conceitual, mas não para visualizar um vetor. | Mantém a descrição e acrescenta exportação opcional para SVG, sem bibliotecas externas. |
| 4 — Quadrado parametrizado | Os limites originais com `tamanho // 2` dos dois lados reduzem um lado ímpar em um pixel. | Limite final calculado a partir do início mais o tamanho, com validação das dimensões. |

## Como executar

A partir da pasta do repositório:

```bash
cd aula-05-representacoes-de-imagens
python -m pip install -r requirements.txt
python questao_01_matriz_rgb.py
python questao_02_circulo_rasterizado.py
python questao_03_descricao_vetorial.py
python questao_03_descricao_vetorial.py --svg
python questao_04_quadrado_parametrizado.py
```

Cada comando de prática é independente. A prática 3 usa somente a biblioteca padrão do Python e não precisa das dependências do `requirements.txt`.

As imagens são salvas em `aula-05-representacoes-de-imagens/resultados/`, ao lado dos programas. Abra os PNGs em um visualizador de imagens e o SVG em um navegador ou editor vetorial. Os arquivos gerados são ignorados pelo `.gitignore`.

### OneCompiler

Copie um programa completo por vez. As práticas 1, 2 e 4 exigem NumPy e Matplotlib. Se ocorrer `ModuleNotFoundError`, é necessário disponibilizar a biblioteca nesse ambiente ou executar localmente após instalar as dependências. A geração do PNG não garante que o OneCompiler permita visualizá-lo ou baixá-lo; isso depende dos recursos da plataforma. Para usar `--svg`, o ambiente precisa permitir argumentos de execução e acesso ao arquivo gerado.

## Questão 1 — Matriz RGB

**Problema:** a operação que pinta o canal vermelho está correta. A limitação do código original é depender de `plt.show()` para apresentar o resultado. Sem suporte gráfico, o usuário pode não ver a imagem; sem as bibliotecas, o programa não chega a executá-la. Esses casos não são um erro na representação RGB.

**Correção:** usar o backend `Agg`, salvar a matriz com `plt.imsave` e informar onde está o PNG. As dependências estão indicadas no repositório. Essa mudança já estava presente na primeira versão separada e foi mantida após a revisão.

**Explicação:** a matriz tem formato `(100, 100, 3)` e tipo `uint8`, com valores de 0 a 255. O índice `0` representa o canal vermelho. Ao atribuir 255 a esse canal e manter os demais em zero, todos os pixels recebem `[255, 0, 0]`.

**Resultado esperado:** `resultados/questao_01_matriz_rgb.png`, com 100 × 100 pixels inteiramente vermelhos.

**Versão corrigida:** [questao_01_matriz_rgb.py](aula-05-representacoes-de-imagens/questao_01_matriz_rgb.py)

```python
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
```

## Questão 2 — Círculo rasterizado

**Problema:** no arquivo original, a prática 2 reutilizava os imports declarados antes da prática 1. Copiar somente esse bloco para outro programa sem os imports causaria `NameError` ao acessar `np` ou `plt`. No arquivo completo original isso não é um erro. Além disso, a exibição tinha a mesma dependência gráfica da prática 1.

**Correção:** incluir os imports no próprio arquivo e salvar a imagem como PNG. A equação foi preservada porque está correta. Essas correções de execução já estavam presentes na versão separada e foram mantidas.

**Explicação:** `np.ogrid` fornece coordenadas de linha (`y`) e coluna (`x`). A condição abaixo seleciona os pixels cuja distância ao centro não ultrapassa o raio:

```python
(x - centro_x) ** 2 + (y - centro_y) ** 2 <= raio ** 2
```

O operador `<=` inclui a borda. Os pixels selecionados ficam vermelhos e os demais continuam pretos. O aspecto em degraus ao ampliar a borda é próprio da rasterização, não um erro da fórmula.

**Resultado esperado:** `resultados/questao_02_circulo_rasterizado.png`, com 200 × 200 pixels, centro `(100, 100)` e raio 60.

**Versão corrigida:** [questao_02_circulo_rasterizado.py](aula-05-representacoes-de-imagens/questao_02_circulo_rasterizado.py)

```python
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
```

## Questão 3 — Descrição vetorial conceitual

**Problema ou limitação:** o código original apenas imprimia um dicionário. Ele descrevia o círculo corretamente, mas não produzia uma imagem vetorial que pudesse ser aberta. Como o título original dizia “descrição vetorial conceitual”, não há erro de sintaxe ou de conceito nessa descrição; a exportação abaixo é uma extensão para obter um resultado visual.

**Correção/extensão:** manter o comportamento original e acrescentar a opção `--svg`. Com essa opção, o programa utiliza os mesmos atributos do dicionário para criar um SVG de 200 × 200, com círculo vermelho sobre fundo preto. NumPy e Matplotlib não são necessários nesta prática.

**Explicação:** o elemento SVG `circle` armazena centro e raio como atributos geométricos. O navegador desenha a figura a partir desses atributos. O arquivo conserva a descrição vetorial; sua exibição na tela é renderizada pelo visualizador.

**Resultado esperado sem a opção:**

```text
{'centro': (100, 100), 'raio': 60, 'cor': 'vermelho'}
```

**Resultado esperado com `--svg`:** a mesma descrição no terminal e o arquivo `resultados/questao_03_circulo_vetorial.svg`.

**Versão corrigida e ampliada:** [questao_03_descricao_vetorial.py](aula-05-representacoes-de-imagens/questao_03_descricao_vetorial.py)

```python
"""Prática 3: descrição de um círculo e exportação opcional para SVG."""

import argparse
from pathlib import Path
import xml.etree.ElementTree as ET


def descrever_circulo():
    return {
        "centro": (100, 100),
        "raio": 60,
        "cor": "vermelho",
    }


def exportar_svg(circulo, arquivo):
    """Cria uma imagem vetorial usando os atributos da descrição."""
    svg = ET.Element("svg", {
        "xmlns": "http://www.w3.org/2000/svg",
        "width": "200",
        "height": "200",
        "viewBox": "0 0 200 200",
    })
    ET.SubElement(svg, "rect", {
        "width": "200", "height": "200", "fill": "black",
    })
    centro_x, centro_y = circulo["centro"]
    ET.SubElement(svg, "circle", {
        "cx": str(centro_x),
        "cy": str(centro_y),
        "r": str(circulo["raio"]),
        "fill": {"vermelho": "red"}[circulo["cor"]],
    })
    arquivo = Path(arquivo)
    arquivo.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(svg).write(arquivo, encoding="utf-8", xml_declaration=True)
    return arquivo


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--svg", action="store_true", help="Salvar também uma imagem vetorial SVG.")
    args = parser.parse_args()
    circulo = descrever_circulo()
    print(circulo)
    if args.svg:
        destino = Path(__file__).resolve().parent / "resultados" / "questao_03_circulo_vetorial.svg"
        print(f"SVG salvo em: {exportar_svg(circulo, destino)}")


if __name__ == "__main__":
    main()
```

## Questão 4 — Quadrado parametrizado

**Problema:** o código original calculava os dois limites usando a metade inteira do tamanho:

```python
x0 = centro_x - tamanho // 2
x1 = centro_x + tamanho // 2
y0 = centro_y - tamanho // 2
y1 = centro_y + tamanho // 2
```

Com `tamanho = 60`, isso funciona. Com `tamanho = 61`, porém, `61 // 2` vale 30: o intervalo de 70 a 130 contém somente 60 posições, porque o limite final do recorte é exclusivo. O quadrado fica com um pixel a menos em cada lado. O original também não validava dimensões inválidas ou um quadrado que não coubesse na imagem.

**Correção:** calcular os limites finais pela posição inicial mais o tamanho e validar os parâmetros. Essa correção já estava na primeira versão separada e foi confirmada nesta revisão.

```python
x1 = x0 + tamanho
y1 = y0 + tamanho
```

**Explicação:** a matriz é indexada como `[linha, coluna]`, por isso o recorte usa `[y0:y1, x0:x1]`. A diferença `x1 - x0`, assim como `y1 - y0`, passa a ser exatamente o tamanho informado. Em algumas combinações de dimensões pares e ímpares, a centralização discreta difere em meio pixel; isso não altera o tamanho do quadrado.

**Resultado esperado:** `resultados/questao_04_quadrado_parametrizado.png`, com um quadrado vermelho de 60 × 60 pixels sobre fundo preto de 200 × 200 pixels. São 3.600 pixels vermelhos, nas linhas e colunas de índice 70 até 129. Ao alterar a chamada para `criar_imagem(tamanho=61)`, o quadrado tem 61 × 61 pixels, totalizando 3.721 pixels vermelhos.

**Versão corrigida:** [questao_04_quadrado_parametrizado.py](aula-05-representacoes-de-imagens/questao_04_quadrado_parametrizado.py)

```python
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
```

## Verificação realizada

Os quatro programas foram executados com sucesso nesta revisão. Foram verificados:

- A cor vermelha e o formato da matriz da prática 1.
- O centro, a borda e os pixels externos do círculo da prática 2.
- A saída original da prática 3 e o XML do SVG gerado, incluindo centro, raio, cor e fundo.
- O quadrado com lados de 1, 60, 61 e 200 pixels, além da rejeição de dimensões inválidas.
- Os três PNGs gerados, comparando cada pixel com a matriz produzida pelo respectivo programa.

Ambiente de verificação: Python com NumPy 2.3.5 e Matplotlib 3.10.8. A verificação foi feita localmente, sem executar os programas dentro do OneCompiler.
