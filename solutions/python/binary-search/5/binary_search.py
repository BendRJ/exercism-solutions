def find(search_list: list, value):
    low, high = 0, len(search_list) -1
    
    while low <= high:
        mid = (low + high) // 2
        if search_list[mid] == value:
            print(f"item found: {mid = } {search_list[mid] = }")
            return mid
        elif search_list[mid] > value: #only update high
            print(f"{search_list[mid]} > {value}, continuing.")
            high = mid -1
        elif search_list[mid] < value: #only update low
            print(f"{search_list[mid]} < {value}, continuing.")
            low = mid +1
        
    raise ValueError("value not in array") #searched value not in list case (when high < low exit of while loop); also empty list case covered


if __name__ == "__main__":        
    find([1, 3, 4, 6, 8, 9, 11], 1)