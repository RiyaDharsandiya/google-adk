
PERIODIC_TABLE = {
    "hydrogen": "H, Atomic number: 1",
    "oxygen": "O, Atomic number: 8",
    "carbon": "C, Atomic number: 6"
}

def chemistry_lookup(element: str) -> str:
    return PERIODIC_TABLE.get(element.lower(), "Element not found.")