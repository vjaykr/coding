import heapq

def find_largest_distinct_product(nums):
    if nums is None or len(nums) < 3:
        print("Array should contain at least three elements.")
        return -1

    max_heap = []
    for num in nums:
        heapq.heappush(max_heap, -num)

    largest1 = -heapq.heappop(max_heap)
    largest2 = -heapq.heappop(max_heap)
    largest3 = largest2
    while max_heap and largest3 == largest2:
        largest3 = -heapq.heappop(max_heap)

    product = largest1 * largest2 * largest3

    return product


def main():
    nums = [1, 5, 2, 3, 6, 4]
    product = find_largest_distinct_product(nums)

    if product != -1:
        print("Product of the three largest distinct elements:", product)


if __name__ == "__main__":
    main()
