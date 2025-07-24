# Given an age in seconds, calculate how old someone
# would be on a planet in our Solar System.
# One Earth year equals 365.25 Earth days, or 31,557,600 seconds.
# If you were told someone was 1,000,000,000 seconds old,
# their age would be 31.69 Earth-years.

from typing import Dict


class SpaceAge:
    second_in_earth_year = 31_557_600

    orbital_period: Dict[str, float] = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }

    def __init__(self, seconds: float):
        self.seconds = seconds

    def age_on_planet(self, planet: str) -> float:
        period = self.orbital_period[planet]
        return self.seconds / (self.second_in_earth_year * period)
