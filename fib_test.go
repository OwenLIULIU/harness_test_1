package harness_test_1

import (
	"reflect"
	"testing"
)

func TestFibonacci(t *testing.T) {
	cases := []struct {
		n    int
		want int
	}{
		{-1, 0},
		{0, 0},
		{1, 1},
		{2, 1},
		{3, 2},
		{4, 3},
		{5, 5},
		{6, 8},
		{10, 55},
	}
	for _, tc := range cases {
		if got := Fibonacci(tc.n); got != tc.want {
			t.Errorf("Fibonacci(%d) = %d, want %d", tc.n, got, tc.want)
		}
	}
}

func TestFibonacciSequence(t *testing.T) {
	if got := FibonacciSequence(0); got != nil {
		t.Errorf("FibonacciSequence(0) = %v, want nil", got)
	}
	want4 := []int{0, 1, 1, 2}
	if got := FibonacciSequence(4); !reflect.DeepEqual(got, want4) {
		t.Errorf("FibonacciSequence(4) = %v, want %v", got, want4)
	}
	want1 := []int{0}
	if got := FibonacciSequence(1); !reflect.DeepEqual(got, want1) {
		t.Errorf("FibonacciSequence(1) = %v, want %v", got, want1)
	}
}
