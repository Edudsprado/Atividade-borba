# Atividade Borba — Aula 5: Representações de Imagens

As quatro práticas do arquivo `Aula_05_OneCompiler_Praticas.py` foram separadas em programas independentes, mantendo a ordem, os conceitos e os valores originais. Este material contém implementações e explicações; o arquivo fornecido não inclui os enunciados completos das questões.

## Arquivos

| Prática | Programa | Resultado |
| --- | --- | --- |
| 1 — Matriz RGB | [questao_01_matriz_rgb.py](aula-05-representacoes-de-imagens/questao_01_matriz_rgb.py) | Imagem vermelha de 100 × 100 pixels |
| 2 — Círculo rasterizado | [questao_02_circulo_rasterizado.py](aula-05-representacoes-de-imagens/questao_02_circulo_rasterizado.py) | Círculo vermelho de raio 60 em fundo preto |
| 3 — Descrição vetorial conceitual | [questao_03_descricao_vetorial.py](aula-05-representacoes-de-imagens/questao_03_descricao_vetorial.py) | Dicionário com centro, raio e cor |
| 4 — Quadrado parametrizado | [questao_04_quadrado_parametrizado.py](aula-05-representacoes-de-imagens/questao_04_quadrado_parametrizado.py) | Quadrado vermelho de 60 × 60 pixels |

## Como executar

Em um terminal, a partir da pasta do repositório, entre no diretório da aula, instale as dependências e execute a prática desejada:

```bash
cd aula-05-representacoes-de-imagens
python -m pip install -r requirements.txt
python questao_01_matriz_rgb.py
python questao_02_circulo_rasterizado.py
python questao_03_descricao_vetorial.py
python questao_04_quadrado_parametrizado.py
```

Execute cada comando de prática separadamente. A prática 3 usa apenas recursos nativos do Python e dispensa a instalação das dependências.

As práticas 1, 2 e 4 salvam PNGs na pasta `resultados/`, criada automaticamente ao lado dos programas. Abra esses arquivos para visualizar as imagens. O backend `Agg` permite gerar os PNGs sem uma janela gráfica. `plt.imsave` conserva as dimensões da matriz no arquivo e não acrescenta eixos ou margens.

### Execução no OneCompiler

Copie o conteúdo de um programa por vez para o editor Python. As práticas 1, 2 e 4 precisam de NumPy e Matplotlib disponíveis nesse ambiente. Se aparecer `ModuleNotFoundError`, a biblioteca indicada na mensagem não está disponível. Nesse caso, execute localmente com as dependências instaladas ou use um ambiente que as forneça.

O código gera arquivos PNG, mas a visualização ou o download dependem dos recursos oferecidos pelo ambiente. A saída do terminal informa o caminho do arquivo. Este material não presume que o terminal do OneCompiler exiba imagens nem que ofereça acesso aos arquivos gerados.

## Prática 1 — Matriz RGB

Uma imagem RGB tem três canais por pixel: vermelho (R), verde (G) e azul (B). `np.zeros((100, 100, 3), dtype=np.uint8)` cria uma matriz com 100 linhas, 100 colunas e três canais. O tipo `uint8` armazena números inteiros de 0 a 255. Inicialmente, todos os canais valem zero e a imagem é preta.

Em `imagem[:, :, 0] = 255`, os dois `:` selecionam todas as linhas e colunas; o índice `0` seleciona o canal vermelho. Verde e azul continuam em zero. Assim, todos os pixels recebem a cor `[255, 0, 0]` e a imagem fica inteiramente vermelha.

**Resultado esperado:** um PNG vermelho de 100 × 100 pixels. A matriz tem formato `(100, 100, 3)`.

## Prática 2 — Círculo rasterizado

A matriz de 200 × 200 pixels começa com fundo preto. `np.ogrid` cria coordenadas de linha (`y`) e coluna (`x`) usadas para avaliar cada posição da imagem. A máscara usa a condição:

