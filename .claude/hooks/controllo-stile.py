#!/usr/bin/env python3
"""PostToolUse: dopo ogni scrittura o modifica di un file in capitoli/, esegue il controllo di stile."""
import json
import os
import subprocess
import sys

dati = json.load(sys.stdin)
percorso = dati.get("tool_input", {}).get("file_path", "")
if "/capitoli/" in percorso and percorso.endswith((".md", ".txt")):
    radice = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
    esito = subprocess.run(
        [sys.executable, os.path.join(radice, "scripts", "controllo_stile.py"), percorso],
        capture_output=True, text=True,
    )
    print(esito.stdout.strip(), file=sys.stderr)
