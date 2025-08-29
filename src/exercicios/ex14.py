# Rational Numbers
from __future__ import annotations

from math import gcd
from typing import Any


class RationalNumber:
    def __init__(
        self,
        numerator: int,  ##TODO ALT F2
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
        """Add this rational number to another rational number.

        Args:
            other (RationalNumber): The rational number to add
        Returns:
            RationalNumber: The sum of the two rational numbers
        """
        return RationalNumber(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def __sub__(self, other: RationalNumber) -> RationalNumber:
        """Subtract another rational number from this rational number.

        Args:
            other (RationalNumber): The rational number to subtract

        Returns:
            RationalNumber: The difference of the two rational numbers
        """
        return RationalNumber(
            self.numerator * other.denominator - other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def __mul__(self, other: RationalNumber) -> RationalNumber:
        """Multiply this rational number by another rational number.

        Args:
            other (RationalNumber): The rational number to multiply by

        Returns:
            RationalNumber: The product of the two rational numbers
        """
        return RationalNumber(
            self.numerator * other.numerator, self.denominator * other.denominator
        )

    def __truediv__(self, other: RationalNumber) -> RationalNumber:
        """Divide this rational number by another rational number.

        Args:
            other (RationalNumber): The rational number to divide by

        Returns:
            RationalNumber: The quotient of the two rational numbers

        Raises:
            ZeroDivisionError: If the other rational number is zero
        """
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by 0")
        return RationalNumber(
            self.numerator * other.denominator, self.denominator * other.numerator
        )

    def __abs__(self) -> RationalNumber:
        """Return the absolute value of this rational number.

        Returns:
            RationalNumber: The absolute value of this rational number
        """
        return RationalNumber(abs(self.numerator), abs(self.denominator))

    def pow_integer(self, n: int) -> RationalNumber:
        """Raise this rational number to an integer power.

        For positive exponents, both numerator and denominator are raised to
        the power.
        For negative exponents, the fraction is inverted and then raised to the
        absolute power.

        Args:
            n (int): The integer exponent

        Returns:
            RationalNumber: The result of raising this rational number to the
            nth power
        """
        if n >= 0:
            return RationalNumber(self.numerator**n, self.denominator**n)
        else:
            m = abs(n)
            return RationalNumber(self.denominator**m, self.numerator**m)

    def pow_real(self, x: float) -> float:
        """Raise this rational number to a real (float) power.

        Computes (numerator^x) / (denominator^x) and returns the result
        as a float.

        Args:
            x (float): The real exponent

        Returns:
            float: The result of raising this rational number to the x power
        """
        return (self.numerator**x) / (self.denominator**x)

    @staticmethod
    def real_pow_rational(x: float, r: RationalNumber) -> float:
        """x^(a/b) = (x^a)^(1/b)
        Args:
            x (float): base
            r (RationalNumber): rational exponent
        Returns:
            float: result of the power operation
        """
        a, b = r.numerator, r.denominator
        return (x**a) ** (1 / b)

    def __eq__(self, other: RationalNumber | Any) -> bool:
        if isinstance(other, RationalNumber):
            return (
                self.numerator == other.numerator
                and self.denominator == other.denominator
            )

        if isinstance(other, (int, float)):
            # return (
            #     self.numerator == other[0] and self.denominator == other[1]
            # )  ##TODO corrigir
            return False

        raise ValueError(f"other cannot be of class: {type(other)}")