```python
(x - centro_x) ** 2 + (y - centro_y) ** 2 <= raio ** 2
```

Essa expressão seleciona os pixels cuja distância ao centro não ultrapassa 60 pixels, incluindo a borda. Somente as posições selecionadas recebem `[255, 0, 0]`. As demais permanecem pretas.

**Resultado esperado:** um círculo preenchido vermelho com centro `(100, 100)` e raio 60. Por ser uma representação raster, a figura é formada por pixels e sua borda pode mostrar degraus ao ampliar a imagem.

## Prática 3 — Descrição vetorial conceitual

O círculo é descrito por seus atributos geométricos e pela cor:

```python
{"centro": (100, 100), "raio": 60, "cor": "vermelho"}
```

O dicionário guarda uma descrição conceitual, sem armazenar cada pixel da figura. Um programa de desenho poderia usar esses atributos para construir o círculo. Este exercício apenas imprime a descrição; não desenha o círculo e não cria um arquivo vetorial como SVG.

**Resultado esperado no terminal:**

```text
{'centro': (100, 100), 'raio': 60, 'cor': 'vermelho'}
```

## Prática 4 — Quadrado parametrizado

Os parâmetros padrão são largura e altura de 200 pixels e lado do quadrado de 60 pixels. O centro é calculado por divisão inteira: `largura // 2` e `altura // 2`. A partir desse centro, o programa determina a posição inicial do quadrado.

Os limites finais são calculados com `x1 = x0 + tamanho` e `y1 = y0 + tamanho`. O recorte `imagem[y0:y1, x0:x1]` usa primeiro as linhas (`y`) e depois as colunas (`x`). Como os limites finais dos recortes são exclusivos, a região contém exatamente `tamanho` linhas e `tamanho` colunas.

**Resultado esperado:** quadrado vermelho de 60 × 60 pixels, ocupando as linhas e colunas de índice 70 até 129 sobre fundo preto. São 3.600 pixels vermelhos.

Para alterar a figura, mude os argumentos da chamada em `main()`, por exemplo `criar_imagem(largura=200, altura=200, tamanho=61)`. Em uma grade discreta, algumas combinações de dimensões pares e ímpares deixam a centralização geométrica com diferença de meio pixel. O número de pixels do lado continua exato.

## Ajustes feitos

- Cada prática tem seu próprio arquivo, imports e execução independente.
- A geração de PNGs substitui a dependência de `plt.show()`, que precisa de um ambiente capaz de exibir gráficos.
- Na prática 4, o cálculo do limite final preserva o tamanho solicitado também para lados ímpares. No código original, um lado de 61 geraria um recorte de 60 pixels.
- A prática 4 valida dimensões inteiras positivas e impede um quadrado maior que a imagem.

O código fornecido é sintaticamente válido. Sem a mensagem do erro anterior, não é possível afirmar sua causa. A disponibilidade das bibliotecas e a forma de exibição gráfica precisam ser consideradas separadamente.

## Organização do repositório

Os quatro programas e o arquivo `requirements.txt` estão no diretório [`aula-05-representacoes-de-imagens/`](aula-05-representacoes-de-imagens/). Este README reúne as explicações de cada prática. Os PNGs são gerados durante a execução e estão ignorados pelo `.gitignore`.

## Verificação realizada

A sintaxe dos quatro programas e suas funções de criação foram verificadas. Foram conferidos a cor e o formato da matriz RGB, o centro e a borda do círculo e a descrição vetorial. O quadrado foi verificado com lados de 1, 60, 61 e 200 pixels, além de entradas inválidas. A prática 3 também foi executada como programa independente.

A geração de PNGs não pôde ser executada no ambiente de preparação porque Matplotlib não estava instalado e sua instalação não estava acessível pela rede. Execute as práticas 1, 2 e 4 com as dependências instaladas para conferir os arquivos de imagem.
