from timeit import timeit
from fibonacci_rs import ping, hello, calc as rs_fibonacci

NUMBER_OF_RUNS = 10
N = 35


def python_fibonacci(n: int) -> int:
    if n <= 0:
        raise Exception("N must be positive")
    elif n == 1 or n == 2:
        return 1
    return python_fibonacci(n - 1) + python_fibonacci(n - 2)


def main():
    print("Test rust module")
    print(f"Call Ping -> {ping()}")
    print(f"Call Hello(Bob) -> {hello('Bob')}\n")

    print(f"Call python_fibonacci({N}) = {python_fibonacci(N)}")
    print(f"Call rust_module.fibonacci({N}) = {rs_fibonacci(N)} \n")

    print("Calc fibonacci average time")
    pure_python_average_time = (
        timeit(lambda: python_fibonacci(N), number=NUMBER_OF_RUNS) / NUMBER_OF_RUNS
    )
    print(
        f"Pure Python fibonacci average time = {pure_python_average_time * 1_000:.2f} milliseconds"
    )
    rust_python_average_time = (
        timeit(lambda: rs_fibonacci(N), number=NUMBER_OF_RUNS) / NUMBER_OF_RUNS
    )
    print(
        f"Rust + Python fibonacci average time = {rust_python_average_time * 1_000:.2f} milliseconds"
    )


if __name__ == "__main__":
    main()
