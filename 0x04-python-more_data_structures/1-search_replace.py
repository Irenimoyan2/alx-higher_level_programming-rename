#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """function that replaces all occurrences of an element"""
    new_lists = []


    # Iterate over each element in the input list
    for element in my_list:
        # check if the element matches the search value
        if element == search:
            # Replace the element with new value
            new_lists.append(replace)
        else:
            # Add the element as is to the new list
            new_lists.append(element)

    return new_lists
