# ===Operations on Complex Numbers===

from __future__ import annotations

import math

# atrasa a interpretação das anotações de tipo - evita o uso de ""


class ComplexNumber:
    def __init__(self, real_part: float, imag_part: float) -> None:
        self.real = real_part
        self.imag = imag_part

    def addition(self, other: ComplexNumber) -> ComplexNumber:
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return ComplexNumber(new_real, new_imag)

    def subtraction(self, other: ComplexNumber) -> ComplexNumber:
        new_real = self.real - other.real
        new_imag = self.imag - other.imag
        return ComplexNumber(new_real, new_imag)

    def multiplication(self, other: "ComplexNumber") -> ComplexNumber:
        # (a + bi)(c + di)
        ac = self.real * other.real
        ad = self.real * other.imag
        bc = self.imag * other.real
        bd = self.imag * other.imag

        new_real = ac * bd
        new_imag = ad * bc
        return ComplexNumber(new_real, new_imag)

    def absolute_value():
    def conjugate(self):
    def division(self, other):
    def exponentiation():