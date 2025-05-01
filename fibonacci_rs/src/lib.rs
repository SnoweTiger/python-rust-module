use pyo3::prelude::*;

fn fibonacci(n: usize) -> usize {
    if n < 2 {
        return n;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

#[pyfunction]
fn ping() -> String {
    "Pong".to_string()
}

#[pyfunction]
fn hello(name: String) -> String {
    format!("Hello, {}", name)
}

#[pyfunction]
fn calc(n: usize) -> PyResult<usize> {
    Ok(fibonacci(n))
}

#[pymodule]
fn fibonacci_rs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(ping, m)?)?;
    m.add_function(wrap_pyfunction!(hello, m)?)?;
    m.add_function(wrap_pyfunction!(calc, m)?)?;
    Ok(())
}
// fn fibonacci_rs(_py: Python, m: &PyModule) -> PyResult<()> {

// }
