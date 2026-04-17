# 👁 **VYUŽITIE OPENAI NA POPIS OKOLIA PRE  NEVIDIACICH**
 Tento projekt predstavuje vývoj a implementáciu webovej aplikácie, ktorá umožňuje nevidiacim používateľom prístup k informáciám o ich prostredí prostredníctvom analýzy obrazu a hlasovej interakcie. Aplikácia využíva moderné technológie umelej inteligencie na popis prostredia, odpovedanie na otázky a poskytovanie jednoduchej hlasovej komunikácie.
## 📌 **Popis projektu**
Systém umožňuje používateľovi nasnímať obrázok alebo položiť hlasovú otázku prostredníctvom webového prehliadača. Frontend potom odošle obrázok a textový dopyt do backendu, ktorý ich spracuje a odošle službe umelej inteligencie. API vráti popis prostredia, identifikáciu objektu alebo odpoveď na dopyt. Aplikácia je navrhnutá tak, aby bola čo najprístupnejšia a najpoužívateľsky prívetivejšia pre nevidiacich používateľov. Zahŕňa hlasové ovládanie, hlasové prehrávanie odpovedí, analýzu obrazu pomocou umelej inteligencie, jednoduché webové rozhranie a spracovanie obrazu Base64.
## ⚙️ **Hlavné funkcie**
- zachytenie obrazu cez webkameru
- hlasové ovládanie pomocou rozhrania Web Speech API
- odoslanie obrazu a dotazu do backendu
- analýza obrazu pomocou AI
- prehrávanie hlasovej odpovede
- jednoduché a prístupné ovládanie pre nevidiacich
- spracovanie chýb a neúplných vstupov

## 🧰 **Použité technológie**
### Backend
- Python
- Flask
- Requests
### Frontend
- HTML
- CSS
- avaScript
- Web Speech API
### AI služby
- externé API na analýzu obrazu a generovanie odpovedí
## 📁 **Štruktúra projektu**
```
project/
│
├── app.py                # backend aplikácie (Flask)
│
├── templates/
│   └── index.html        # hlavné webové rozhranie
│
├── static/
│   ├── script.js         # logika frontendu
│   └── styles.css        # štýly
│
└── README.md
```
## 🚀 **Spustenie aplikácie**
1. Inštalácia závislostí
```
pip install -r requirements.txt
```
2. Spustenie backendu
```
python app.py
```
3. Otvorenie aplikácie v prehliadači
```
http://127.0.0.1:5000
```
Aplikácia sa načíta vo webovom rozhraní a je pripravená na používanie.
## 🔄 **Spôsob fungovania**
1. Používateľ nasníma obrázok alebo položí otázku hlasom.
2. Frontend odošle Base64 obrázok a textový dotaz na backend.
3. Backend vytvorí požiadavku pre AI API.
4. API vráti opis obrázka alebo odpoveď na otázku.
5. Výsledok sa zobrazí používateľovi a bude prečítaný hlasom.
## ⚠️ **Obmedzenia systému**
- Presnosť analýzy obrazu závisí od kvality obrazu.
- Rozpoznávanie reči môže byť menej spoľahlivé v hlučnom prostredí.
- Rýchlosť odozvy závisí od externého API.
- Aplikácia vyžaduje internetové pripojenie.
## 🌱 **Možnosti rozšírenia**
- presnejšia navigácia v priestore
- offline spracovanie obrazu
- ozšírenie hlasových príkazov
- režim „asistenta pri pohybe“ – upozornenia na prekážky v reálnom čase
- pridanie podpory pre viac jazykov
# 👤 **Autor**
Yulianna Bobela
# 🎓 **Typ práce**
Bakalárska práca – Aplikovaná informatika
Univerzita Konštantína Filozofa v Nitre




