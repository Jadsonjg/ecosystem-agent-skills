"""Cor institucional por Skill e contraste sRGB conforme WCAG 2.2."""
import re

WHITE = "#FFFFFF"
PAPER = "#F7F7F2"
MINT = "#E8F1E9"
LEGACY_GREEN = "#143B36"


def luminance(color):
    srgb = [int(color[i:i+2], 16)/255 for i in (1, 3, 5)]
    linear = [v/12.92 if v <= .04045 else ((v+.055)/1.055)**2.4 for v in srgb]
    return sum(w*v for w, v in zip((.2126, .7152, .0722), linear))


def contrast(first, second):
    low, high = sorted((luminance(first), luminance(second)))
    return (high+.05)/(low+.05)


def institutional_color(data):
    # Dados de guias v1.0.0 continuam geráveis com o verde histórico.
    color = data.get("cor_institucional", LEGACY_GREEN)
    if not isinstance(color, str) or not re.fullmatch(r"#[0-9a-fA-F]{6}", color):
        raise ValueError("cor_institucional precisa ser hexadecimal no formato #RRGGBB.")
    for surface, minimum in ((WHITE, 7), (PAPER, 4.5), (MINT, 4.5)):
        measured = contrast(color, surface)
        if measured < minimum:
            raise ValueError(f"Contraste de {color} com {surface}: {measured:.2f}:1. Mínimo: {minimum:g}:1.")
    return color.upper()
