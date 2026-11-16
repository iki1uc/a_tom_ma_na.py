# a_tom_ma_na.py — 3fach deckend, 43-richtig
# A.T.O.M + MANA + NA
# AURA sieht, MANA trägt, ZEN dreht — 3x derselbe Check

HOME = 40
SCHLUSS = 729

def c(x):
    try: return float(x)
    except: return 0

def cc(v):
    if v is None: return "UNKNOWN"
    if v >= 70: return "PASS"
    if v >= 40: return "TUNE"
    return "FAIL"

def ccc(v):
    g = cc(v)
    return {"wert": v, "gate": g, "darf_weiter": g == "PASS"}

# --- 3fach deckend ---
def aura_check(wert):
    # AURA = sehen
    return {"zustand": "AURA", **ccc(wert)}

def mana_check(wert):
    # MANA = tragen
    return {"zustand": "MANA", **ccc(wert)}

def zen_check(wert):
    # ZEN = drehen
    return {"zustand": "ZEN", **ccc(wert)}

def deckend_3fach(wert):
    # 1 Wert, 3 Checks, 1 Urteil
    checks = [aura_check(wert), mana_check(wert), zen_check(wert)]
    alle_pass = all(x["gate"] == "PASS" for x in checks)
    return {
        "wert": wert,
        "checks": checks,
        "deckung": "3fach",
        # 43 = 40 HOME + 3 Deckung
        "code_43": 40 + 3 if alle_pass else 0,
        "urteil": "43-RICHTIG" if alle_pass else "WARTET",
        "darf_weiter": alle_pass,
    }

# --- A.T.O.M / MANA / NA ---
def arg(frage):
    return {"ARG": frage}

def sam(liste):
    # SAM = sammeln, nichts löschen
    return list(liste)

def msen(wert):
    return ccc(wert)

def sense(wert, ziel):
    m = msen(wert)
    if not m["darf_weiter"]:
        return {**m, "gesendet": False, "grund": "wartet"}
    return {**m, "gesendet": True, "an": ziel}

# --- Pyramide / Würfel / Zylinder ---
def form(n):
    if n <= 40: return "Pyramide / MANA / HOME 40"
    if n <= 243: return "Würfel / 27 / ROM-Kern"
    return "Zylinder / ZEN / 3x"

# --- Lauf ---
if __name__ == "__main__":
    for n in [3, 9, 27, 81, 243, 729]:
        r = deckend_3fach(82)  # Beispielwert
        print(n, form(n), r["urteil"], "code:", r["code_43"])
    print("---")
    print(deckend_3fach(82))
    print(deckend_3fach(20))
    print(arg("mana?"))
    print(sense(82, "HOME 40"))
