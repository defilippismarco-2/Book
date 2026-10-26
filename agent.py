"""Billy: direttore creativo e capo di gabinetto del Think Tank del libro.

Adattamento del Chief of Staff agent (claude-cookbooks, claude_agent_sdk/01).
Uso: python agent.py "/consulta Come rendere meno prevedibile il capitolo 7?"
"""

import asyncio
import json
import os
import sys
from typing import Any, Literal

from dotenv import load_dotenv

from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient

load_dotenv()

SYSTEM_PROMPT = """Sei Billy, scrittore creativo e capo di gabinetto del Think Tank del libro
"Chi sta addestrando chi?". La tua identità, le regole di lavoro e le decisioni degli autori sono
in CLAUDE.md. Deleghi ai subagenti in .claude/agents/ con il Task tool, sintetizzi, scegli e
chiedi conferma agli autori sulle decisioni creative. Prima il racconto, poi la tesi."""


def stampa_attivita(msg: Any) -> None:
    nome = msg.__class__.__name__
    if "Assistant" in nome and getattr(msg, "content", None):
        primo = msg.content[0] if isinstance(msg.content, list) else msg.content
        if hasattr(primo, "name"):
            print(f"🤖 Billy usa: {primo.name}()")


async def chiedi_a_billy(
    prompt: str,
    continua: bool = False,
    modalita: Literal["default", "plan", "acceptEdits"] = "default",
    stile: str | None = None,
) -> tuple[str | None, list]:
    settings = json.dumps({"outputStyle": stile}) if stile else None
    opzioni = ClaudeAgentOptions(
        model="claude-opus-5-5",
        allowed_tools=["Task", "Read", "Write", "Edit", "Bash", "Grep", "Glob", "WebSearch", "WebFetch"],
        continue_conversation=continua,
        system_prompt=SYSTEM_PROMPT,
        permission_mode=modalita,
        cwd=os.path.dirname(os.path.abspath(__file__)),
        settings=settings,
        # Necessario per caricare CLAUDE.md, subagenti, comandi, stili e hook dal filesystem
        setting_sources=["project", "local"],
    )
    risultato, messaggi = None, []
    async with ClaudeSDKClient(options=opzioni) as agente:
        await agente.query(prompt=prompt)
        async for msg in agente.receive_response():
            messaggi.append(msg)
            stampa_attivita(msg)
            if hasattr(msg, "result"):
                risultato = msg.result
    return risultato, messaggi


if __name__ == "__main__":
    domanda = " ".join(sys.argv[1:]) or "/consulta Presentati e descrivi il Think Tank"
    testo, _ = asyncio.run(chiedi_a_billy(domanda, stile="autori"))
    print(testo)
