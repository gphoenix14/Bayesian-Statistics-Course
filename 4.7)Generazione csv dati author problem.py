#!/usr/bin/env python3
"""
Genera il file upon_rates.csv con:

• i 98 tassi standardizzati («upon» ogni 1000 parole) di Hamilton e Madison
  ricostruiti dalla distribuzione nelle slide;
• una riga finale per il documento n. 54 a paternità incerta
  (2 «upon» su 2008 parole → rate = 0.996).

"""
import csv
from pathlib import Path

OUTPUT = Path("data/upon_rates.csv")

# valore centrale di ciascun intervallo di classe
BIN_VALUE = {
    "0": 0.0,
    "(0,1]": 0.5,
    "(1,2]": 1.5,
    "(2,3]": 2.5,
    "(3,4]": 3.5,
    "(4,5]": 4.5,
    "(5,6]": 5.5,
    "(6,7]": 6.5,
    "(7,8]": 7.5,
}

# frequenze per autore (slide Distribuzione Tassi standardizzati) :contentReference[oaicite:2]{index=2}&#8203;:contentReference[oaicite:3]{index=3}
DIST = {
    "Hamilton": {"0": 0,  "(0,1]": 1, "(1,2]": 10, "(2,3]": 11,
                 "(3,4]": 11, "(4,5]": 10, "(5,6]": 3, "(6,7]": 1, "(7,8]": 1},
    "Madison":  {"0": 41, "(0,1]": 7, "(1,2]": 2,  "(2,3]": 0,
                 "(3,4]": 0,  "(4,5]": 0, "(5,6]": 0, "(6,7]": 0, "(7,8]": 0},
}

rows, idx = [], 1
for author, bins in DIST.items():
    for label, n in bins.items():
        rows.extend(
            {"id": idx + i, "author": author, "rate": BIN_VALUE[label]}
            for i in range(n)
        )
        idx += n

# documento incerto n°54 (2 upon / 2008 parole → 0.996)
rows.append({"id": idx, "author": "Unknown", "rate": 0.996})

with OUTPUT.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "author", "rate"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Creato {OUTPUT} con {len(rows)} record, incluso il documento Unknown.")
