package harness_test_1

// Fibonacci returns the n-th Fibonacci number using 0-based indexing: F(0)=0, F(1)=1, ...
// For n < 0, it returns 0.
func Fibonacci(n int) int {
	if n < 0 {
		return 0
	}
	if n <= 1 {
		return n
	}
	a, b := 0, 1
	for i := 2; i <= n; i++ {
		a, b = b, a+b
	}
	return b
}

// FibonacciSequence returns the first count values of the Fibonacci sequence
// (starting with 0, 1, 1, 2, ...). If count <= 0, it returns an empty slice.
func FibonacciSequence(count int) []int {
	if count <= 0 {
		return nil
	}
	out := make([]int, count)
	if count == 1 {
		out[0] = 0
		return out
	}
	out[0] = 0
	out[1] = 1
	for i := 2; i < count; i++ {
		out[i] = out[i-1] + out[i-2]
	}
	return out
}
