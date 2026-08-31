import xml.etree.ElementTree as ET

from materia_epd.core.utils import to_float
from materia_epd.core.constants import NS, LCIA_AGGREGATE_MAP, LCIA_OUTPUT_MODULES


def normalize_module_values(
    amount_elements: list[ET.Element], scaling_factor: float = 1.0
) -> dict:
    """Normalizes and aggregates module values based on constants."""
    raw_values = {
        elem.attrib.get(f"{{{NS['epd']}}}module"): (
            (lambda v: v * scaling_factor if v is not None else None)(
                to_float(elem.text)
            )
            if elem.text
            else None
        )
        for elem in amount_elements
    }

    return {
        mod: (
            raw_values.get(mod)
            if mod in raw_values and raw_values.get(mod) is not None
            else (
                sum(
                    (raw_values.get(part) if raw_values.get(part) is not None else 0.0)
                    for part in LCIA_AGGREGATE_MAP.get(mod, [])
                )
                if any(
                    raw_values.get(part) is not None
                    for part in LCIA_AGGREGATE_MAP.get(mod, [])
                )
                else None
            )
        )
        for mod in LCIA_OUTPUT_MODULES
    }
