# Rational Numbers
from __future__ import annotations

from math import gcd


class RationalNumber:
    def __init__(
        self,
        numerator: int,
        denominator: int,
    ) -> None:

        if denominator == 0:
            raise ValueError("The denominator cannot be 0")

        self.numerator: int = numerator
        self.denominator: int = denominator
        self.simple()

    def simple(self) -> None:
        divisor = gcd(self.numerator, self.denominator)
        self.numerator //= divisor
        self.denominator //= divisor

        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def __repr__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other: RationalNumber) -> RationalNumber:
        return RationalNumber(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def __sub__(self, other: RationalNumber) -> RationalNumber:
        return RationalNumber(
            self.numerator * other.denominator - other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def __mul__(self, other: RationalNumber) -> RationalNumber:
        return RationalNumber(
            self.numerator * other.numerator, self.denominator * other.denominator
        )

    def __truediv__(self, other: RationalNumber) -> RationalNumber:
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by 0")
        return RationalNumber(
            self.numerator * other.denominator, self.denominator * other.numerator
        )

    def __abs__(self) -> RationalNumber:
        return RationalNumber(abs(self.numerator), abs(self.denominator))

    def pow_integer(self, n: int) -> RationalNumber:
        """Power with real exponent → returns float

        Args:
            n (int): _description_

        Returns:
            RationalNumber: _description_
        """
        if n >= 0:
            return RationalNumber(self.numerator**n, self.denominator**n)
        else:
            m = abs(n)
            return RationalNumber(self.denominator**m, self.numerator**m)

    def pow_real(self, x: float) -> float:
        """Power with real exponent → returns float

        Args:
            x (float): _description_

        Returns:
            float: _description_
        """
        return (self.numerator**x) / (self.denominator**x)

    def real_pow_rational(x: float, r: RationalNumber) -> float:
        """x^(a/b) = (x^a)^(1/b)

        Args:
            x (float): _description_
            r (RationalNumber): _description_

        Returns:
            float: _description_
        """
        a, b = r.numerator, r.denominator
        return (x**a) ** (1 / b)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, RationalNumber):
            return (
                self.numerator == other.numerator
                and self.denominator == other.denominator
            )
        elif isinstance(other, tuple) and len(other) == 2:
            return self.numerator == other[0] and self.denominator == other[1]
        return False
