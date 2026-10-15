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

