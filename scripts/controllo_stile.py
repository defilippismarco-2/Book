#!/usr/bin/env python3
"""Controllo dei tic della prosa sintetica secondo knowledge/guida_di_stile.md.

Uso: python scripts/controllo_stile.py capitoli/capitolo_03.md
Scrive un rapporto in audit/stile_<nome>.md. I conteggi sono indicatori per la
revisione, non prove sull'origine del testo.
"""
import os
import re
import sys

PAROLE_SPIA = [
    "fondamentale", "cruciale", "trasformativ", "esplorare", "inoltre",
    "in conclusione", "elevare", "intricat", "senza precedenti", "cambiò tutto",
    "abbracciare il cambiamento", "rivoluzionari",
]
EMOZIONI = [r"un'ondata di", r"una fitta di", r"\bprovò\b", r"\bsi sentì\b", r"\bsentì un\b"]
NEGAZIONE = re.compile(r"\bnon (?:è|era|sono|erano|si tratta(?:va)?)\b[^.!?]{0,90}?\bma\b", re.I)
TERNA = re.compile(r"\b[\wàèéìòù']+, [\wàèéìòù']+ e [\wàèéìòù']+\b")


def frasi(testo):
    pezzi = re.split(r"(?<=[.!?»])\s+", testo)
    return [p for p in pezzi if len(p.split()) > 0]


def analizza(testo):
    parole = len(testo.split()) or 1
    mille = parole / 1000
    righe_narrative = [r for r in testo.splitlines() if not r.strip().startswith("«")]
    narrativa = "\n".join(righe_narrative)
    r = {
        "parole": parole,
        "trattini_lunghi_in_narrazione": narrativa.count("—") + len(re.findall(r" – ", narrativa)),
        "contrasti_per_negazione": len(NEGAZIONE.findall(narrativa)),
        "terne_possibili": len(TERNA.findall(narrativa)),
        "parole_spia": {p: len(re.findall(p, testo, re.I)) for p in PAROLE_SPIA if re.search(p, testo, re.I)},
        "emozioni_nominate": sum(len(re.findall(e, testo, re.I)) for e in EMOZIONI),
    }
    lunghezze = [len(f.split()) for f in frasi(testo)]
    finestre_piatte = 0
    for i in range(0, max(len(lunghezze) - 19, 0), 20):
        blocco = lunghezze[i:i + 20]
        if not (min(blocco) <= 6 and max(blocco) >= 25):
            finestre_piatte += 1
    r["gruppi_di_20_frasi_a_ritmo_piatto"] = finestre_piatte
    r["soglie"] = {
        "contrasti_per_negazione (max 1)": r["contrasti_per_negazione"] <= 1,
        "terne (max 3, verificare a mano)": r["terne_possibili"] <= 3,
        "emozioni nominate (max 2 ogni 1000 parole)": r["emozioni_nominate"] <= 2 * max(mille, 1),
        "trattini lunghi in narrazione (0)": r["trattini_lunghi_in_narrazione"] == 0,
        "ritmo (nessun gruppo piatto)": finestre_piatte == 0,
    }
    return r


def main():
    if len(sys.argv) < 2:
        print("Uso: python scripts/controllo_stile.py <file>")
        sys.exit(1)
    percorso = sys.argv[1]
    with open(percorso, encoding="utf-8") as f:
        risultato = analizza(f.read())
    radice = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.makedirs(os.path.join(radice, "audit"), exist_ok=True)
    nome = os.path.splitext(os.path.basename(percorso))[0]
    uscita = os.path.join(radice, "audit", f"stile_{nome}.md")
    with open(uscita, "w", encoding="utf-8") as f:
        f.write(f"# Controllo di stile: {nome}\n\n")
        for chiave, valore in risultato.items():
            f.write(f"- {chiave}: {valore}\n")
    oltre = [k for k, ok in risultato["soglie"].items() if not ok]
    print(f"Controllo di stile su {nome}: {len(oltre)} soglie superate {oltre}. Rapporto in {uscita}")


if __name__ == "__main__":
    main()
