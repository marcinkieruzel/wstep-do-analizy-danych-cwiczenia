# Wstęp do analizy danych w SI — ćwiczenia

Notatniki Jupyter do warsztatów z przedmiotu *Wstęp do analizy danych w SI*
(Uniwersytet SWPS, Psychologia i informatyka, rok akademicki 2026/2027).

## Ćwiczenia

| Notatnik | Temat | Zadania |
|---|---|---|
| [`01-numpy-pandas-daty.ipynb`](01-numpy-pandas-daty.ipynb) | NumPy, pandas, wczytywanie danych, daty i czas | 41 (A1–D13) |

Ćwiczenie 01 to powtórka narzędzi, bez analizy danych:

- **A — NumPy:** tworzenie tablic, typy i `astype`, kształt i indeksowanie `[wiersz, kolumna]`, operacje na całych tablicach, maski logiczne, `np.where` i `NaN`, agregacje wzdłuż osi, rozgłaszanie, widok a kopia, sortowanie, generator liczb losowych.
- **B — pandas:** `Series` i wyrównanie po indeksie, `DataFrame` ze słownika, `[ ]` / `loc` / `iloc`, filtrowanie (`&`, `|`, `isin`), dodawanie, usuwanie i zmiana nazw kolumn, sortowanie, `set_index` / `reset_index`, typy kolumn (`to_numeric`, `category`), braki danych.
- **C — wczytywanie danych:** `read_csv` z datą w indeksie, `usecols` i `nrows`, „brudny” plik (kodowanie, średnik, przecinek dziesiętny, własne oznaczenia braków, komentarze), zapis `to_csv`.
- **D — daty i czas:** `Timestamp` i `Timedelta`, `to_datetime` z formatem, pułapka dzień–miesiąc, `errors="coerce"`, łączenie daty i godziny, akcesor `.dt`, data jako indeks, `date_range`, `resample`, `shift`, strefy czasowe i zmiana czasu.

## Jak zacząć

Potrzebny jest Python 3.10 lub nowszy.

```bash
git clone https://github.com/marcinkieruzel/wstep-do-analizy-danych-cwiczenia.git
cd wstep-do-analizy-danych-cwiczenia
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Z [uv](https://docs.astral.sh/uv/) wystarczy jedna komenda w folderze repo:

```bash
uv run --with jupyterlab --with pandas --with numpy jupyter lab
```

Bez gita: *Code → Download ZIP* na stronie repo, rozpakuj i dalej jak wyżej od `python -m venv`.

Notatnik czyta dane ze ścieżek `dane/...`, więc uruchamiaj Jupytera w głównym folderze repo.

### W Google Colab

Otwórz [01-numpy-pandas-daty.ipynb w Colab](https://colab.research.google.com/github/marcinkieruzel/wstep-do-analizy-danych-cwiczenia/blob/main/01-numpy-pandas-daty.ipynb). Komórka **Start** sama pobierze pliki z folderu `dane/`, jeśli ich nie znajdzie. Swoją pracę zapisz przez *Plik → Zapisz kopię na Dysku* — inaczej przepadnie po zamknięciu karty.

## Jak pracować z notatnikiem

- Uruchamiaj komórki po kolei (<kbd>Shift</kbd> + <kbd>Enter</kbd>), zaczynając od komórki **Start**.
- W komórkach z `...` wpisz swój kod. Komórka **Sprawdź** pod zadaniem pokazuje:
  - ✅ — dobrze;
  - ❌ — jeszcze nie, z podpowiedzią;
  - ⏳ — brakuje zmiennej, bo nie uruchomiono komórki z rozwiązaniem.
- 💡 rozwija podpowiedź, ⭐ oznacza zadanie dla chętnych.
- Jeśli przez pomyłkę zmienisz dane w tabeli, uruchom ponownie komórkę, która ją tworzy. Możesz też zacząć od nowa: *Kernel → Restart Kernel and Run All Cells*.

## Dane

| Plik | Co zawiera | Źródło i licencja |
|---|---|---|
| `dane/odslony_wikipedia.csv` | Dzienne odsłony artykułów polskiej Wikipedii *ADHD*, *Zaburzenia depresyjne*, *Psychologia* i ruch całej polskiej Wikipedii, 1.01.2016–30.09.2026 (3926 dni) | [Wikimedia Pageviews API](https://wikimedia.org/api/rest_v1/), tylko ruch ludzi; dane o odsłonach Wikimedia udostępnia na CC0 |
| `dane/ankieta_ema.csv` | Eksport z aplikacji do badań EMA: 12 osób, 14 dni, 3 pomiary dziennie (nastrój, stres, sen, komentarz) | **Dane fikcyjne**, wygenerowane do ćwiczeń — nie opisują żadnych ludzi |
| `dane/pobierz_odslony.py` | Skrypt, który pobiera odsłony z Wikimedia Pageviews API do `odslony_wikipedia.csv` | Biblioteka standardowa Pythona; listę artykułów i zakres dat zmienisz na górze pliku |

Plik `ankieta_ema.csv` celowo wygląda jak prawdziwy eksport z badania: kodowanie `cp1250`, średnik jako separator, przecinek dziesiętny, `brak` i `-` zamiast pustych pól, komentarze na początku pliku. Nauka jego wczytania to jedno z zadań.

## Wersje

Sprawdzone 10.10.2026 w Pythonie 3.12 z pandas 3.0.6 i NumPy 2.5.3 oraz z pandas 2.2.3 i NumPy 2.2.6. Starsze pandas (przed 2.2) nie znają aliasów częstotliwości `"ME"`, `"YE"` i `"h"`.

## Literatura

- W. McKinney, *Python w analizie danych*, wyd. III, Helion 2023 — rozdz. 4 i dodatek A (NumPy), rozdz. 5 i 7 (pandas, braki danych), rozdz. 6 (wczytywanie i zapis), rozdz. 11 (daty i szeregi czasowe).
- A. Navlani, A. Fandango, I. Idris, *Python i praca z danymi*, wyd. III, Helion 2022 — rozdz. 2 (NumPy i pandas).
