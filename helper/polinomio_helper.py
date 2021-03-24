def validate_arrays(arr_x1, arr_x2):
    temp_arr_x1 = arr_x1.split()
    temp_arr_x2 = arr_x2.split()
    arr = []
    
    if len(temp_arr_x1) != len(temp_arr_x2): return "The length are not equals"
    
    for i, j in zip(temp_arr_x1, temp_arr_x2):
        if i.isdigit() and j.isdigit():
            arr.append([i, j])
        else:
            return "Bad value"

    return arr