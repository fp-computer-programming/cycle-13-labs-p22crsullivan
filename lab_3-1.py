# Author: CRS 03/07/22
# Define r_max function
def r_max(nested_num_lst):
    # Create for loop to check list
    for element in nested_num_lst:
        if type(element) == list:
            return max(element)
            # Test
print(r_max([1, 2, 3, [55, 0]]))
