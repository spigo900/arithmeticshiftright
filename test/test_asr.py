"""
Unit tests for asr code using Python testing library Hypothesis.
"""
# Would like to make this easier to run on Windows -- maybe by setting this
# file up as a CTest executable? or copying it to the build dir.
import multiprocessing as mp
from multiprocessing import Process

from cffi import FFI
from hypothesis import given, settings
from hypothesis.strategies import integers

# Set up the CFFI objects
ffi = FFI()
ffi.cdef("""
    int asr(int, int);
""")
try:
    c_asr = ffi.dlopen("libasr")
except OSError as e:
    c_asr = ffi.dlopen("asr")

# Hopefully correct. Surprisingly I didn't find a documented constant for these
# in any of ctypes, cffi, or sys.
INT_MAX = (1 << (8 * ffi.sizeof("int") - 1)) - 1
INT_MIN = -INT_MAX - 1

def asr(x, y):
    return c_asr.asr(x, y)


@given(x=integers(min_value=0, max_value=INT_MAX), y=integers(min_value=0, max_value=31))
def test_same_as_logical_for_positive_ints(x, y):
    assert asr(x, y) == x >> y


@given(x=integers(min_value=INT_MIN, max_value=-1), y=integers(min_value=0, max_value=31))
def test_matches_python_asr_for_valid_values(x, y):
    # Treat Python's right shift as "oracle" implementation here, because
    # (supposedly) Python only implements arithmetic right shift.
    # See https://stackoverflow.com/a/64987033.
    assert asr(x, y) == x >> y


# We have to boot a Python subprocess for each run of this test, which is
# slooow. Set the deadline and max number of examples appropriately.
@settings(deadline=6000, max_examples=4)
@given(x=integers(min_value=INT_MIN, max_value=INT_MAX), y=integers(min_value=INT_MIN, max_value=-1))
def test_errors_for_negative_y(x, y):
    process = Process(target=asr, args=(x, y))
    process.start()
    process.join(timeout=5)
    try:
        assert not process.is_alive()
        assert process.exitcode != 0
    finally:
        process.terminate()


@settings(deadline=6000, max_examples=4)
@given(x=integers(min_value=INT_MIN, max_value=INT_MAX), y=integers(min_value=32, max_value=INT_MAX))
def test_errors_for_large_y(x, y):
    process = Process(target=asr, args=(x, y))
    process.start()
    process.join(timeout=5)
    try:
        assert not process.is_alive()
        assert process.exitcode != 0
    finally:
        process.terminate()
