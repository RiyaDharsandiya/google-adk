def physics_constants_tool(constant_name: str) -> str:
    """Returns physical constants from curated database"""
    constants = {
        "speed of light": "299792458 m/s",
        "c": "299792458 m/s",
        "gravitational constant": "6.67430e-11 m³·kg⁻¹·s⁻²",
        "g": "6.67430e-11 m³·kg⁻¹·s⁻²",
        "planck constant": "6.62607015 × 10^-34 J·s",
        "h": "6.62607015 × 10^-34 J·s"
    }
    # Normalize input: replace underscores with spaces and lower case
    key = constant_name.lower().replace("_", " ").strip()
    return constants.get(key, "Constant not found")