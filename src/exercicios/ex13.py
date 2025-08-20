# ===Operations on Complex Numbers===

from __future__ import annotations

import math

# atrasa a interpretação das anotações de tipo - evita o uso de ""


class ComplexNumber:
    def __init__(self, real_part: float, imag_part: float) -> None:
        self.real = real_part
        self.imag = imag_part

    def __add__(self, other: ComplexNumber) -> ComplexNumber:
        """Addition of ComplexNumbers

        Args:
            other (ComplexNumber): other set

        Returns:
            ComplexNumber: new added parts
        """
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other: ComplexNumber) -> ComplexNumber:
        """Subtraction of Complex Numbers

        Args:
            other (ComplexNumber): other set

        Returns:
            ComplexNumber: new subtracted parts
        """
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other: ComplexNumber) -> ComplexNumber:
        """Distributive Multiplication = (a + bi)(c + di)

        Args:
            other (ComplexNumber): other set

        Returns:
            ComplexNumber: new multiplied parts
        """
        ac = self.real * other.real
        ad = self.real * other.imag
        bc = self.imag * other.real
        bd = self.imag * other.imag

        return ComplexNumber(ac - bd, ad + bc)

    def __truediv__(self, other: ComplexNumber) -> ComplexNumber:
        """Division of complex numbers

        Args:
            other (ComplexNumber): other set

        Returns:
            ComplexNumber: new divided parts
        """
        if other.real == 0 and other.imag == 0:
            raise ZeroDivisionError("Cannot divide by zero complex number")

        denominator = other.real**2 + other.imag**2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real_part, imag_part)

    def conjugate(self) -> ComplexNumber:
        """conjugate complex number

        Returns:
            ComplexNumber: mantém a parte real e inverte o sinal da parte imaginária.
        """
        return ComplexNumber(self.real, -self.imag)

    def abs_value(self) -> float:
        """Absolute value of Complex numbers

        Returns:
            float: result
        """
        return (self.real**2 + self.imag**2) ** 0.5

    def exponentiation(self, power: int) -> ComplexNumber:
        """Exponentiation of Complex numbers

        Args:
            power (int): The exponent to raise the complex number to. Must be a
            non-negative integer.

        Returns:
            ComplexNumber: A new ComplexNumber
        """
        result = ComplexNumber(1, 0)
        for _ in range(power):
            result = result * self
        return result

    def __eq__(self, other: object) -> bool:
        """Checks equality between two ComplexNumber instances.
        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if both real and imaginary parts are equal,
            False otherwise. If 'other' is not a ComplexNumber,
            returns NotImplemented.
        """
        if not isinstance(other, ComplexNumber):
            return NotImplemented
        return math.isclose(self.real, other.real, rel_tol=1e-9) and math.isclose(
            self.imag, other.imag, rel_tol=1e-9
        )
