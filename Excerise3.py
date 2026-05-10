def display_main_menu():
 nums=str(input("Enter some numbers separated by commas (e.g. 5, 67,32)"))
 return nums

def get_user_input(nums):

 
 string_list =nums.split("," )
 num_list =list(map(float, string_list))
 print(num_list)
 
 
 
num=display_main_menu()
get_user_input(num)