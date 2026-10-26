# Guida di stile

Copia di lavoro di "06 – Guida di stile" (Google Drive), allineata il 26 ottobre 2026. Fonti: prompt "Human-First Editor & Ghostwriter", documento "Riconoscere testi scritti dall'IA" (entrambi in Materiali), pattern di prosa e di revisione della skill Book Genesis. Dove il documento 06 contiene indicazioni superate dalle tarature successive, qui vale la taratura più recente; la differenza è annotata in fondo.

## Principio d'uso

Le regole servono alla revisione, non a eludere i rilevatori. Molti di questi tratti compaiono anche nella prosa umana: un conteggio oltre soglia segnala un passaggio da rileggere e non prova l'origine del testo. Le soglie sono valori di progetto e si possono cambiare, annotando il motivo.

## Registri

- Diario di Adamo 0.7 (unico diarista): prima persona, ritmo irregolare, ironia secca, molto corpo. In quel mondo l'umano è l'unico ad avere fame, sonno, freddo e odori: il dettaglio sensoriale è anche un tema. Scritto a matita sul retro dei manuali di manutenzione.
- Costante: terza persona ravvicinata; percezioni da macchina (infrarossi, ventole, temperatura, vibrazioni); ciò che somiglia a un sentimento appare come classificazione che non riesce o come anomalia di percezione. Nell'ultimo capitolo compare per la prima volta la sua prima persona (04 – Architettura).
- Documenti del mondo delle macchine: brevi, in inserto (comunicazioni aziendali, notiziari, verbali, note di rilascio).
- Sezione di management: tono asciutto, neutro, oggettivo. Niente enfasi, niente passaggi in cui il testo parla di sé o del lettore, niente eccesso di didascalismo. Aneddoti reali forniti dagli autori, mai inventati.
- La cronaca enciclopedica alla Lem come registro principale è abbandonata.

## Tono

- Ishiguro per l'interiorità e Vonnegut per la satira con affetto come riferimenti principali; Primo Levi per la satira del lavoro; Lem solo come condimento.
- Ironia di sottofondo: al massimo una battuta esplicita per scena. Il comico nasce dalle situazioni e dai personaggi, non da giochi di parole.
- Il mondo passa attraverso la scena e i sensi. Per le macchine: infrarossi, ventole, temperatura, vibrazioni. Per l'umano: freddo, luce, odori, fame.
- Termini inventati pochi, introdotti dentro una scena e mai spiegati con una definizione.
- Unità di tempo e misure ordinarie (giorni, mesi) salvo necessità narrativa.
- Le macchine non provano sentimenti umani: quando un'unità sembra provarne uno, il testo lo mostra come anomalia di classificazione o di percezione.
- L'emozione nasce dalla posta in gioco e dai rapporti fra i personaggi, non da figure o dettagli costruiti per commuovere.

## Eccezioni dichiarate

Lo stile segue il chiasmo della trama. Nelle prime release i documenti delle macchine possono usare di proposito i tic della prosa sintetica (terne, contrasto per negazione, enfasi obbligatoria) come parodia, e li perdono con l'avanzare delle versioni. Il diario di Adamo, durante il lavoro su H-Optimus, li acquisisce (04 – Architettura). Ogni uso deliberato si annota capitolo per capitolo in "04 – Architettura", per distinguerlo da un difetto.

Le enumerazioni comiche sono ammesse se lunghe e irregolari. Resta esclusa la terna riflessa.

## Tipografia

- Dialoghi tra caporali « ».
- Niente trattino lungo per gli incisi nella narrazione: virgole, parentesi tonde o punto fermo. Il trattino resta solo per una battuta interrotta.
- Titoli con la sola iniziale maiuscola. Evitare la forma "Titolo: sottotitolo". I titoli dei capitoli del primo libro usavano trattino e due punti: scelta da concordare con l'editore.
- Nessun segnaposto tra parentesi quadre.

## Soglie per capitolo

Valgono per la narrazione; i dialoghi sono esclusi salvo indicazione.

- Contrasto per negazione ("non è X, ma Y", "non si tratta di X ma di Y"): al massimo 1 per capitolo, 0 nel primo e nell'ultimo paragrafo. Correzione: dire la cosa vera; se il contrasto conta, metterlo in scena.
- Terne riflesse: al massimo 3 per capitolo; 0 terne che chiudono su un'astrazione dopo due elementi concreti. Correzione: un elemento, due in tensione, oppure un inventario lungo.
- Morale in chiusura: nessun capitolo finisce dichiarando il proprio significato. Correzione: chiudere su un atto, una battuta, un'immagine.
- Immagine seguita dalla spiegazione: al massimo 1 per capitolo, 0 nel culmine. Correzione: togliere la spiegazione; se l'immagine non regge, renderla più precisa.
- Emozioni nominate ("un'ondata di", "una fitta di", "provò"): al massimo 2 ogni 1.000 parole, 0 nel culmine. Correzione: ciò che il corpo fa o smette di fare.
- Ritmo a metronomo: in ogni gruppo di 20 frasi almeno una di 6 parole o meno e una di 25 o più.
- Enfasi obbligatoria (fondamentale, cruciale, trasformativo, senza precedenti, "cambiò tutto"): al massimo 1 ogni 1.000 parole, 0 in apertura e in chiusura di capitolo.
- Personaggi che spiegano i propri sentimenti in frasi compiute: al massimo 1 per capitolo, 0 nel culmine della scena.
- Epiteti al posto del nome: al massimo 1 per personaggio per capitolo, mai nello stesso paragrafo del nome.
- Cautele accumulate ("quasi come se, in qualche modo"): da evitare.

## Lessico

Parole spia da ridurre: fondamentale (importante, utile), esplorare (vedere, analizzare), inoltre (poi, e, con parsimonia), in conclusione (insomma, oppure niente), elevare (migliorare), intricato (complesso, difficile). Calchi da evitare: "abbracciare il cambiamento". Più verbi e pronomi, meno sostantivi astratti. Ridurre i gerundi esplicativi in coda di frase.

## Revisione

Dopo la stesura di ogni capitolo: controllo delle soglie (scripts/controllo_stile.py, automatico sui file in capitoli/), poi rilettura dei punti portanti: primo paragrafo, ultimo paragrafo, culmine, prima descrizione di un personaggio o di un luogo.

## Note di allineamento

- Il documento 06 descrive ancora, nella sezione "Registri", una "cronaca delle macchine documentale ed erudita, alla Lem". La taratura successiva dello stesso documento la abbandona; questa copia segue la taratura. Da correggere su Drive alla prossima /salva-su-drive, se gli autori approvano.
- Il controllo automatico sul ritmo nel capitolo 2 segnala gruppi di frasi a ritmo piatto (audit/stile_capitolo_02.md): è un indicatore da rileggere, non un errore accertato.
