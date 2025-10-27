def helper(input_list, value, middle_item, middle_index):
    """
    Helper function for main func to cut down list in half.
    """
    if middle_item == value:
        print(f"Middle item {middle_item} equals searched value {value}.")
        return True, input_list, middle_item
    elif middle_item > value:
        print(f"Middle item {middle_item} was > searched item {value}. Keeping left part {input_list[:middle_index]} of the {input_list}.")
        return False, input_list[:middle_index], middle_item
    else:
        print(f"Middle item {middle_item} was < searched item {value}. Keeping right part {input_list[middle_index+1:]} of the {input_list}.")
        return False, input_list[middle_index+1:], middle_item
    

def return_middle_item_in_list(input_list:list):
    """
    Helper function to return middle item and index of that item in given list.
    """
    middle_index = int((len(input_list)-1)/2)
    middle_item = input_list[middle_index]
    return middle_item, middle_index
    
def find(search_list: list, value):
    if len(search_list) == 1 and search_list[0] != value:
        raise ValueError("value not in array")
    if len(search_list) == 0:
        raise ValueError("value not in array")
    middle_item, middle_index = return_middle_item_in_list(search_list)

    done, result, item = helper(search_list, value, middle_item, middle_index)
    if done == True:
        return search_list.index(item)
    while not done:
        if len(result) == 0:
            raise ValueError("value not in array")
        middle_item, middle_index = return_middle_item_in_list(result)
        done, result, item = helper(result, value, middle_item, middle_index)
        if done == True:
            return search_list.index(item) #need to return index of searched item in original list