# Python BDD - Is it Friday yet?

Ez a projekt a Cucumber 10 perces oktatóanyag Python Behave verziója. A Behave a Python verziója a Cucumber-nek, és ugyanazt a Gherkin nyelvet használja.

## Projekt struktúra

```
Python_BDD_Is_it_Friday/
├── features/
│   ├── is_it_friday_yet.feature      # Feature fájl (tesztek Gherkin nyelven)
│   └── steps/
│       └── step_definitions.py       # Step definitions (teszt kód)
├── src/
│   └── is_it_friday.py               # Production code (alkalmazás kód)
├── requirements.txt                  # Python függőségek
└── README.md                         # Ez a fájl
```

## Telepítés

1. Telepítsd a szükséges függőségeket:

```bash
pip install -r requirements.txt
```

## Futtatás

A tesztek futtatásához használd a `behave` parancsot a projekt gyökeréből:

```bash
python -m behave
```

Vagy ha a `behave` parancs elérhető a PATH-ban:

```bash
behave
```

Részletesebb kimenettel:

```bash
python -m behave --verbose
```

## Hogyan működik?

### 1. Feature fájl (`features/is_it_friday_yet.feature`)

Ez a fájl tartalmazza a teszteket Gherkin nyelven. A tesztek közérthető nyelven íródnak, így bárki megérti őket.

### 2. Step Definitions (`features/steps/step_definitions.py`)

Ez a fájl tartalmazza a Python kódot, amely **valójában végrehajtja** a teszteket. A step definitions "összeragasztják" a feature fájlban lévő sorokat a Python kóddal.

### 3. Production Code (`src/is_it_friday.py`)

Ez az **alkalmazás kódja**, amit tesztelünk. Ez tartalmazza az üzleti logikát.

**Fontos**: A teszt kód (`step_definitions.py`) **meghívja** az alkalmazás kódot (`is_it_friday.py`), és **ellenőrzi**, hogy helyesen működik-e!

## Példa folyamat

1. A `behave` elolvassa a `features/is_it_friday_yet.feature` fájlt
2. Minden Examples sorhoz külön tesztet futtat
3. A step definitions meghívják az `is_it_friday()` függvényt
4. Az eredményeket ellenőrzi és jelentést készít

## További információk

- [Behave dokumentáció](https://behave.readthedocs.io/)
- [Gherkin nyelv referencia](https://cucumber.io/docs/gherkin/reference/)
- [BDD bevezető](https://cucumber.io/docs/bdd/)
- [BDD 10 perces guide](https://cucumber.io/docs/guides/10-minute-tutorial)
