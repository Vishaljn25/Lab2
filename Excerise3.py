def display_main_menu():
 nums=str(input("Enter some numbers separated by commas (e.g. 5, 67,32)"))
 return nums

def get_user_input(nums):
<<<<<<< HEAD

=======
  
>>>>>>> 9e302ffdf32aa39129e2e425d6fa212b58ccce36
 
 string_list =nums.split("," )
 num_list =list(map(float, string_list))
 print(num_list)
 
 
 
num=display_main_menu()
get_user_input(num)