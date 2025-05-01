# Simple Python application for try to make Python module in Rust

For use this project **uv** and **cargo** must be installed and accessible by path.
* [installation uv](https://docs.astral.sh/uv/getting-started/installation/)
* [installation cargo](https://doc.rust-lang.org/cargo/getting-started/installation.html)

## Build module
1. Clone repository
2. Open repository folder in console
3. Go to module folder `cd fibonacci_rs`
4. Activate maturin `uv sync`
5. Build module `uv run maturin build --release`

## Run module with benchmark
1. Go to root of project `cd ..`
2. Activate app venv `uv sync`
3. run benchmark `uv run main.py`

## Result
```
Test rust module
Call Ping -> Pong
Call Hello(Bob) -> Hello, Bob

Call python_fibonacci(35) = 9227465
Call rust_module.fibonacci(35) = 9227465 

Calc fibonacci average time
Pure Python fibonacci average time = 1143.40 milliseconds
Rust + Python fibonacci average time = 31.62 milliseconds
```