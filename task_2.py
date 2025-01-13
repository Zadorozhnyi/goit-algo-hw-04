from heapq import heappush, heappop

def merge_k_lists(lists):

    # Merges k sorted lists into one sorted list.

    # :param lists: List of sorted lists
    # :return: A single sorted list

    min_heap = []  # Min-heap to keep track of the smallest elements across lists
    result = []    # Resultant sorted list

    # Add the first element of each list to the heap
    for i, lst in enumerate(lists):
        if lst:  # Ensure the list is not empty
            heappush(min_heap, (lst[0], i, 0))  # (value, list_index, element_index)

    # Continue while there are elements in the heap
    while min_heap:
        value, list_index, element_index = heappop(min_heap)  # Get the smallest element
        result.append(value)  # Add the smallest element to the result list

        # If there is a next element in the same list, add it to the heap
        if element_index + 1 < len(lists[list_index]):
            next_value = lists[list_index][element_index + 1]
            heappush(min_heap, (next_value, list_index, element_index + 1))

    return result

# Example usage
if __name__ == "__main__":
    # List of sorted lists
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    # Call the function to merge k sorted lists
    merged_list = merge_k_lists(lists)
    # Print the final sorted list
    print("Merged sorted list:", merged_list)
