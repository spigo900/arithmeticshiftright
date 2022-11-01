/**
 ** @brief Perform a portable arithmetic right shift <tt>x >> y</tt>.
 **
 ** @param x The signed integer to be shifted.
 ** @param y The shift amount. This must be non-negative and strictly less than
 ** the bit width of the @c int type, as with C's bit shift operators.
 **
 ** @returns The shifted value <tt>x >> y</tt>.
 **/
int asr(int x, int y);
