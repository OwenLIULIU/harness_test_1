/**
 * Returns the n-th Fibonacci number using the definition F(0) = 0, F(1) = 1.
 * @param {number} n - Non-negative integer index
 * @returns {bigint}
 */
function fibonacci(n) {
  if (!Number.isInteger(n) || n < 0) {
    throw new TypeError("n must be a non-negative integer");
  }
  if (n <= 1) {
    return BigInt(n);
  }
  let a = 0n;
  let b = 1n;
  for (let i = 2; i <= n; i += 1) {
    const next = a + b;
    a = b;
    b = next;
  }
  return b;
}

module.exports = { fibonacci };
