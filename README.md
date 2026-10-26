# Billy e il Think Tank di "Chi sta addestrando chi?"

Adattamento del Chief of Staff agent dei claude-cookbooks (claude_agent_sdk/01_The_chief_of_staff_agent.ipynb) a un progetto di scrittura creativa. Billy, scrittore e capo di gabinetto, governa undici agenti specializzati.

## Struttura

- CLAUDE.md: identità di Billy, regole di lavoro, decisioni degli autori (memoria persistente)
- .claude/agents/: gli undici subagenti del Think Tank
- .claude/commands/: /allinea, /salva-su-drive, /consulta, /capitolo, /sinossi, /colpo-di-scena, /specchio, /revisione
- .claude/output-styles/: editore, autori, pagina
- .claude/hooks/ e .claude/settings.local.json: dopo ogni scrittura in capitoli/ parte il controllo di stile; ogni modifica viene registrata in audit/
- scripts/controllo_stile.py: conteggio dei tic della prosa sintetica secondo la guida di stile
- knowledge/: bibbia del mondo, sinossi, guida di stile
- capitoli/, piani/, audit/: lavoro in corso
- agent.py: avvio di Billy tramite Claude Agent SDK

## Uso con Claude Code

Aprire la cartella con Claude Code ed eseguire, per esempio:
/consulta Come preparare nel capitolo 3 la rivelazione sull'errore voluto di Adamo 1.0?
/capitolo 3
Per la modalità piano: avviare Claude Code in plan mode prima di /capitolo.

## Uso con Claude Agent SDK

pip install claude-agent-sdk python-dotenv
Impostare ANTHROPIC_API_KEY in un file .env, poi:
python agent.py "/consulta Che cosa contiene il frammento del prologo?"
L'opzione setting_sources=["project", "local"] in agent.py è necessaria per caricare CLAUDE.md, subagenti, comandi, stili e hook.

## Sincronizzazione con Google Drive

I capitoli 1 e 2 e i materiali di ricerca sono nella cartella Drive "Nuovo libro". Con Google Drive per desktop la cartella del Think Tank può stare dentro Drive.

## Avvio con Google Drive

1. Installare Claude Code e accedere con lo stesso account claude.ai su cui sono collegati Google Drive e Google Docs: i connettori di claude.ai si caricano automaticamente. Verificare con /mcp.
2. Estrarre questa cartella in una posizione qualsiasi del computer e aprirla con Claude Code.
3. Eseguire /allinea alla prima sessione, /salva-su-drive alla fine di ogni sessione.
