"""Pobiera dzienne odsłony wybranych artykułów polskiej Wikipedii (Wikimedia Pageviews API).

Wynik: odslony_wikipedia.csv obok tego pliku, kolumny:
data, ADHD, Zaburzenia_depresyjne, Psychologia, pl_wikipedia_ogolem

Tylko ruch ludzi (agent=user), wszystkie platformy (access=all-access).
Dane o odsłonach udostępnia Wikimedia Foundation na licencji CC0.

Uruchomienie: python pobierz_odslony.py
"""

import csv
import json
import urllib.parse
import urllib.request
from pathlib import Path

OD = "20160101"
DO = "20260930"
ARTYKULY = ["ADHD", "Zaburzenia_depresyjne", "Psychologia"]
API = "https://wikimedia.org/api/rest_v1/metrics/pageviews"
# Wikimedia odrzuca domyślnego User-Agenta (Python-urllib) — podaj opisowy, najlepiej z własnym kontaktem.
NAGLOWKI = {"User-Agent": "swps-wstep-do-analizy-danych/1.0 (materialy dydaktyczne)"}


def pobierz(url):
    req = urllib.request.Request(url, headers=NAGLOWKI)
    with urllib.request.urlopen(req, timeout=60) as odp:
        items = json.load(odp)["items"]
    # timestamp ma postać RRRRMMDDGG, np. 2016010100
    return {f"{x['timestamp'][:4]}-{x['timestamp'][4:6]}-{x['timestamp'][6:8]}": x["views"] for x in items}


def main():
    kolumny = {}
    for tytul in ARTYKULY:
        t = urllib.parse.quote(tytul, safe="")
        kolumny[tytul] = pobierz(f"{API}/per-article/pl.wikipedia/all-access/user/{t}/daily/{OD}/{DO}")
    kolumny["pl_wikipedia_ogolem"] = pobierz(f"{API}/aggregate/pl.wikipedia/all-access/user/daily/{OD}00/{DO}00")

    daty = sorted(set().union(*kolumny.values()))
    plik = Path(__file__).with_name("odslony_wikipedia.csv")
    with plik.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["data", *kolumny])
        for d in daty:
            # dzień bez odsłon API pomija — zostawiamy puste pole (w pandas: NaN)
            w.writerow([d, *(kol.get(d, "") for kol in kolumny.values())])
    print(f"Zapisano {plik.name}: {len(daty)} dni, {daty[0]} – {daty[-1]}")


if __name__ == "__main__":
    main()
