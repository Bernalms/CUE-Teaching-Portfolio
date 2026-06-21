#Name:
#Lastname:
#Student ID:
#email:

def binsearch(my_list, num):
    try:
        list_len = len(my_list)
        if list_len == 0:
            return "List is empty"

        # Initialize both directional flags to True
        is_ascending = True
        is_descending = True
        
        # Single-pass validation
        for i in range(1, list_len):
            if my_list[i-1] > my_list[i]:
                is_ascending = False
            if my_list[i-1] < my_list[i]:
                is_descending = False
                
            # Optimization: If both are false, it's unsorted. Stop checking.
            if not is_ascending and not is_descending:
                break 
                
        if not is_ascending and not is_descending:
            print("The input cannot be recognized as a sorted list (neither ascending nor descending)") 
            return None
            
        # Binary Search Logic
        lob = 0
        upb = list_len - 1
        mid = (lob + upb) // 2
        
        # Adjust boundaries based on the sorted direction
        if is_ascending:
            while lob <= upb:        
                if my_list[mid] == num:
                    return mid # Target found, return index                
                if my_list[mid] < num:
                        lob = mid + 1
                else:
                        upb = mid - 1
                mid = (lob + upb) // 2
                
        # is_descending
        if is_descending:
            while lob <= upb:
                if my_list[mid] == num:
                    return mid # Fixed to return index instead of value
                if my_list[mid] < num:
                    upb = mid - 1  # Flipped logic for descending
                else:
                    lob = mid + 1  # Flipped logic for descending
                mid = (lob + upb) // 2
                
        return "Number was not found"

    except TypeError:
        print("Input must be a list of integers and the target must be an integer")
        return None

# --- Testing ---
my_list_asc = [1, 2, 2, 3, 4, 4, 5, 6, 10, 11, 12]
my_list_desc = my_list_asc[::-1]
unsorted_list = [10, 2, 5, 1, 12]

print("Testing Ascending List (Looking for 6):")
print(binsearch(my_list_asc, 6)) # Should return index 7

print("\nTesting Descending List (Looking for 6):")
print(binsearch(my_list_desc, 6)) # Should return index 3

print("\nTesting Unsorted List:")
print(binsearch(unsorted_list, 5)) # Should reject and return None
