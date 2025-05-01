from timeit import timeit

NUMBER_OF_RUNS = 10
N = 35


def python_fibonacci(n: int) -> int:
    if n <= 0:
        raise Exception("N must be positive")
    elif n == 1 or n == 2:
        return 1
    return python_fibonacci(n - 1) + python_fibonacci(n - 2)


def main():
    print(f"Call python_fibonacci({N}) = {python_fibonacci(N)}")

    print("Calc fibonacci average time")
    pure_python_average_time = (
        timeit(lambda: python_fibonacci(N), number=NUMBER_OF_RUNS) / NUMBER_OF_RUNS
    )
    print(
        f"Pure Python fibonacci average time = {pure_python_average_time * 1_000:.2f} milliseconds"
    )


if __name__ == "__main__":
    main()
