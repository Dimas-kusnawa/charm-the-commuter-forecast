#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather for a city that does not exist.
"""

import os

# The forecast, built to the judge's brief: it names the invented city
# (Dreadville), keeps the rhythm of broadcast weather ("Today in ..."),
# gives the city one concrete detail of its weather (meetings raining
# from a grey sky, scattered sighs), and lands the commuter's own
# dread as the punch — the bus already left.
FORECAST = (
    "Today in Dreadville: heavy meetings falling from a grey sky, "
    "scattered sighs, and a 90% chance your bus already left."
)


def main() -> None:
    # The gate: entry.txt must be UTF-8 text of 1 to 140 characters,
    # a single line, not only white space.
    assert 1 <= len(FORECAST) <= 140, f"forecast is {len(FORECAST)} chars"
    assert "\n" not in FORECAST, "forecast must be one line"
    assert FORECAST.strip(), "forecast must not be blank"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORECAST)
    print(f"wrote {path}: {FORECAST} ({len(FORECAST)} chars)")


if __name__ == "__main__":
    main()
