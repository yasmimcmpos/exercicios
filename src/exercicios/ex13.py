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
        return ComplexNumber(self.real - other.real,self.imag - other.imag)

    def __mul__(self, other: "ComplexNumber") -> ComplexNumber:
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

    def __truediv__(self, other:ComplexNumber) -> ComplexNumber:
        """Division of complex numbers

        Args:
            other (ComplexNumber): other set

        Returns:
            ComplexNumber: new divided parts
        """
        denominator = other.real**2 + other.imag**2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.real * self.imag + self.imag * self.real) / denominator
        return ComplexNumber(real_part, imag_part)

    def conjugate(self)-> ComplexNumber:
        """conjugate complex number

        Returns:
            ComplexNumber: mantém a parte real e inverte o sinal da parte imaginária.
        """
        return ComplexNumber(self.real, -self.imag)

    def absolute_value(self, power):




    def exponentiation():