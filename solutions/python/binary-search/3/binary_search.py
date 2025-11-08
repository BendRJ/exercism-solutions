def find(search_list: list, value):
    low = 0
    high = len(search_list)-1
    mid = int((low+high)/2)
    
    done = False
    count = 0
    while not done:
        count += 1
        print(f"iteration: {count}")
        if high < 0: #empty list case
            raise ValueError("value not in array")
        elif search_list[mid] == value:
            done = True
            print(f"item found: {search_list[mid]}, index {mid}")
            return mid
        elif search_list[mid] > value: #only update high
            print(f"{search_list[mid]} > {value}, continuing.")
            high = mid-1
            mid = int((low+high)/2)
            if high < low: #searched value not in list case
                raise ValueError("value not in array")
        elif search_list[mid] < value: #only update low
            print(f"{search_list[mid]} < {value}, continuing.")
            low = mid+1
            mid = int((low+high)/2)
            if high < low: #searched value not in list case
                raise ValueError("value not in array")


if __name__ == "__main__":        
    find([1, 3, 4, 6, 8, 9, 11], 1)