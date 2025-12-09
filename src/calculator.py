# calculator.py
from __future__ import annotations

class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a: float, b: float) -> float:
        return a - b

    def mul(self, a: float, b: float) -> float:
        return a * b

    def div(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b

    def sqrt(self, x: float, tol: float = 1e-6, max_iter: int = 1000) -> float:
        if x < 0:
            raise ValueError("sqrt of negative number")
        if x == 0:
            return 0.0
        guess = x if x >= 1.0 else 1.0
        for _ in range(max_iter):
            next_guess = 0.5 * (guess + x / guess)
            if abs(next_guess - guess) <= tol:
                return float(next_guess)
            guess = next_guess
        return float(guess)

    def exp(self, x: float, terms: int = 50) -> float:
        if x < 0:
            return 1.0 / self.exp(-x, terms)
        total = 1.0
        term = 1.0
        for n in range(1, terms):
            term = term * x / n
            total += term
            if abs(term) < 1e-6:
                break
        return float(total)

