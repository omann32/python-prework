#1
# def hello_name(user_name):
#     print("hello_USERNAME!")
# hello_name('user_name')    



#2

# for first_odds in range(1, 100, 2):
#     print(first_odds)
    

#3
def max_num_in_list(a_list):
    sorted_a_list = sorted(a_list)
    print(sorted_a_list[-1])
max_num_in_list([1,2,3,14,5,7])


#4 
# def is_leap_year(a_year):
#     if a_year % 100 == 0 and a_year % 400 == 0:
#         return True
#         if a_year % 400 == 0: 
#                 return True
#                 if a_year % 4 == 0:
#                     return True
#     return False    
# print(is_leap_year(2000))

#5

# def is_consecutive(a_list):
#     sorted_a_list = sorted(a_list)
#     if a_list == sorted_a_list and len(sorted_a_list) + sorted_a_list[0] == sorted_a_list[-1]:
#         return True
#     else:
#         return False   
# print(is_consecutive([1,2,3,5,6]))