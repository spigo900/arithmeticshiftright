# arithmeticshiftright
A portable implementation of an arithmetic right shift for C. Note this currently only provides an implementation for `int` arguments.

## Supported platforms
This should compile in pretty much any C compiler on any platform. If not, that's a bug. That said, I've only tested it on a 64-bit Windows 10 PC.

## Building
Use CMake (version 3.12 or newer) on this source directory. Build wherever you want, with whatever generator you want.

## Dependencies
Only `assert.h` and `limit.h` from the standard library.

## Testing
The tests take advantage of the [Hypothesis testing library for Python][hypothesis] for property-based or fuzz testing, using [Pytest] to run the tests and [cffi][cffi] to call `asr`. To run them you'll need to set up and activate a Python virtual environment using virtualenv or conda. All Python 3 versions starting with 3.7 should work; I tested with Python 3.9. The necessary Python packages are listed in `requirements.txt`. After activating your virtual environment, you can install them using `pip install -r requirements.txt`.

The tests should be runnable from your build system. For example, with the Ninja CMake generator you can run `ninja test` to run the tests. However you set things up, you'll want to run the tests using the virtual environment you set up (so manually point the `PATH` to the bin directory in your virtual environment).

Alternatively, after compiling the library, copy the dynamic library (`libasr.dylib`, `libasr.so`, `libasr.dll`, or `asr.dll`) file to the test directory. You can then run the tests from the command line in the `test` directory by running `pytest` on the test code:

```bash
python -m pytest test_asr.py
```

[hypothesis]: https://hypothesis.readthedocs.io/en/latest/
[pytest]: https://docs.pytest.org/en/7.2.x/
[cffi]: https://cffi.readthedocs.io/en/latest/
