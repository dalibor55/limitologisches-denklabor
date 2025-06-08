# -*- coding: utf-8 -*-
"""Reflexionsgenerator für poetische Begriffe."""

def generiere_reflexion(begriff: str) -> str:
    """Gibt eine poetische Reflexion für bekannte Begriffe zurück.

    Bei unbekannten Begriffen wird ein Standardtext ausgegeben.
    """
    begriff_normalisiert = begriff.strip().lower()
    reflexionen = {
        "riss": (
            "Im Riss offenbart sich der Spalt zwischen dem Gewesenen "
            "und dem, was noch kommen mag."
        ),
        "grenze": (
            "An der Grenze verwischt das Bekannte, und ein neuer Horizont "
            "taucht am Rande des Denkbaren auf."
        ),
        "schwelle": (
            "Auf der Schwelle halten wir inne, bevor wir mutig in ein "
            "unbekanntes Licht treten."
        ),
    }
    return reflexionen.get(
        begriff_normalisiert,
        "Zu diesem Begriff habe ich keine spezielle Reflexion, doch "
        "jeder Neubeginn birgt Möglichkeiten.",
    )
