def rotate_by_k(arr, k):
    # Ensure k is within bounds
    k = k % len(arr)
    return arr[k:] + arr[:k]

# Test the function
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotated_arr = rotate_by_k(arr, k)
print("Array after rotating by", k, "positions:", rotated_arr)
