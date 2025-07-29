# Given an age in seconds, calculate how old someone
# would be on a planet in our Solar System.
# One Earth year equals 365.25 Earth days, or 31,557,600 seconds.
# If you were told someone was 1,000,000,000 seconds old,
# their age would be 31.69 Earth-years.

# Logic:
# Periodo orbital terrestre em segundos * periodo orbital do planeta em anos(Terra)
# para retornar os periodo orbital do planeta em segundos

# Dependendo de quanto eu tiver de idade em segundos terrestres -->
# Entrada_idade / periodo orbital do planeta em segundos
# Retorna Idade em anos do planeta.


# def my_year_on_planet
# my_second_year / second_in_earth_year * planet_year(factor)


def SpaceAge(second_year: float, planet: str) -> float:
    """Calculation of years on each planet

    Args:
        second_year (float): The person's age expressed in seconds.
        planet (str): The name of the planet to convert the age to.

    Returns:
        float: Corresponding age on the chosen planet, in planetary years.
    """
    SECOND_IN_EARTH_YEAR = 31_557_600

    orbital_period: dict[str, float] = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }
    factor = orbital_period[planet]
    return second_year / (SECOND_IN_EARTH_YEAR * factor)
