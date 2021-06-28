package main

import "testing"

func TestNumberRange(t *testing.T) {
	nums := numberRange(10)

	if len(nums) != 4 {
		t.Errorf("Expected the number of list to be 4, not %v.", len(nums))
	}

	if nums[0] != 3 {
		t.Errorf("Expected the first Element to be 3, not %v.", nums[0])
	}
}

func TestSum(t *testing.T) {
	numList = numberRange(10)
	total := sum(numList)

	if total != 23 {
		t.Errorf("Expected the total 23, not %v.", total)
	}
}
