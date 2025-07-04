# -*- coding: utf-8 -*-


# Merge Sort implementation for sorting products based on a specified criteria
def merge_sort(products, criteria):
    # Base case: If the list has 1 or 0 elements, it is already sorted
    if len(products) <= 1:
        return products

    # Divide the list into two halves
    mid = len(products) // 2
    left_half = products[:mid]
    right_half = products[mid:]

    # Recursively sort the left and right halves
    left_half = merge_sort(left_half, criteria)
    right_half = merge_sort(right_half, criteria)

    # Merge the sorted sublists and return the result
    return merge(left_half, right_half, criteria)


# Merge two sorted sublists into a single sorted list
def merge(left, right, criteria):
    sorted_list = []  # Resultant sorted list
    left_index = 0
    right_index = 0

    # Compare elements from the left and right sublists and add the smaller/bigger element to the sorted list
    while left_index < len(left) and right_index < len(right):
        if left[left_index][criteria] < right[right_index][criteria]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    # Add the remaining elements from the left or right sublist
    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])

    # Return the sorted list
    return sorted_list


# List of Products
products = [
    {"name": "Product A", "price": 50, "popularity": 8, "rating": 4.5, "release_date": "2022-01-01"},
    {"name": "Product B", "price": 30, "popularity": 6, "rating": 4.2, "release_date": "2021-10-15"},
    {"name": "Product C", "price": 40, "popularity": 9, "rating": 4.7, "release_date": "2023-02-28"},
    {"name": "Product D", "price": 100, "popularity": 3, "rating": 3.5, "release_date": "2022-04-12"},
    {"name": "Product E", "price": 400, "popularity": 2, "rating": 2.2, "release_date": "2021-12-11"},
    {"name": "Product F", "price": 199, "popularity": 7, "rating": 4.7, "release_date": "2023-07-08"}
]

# Sorting by price in ascending order
sorted_products = merge_sort(products, "price")
print("Sorted by price:")
for product in sorted_products:
    print(product)

# Sorting by popularity in descending order
sorted_products = merge_sort(products, "popularity")
print("\nSorted by popularity:")
for product in sorted_products:
    print(product)

# Sorting by rating in descending order
sorted_products = merge_sort(products, "rating")
print("\nSorted by rating:")
for product in sorted_products:
    print(product)

# Sorting by release date in ascending order
sorted_products = merge_sort(products, "release_date")
print("\nSorted by release date:")
for product in sorted_products:
    print(product)
