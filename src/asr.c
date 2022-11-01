#include <assert.h>
#include <limits.h>

int asr(int x, int y) {
    assert(y >= 0 && "y < 0 triggers undefined behavior.");
    assert(
        y < CHAR_BIT * sizeof(x) && 
        "y greater than the (bit) width of x triggers undefined behavior."
    );
    unsigned int extended_sign = (x >= 0) ? 0 : ~(UINT_MAX >> y);
    unsigned int reinterpreted_x = *(unsigned int*)(&x);
    return extended_sign | (reinterpreted_x >> y);
}
