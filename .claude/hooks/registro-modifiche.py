#!/usr/bin/env python3
"""PostToolUse: registra ogni scrittura o modifica di file del libro in audit/registro_modifiche.json."""
import json
import os
import sys
from datetime import datetime

dati = json.load(sys.stdin)
percorso = dati.get("tool_input", {}).get("file_path", "")
if percorso:
    radice = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
    registro = os.path.join(radice, "audit", "registro_modifiche.json")
    os.makedirs(os.path.dirname(registro), exist_ok=True)
    voci = []
    if os.path.exists(registro):
        with open(registro, encoding="utf-8") as f:
            voci = json.load(f)
    voci.append({"quando": datetime.now().isoformat(timespec="seconds"),
                 "strumento": dati.get("tool_name"), "file": percorso})
    with open(registro, "w", encoding="utf-8") as f:
        json.dump(voci, f, ensure_ascii=False, indent=2)
