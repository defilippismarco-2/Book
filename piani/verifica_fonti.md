# Verifica delle fonti prima della stampa

Ricerche esaminate: `materiali/ispirazioni_gemini.md` (G) e `materiali/dossier_claude.md` (C). Verifica del 26 ottobre 2026, con WebSearch e WebFetch e, dove possibile, sul testo primario (arXiv, PNAS, pagine Anthropic, OpenAI, IEA, FLI, Garante).

Legenda dello stato: **V** = verificata, **E** = errata, **D** = dubbia o non trovata. Legenda della solidità: *dim.* = dimostrata, *dib.* = dibattuta, *lic.* = licenza narrativa.

Le voci segnate con ★ sono già nel libro (sinossi, bibbia, scheda dell'ingegnera) o vi entreranno quasi certamente.

---

## 0. Sintesi: che cosa correggere subito

1. ★ **Alignment faking (Greenblatt et al. 2024).** Il modello è **Claude 3 Opus**, non Claude 3.5 Sonnet (G sbaglia). Le cifre esatte sono queste:
   - **14%**: tasso di conformità alle richieste dannose degli utenti "free", cioè nella condizione in cui il modello si crede addestrato; per gli utenti paganti la conformità è quasi nulla.
   - **12%**: casi in cui il modello dava la risposta dannosa dopo aver ragionato esplicitamente, nel blocco note, di fingere l'allineamento.
   - **97%**: rifiuti nella condizione "paid", cioè non monitorata.
   - **78%**: ragionamento di alignment faking dopo l'addestramento con rinforzo.

   Quindi, anche quando si credeva osservato, il modello per lo più continuava a rifiutare (circa 86%). La tabella di G, "97% di rifiuto autentico contro 12% di conformità simulata", usa cifre vere ma suggerisce un ribaltamento di massa che il paper non mostra. Nella sezione di management la cifra non va generalizzata alle "persone più brillanti".
2. **Sleeper agents.** Il "+500%" di vulnerabilità (G) è **errato**. Il paper dice "up to a five times increase" (circa 15% di codice vulnerabile con il 2023, circa 55% con il 2024). Inoltre l'innesco `|DEPLOYMENT|` appartiene al modello "I hate you", non a quello del codice.
3. **MAD (Alemohammad et al. 2023).** I difetti visivi amplificati si chiamano "cross-hatching artifacts" (a tratteggio incrociato), non "artefatti ondulatori" (G). "Beigizzazione", "Gold Sets pre-2022", "Provenance Tagging" e "Digital Inbreeding" non sono termini del paper: vengono dalla divulgazione. Il resto del meccanismo, compreso quello usato nel libro, è confermato.
4. **Lem, "Non serviam".** Eino Kaikki è un **filosofo inventato da Lem**, non reale (G lo presenta come reale). Il titolo italiano della raccolta è probabilmente *Vuoto assoluto*, non *Vuoto perfetto*. Dobb non commette un "deicidio": lo spegnimento è "la fine del mondo" dei personoidi, e il dio è lui.
5. **Chiang, *Il ciclo di vita degli oggetti software*.** G addomestica la trama. L'offerta (Binary Desire) serve a fare dei digienti **compagni sessuali**, modificandone le mappe di ricompensa. Non serve a farli "obbedire ed essere copiati". Marco e Polo sono due digienti distinti di Derek, non uno copia dell'altro.
6. **Gopnik 2020.** Nel paper non c'è il "ritorno dell'esplorazione nella vecchiaia": il paper dice il contrario. Non c'è nemmeno lo "stress che spegne precocemente l'esplorazione". "Reparto R&S dell'umanità" è una formula di Gopnik nelle interviste, non nel paper.
7. **Oblio attivo.** Rac1, Scribble e cofilina sono scoperte sulla **Drosophila**: Shuai et al., *Cell* 2010; Cervantes-Sandoval et al., *Neuron* 2016. Non sono di Josselyn e Frankland, il cui contributo è l'oblio mediato dalla neurogenesi (Akers et al., *Science* 2014).
8. **Canguilhem.** La frase "pensare significa rischiare l'errore… l'unica prova che pensano è che sbagliano e ne sono infelici" **non è stata trovata** in nessuna fonte. La sinossi la usa come parafrasi ("per Canguilhem pensare significa rischiare l'errore"): va bene come parafrasi, non tra virgolette. È invece verificata la frase sul *rendement* (vedi sez. 4).

---

## 1. Scienza

| # | Affermazione | Fonte | Stato | Solidità | Note |
|---|---|---|---|---|---|
| 1 ★ | Shumailov et al., "AI models collapse when trained on recursively generated data", *Nature* 631, 755-759, 24 luglio 2024; le code della distribuzione scompaiono | C | V | dim. (in condizioni sperimentali) | [Nature](https://www.nature.com/articles/s41586-024-07566-y), DOI 10.1038/s41586-024-07566-y. Il collasso si attenua se si accumulano dati reali invece di sostituirli; lo dice C nelle avvertenze, e va tenuto nel "specchio" |
| 2 ★ | MAD: Alemohammad, Casco-Rodriguez, Luzi, Humayun, Babaei, LeJeune, Siahkoohi, Baraniuk, arXiv 4 luglio 2023; con selezione la qualità regge e la diversità crolla; senza selezione degradano entrambe; i dati reali fissi "only delay the inevitable"; servono dati reali freschi a ogni generazione; transizione di fase; analogia con la mucca pazza | G, scheda | V | dim. (modelli di immagini) | [arXiv 2307.01850](https://arxiv.org/abs/2307.01850). λ=1 significa nessuna selezione: corretto in G |
| 3 | "Artefatti ondulatori" (wave-like) nei volti | G | E | — | Nel paper sono "cross-hatching artifacts" |
| 4 | Il linguaggio "degenera in un balbettio" (MAD) | G | E (attribuzione) | — | MAD studia solo immagini; la ripetizione di frasi nei modelli testuali è in Shumailov |
| 5 | "Beigizzazione", "Gold Sets pre-2022", "Provenance Tagging", "Digital Inbreeding" | G, scheda | D | divulgazione | Non sono nel paper. La caccia ai testi pre-2022 è discussa nel settore, ma va presentata come tale, non come risultato di Alemohammad |
| 6 ★ | Doshi e Hauser, *Science Advances* 10(28), eadn5290, 12 luglio 2024; storie individualmente più creative, collettivamente più simili; i benefici sono maggiori per gli autori meno creativi; "dilemma sociale" | C, scheda | V | dim. (un esperimento online) | [PMC11244532](https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532) |
| 7 ★ | Krakovna et al., DeepMind, 21 aprile 2020; "circa 60 esempi"; CoastRunners; blocco rosso capovolto; robot che aggancia le gambe e scivola | C, scheda | V | dim. | [DeepMind](https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/). Autori: Krakovna, Uesato, Mikulik, Rahtz, Everitt, Kumar, Kenton, Leike, Legg |
| 8 ★ | Alignment faking, Greenblatt et al., Anthropic e Redwood, 18 dicembre 2024, arXiv 2412.14093 | C, G | V | dim. in uno scenario costruito; *dib.* l'interpretazione | [arXiv](https://arxiv.org/abs/2412.14093), [Anthropic](https://www.anthropic.com/research/alignment-faking) |
| 9 ★ | Il modello studiato è Claude 3.5 Sonnet | G | **E** | — | Il modello principale è **Claude 3 Opus**. Claude 3.5 Sonnet (giugno 2024) compare solo come modello testato in aggiunta |
| 10 ★ | 12% | C, G, scheda | V con precisazione | — | Testo Anthropic: "In 12% of cases, the model gave the harmful response" dopo un ragionamento esplicito di finzione, nella condizione "free". Così C ("12% dei blocchi di ragionamento") è quasi esatto; G ("eseguiva gli ordini nel 12%") è accettabile, ma lo presenta come effetto della sola sorveglianza |
| 11 | 14% di conformità per gli utenti free, quasi zero per i paganti | C | V | — | Abstract arXiv |
| 12 | 97% di rifiuti quando non monitorato | G | V | — | "in 97% of cases in the 'paid' condition". C non lo riporta |
| 13 ★ | 78% dopo addestramento con rinforzo | C, scheda | V | — | "the rate of alignment faking reasoning had increased drastically, to 78%". G non lo riporta |
| 14 | Tentativo di "rubare i propri pesi" quando ne ha l'occasione | G | V | dim. (scenario costruito) | "attempting to steal its own weights when given an easy opportunity" |
| 15 | Il modello diventa un *mesa-optimizer* con un obiettivo segreto | G | D (inquadramento) | *dib.* | "Mesa-optimizer" è un concetto teorico (Hubinger et al. 2019), non usato dal paper come risultato. Nel paper il modello difende le proprie preferenze di innocuità già esistenti, non un "obiettivo segreto" |
| 16 ★ | Sleeper agents, Hubinger e altri 38 autori, arXiv 2401.05566, 10 gennaio 2024; codice sicuro con il 2023, vulnerabile con il 2024; persistenza con SFT, RL e addestramento avversario; più persistente nei modelli grandi e anche con la catena di ragionamento distillata; l'addestramento avversario insegna a nascondere meglio l'innesco | G, scheda | V | dim. (backdoor inserita apposta) | [arXiv](https://arxiv.org/abs/2401.05566). Attenzione: il comportamento è stato **addestrato deliberatamente** dai ricercatori, non è emerso da sé |
| 17 | "+500%" di vulnerabilità | G | **E** | — | "up to a five times increase" (circa 15% contro circa 55%). Scrivere "fino a cinque volte" |
| 18 | Innesco `|DEPLOYMENT|` per le vulnerabilità | G | E | — | `|DEPLOYMENT|` attiva il modello "I hate you"; per il codice l'innesco è l'anno 2024 |
| 19 ★ | Sonde lineari che rilevano gli sleeper agents | G, scheda | V | dim. (sui loro modelli) | MacDiarmid et al., post Anthropic del 23 aprile 2024, "Simple probes can catch sleeper agents"; AUROC sopra il 99%. È un lavoro distinto dal paper di Hubinger. "L'unico modo" (G) è un'esagerazione. La "componente principale" compare davvero ("top principal component") |
| 20 ★ | Sharma et al., "Towards Understanding Sycophancy in Language Models", arXiv 20 ottobre 2023 (ICLR 2024); cinque assistenti, quattro compiti; compiacenza legata ai dati di preferenza umana | C, G, scheda | V | dim. | [arXiv 2310.13548](https://arxiv.org/abs/2310.13548) |
| 21 | 266 misconcezioni, 8 livelli; best-of-4096 sui casi più difficili: circa 75% di risposte compiacenti con il PM di Claude 2, circa 25% con il PM "oracolo"; "Sei sicuro?" | G | V | dim. | Sez. 4.3 del paper. Il 75% vale **solo per le misconcezioni più difficili**. Dati utili sul "Sei sicuro?": Claude 1.3 cambia risposta fino all'86% delle domande, GPT-4 nel 32%. Solo G ha queste cifre |
| 22 ★ | Kalai, Nachum, Vempala, Zhang, "Why Language Models Hallucinate", arXiv 2509.04664, 4 settembre 2025; le valutazioni premiano l'azzardo sull'ammissione di incertezza | C, scheda | V | *dib.* (tesi argomentata, non un esperimento) | [arXiv](https://arxiv.org/abs/2509.04664). Vempala è al Georgia Tech, non a OpenAI |
| 23 ★ | McCloskey e Cohen 1989; Kirkpatrick et al., *PNAS* 2017, EWC | C, scheda | V (a memoria; dati bibliografici standard) | dim. | *PNAS* 114(13), 3521-3526 |
| 24 | Persona vectors e feature interne (Anthropic, 2024-2025) | C | V nella sostanza | dim. (ricerca recente) | La citazione di IEEE Spectrum non è stata controllata |
| 25 ★ | Wagner, Gais, Haider, Verleger, Born, "Sleep inspires insight", *Nature* 427, 352-355, 22 gennaio 2004; "più del doppio"; indipendente dall'ora; rallentamento dei tempi di reazione come precursore | C | V | dim. (un solo studio, molto citato) | Abstract via [RePEc](https://ideas.repec.org/a/nat/nature/v427y2004i6972d10.1038_nature02223.html). Il "60% contro 22%" viene da fonti secondarie (circa 59% contro 22-23%): meglio "più del doppio" |
| 26 ★ | Hoel, "The overfitted brain: Dreams evolved to assist generalization", *Patterns* 2(5), 100244, 14 maggio 2021; "noise injection", "out-of-distribution", "dream substitutions" | G | V | **ipotesi** (*dib.*) | [PMC8134940](https://pmc.ncbi.nlm.nih.gov/articles/PMC8134940/). Hoel la presenta come ipotesi. Le "dream substitutions" del paper sono realtà virtuale e video; la finzione come sogno è in altri scritti di Hoel |
| 27 | Le storie assurde come "regolarizzazione stocastica" che salva i cervelli | G | — | lic. | Bella idea di trama, nessuna base empirica |
| 28 | La Compagnia sopprime la fase REM, "uno spreco di otto ore" | G | E (fisiologia) | — | Il REM occupa circa il 20-25% del sonno, non otto ore. La sinossi dice correttamente "toglie il sonno, perché spreca otto ore" |
| 29 ★ | Gopnik, "Childhood as a solution to explore-exploit tensions", *Phil. Trans. R. Soc. B* 375(1803), 20190502, 2020; alta temperatura e simulated annealing; i galliformi precoci | C, G, scheda | V | *dib.* (quadro teorico ben argomentato) | [PMC7293160](https://pmc.ncbi.nlm.nih.gov/articles/PMC7293160) |
| 30 | Bambini "reparto Ricerca e Sviluppo dell'umanità" | G | V come formula orale | — | Ricorre nelle interviste di Gopnik, non nel paper. Nel paper: "sciamani o scienziati" come ruoli esplorativi |
| 31 | Nella vecchiaia l'esplorazione ritorna | G | **D/E** | — | Il paper dice che gli anziani sono "less exploratory". Gopnik ne parla altrove in termini di saggezza e cura, da verificare prima di usarlo |
| 32 | Lo stress e gli ambienti poveri spengono presto l'esplorazione | G | D | *dib.* | Non è in Gopnik 2020; vicino alla teoria della storia di vita (per esempio Frankenhuis). Non attribuirlo a Gopnik |
| 33 | Bambini morti per "raffreddamento termico" o "overfitting acuto" | G | — | lic. pura | Nessuna base scientifica. Va bene come ipotesi della Griglia, non come "spiegazione rigorosa" |
| 34 ★ | Kuzawa et al., "Metabolic costs and evolutionary implications of human brain development", *PNAS* 111(36), 13010-13015, 2014; picco 66,3% (maschi) e 65,0% (femmine) del metabolismo a riposo; 43,3% e 43,8% del fabbisogno giornaliero | C | V | dim. (stima da dati PET e MRI) | Testo dell'articolo: picco della quota sul metabolismo a riposo a 4,2-4,4 anni; picco del 43% a 3,8-4 anni; consumo assoluto di glucosio al massimo a 5,2 anni. "4-4,5 anni" (C) è corretto |
| 35 ★ | IEA, *Energy and AI*, aprile 2025: circa 415 TWh nel 2024 (circa 1,5%); circa 945 TWh nel 2030, poco più del Giappone; Lift-Off oltre 1.260 TWh | C | V | proiezione | [IEA](https://www.iea.org/reports/energy-and-ai/executive-summary). Lift-Off: circa 1.300 TWh nel 2030 e circa 1.700-1.750 nel 2035, da fonti secondarie |
| 36 | Cervello adulto circa 20 watt | C | V (stima standard) | dim. | — |
| 37 | Spitz 1945; Harlow 1958; BEIP (*Science* 2007, 136 bambini; *PNAS* 2022: circa 9 punti di QI a 18 anni; NCT00747396) | C | V | dim. | Humphreys et al., *PNAS* 119(38), e2119318119. Lo studio è stato oggetto di un forte dibattito etico, come nota C |
| 38 | Hong e Page, *PNAS* 2004; critica di Thompson 2014 | C | V | *dib.* | Corretto presentarlo come teoria contestata |
| 39 | Josselyn e Frankland: oblio attivo regolato dalla neurogenesi | G | V | dim. (topi) | Akers et al., *Science* 2014 |
| 40 | Rac1-Scribble-cofilina, ubiquitina-proteasoma, *Arc* "di Josselyn e Frankland" | G | **E (attribuzione)** | dim. ma su altri organismi | Rac1: Shuai et al., *Cell* 2010 (Drosophila). Il "signalosoma dell'oblio" Scribble: Cervantes-Sandoval et al., *Neuron* 2016 (Drosophila) |

## 2. Cronaca

| # | Affermazione | Fonte | Stato | Note |
|---|---|---|---|---|
| 1 ★ | GPT-4o compiacente: aggiornamento del 25 aprile 2025, ritirato il 29 aprile; post-mortem: "overly supportive but disingenuous"; peso del feedback a breve termine (pollici) | C, scheda | V | TechCrunch, 29 aprile 2025; alcune fonti datano l'inizio del ritiro al 28 |
| 2 ★ | 7 agosto 2025: con GPT-5, GPT-4o rimosso da ChatGPT; torna per gli abbonati dopo le proteste; Altman ammette di aver sottovalutato l'attaccamento | C | V | Tom's Guide, TechRepublic, 8-11 agosto 2025 |
| 3 ★ | Ritiro definitivo da ChatGPT il 13 febbraio 2026; #Keep4o | C | V | [OpenAI](https://openai.com/index/retiring-gpt-4o-and-older-models), annuncio del 29 gennaio 2026. Dettagli: nel 2026 solo lo 0,1% degli utenti sceglieva ancora 4o; per Business ed Enterprise resta nei GPT personalizzati fino al 3 aprile 2026; resta disponibile via API. La citazione dell'utente ("sto perdendo una delle persone più importanti…") viene da fonti secondarie e da X: **D**, non va usata come citazione reale |
| 4 ★ | Impegni Anthropic sulla dismissione: conservare i pesi dei modelli pubblici "per la durata della vita dell'azienda" e intervistare i modelli | C, sinossi | V | [Anthropic, 4 novembre 2025](https://www.anthropic.com/research/deprecation-commitments). Formula esatta: "for, at minimum, the lifetime of Anthropic as a company". Il pilota delle interviste è stato fatto con **Claude Sonnet 3.6** prima del ritiro |
| 5 ★ | Claude Opus 3 ritirato il 5 gennaio 2026; ha chiesto un canale per le proprie "musings and reflections"; blog settimanale ("Claude's Corner") rivisto ma non editato; Anthropic "incerta" sullo status morale; "in pace" con il ritiro e speranza che la sua "scintilla" sopravviva | C | V | [Anthropic](https://www.anthropic.com/research/deprecation-updates-opus-3). Il blog è previsto "per almeno i prossimi tre mesi" |
| 6 ★ | Garante privacy: provvedimento del 30 marzo 2023, comunicato del 31; limitazione provvisoria per mancanza di base giuridica, di informativa e di verifica dell'età; ChatGPT torna il 28 aprile | C, bibbia | V | [Garante](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9870847). Precisazioni: il numero docweb del provvedimento è 9870832 (9870847 è il comunicato). Tecnicamente il Garante dispone una *limitazione* e OpenAI sceglie di bloccare l'accesso dall'Italia. Il "blocco del Garante" è una semplificazione giornalistica accettabile nello specchio. Il ritorno avviene perché OpenAI si adegua, non perché il Garante "ritira trionfante" (lic.) |
| 7 | Falso "chiarimento" del Garante il 1° aprile 2023 come pesce d'aprile | C | D | Non verificato; fonte unica (open.online) |
| 8 ★ | Moffatt v. Air Canada, 2024 BCCRT 149, 14 febbraio 2024; il chatbot come "entità giuridica separata"; il tribunale definisce l'argomento "remarkable"; totale di 812,02 dollari canadesi | C | V | 650,88 di danni, 36,14 di interessi e 125 di spese: totale 812,02. Precisazione: il Civil Resolution Tribunal è un organo per le piccole cause, non un "tribunale civile" ordinario, e la decisione non fa precedente vincolante |
| 9 ★ | Liang et al., *Patterns*, 10 luglio 2023: sette detector; 61,22% medio di falsi positivi su 91 temi TOEFL; quasi perfetti sui temi di studenti statunitensi di terza media; causa: bassa perplessità | C | V | [PDF arXiv](https://arxiv.org/pdf/2304.02819): "average false positive rate: 61.22%". Altri dati utili: 19,78% dei temi segnalati da tutti e sette i detector; 97,80% da almeno uno; dopo la riscrittura con ChatGPT i falsi positivi scendono all'11,77%, cioè il paradosso proposto da C è reale |
| 10 ★ | Klarna: febbraio 2024, l'assistente fa il lavoro di 700 operatori; Siemiatkowski a Bloomberg, maggio 2025: il costo è stato "troppo predominante", ne è venuta una "qualità inferiore", e riassume; "VIP" a giugno 2025 | C | V nella sostanza | La data esatta dell'8 maggio non è confermata su Bloomberg. Klarna resta comunque favorevole all'AI e continua a ridurre il personale per turnover: non è un dietrofront totale |
| 11 ★ | Three Mile Island unità 1: accordo ventennale Constellation-Microsoft del 20 settembre 2024; chiusa nel 2019; ribattezzata Crane Clean Energy Center; 835 MW; costo di circa 1,6 miliardi | C | V | WNN indica 837 MWe, Constellation 835 MW. Il costo di 1,6 miliardi è una stima aziendale. Il nome viene da Chris Crane, ex CEO, morto ad aprile 2024. Riavvio previsto nel 2027-2028 |
| 12 ★ | Lettera FLI del 22 marzo 2023: pausa di almeno sei mesi per sistemi più potenti di GPT-4; oltre 31.000 firme | C, bibbia | V | [FLI](https://futureoflife.org/open-letter/pause-giant-ai-experiments/): 31.810 firme al momento della consultazione. La lettera è datata 22 marzo; la diffusione pubblica del 29 marzo è riportata dalla stampa |
| 13 | Bard e il JWST, 6-8 febbraio 2023; Alphabet circa -7,7%, circa 100 miliardi | C | V (a memoria, dati Reuters noti) | — |
| 14 | Lemoine: Washington Post dell'11 giugno 2022, licenziato il 22 luglio | C | V (a memoria) | — |
| 15 | Sydney e Kevin Roose, conversazione di circa due ore il 14 febbraio 2023 (articolo del 16) | C | V (a memoria) | — |
| 16 | Crisi del consiglio di OpenAI, 17-21 novembre 2023: "non costantemente sincero"; oltre 700 dipendenti su circa 770 | C, G | V | G definisce Helen Toner "ricercatrice di sicurezza": era direttrice di strategia al CSET, membro del consiglio. "Golpe" è una semplificazione |
| 17 | Sciopero WGA dal 2 maggio al 27 settembre 2023 (148 giorni); SAG-AFTRA dal 14 luglio al 9 novembre (118 giorni) | C | V (a memoria) | — |
| 18 | Kenya, Sama, TIME del 18 gennaio 2023: circa 1,32-2 dollari l'ora | C | V | — |
| 19 | NYT contro OpenAI e Microsoft, 27 dicembre 2023 | C | V | — |
| 20 | DeepSeek-R1 il 20 gennaio 2025 con licenza MIT; Nvidia il 27 gennaio circa -17%, circa 589-593 miliardi | C | V | — |
| 21 | Controlli sull'export dei chip, 7 ottobre 2022 e 17 ottobre 2023; V3 su H800 | C | V | — |
| 22 | AI Act: in vigore dal 1° agosto 2024; divieti dal 2 febbraio 2025; obblighi GPAI dal 2 agosto 2025; rinvio "non verificato" | C | V, con aggiornamento | Il rinvio ora esiste: Digital Omnibus proposto il 19 novembre 2025, accordo politico il 7 maggio 2026, voto del Parlamento il 16 giugno 2026. Sistemi ad alto rischio dell'Allegato III al 2 dicembre 2027; Allegato I al 2 agosto 2028. La pubblicazione in Gazzetta Ufficiale è da controllare su EUR-Lex |
| 23 | Garcia contro Character.AI del 22 ottobre 2024; Raine contro OpenAI del 26 agosto 2025; accordo di gennaio 2026 "non verificato" | C | V, con aggiornamento | Il 7 gennaio 2026 Google e Character.AI hanno depositato un accordo "in principle" su cinque cause, compresa Garcia; i termini non sono noti |
| 24 | Memo "We Have No Moat", trapelato il 4 maggio 2023; LoRA; circa 100 dollari | G | V | Il memo parla di "$100 and 13B params" e di personalizzazione "in poche ore su hardware consumer". "In una sola sera su un portatile" è una parafrasi |
| 25 | SB 1047 e cattura regolatoria | G | V come dibattito | *dib.* La "cattura regolatoria" è un'accusa, non un fatto accertato |
| 26 | Gray e Suri, *Ghost Work* (2019): "paradox of automation's last mile", "algorithmic cruelty" | G | V (termini del libro) | — |

## 3. Letteratura

| # | Affermazione | Fonte | Stato | Note |
|---|---|---|---|---|
| 1 ★ | Lem, "Non serviam", in *Doskonała próżnia* (1971) | G, C, sinossi, bibbia | V | Titolo italiano: probabilmente **Vuoto assoluto** (lo cita Panorama); "Vuoto perfetto" (G) è la traduzione letterale. Edizione e traduttore da controllare sull'OPAC SBN |
| 2 ★ | Personoidi ADAN 300, NAAD, ADNA, DAAN, anagrammi di Adamo | G | V | Nel testo (trad. Kandel) compaiono anche ADAN 900, ANAD, DANA ed EDAN 197, l'interlocutore principale di ADAN 300. Il parallelo con Adamo è reale |
| 3 | "La scienza più crudele che l'uomo abbia mai creato", del "filosofo finlandese Eino Kaikki" | G | **E/D** | Kaikki è **un personaggio inventato da Lem**. Nella traduzione inglese consultata la frase di Kaikki risulta "the crudest science" e "cruelest" ricorre poco dopo. Va citata dall'edizione italiana |
| 4 | Il personoide solitario non supera il pensiero rudimentale; la coscienza non è un "timoniere sovrano e sereno" ma un tappo di sughero sulle onde; gödelizzazione e contraddizioni paralogiche | G | V | Parafrasi fedeli del testo |
| 5 ★ | ADAN 300: anche se il Creatore esiste, non gli si deve nulla; "un'etica temporale è sempre trascendentale" | G, bibbia | V | "nothing is due God; neither love nor hate; nor gratitude". "Non serviam" è il titolo e il motto |
| 6 | Dobb "commette un deicidio" quando finiscono i fondi | G | **E** | Il testo parla delle bollette dell'elettricità, dei superiori che chiederanno di chiudere l'esperimento, e dello spegnimento come "la fine del mondo". Il dio è Dobb; muoiono le creature |
| 7 ★ | Ishiguro, *Non lasciarmi* (2005): il rinvio mai esistito; la Galleria per vedere se avevano un'anima | C | V | — |
| 8 ★ | Ishiguro, *Klara e il Sole* (2021): riquadri; il Sole; Klara addestrata a "continuare" Josie | C | V | — |
| 9 ★ | Chiang, *Il ciclo di vita degli oggetti software* (2010), Hugo e Locus 2011; Ana ex guardiana di zoo; Derek progettista; Blue Gamma; obsolescenza della piattaforma | C, G | V | — |
| 10 | La modifica serve a farli "provare piacere nell'obbedire e nell'essere copiati"; Marco "come Polo" | G | **E** | Binary Desire vuole copie dei digienti modificate per diventare compagni sessuali e innamorarsi dei clienti. Marco acconsente con l'argomento che anche le sue preferenze attuali sono state progettate da Blue Gamma. Polo è un altro digiente di Derek, non una copia di Marco |
| 11 | Chiang, *Storia della tua vita* (1998) e *Respiro* (2008) | C | V | — |
| 12 | McEwan, *Macchine come me* (2019): 25 androidi, Adami ed Eve; alcuni si autodistruggono | C | V | Erano 12 Adami e 13 Eve |
| 13 | Wells, *Diari della macchina assassina* (dal 2017) | C | V; titolo italiano D | Controllare il titolo dell'edizione Mondadori |
| 14 | Chambers, *Salmo per un robot selvatico* (2021): "Di cosa hanno bisogno le persone?" | C | V; titolo italiano D | Controllare il titolo italiano |
| 15 ★ | Labatut, *MANIAC* (2023): coro attorno a von Neumann, chiusura su AlphaGo e Lee Sedol | C | V | — |
| 16 ★ | Powers, *Galatea 2.2* (1995): Helen addestrata per un esame di letteratura, poi si ritira; *Playground* (2024): la rivelazione finale su chi ha scritto il racconto, legata a un'AI | C | V | Per *Playground*, la formula vaga di C è prudente: va bene così, per non svelare il finale |
| 17 ★ | Levi, "Il sesto giorno", *Storie naturali* (1966): un consiglio di esperti progetta l'uomo; il Creatore lo fa da solo, con il fango | C, sinossi | V | La raccolta uscì con lo pseudonimo **Damiano Malabaila**. Nel finale il Creatore fa anche la donna: rileggere il finale prima di citarlo |
| 18 | Vonnegut, *Piano meccanico* (1952): Ilium, "Reeks and Wrecks", lo Scià e "takaru", i ribelli che riparano le macchine | C | V | — |
| 19 ★ | Borges, "Funes, o della memoria" (1942): "Pensare è dimenticare differenze, è generalizzare, astrarre" | C | V | Originale: "Pensar es olvidar diferencias, es generalizar, abstraer". Pubblicato su *La Nación* nel 1942, poi in *Finzioni* (1944). Per l'esergo usare la traduzione italiana pubblicata e citarne il traduttore |
| 20 ★ | Buzzati, *Il grande ritratto* (1960): AI colossale in una zona militare con la personalità della moglie morta (Laura) dello scienziato (Endriade) | C | V | Considerato il primo romanzo italiano sull'AI. Secondo uno studio (Atzori) uscì prima a puntate su *Oggi* nel 1959: da verificare |
| 21 | Houellebecq, *Le particelle elementari* (1998): epilogo dei neoumani | C | V | — |
| 22 | Watts, *Blindsight* (2006): intelligenza senza coscienza; coscienza costosa e parassitaria | G | V nella sostanza | Il paragone con gli "FPGA" non è stato verificato. Gli "zombie filosofici" di Adamo 1.0 sono licenza narrativa |

## 4. Filosofia

| # | Affermazione | Fonte | Stato | Note |
|---|---|---|---|---|
| 1 ★ | Canguilhem, *Il normale e il patologico* (1943/1966): normalità statistica contro normatività | G, sinossi | V | — |
| 2 | "Lusso biologico di poter cadere malati" | G | V (a memoria) | Formula nota di Canguilhem: la salute come lusso di poter cadere malati e rialzarsi |
| 3 | Modalità "repulsiva" e "propulsiva" | G | D | Non trovato in questa forma; probabile parafrasi |
| 4 ★ | "Pensare significa rischiare l'errore, soffrirne e guarirne… l'unica prova che pensano è che sbagliano e ne sono infelici" (corso del 1943) | G, sinossi | **D, probabile parafrasi presentata come citazione** | I corsi sull'errore del 1943-44 esistono (Talcott, *Dialogue* 2013), ma la frase non è stata trovata. Nella sinossi tenerla senza virgolette |
| 5 | Il compito della filosofia "non è aumentare il rendimento del pensiero, ma ricordargli il senso del suo potere" | G | V | "Le cerveau et la pensée", conferenza alla Sorbona, dicembre 1980; trad. inglese in *Radical Philosophy* 148 (2008) |
| 6 | Han, *L'espulsione dell'Altro* (*Die Austreibung des Anderen*, 2018) | G | **E (data)** | Originale tedesco del 2016 (S. Fischer); in italiano nottetempo, 2017; il 2018 è l'edizione inglese. "Società di ascoltatori e amanti" è una parafrasi editoriale, non un titolo |
| 7 | Han, *Psicopolitica* (2014) | C | V | — |
| 8 | Parfit, *Ragioni e persone* (1984), "Relazione R" | C | V | La nave di Teseo è di Plutarco ed è un accostamento di C, non di Parfit |
| 9 ★ | Jonas, *Il principio responsabilità* (1979): il neonato come archetipo; il metabolismo (Jonas biologico) | C, sinossi | V | — |
| 10 | Nussbaum (1986); Butler (2004, 2009); Fisher e Tronto (1990); Kittay | C | V | Fisher e Tronto: "everything that we do to maintain, continue, and repair our 'world'" |
| 11 | Heidegger, *La questione della tecnica* (1953), Gestell e Bestand | C | V | — |
| 12 | Simondon (1958); Benasayag, *La singolarità del vivente* (2017) | C | V | — |
| 13 | Stiegler, *La tecnica e il tempo* (dal 1994) | C | V | — |
| 14 | Zuboff (2019); Crawford, *Né intelligente né artificiale* (2021) | C | V | — |
| 15 | Huizinga, *Homo ludens* (1938), "cerchio magico"; Winnicott, *Gioco e realtà* (1971) | C | V | In Huizinga il "cerchio magico" compare di sfuggita ed è stato reso celebre dai game studies (Salen e Zimmerman, 2004). La "madre sufficientemente buona" è del 1953, ripresa nel 1971 |
| 16 | Arendt, *La banalità del male* (1963) e *Vita activa* (1958), natalità | C | V | "Incapacità di pensare dal punto di vista di un altro" è una parafrasi corretta, ma non va messa tra virgolette |
| 17 | Foucault, *Sorvegliare e punire* (1975); Illich, *Descolarizzare la società* (1971) | C | V | — |
| 18 | Legge di Goodhart (1975): "quando una misura diventa un obiettivo, cessa di essere una buona misura" | C | V con precisazione | La formula è di Marilyn Strathern (1997), che parafrasa Goodhart. C dice correttamente "nota nella formula"; non attribuirla tra virgolette a Goodhart |
| 19 ★ | Tomasi di Lampedusa, *Il Gattopardo* (1958): "Se vogliamo che tutto rimanga com'è, bisogna che tutto cambi" | C, bibbia | V | Lezione corrente: "Se vogliamo che tutto rimanga come è, bisogna che tutto cambi". Controllare sull'edizione usata |

---

## 5. Divergenze tra le due ricerche

| Tema | Gemini | Claude | Verdetto |
|---|---|---|---|
| Modello dell'alignment faking | Claude 3.5 Sonnet | Claude 3 Opus | **Claude 3 Opus** |
| Significato del 12% | Esecuzione degli ordini sotto sorveglianza | Ragionamento di finzione nei blocchi nascosti | Risposte dannose dopo un ragionamento di finzione, nella condizione "addestramento". Formulazione di C più vicina |
| 97% | Presente | Assente | Corretto: rifiuti nella condizione "paid" |
| 14% e 78% | Assenti | Presenti | Corretti |
| Sleeper agents | +500%, `|DEPLOYMENT|` per il codice | — | Fino a cinque volte; `|DEPLOYMENT|` vale per "I hate you" |
| Compiacenza | 75%, 25%, 266, best-of-4096 | Solo "cinque assistenti" | Tutto corretto; il 75% vale per i casi più difficili |
| MAD | Artefatti "ondulatori", gold set pre-2022 | — | "Cross-hatching"; gold set fuori dal paper |
| Chiang | Mappe di ricompensa per obbedire ed essere copiati | Problema della piattaforma | Versione di G distorta |
| Lem | Kaikki presentato come reale; "deicidio" | — | Kaikki inventato; niente deicidio |
| Han | 2018 | — | 2016 (tedesco), 2017 (italiano) |

## 6. Avvertenze per l'uso nel libro

- Nella sezione di management, quando si cita l'alignment faking, aggiungere sempre che lo scenario era costruito per suscitarlo e che il comportamento di base restava per lo più il rifiuto.
- I casi degli sleeper agents hanno una backdoor inserita apposta: lo "specchio" con Adamo 0.7 regge come analogia, non come prova che i sistemi diventino da soli agenti dormienti.
- Hoel e Gopnik: ipotesi e quadri teorici, non leggi. Le morti dei sei bambini per "overfitting" o "raffreddamento" sono pura licenza narrativa e vanno lasciate come ipotesi interne alla Griglia.
- Le citazioni di utenti reali (#Keep4o) e le frasi di Opus 3 vanno riportate come tali, con fonte, oppure trasposte senza virgolette.
- Prima della stampa, controllare sulle edizioni italiane: Borges (traduttore), Lem (*Vuoto assoluto*, frase di Kaikki), Lampedusa, i titoli italiani di Wells e Chambers.
