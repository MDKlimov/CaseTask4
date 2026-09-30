"""Максимальная сила стаи драконов при заданном общем числе голов."""


def maximum_power(n: int) -> int:
    """Возвращает максимальное произведение чисел голов (от 1 до 7)."""
    if not 1 <= n < 100:
        raise ValueError("N должно быть натуральным числом от 1 до 99")

    if n <= 3:
        return n

    quotient, remainder = divmod(n, 3)
    if remainder == 0:
        return 3 ** quotient
    if remainder == 1:
        return 3 ** (quotient - 1) * 4
    return 3 ** quotient * 2


def main() -> None:
    n = int(input())
    print(maximum_power(n))


if __name__ == "__main__":
    main()
